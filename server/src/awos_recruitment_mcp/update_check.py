"""Compare installed skill hashes with the registry index.

Shared by ``POST /check`` (called by the ``skill-update-check`` hook with
the project's lock file) and the ``check_skill_updates`` MCP tool (called
by ``/awos:hire`` and agents).  Local edits cannot be seen from here: the
CLI's ``skill status`` compares file by file.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

UPDATE_COMMAND = "npx @provectusinc/awos-recruitment skill update"


@dataclass
class CheckResult:
    """Outcome of one update check.

    Attributes:
        outdated: Installed skills whose registry hash differs.
        removed: ``{name, replacement}`` for skills with a tombstone.
        unknown: Installed skills the registry does not know.
        up_to_date: Count of skills whose hash matches.
    """

    outdated: list[str] = field(default_factory=list)
    removed: list[dict[str, str | None]] = field(default_factory=list)
    unknown: list[str] = field(default_factory=list)
    up_to_date: int = 0

    @property
    def summary(self) -> str:
        """One line for the user, empty when there is nothing to report."""
        parts: list[str] = []
        if self.outdated:
            parts.append(
                f"{len(self.outdated)} skill{'s' if len(self.outdated) != 1 else ''} outdated "
                f"({', '.join(self.outdated)})"
            )
        if self.removed:
            names = ", ".join(
                f"{r['name']} -> {r['replacement']}" if r["replacement"] else str(r["name"])
                for r in self.removed
            )
            parts.append(
                f"{len(self.removed)} removed from registry ({names})"
            )
        if not parts:
            return ""
        return f"awos-recruitment: {'; '.join(parts)}. Run `{UPDATE_COMMAND}`."

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": self.summary,
            "outdated": self.outdated,
            "removed": self.removed,
            "unknown": self.unknown,
            "up_to_date": self.up_to_date,
            "command": UPDATE_COMMAND,
        }


def check_skills(installed: dict[str, str], index: dict[str, Any]) -> CheckResult:
    """Compare ``{skill name: lock hash}`` with a registry index.

    Args:
        installed: Skill names and the capability hash from the lock file.
        index: The document ``build_registry_index`` returns.

    Returns:
        A :class:`CheckResult` with names sorted.
    """
    result = CheckResult()
    registry_skills = index.get("skills", {})
    removed_skills = index.get("removed", {}).get("skills", {})

    for name in sorted(installed):
        if name in removed_skills:
            result.removed.append(
                {"name": name, "replacement": removed_skills[name].get("replacement")}
            )
        elif name not in registry_skills:
            result.unknown.append(name)
        elif registry_skills[name]["hash"] != installed[name]:
            result.outdated.append(name)
        else:
            result.up_to_date += 1

    return result
