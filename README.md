# Apple Cursor

Open source macOS Cursors for `Windows` and `Linux` with _HiDPI Support_ .

[![Build](https://github.com/ful1e5/apple_cursor/workflows/build/badge.svg)](https://github.com/ful1e5/apple_cursor/actions?query=workflow%3Abuild)

## Apple Cursor needs your Input

Until 2021 my cursors projects were well funded by [pling.com](https://www.pling.com) but since the
[pling-factor](https://www.pling.com/terms/payout) on the website has decreased and monthly payments
are <500$, It is now dependent on community funding and sponsorships. If you want to help me to maintain
this project and my other open source projects actively, consider sponsoring my work on [GitHub Sponsor](https://github.com/sponsors/ful1e5)
or DM me on [Twitter](https://twitter.com/ful1e5) if your company would like to support my projects,
I will gladly look into it and post your avatar in the project's README.

I appreciate all the wonderful people who patronize and sponsoring my work.

## Sponsors

<!-- Add your name or avatar here with the Pull Request in case I missed it. -->

N/A

---

![macOSMonterey](https://imgur.com/bmS0fRT.png)
![macOSMonterey White](https://imgur.com/s0nqcje.png)
![macOSBigSur](https://imgur.com/Q022eSp.png)
![macOSBigSur White](https://imgur.com/SFVR945.png)

> **Note**
> All cursor's `.svg` files are found in [svg](./svg) directory or you can also find them on
> [Figma](https://www.figma.com/file/OZw8Ylb9xPFw9h1uZYSMFa/Mac-Cursor?node-id=0%3A1).

## Cursor Sizes

### Xcursor Sizes:

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

- <kbd>16x16</kbd> - Small
- <kbd>24x24</kbd> - Regular
- <kbd>32x32</kbd> - Large
- <kbd>48x48</kbd> - Extra Large

## Colors

### Default

- Base Color - `#000000` (Black)
- Outline Color - `#FFFFFF` (White)

### White

- Base Color - `#FFFFFF` (White)
- Outline Color - `#000000` (Black)

## How to get it

You can download latest `stable` & `development` releases from
[Release Page](https://github.com/ful1e5/apple_cursor/releases).

## Installing Apple Cursor

#### Linux/X11

**Installation:**

```bash
tar -xvf macOS-Bigsur.tar.gz                # extract `.tar.gz`
mv macOS-* ~/.icons/                        # Install to local users
sudo mv macOS-* /usr/share/icons/           # Install to all users
```

**Uninstallation:**

```bash
rm ~/.icons/macOS-*                         # Remove from local users
sudo rm /usr/share/icons/macOS-*            # Remove from all users
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

#### Notes

- Apple Cursor's build configuration and cursor hotspot settings are bundled in the `build.toml` file.
- Check out the scripts section in [package.json](./package.json) to see how we build the cursor theme,
  excluding the render scripts. They are useful for converting `.svg` files to `.png` files.
- yarn is optional, For building XCursors and Windows cursors from `.png` files or resizing them
  you don't need that. If you want to develop/modify Apple Cursor's colors, and bitmaps, or generate a png
  file from a svg, Then you can use yarn because bitmapper is written in TypeScript.
- Since macOS Bigsur and macOS Monterey are designed similarly, they share the same hotspot settings so a
  single configuration file `build.toml` is responsible for building all variants. Due to this, you will have
  to change the following options in `ctgen` to build the appropriate variant:
  - **-d**: bitmaps directory
  - **-n**: The name you want to give to the generated theme.
  - **-c**: Theme comment.
  - See `ctgen --help` for all available options.

### Build prerequisites

- Python version 3.7 or higher
- [clickgen](https://github.com/ful1e5/clickgen)>=2.1.2 (`pip install clickgen`)
- [yarn](https://github.com/yarnpkg/yarn)

### Quick start

1. Install [build prerequisites](#build-prerequisites) on your system
2. `git clone https://github.com/ful1e5/apple_cursor`
3. `cd apple_cursor && yarn build`
4. See [Installing Apple Cursor](#installing-apple-cursor).

### Building

> **Note**
> Bitmaps are already generated in the `bitmaps` directory and **managed by the maintainer**
> (do not edit them directly).

First make sure you installed the [build prerequisites](#build-prerequisites).
Now that you have the dependencies, you can try build individual themes from bitmaps and
customize sizes, target platform, and etc. with the `ctgen` CLI (packed with `clickgen`).

#### `yarn build` aberration

Here are the default commands we used to build the macOS variants and packed them into `yarn build`:

```bash
npx cbmp -d 'svg/bigsur' -n 'macOS-BigSur' -bc '#000000' -oc '#FFFFFF'
npx cbmp -d 'svg/bigsur' -n 'macOS-BigSur-White' -bc '#FFFFFF' -oc '#000000'

npx cbmp -d 'svg/monterey' -n 'macOS-Monterey' -bc '#000000' -oc '#FFFFFF'
npx cbmp -d 'svg/monterey' -n 'macOS-Monterey-White' -bc '#FFFFFF' -oc '#000000'
```

Afterwards, the themes can be found in the `themes` directory.

#### Customize Sizes

> **Note**
> You can change the cursor size up to 200 because pngs are rendered with 200x200.
> If the cursor is resized by more than rendered png size, the final cursor will be blurred.

##### Customize Windows Cursor size

To build Windows cursor with size `16`:

> **Warning**
> Windows cursor supports only one size, if multiple sizes are given with `-s` the first size will
> be considered in build.

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/macOS-BigSur' -n 'macOS-BigSur' -c 'macOS Big Sur Windows Cursors with size 16'
```

You can also customize output directory with `-o` option:

```bash
ctgen build.toml -s 16 -p windows -d 'bitmaps/macOS-BigSur' -o 'out' -n 'macOS-BigSur' -c 'macOS Big Sur Windows Cursors with size 16'
```

##### Customize XCursor size

To build XCursor with size `16`:

```bash
ctgen build.toml -s 16 -p x11 -d 'bitmaps/macOS-BigSur' -n 'macOS-BigSur' -c 'macOS Big Sur XCursors with size 16'
```

You can also assign multiple sizes to `ctgen` for XCursors build:

```bash
ctgen build.toml -s 16 24 32 -p x11 -d 'bitmaps/macOS-BigSur' -n 'macOS-BigSur' -c 'Custom Sizes macOS Big Sur XCursors'
```

#### Customize Colors

To customize cursors color you have to install node dependencies with `yarn install` command.
After installing dependencies you can customize the colors via `npx cbmp` Node CLI App which packed with
[cbmp](https://github.com/ful1e5/cbmp) node package.

##### `yarn render` aberration

Here are the default commands we used for generating the macOS bitmaps and packed them into `yarn render`:

```bash
npx cbmp -d 'svg/bigsur' -n 'macOS-BigSur' -bc '#000000' -oc '#FFFFFF'
npx cbmp -d 'svg/bigsur' -n 'macOS-BigSur-White' -bc '#FFFFFF' -oc '#000000'
npx cbmp -d 'svg/monterey' -n 'macOS-Monterey' -bc '#000000' -oc '#FFFFFF'
npx cbmp -d 'svg/monterey' -n 'macOS-Monterey-White' -bc '#FFFFFF' -oc '#000000'
```

#### Examples

Lets generate Big Sur cursor with green base color and black outline:

```bash
npx cbmp -d 'svg/bigsur' -n 'macOS-BigSur-Hacker' -bc '#00FE00' -oc '#000000'
```

After rendering custom color you have to build cursor through `ctgen`:

```bash
ctgen build.toml -d 'bitmaps/macOS-BigSur-Hacker' -n 'macOS-BigSur-Hacker' -c 'Green and black macOS Big Sur cursors.'
```

Afterwards, Generated theme can be found in the `themes` directory.

###### macOS Gruvbox

```bash
npx cbmp -d 'svg/monterey' -n 'macOS-Gruvbox' -bc '#282828' -oc '#EBDBB2'
ctgen build.toml -d 'bitmaps/macOS-Gruvbox' -n 'macOS-Gruvbox' -c 'Groovy macOS cursors.'
```

###### macOS Solarized Dark

```bash
npx cbmp -d 'svg/monterey' -n 'macOS-Solarized-Dark' -bc '#002b36' -oc '#839496'
ctgen build.toml -d 'bitmaps/macOS-Solarized-Dark' -n 'macOS-Solarized-Dark' -c 'Solarized Dark macOS cursors.'
```

###### macOS Solarized Light

```bash
npx cbmp -d 'svg/bigsur' -n 'macOS-Solarized-Light' -bc '#839496' -oc '#002b36'
ctgen build.toml -d 'bitmaps/macOS-Solarized-Light' -n 'macOS-Solarized-Light' -c 'Solarized Light macOS cursors.'
```

###### macOS Dracula

```bash
npx cbmp -d 'svg/bigsur' -n 'macOS-Dracula' -bc '#282a36' -oc '#f8f8f2'
ctgen build.toml -d 'bitmaps/macOS-Dracula' -n 'macOS-Dracula' -c 'Dracula macOS cursors.'
```

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.
