---
name: expo-sdk-upgrades
description: >-
  Upgrading an Expo or React Native app between SDK versions. Use when bumping
  the Expo SDK, enabling the New Architecture, moving to React 19 or the React
  Compiler, adopting native tabs, or replacing expo-av with expo-audio and
  expo-video. Does not cover app UI (expo-react-native) or EAS builds and
  store submission (expo-deployment).
metadata:
  version: "0.1"
---

# Expo SDK Upgrades

Migration guides for moving an Expo app from one SDK version to the next. Each guide is tied to the SDK that introduced the change; retire it once the team is past that version.

> Sourced from [expo/skills](https://github.com/expo/skills) (MIT License, © 2025-present 650 Industries, Inc.), adapted to the registry layout.

## Process

```bash
npx expo install expo@latest   # bump the SDK
npx expo install --fix         # align dependency versions
npx expo-doctor                # check for known problems
```

Start with [upgrading-expo.md](references/upgrading-expo.md) for the order of operations and the per-SDK checklist. Then apply the guides that match the versions you cross:

| Change | Since SDK | Reference |
| --- | --- | --- |
| New Architecture migration | 53 | [new-architecture.md](references/new-architecture.md) |
| React 19: `use`, Context changes, `forwardRef` removal | 54 | [react-19.md](references/react-19.md) |
| React Compiler setup | 54 | [react-compiler.md](references/react-compiler.md) |
| Native tabs API changes | 55 | [native-tabs.md](references/native-tabs.md) |
| expo-av to expo-audio | 54 | [expo-av-to-audio.md](references/expo-av-to-audio.md) |
| expo-av to expo-video | 54 | [expo-av-to-video.md](references/expo-av-to-video.md) |

## Related skills

- `expo-react-native`: screens, navigation, data fetching, API routes.
- `expo-deployment`: EAS builds, TestFlight, store submission.
