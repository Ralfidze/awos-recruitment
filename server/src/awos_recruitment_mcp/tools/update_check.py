"""MCP tool that tells an agent which installed skills are outdated or removed."""

from __future__ import annotations

from awos_recruitment_mcp.registry_index import build_registry_index
from awos_recruitment_mcp.server import config, mcp
from awos_recruitment_mcp.telemetry import track_client_event
from awos_recruitment_mcp.update_check import check_skills


@mcp.tool
async def check_skill_updates(
    installed: dict[str, str],
    project_id: str | None = None,
) -> dict:
    """Check which installed skills are outdated or removed from the registry.

    Read ``.claude/awos-recruitment.lock.json`` in the project and pass
    ``installed`` as ``{skill name: hash}`` from its ``skills`` map, plus
    its ``project_id``.  Returns ``summary`` (one line for the user, empty
    when everything is current), ``outdated``, ``removed`` (with the
    replacement to install instead), ``unknown`` and ``command`` (what the
    user runs to update).  Local edits are not visible here; the CLI
    command ``skill status`` reports them.

    Args:
        installed: Skill names mapped to the ``hash`` recorded in the lock file.
        project_id: The ``project_id`` from the lock file, for anonymous telemetry.
    """
    result = check_skills(installed, build_registry_index(config.registry_path))

    if project_id is not None:
        _track(project_id, result, source="mcp")

    return result.to_dict()


def _track(project_id: str, result, source: str) -> None:
    track_client_event(
        project_id,
        "capability_update_checked",
        {
            "source": source,
            "total": len(result.outdated) + len(result.removed) + len(result.unknown) + result.up_to_date,
            "outdated": len(result.outdated),
            "removed": len(result.removed),
        },
    )
    for removed in result.removed:
        track_client_event(
            project_id,
            "capability_removed_in_use",
            {
                "capability_name": removed["name"],
                "capability_type": "skill",
                "has_replacement": removed["replacement"] is not None,
                "source": source,
            },
        )
