# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Added

- macOSMonterey cursors added 🎊 fixed #66
- Generate master `bitmaps.zip` inside `bin` directory
- `Makefile` binaries targets with variable
- pling docs: size and support info updated
- `bigsur` cursor bitmapper as node package
- New commands added inside `Makefile` for `bitmapper`
- symlink script for `macOSMonterey` svg files

### Changed

- Removed unnecessary badges from `README.md`
- Simplified README.md (removed emojis)
- sponsor with liberapay
- fixed text cursor state in `xterm` & `vertical-text` (increase border size) #67
- bitmapper `core` as node package
- macOSBigSur .svg files moved to `svgs/bigsur` directory

## [v1.2.2] - 31 Oct 2021

### Added

- Rounded pointer tail #63
- make binaries inside sub directory `make preapre`

### Changed

- soft shadows in all cursors #62
- fixed some cursor size #64
- cursor preview updated
- project description changed

## [v1.2.1] - 14 Oct 2021

### Added

- docs: macOSBigSur-White pling document added to `pling/white.bbcode`.
- quick install links updated inside README.md#quick-install

### Changed

- docs: pling documents renamed to `pling/` directory.
- build: logging character updated

## [v1.2.0] - 25 Aug 2021

### Added

- Dark branding
- Multiple config supports inside bitmapper
- `macOSBigSur-White` CI added inside `build.yml`

### Changed

- Drop shadow removed from `plus.svg`
- Key colors added inside `.svg` files
- `builder/src` configured as dynamic comment and theme-name
- `builder/Makefile` updated
- `Makefile` with macOSBigSur-White cursor theme
- `PULL_REQUEST_TEMPLATE.md` template updated

## [v1.1.6] - 13 Aug 2021

### Added

- Support button inside PLING.bbcode product page
- `make prepare` command for preparing bibata binaries
- `pyrightconfig.json` init

### Changed

- Removed **clean** target from `builder/Makefile`
- Compact code inside `builder/*`
- Remove `setup.py`
- Builder code moved to `src`
- Import `src` module directly inside `build.py`
- `Makefile` build commands re-arrange with groups
- `crosshair` cursors border added fixed #59

## [v1.1.5] - 21 Jun 2021

### Added

- Setup target updated inside `builder/Makefile`

### Changed

- `applbuild` modules relative imports
- Removed `setup.py` from `builder/`

## [v1.1.4] - 4 Apr 2021

### Added

- Cursors Preview with **shadows**
- use `clickgen.packagers` for packaging **X11/UNIX** cursors
- typing supports from `clickgen` (v1.1.9)
- Set clickgen version to v1.1.9 inside `builder/setup.py`
- `Pillow` version locked at **8.1.1** by clickgen **v1.1.9**
- **2 Space** format in `bitmapper`
- Sphinx based docsstring in `builder/applbuild`

### Changed

- Clean builder cache on every `make` commands
- Apple Cursors builder `applbuild` install as system level
- Removed python3 virtual environment from `builder/Makefile`
- **clean** target fixed in `builder/Makefile`
- Format `svg` files
- Add Shadows / Drop Shadows to arrow cursor fixed #45 (check 29ab657)
- Fixed Windows HiDPi issue #43 (check 7b49e34)

## [v1.1.3] - 21 Feb 2021

### Added

- Shadow underneath cursor #41 fixed

### Changed

- Preview with shadows cursors

## [v1.1.2] - 15 Feb 2021

### Added

- `reinstall` target added in project **makeFile**

### Changed

- Dynamic make install
- #39 Corner resize cursors are inverted fixed

## [v1.1.1] - 9 Feb 2021

### Changed

- Cursor is not in expected position fixed #37

## [v1.1.0] - 7 Feb 2021

### Added

- Smooth animation of `Animated Cursors`
- Auto-Package by `clickgen`
- Customize & Build with `make`
- Organized project
- Builder with `setup.py`
- Cursors design #33 **fixed**

### Changed

- Variable length frames render **fixed**
- Minimum frames rendering added.
- Windows cursors are renamed
- cursor's config moved to `builder/applbuild/constants.py`

## [v1.0.6] - 1 Nov 2020

### Added

- `left_ptr_watch` with **blue pinwheel**

### Changed

- `build.log` removed feature in **clickgen v1.1.8**
- Repack Windows cursors
- Removed npm scripts & documentation (`yon` package removed)
- npm dependencies got upgraded (**dependabot** 🤖 security warning)

## [v1.0.6] - 1 Nov 2020

### Added

- `left_ptr_watch` with **blue pinwheel**

### Changed

- Pixel match ratio set to **0.1** in `src\utils\matchImages.ts`
- Symlinks of `watch` cursor removed
- `AppStarting.ani` changed
- `PLING.bbcode` missing content fix
- Cursor **preview** updated
- `hand2` lines fixed.(from pling.com @peotincelogy)

## [v1.0.5] - 23 Oct 2020

### Added

- utils `getFrameName.ts` added.
- **22** cursor size added.

### Changed

- remove **Quick Install** using scripts.
- Windows **wrong resize** cursor fix.
- README.md docs & Table of Content refactor.

## [v1.0.4] - 25 Sept 2020

### Changed

- Product logo (on [imgur](https://i.imgur.com/GVLFmwF))
- fix wrong implementation vertical resize cursor in **KDE**
- Compressed files in `build` **GitHub Action**

## [v1.0.3] - 30 August 2020

### Changed

- `Windows Cursors Info` added in `src/svg/README.md` ([14d85f7](https://github.com/ful1e5/apple_cursor/commit/14d85f7ed289d681685e698eae4d0f205b6a3f3a))
- Quick install and Build Docs Improved
- Color palette Icons Changed to Semi-Circle
- Node Script with `yarn-or-npm` package ([2b026ea](https://github.com/ful1e5/apple_cursor/commit/2b026eab2cb96ff89839176297eacf80b340c7d6))
- Window **Config** Sorted ([acbbea2](https://github.com/ful1e5/apple_cursor/commit/acbbea24238fbfd43b405e4af73cc9f8b0101a59))
- Store actual data in `install.inf` in Windows Cursors.
- Build Logs stored to the `build.log` file
- Out Directories are `themes` and `bitmaps`
- Windows Cursors Package is Redesign
- `config.ts` cleanup

### Added

- Builder Version in `build` script
- Main method in `render`
- Bitmaps **Pixel** check in `Animated Cursors`
- New `utils` for **Frames Save**
- **OCS** Install support **as default** for Linux users

## [v1.0.2] - 10 August 2020

### Changed

- `hand2` and `left_ptr` hotspots alignments fixed.
- Smooth Animation with `35` Delay ([6698a56](https://github.com/ful1e5/apple_cursor/commit/6698a566c08c1f8e6a36ac7012c9a931dac2edf7))
- Ignored `docs` files (**.md ,LICENCE, **.bbcode) in `build` GitHub Actions. ([0df635b](https://github.com/ful1e5/apple_cursor/commit/0df635b1cdd18840606956f2188e735321f6f8b5))
- Windows Configs inside `config.py` ([e7d5092](https://github.com/ful1e5/apple_cursor/commit/e7d509295b69fbe43cdc3ea3000c493dcee47824))
- Redesign **Windows package** with `install.inf`. ([5f99e05](https://github.com/ful1e5/apple_cursor/commit/5f99e0565a5730165a498695bcbba4716108e82b))
- Remove **unnecessary** Windows Cursors. ([5f99e05](https://github.com/ful1e5/apple_cursor/commit/5f99e0565a5730165a498695bcbba4716108e82b))

### Added

- Cursors Preview, Build Dependencies, Runtime Dependencies and other Documents @ [README.md](https://github.com/ful1e5/apple_cursor/blob/main/README.md)
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- Quick Install (Windows & Linux) Documents @ [README.md](https://github.com/ful1e5/apple_cursor/blob/main/README.md) ([686bde5](https://github.com/ful1e5/apple_cursor/commit/686bde5eda5c4d913dd8c9df49aa94c20d24d9bf), [f36656d](https://github.com/ful1e5/apple_cursor/commit/f36656d1fbcce5c822d78f5964938daf1ad0c4c0))
- **install.sh** and **windows.inf**(automated installation files) added in `scripts` directory.
- Table Of Content in `README.md`([476c64a](https://github.com/ful1e5/apple_cursor/commit/476c64afda50ec48c576b566ce729b575608c529#diff-04c6e90faac2675aa89e2176d2eec7d8))

## [v1.0.1-beta] - 3 August 2020

### Changed

- `hand1 hand2 move` cursors finger gap & border in center
- Drop shadow & FPS(**62**) improvements in `wait, left_ptr_watch` cursors.
- Build size fix **65x65** to **64x64**. ([1120d17](https://github.com/ful1e5/apple_cursor/commit/1120d176636baff2aac1838ba316b4f420be7ca7))
- [Pling](https://www.pling.com/p/1408466/) product page Docs at `PLING.bbcode`.

## [v1.0.0-alpha1] - 31 July 2020

### Added

- Initial release 🎊
- Logo and badges
- CI/CD Pipelines

[unreleased]: https://github.com/ful1e5/apple_cursor/compare/v1.2.2...main
[v1.2.2]: https://github.com/ful1e5/apple_cursor/compare/v1.2.1...v1.2.2
[v1.2.1]: https://github.com/ful1e5/apple_cursor/compare/v1.2.0...v1.2.1
[v1.2.0]: https://github.com/ful1e5/apple_cursor/compare/v1.1.6...v1.2.0
[v1.1.6]: https://github.com/ful1e5/apple_cursor/compare/v1.1.5...v1.1.6
[v1.1.5]: https://github.com/ful1e5/apple_cursor/compare/v1.1.4...v1.1.5
[v1.1.4]: https://github.com/ful1e5/apple_cursor/compare/v1.1.3...v1.1.4
[v1.1.3]: https://github.com/ful1e5/apple_cursor/compare/v1.1.2...v1.1.3
[v1.1.2]: https://github.com/ful1e5/apple_cursor/compare/v1.1.1...v1.1.2
[v1.1.1]: https://github.com/ful1e5/apple_cursor/compare/v1.1.0...v1.1.1
[v1.1.0]: https://github.com/ful1e5/apple_cursor/compare/v1.0.6...v1.1.0
[v1.0.6]: https://github.com/ful1e5/apple_cursor/compare/1.0.5...v1.0.6
[v1.0.5]: https://github.com/ful1e5/apple_cursor/compare/1.0.4...v1.0.5
[v1.0.4]: https://github.com/ful1e5/apple_cursor/compare/1.0.3...1.0.4
[v1.0.3]: https://github.com/ful1e5/apple_cursor/compare/1.0.2...1.0.3
[v1.0.2]: https://github.com/ful1e5/apple_cursor/compare/1.0.1-beta...1.0.2
[v1.0.1-beta]: https://github.com/ful1e5/apple_cursor/compare/1.0.0-alpha1...1.0.1-beta
[v1.0.0-alpha1]: https://github.com/ful1e5/apple_cursor/tree/1.0.0-alpha1
