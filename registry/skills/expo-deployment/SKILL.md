---
name: expo-deployment
description: >-
  Building and shipping Expo and React Native apps with EAS. Use when
  configuring EAS Build profiles or development clients, submitting to
  TestFlight, the App Store, or Google Play, writing App Store metadata, or
  automating builds and releases with EAS Workflows. Does not cover app UI
  (expo-react-native) or SDK upgrades (expo-sdk-upgrades).
metadata:
  version: "0.1"
---

# Expo Deployment with EAS

Build, test, and ship Expo apps with EAS Build, EAS Submit, and EAS Workflows.

> Sourced from [expo/skills](https://github.com/expo/skills) (MIT License, © 2025-present 650 Industries, Inc.), adapted to the registry layout.

## Conventions

- Use EAS Build for cloud builds and EAS Submit for store submission.
- Bump `expo.version` and `ios.buildNumber` / `android.versionCode` before each submission.
- Keep credentials in EAS, not in the repository.
- Test a release build on a physical device before submitting.

## Builds and submission

```bash
eas build --profile development --platform ios   # development client
eas build --profile production --platform all    # store builds
eas submit --platform ios                        # App Store Connect
eas submit --platform android                    # Google Play Console
```

Start with [eas-build-and-submit.md](references/eas-build-and-submit.md): build profiles, credentials, and the submission flow. Then:

| Topic | Reference |
| --- | --- |
| Development clients for custom native code | [expo-dev-client.md](references/expo-dev-client.md) |
| TestFlight internal and external testing | [testflight.md](references/testflight.md) |
| App Store submission and review | [ios-app-store.md](references/ios-app-store.md) |
| App Store metadata and listing optimization | [app-store-metadata.md](references/app-store-metadata.md) |
| Google Play submission | [play-store.md](references/play-store.md) |

## Automation with EAS Workflows

Workflow YAML under `.eas/workflows/` for builds on push, PR previews, and production releases:

```yaml
jobs:
  build:
    type: build
    params:
      platform: all
      profile: production
```

See [eas-workflows.md](references/eas-workflows.md) for triggers, job types, dependencies, and full examples.

## Related skills

- `expo-react-native`: screens, navigation, data fetching, API routes.
- `expo-sdk-upgrades`: migrating between Expo SDK versions.
