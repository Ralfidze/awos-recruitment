---
name: expo-react-native
description: >-
  Building mobile app UI and app code with Expo and React Native. Use when
  creating screens with Expo Router, native tabs and stack headers, animations,
  native controls, icons, media, storage, search, data fetching with React Query
  or SWR, API routes, or Android safe-area handling. Does not cover EAS builds
  and store submission (expo-deployment) or SDK upgrades (expo-sdk-upgrades).
metadata:
  version: "0.2"
---

# Expo and React Native: Building the App

Build mobile app UI and app code with Expo Router and React Native. Each reference below is self-contained; read the one that matches the task.

> Sourced from [expo/skills](https://github.com/expo/skills) (MIT License, © 2025-present 650 Industries, Inc.), adapted to the registry layout.

## Conventions

- Expo-first: prefer Expo APIs over bare React Native when an equivalent exists.
- Expo Router for file-based routing; `_layout.tsx` files define stacks and tabs.
- Address iOS and Android differences explicitly in layouts, permissions, and navigation.
- Wrap the root layout in `SafeAreaProvider`; use `useSafeAreaInsets` for custom headers.
- Use `process.env.EXPO_OS` for platform checks; `Platform.select()` only where a React Native API needs runtime branching.
- Test on a physical device before any store submission.

## UI and navigation

Start with [building-native-ui.md](references/building-native-ui.md): the conventions, the preferred packages, and the list of topic guides. Topic guides:

| Topic | Reference |
| --- | --- |
| Route files, dynamic routes, groups | [route-structure.md](references/route-structure.md) |
| Native tab bar, migration from JS tabs | [tabs.md](references/tabs.md) |
| Stack headers, toolbar buttons, menus (iOS) | [toolbar-and-headers.md](references/toolbar-and-headers.md) |
| Modal and form sheets | [form-sheet.md](references/form-sheet.md) |
| Native controls: Switch, Slider, Picker, DateTimePicker | [controls.md](references/controls.md) |
| Search bars in headers, `useSearch`, filtering | [search.md](references/search.md) |
| SF Symbols with `expo-symbols` | [icons.md](references/icons.md) |
| Reanimated: entering, exiting, layout, scroll-driven, gestures | [animations.md](references/animations.md) |
| Blur and liquid glass effects | [visual-effects.md](references/visual-effects.md) |
| CSS gradients (New Architecture only) | [gradients.md](references/gradients.md) |
| Camera, audio, video, file saving | [media.md](references/media.md) |
| SQLite, AsyncStorage, SecureStore | [storage.md](references/storage.md) |
| Android navigation bar insets | [expo-android-safe-area.md](references/expo-android-safe-area.md) |

## Data fetching

Patterns for `fetch`, React Query, and SWR with caching, optimistic updates, and offline support:

```typescript
import { useQuery } from '@tanstack/react-query';

function useUser(id: string) {
  return useQuery({
    queryKey: ['user', id],
    queryFn: () => fetch(`/api/users/${id}`).then((r) => r.json()),
  });
}
```

See [native-data-fetching.md](references/native-data-fetching.md).

## API routes

Server-side routes with Expo Router and EAS Hosting:

```typescript
// app/api/hello+api.ts
export function GET(request: Request) {
  return Response.json({ hello: 'world' });
}
```

See [expo-api-routes.md](references/expo-api-routes.md).

## Related skills

- `expo-deployment`: EAS Build, development clients, TestFlight, App Store and Play Store submission, EAS Workflows.
- `expo-sdk-upgrades`: migrating between Expo SDK versions, New Architecture, React 19, React Compiler, expo-av replacements.
