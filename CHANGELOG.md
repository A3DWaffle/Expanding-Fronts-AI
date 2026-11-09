# Changelog

This file tracks major public-facing changes to the Expanding Fronts AI scripting project.

## 2026-11-09

- WATER no longer inherits forced worker, ground, or aircraft targeting preferences. Its attacks retain intelligent targeting and reactions to incoming fire.
- Every WATER personality builds a Spaceport followed by a War Center and completes both before TL3. Defensive's turret-first construction hold does not delay this pair.
- Unmarked maps default to LAND and fall back to HYBRID when fish or aquatic carbon vents are present. Explicit map objects retain priority; WATER and ASTEROID require those objects.
- Source and prototype scripts are synchronized. Script-level targeting, map-detection, and advancement checks pass; fresh-match playtesting remains necessary.

## Unreleased

- Added public repository structure.
- Added README documentation.
- Added `.gitignore`.
- Added prototype `.per` AI script files.
- Added notes explaining the project purpose, status, and file format.

## Notes

This project is currently prototype AI work. Some behavior may still be experimental, incomplete, or undergoing reorganization.
