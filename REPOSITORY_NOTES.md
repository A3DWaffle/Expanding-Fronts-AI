# Repository Notes

This repository is meant to showcase AI scripting work in a readable and organized way.

## Before Public Release

Recommended cleanup steps:

1. Remove duplicate backup files.
2. Remove private notes or unfinished comments that should not be public.
3. Rename `PATCH_NOTES_DRAFT.md` to `PATCH_NOTES.md` or `CHANGELOG.md` if it is ready to share.
4. Make sure only files that are safe to distribute are included.
5. Confirm that no game assets, executables, or copyrighted media are included.

## Good GitHub Practices

- Keep the README clear and current.
- Use commits with simple messages, such as `Add AI prototype scripts` or `Update file guide`.
- Add documentation when a file would not be obvious to someone outside the project.
- Keep experimental work labeled clearly.

## Active deployment workflow

Use the Steam archive AI in Game/Data/gamedata_x2.drs for live testing. “Dropbox” means the formally named files in E:/Code Projects/Computer Standard/6-2026/gamedata_x2; retain their existing filenames. Sync production changes to those files and the Steam archive. Computer Diagnostics and its build tools were removed; do not recreate a separate diagnostic AI without a new request.
