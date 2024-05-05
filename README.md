# Apple Cursor

![Apple Cursor](https://github.com/ful1e5/apple_cursor/assets/24286590/ad260d52-6534-441b-902d-440cb368b5c9)
Open source macOS Cursors for `Windows` and `Linux` with _HiDPI Support_ .

[![Build](https://github.com/ful1e5/apple_cursor/workflows/build/badge.svg)](https://github.com/ful1e5/apple_cursor/actions?query=workflow%3Abuild)

## Notes

-   All cursor's SVG files are found in [svg](./svg) directory or you can also find them on
    [Figma](https://www.figma.com/file/OZw8Ylb9xPFw9h1uZYSMFa/apple_cursor?type=design&node-id=73%3A2&mode=design&t=dLILPgJJrLKeAcTE-1).

<!-- If you're interested, you can learn more about "sponsor-spotlight" on
 https://dev.to/ful1e5/lets-give-recognition-to-those-supporting-our-work-on-github-sponsors-b00 -->

![shoutout-sponsors](https://sponsor-spotlight.vercel.app/sponsor?login=ful1e5)

-   **2024-02-23**: https://github.com/ful1e5/apple_cursor/commit/07767c24b0c5dbf912cf37350b86adc11671a18e `bitmaps` directory removed,
    and `macOS Monterey` cursors deprecated.

---

![macOS](https://github.com/ful1e5/apple_cursor/assets/24286590/07018988-36ee-4913-adc7-365854629a20)
![macOS white](https://github.com/ful1e5/apple_cursor/assets/24286590/1d2bcdf5-d3d7-420a-8dae-68c31b191216)

## Cursor Sizes

### Xcursor Sizes:

<kbd>16</kbd>
<kbd>20</kbd>
<kbd>22</kbd>
<kbd>24</kbd>
<kbd>28</kbd>
<kbd>32</kbd>
<kbd>40</kbd>
<kbd>48</kbd>
<kbd>56</kbd>
<kbd>64</kbd>
<kbd>72</kbd>
<kbd>80</kbd>
<kbd>88</kbd>
<kbd>96</kbd>

### Windows Cursor Size:

| size | Regular (× ²⁄₃) | Large (× ⁴⁄₅) | Extra-Large (× 1) |
| ---: | --------------: | ------------: | ----------------: |
|   32 |     21.333 → 22 |     25.6 → 26 |                32 |
|   48 |              32 |     38.4 → 39 |                48 |
|   64 |     42.666 → 43 |     51.2 → 52 |                64 |
|   96 |              64 |     76.8 → 77 |                96 |
|  128 |     85.333 → 86 |   102.4 → 103 |               128 |
|  256 |   170.666 → 171 |   204.8 → 205 |               256 |

## Colors

### Default

-   Base Color - `#000000` (Black)
-   Outline Color - `#FFFFFF` (White)

### White

-   Base Color - `#FFFFFF` (White)
-   Outline Color - `#000000` (Black)

## How to get it

You can download latest `stable` & `development` releases from
[Release Page](https://github.com/ful1e5/apple_cursor/releases).

### Packages

> **Note**
> If you're having trouble with the packages please submit a request to the package maintainer
> before creating an issue.

#### Arch Linux/Manjaro

Arch Linux/Manjaro users can install from the [AUR](https://aur.archlinux.org/packages/apple_cursor)
currently maintained by [_ful1e5_](https://aur.archlinux.org/account/ful1e5) &
[_Grelek_](https://aur.archlinux.org/account/Grelek) .
Can be installed via Pamac (preinstalled in Manjaro), Paru or any other
[AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers).

```bash
paru -S apple_cursor
```

## Installing Apple Cursor

#### Linux/X11

**Installation:**

```bash
tar -xvf macOS.tar.gz                      # extract `.tar.gz`
mv macOS* ~/.icons/                        # Install to local users
sudo mv macOS* /usr/share/icons/           # Install to all users
```

**Uninstallation:**

```bash
rm ~/.icons/macOS*                         # Remove from local users
sudo rm /usr/share/icons/macOS*            # Remove from all users
```

#### Windows

**Installation:**

1. Unzip `.zip` file
2. Open unziped directory in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open Control Panel > Personalization and Appearance > Change mouse pointers,
   and select **macOS Cursors**.
5. Click '**Apply**'.

**Uninstallation:**

Run the `uninstall.bat` script packed with the `.zip` archive

**OR** follow these steps:

1. Go to **Registry Editor** by typing the same in the _start search box_.
2. Expand `HKEY_CURRENT_USER` folder and expand `Control Panel` folder.
3. Go to `Cursors` folder and click on `Schemes` folder - all the available custom cursors that are
   installed will be listed here.
4. **Right Click** on the name of cursor file you want to uninstall; for eg.: _macOS Cursors_ and
   click `Delete`.
5. Click '**yes**' when prompted.

## Build From Source

### Prerequisites

-   Python version 3.7 or higher
-   [clickgen](https://github.com/ful1e5/clickgen)>=2.1.8 (`pip install clickgen`)
-   [yarn](https://github.com/yarnpkg/yarn)

### Quick start

1. Install [build prerequisites](#prerequisites) on your system
2. `git clone https://github.com/ful1e5/apple_cursor`
3. `cd apple_cursor`
4. `yarn install`
5. `yarn generate`
6. See [Installing Apple Cursor](#installing-apple-cursor).

### Getting Started

Once you have the [build prerequisites](#prerequisites) installed, You can personalize colors,
customize sizes, change target platforms, and more. This process involves using external tools,
as this repository only contains SVG files and configuration for these tools:

-   [cbmp](https://github.com/ful1e5/cbmp): Used for customizing colors and generating PNG files.
-   [ctgen](https://github.com/ful1e5/clickgen): Used for customizing sizes and building XCursor and Windows Cursors.

You can refer to the README of each tool for more information on their command-line options.

#### Crafting Your Apple Cursor

The process of creating custom cursor themes involves two main steps:

1. Rendering SVG files to PNG files.
2. Building cursor themes from PNG files.

#### Customize Colors

`cbmp` provides three options for changing colors:

1. `-bc`: Base color, which replaces the `#00FF00` color in the SVG.
2. `-oc`: Outlined color, which replaces the `#0000FF` color in the SVG.
3. `-wc` (optional): Watch Background color, which replaces the `#FF0000` color in the SVG.

```bash
npx cbmp [...] -bc '<hex>' -oc '<hex>' -wc '<hex>'
```

Alternatively, you can provide a JSON configuration file to render SVG files, which contains a sequence of `cbmp` commands:

```bash
npx cbmp render.json
```

#### Customize Sizes

##### Customize Windows Cursor size

To build Windows cursor with size `16`:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/macOS' -n 'macOS' -c 'macOS Cursors with size 16'
```

You can also customize output directory with `-o` option:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/macOS' -o 'out' -n 'macOS' -c 'macOS Cursors with size 16'
```

##### Customize XCursor size

To build XCursor with size `16`:

```bash
ctgen build.toml -s 16 -p x11 -d 'bitmaps/macOS' -n 'macOS' -c 'macOS XCursors with size 16'
```

You can also assign multiple sizes to `ctgen` for XCursors build:

```bash
ctgen build.toml -s 16 24 32 -p x11 -d 'bitmaps/macOS' -n 'macOS' -c 'Custom Sizes macOS XCursors'
```

#### Examples

Lets generate macOS cursor with green and black colors:

```bash
npx cbmp -d 'svg' -o 'bitmaps/macOS-Hacker' -bc '#00FE00' -oc '#000000'
```

After rendering custom color you have to build cursor through `ctgen`:

```bash
ctgen build.toml -d 'bitmaps/macOS-Hacker' -n 'macOS-Hacker' -c 'Green and Black macOS cursors.'
```

Afterwards, Generated theme can be found in the `themes` directory.

###### macOS Gruvbox

```bash
npx cbmp -d 'svg' -o 'bitmaps/macOS-Gruvbox' -bc '#282828' -oc '#EBDBB2' -wc '#000000'
ctgen build.toml -d 'bitmaps/macOS-Gruvbox' -n 'macOS-Gruvbox' -c 'Groovy macOS cursors.'
```

###### macOS Solarized Dark

```bash
npx cbmp -d 'svg' -o 'bitmaps/macOS-Solarized-Dark' -bc '#002b36' -oc '#839496' -wc '#000000'
ctgen build.toml -d 'bitmaps/macOS-Solarized-Dark' -n 'macOS-Solarized-Dark' -c 'Solarized Dark macOS cursors.'
```

###### macOS Solarized Light

```bash
npx cbmp -d 'svg' -o 'bitmaps/macOS-Solarized-Light' -bc '#839496' -oc '#002b36'
ctgen build.toml -d 'bitmaps/macOS-Solarized-Light' -n 'macOS-Solarized-Light' -c 'Solarized Light macOS cursors.'
```

###### macOS Dracula

```bash
npx cbmp -d 'svg' -o 'bitmaas/macOS-Dracula' -bc '#282a36' -oc '#f8f8f2'
ctgen build.toml -d 'bitmaps/macOS-Dracula' -n 'macOS-Dracula' -c 'Dracula macOS cursors.'
```

## Testing Cursor

There are several websites that allow you to test your cursor states by hovering over buttons. This can be very useful when developing or verifying the behavior of a cursor. The following websites cover many of the most commonly used cursors, although they may not include all available options.

-   [Cursor-Test](https://vibhorjaiswal.github.io/Cursor-Test/)
-   [Mozilla CSS Cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)

For a blueprint for creating XCursors, you may also want to refer to [Cursor-demo](https://wiki.tcl-lang.org/page/Cursor+demo).

## Credit

[Adwaita](https://github.com/GNOME/adwaita-icon-theme) ·
[Dmz](https://github.com/GalliumOS/dmz-cursor-theme) ·
[Yaru](https://github.com/ubuntu/yaru)
