<!-- Branding -->
<p align="center">
    <img src="https://i.imgur.com/GVLFmwF.png" width="120" alt="macOS Big Sur" />
</p>

<p align="center">
    🍎 macOS Cursor Theme
</p>

<!-- Badges -->
<p align="center">
  <!-- First Row -->
  <a href="https://github.com/ful1e5/apple_cursor/actions?query=workflow%3Abuild">
    <img alt="GitHub Action Build" src="https://github.com/ful1e5/apple_cursor/workflows/build/badge.svg" width="102" />
  </a>

  <a href="https://www.codefactor.io/repository/github/ful1e5/apple_cursor">
    <img  alt="CodeFactor" src="https://www.codefactor.io/repository/github/ful1e5/apple_cursor/badge" />
  </a>

  <!-- Second Row -->
  </br >
  <a href="https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html">
    <img alt="npm type definitions" src="https://img.shields.io/npm/types/typescript">
  </a>

  <a href="https://github.com/puppeteer/puppeteer/">
    <img alt="Puppeteer version" src="https://img.shields.io/github/package-json/dependency-version/ful1e5/apple_cursor/puppeteer?filename=bitmapper%2Fpackage.json">
  </a>

  <a href="https://github.com/ful1e5/clickgen">
    <img alt="Clickgen" src="https://img.shields.io/badge/theme%20builder-clickgen-FD0542" />
  </a>

  <!-- Second Row -->
  <br />
  <a href="https://github.com/ful1e5/apple_cursor/releases">
    <img alt="Apple Cursor release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/ful1e5/apple_cursor?include_prereleases" />
  </a>

  <a href="https://github.com/ful1e5/apple_cursor/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/ful1e5/apple_cursor?color=0081FB" />
  </a>

  <!-- Third Row -->
  <br />
  <a href="https://www.pling.com/p/1408466#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Linux-grey?logo=linux" />
  </a>

  <a href="https://www.pling.com/p/1408466#files-panel">
    <img alt="License" src="https://img.shields.io/badge/-Windows-blue?logo=windows" />
  </a>

  <a href="https://www.python.org/">
    <img alt="License" src="https://img.shields.io/badge/-Python-yellow?logo=python" />
  </a>
 <!-- Fourth Row -->
  <br />
  <a href="https://github.com/ful1e5">
    <img alt="Made By Kaiz"  src="https://kaiz.vercel.app/api/badge" width="133" />
  </a>
</p>

---

<!-- Intro -->

# Apple Cursor

Enjoy **[macOS Big Sur](https://www.apple.com/macos/big-sur-preview/)** Cursor Theme for `Windows` and `Linux` with _HiDPI Support_ 🎉.

<!-- Table Of Content -->
<details>
 <summary><strong>Table of Contents</strong> (click to expand)</summary>

-   [Apple Cursor](#apple-cursor)
    -   [Cursor Sizes](#cursor-sizes)
    -   [Colors](#colors)
    -   [Quick install](#quick-install)
    -   [Manual Install](#manual-install)
        -   [Linux/X11](#linuxx11)
        -   [Windows](#windows)
        -   [Preview:](#preview)
-   [Dependencies](#dependencies)
    -   [External Libraries](#external-libraries)
        -   [Install External Libraries](#install-external-libraries)
            -   [macOS](#macos)
            -   [Debain/ubuntu](#debainubuntu)
            -   [ArchLinux/Manjaro](#archlinuxmanjaro)
            -   [Fedora/Fedora Silverblue/CentOS/RHEL](#fedorafedora-silverbluecentosrhel)
    -   [Build Dependencies](#build-dependencies)
        -   [Node Packages](#node-packages)
        -   [PyPi Packages](#pypi-packages)
    -   [Build From Scratch](#build-from-scratch)
        -   [⚡ Auto Build (using GitHub Actions)](#-auto-build-using-github-actions)
        -   [Manual Build](#manual-build)
            -   [Build `XCursor` theme](#build-xcursor-theme)
            -   [Customize `XCursor` size](#customize-xcursor-size)
            -   [Install `XCursor` theme](#install-xcursor-theme)
            -   [Build `Windows` theme](#build-windows-theme)
            -   [Customize `Windows Cursor` size](#customize-windows-cursor-size)
-   [Bugs](#bugs)
-   [Getting Help](#getting-help)
-   [Contributing](#contributing)
    -   [Support](#support)

</details>

#### Cursor Sizes

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

#### Colors

![#13A3F5](https://imgur.com/m0JhD7W.png)
![#4DCB2C](https://imgur.com/wtyqDHv.png)
![#FED103](https://imgur.com/5km5GW6.png)
![#FE9D0C](https://imgur.com/Gx2eGbm.png)
![#F2493C](https://imgur.com/hl22EPB.png)
![#B75DCC](https://imgur.com/wev8rfw.png)
![#000000](https://imgur.com/24cocpe.png)
![#fffff](https://imgur.com/YyhMKNT.png)

#### Quick install

<p align="center">
  <a href="https://www.pling.com/p/1408466/" >
    <img title="macOSBig Sur Pling Store" width="40%" src="https://imgur.com/VxSgrWw.png">
  </a>
</p>

### Manual Install

#### Linux/X11

```bash
# extract `macOSBigSur.tar.gz`
tar -xvf macOSBigSur.tar.gz

# For local users
mv macOSBigSur ~/.icons/

# For all users
sudo mv macOSBigSur /usr/share/icons/
```

#### Windows

1. unzip `macOSBigSur_Windows.zip` file
2. Open `macOSBigSur_Windows/` in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open _Control Panel > Personalization and Appearance > Change mouse pointers_, and select **MacOSBigSur Cursors**.
5. Click '**Apply**'.

#### Preview:

> Check Figma file [here](https://www.figma.com/file/OZw8Ylb9xPFw9h1uZYSMFa/Mac-Cursor?node-id=0%3A1)

<!-- Preview -->

<p align="center">
  <img title="macOS Big Sur" src="https://imgur.com/7k7HBWi.png">
  </br>
  <sub>macOSBigSur Cursors 🍎</sub>
</p>

<!-- Build Dependencies -->

# Dependencies

## External Libraries

-   libxcursor
-   libx11
-   libpng (<=1.6)

#### Install External Libraries

##### macOS

```bash
brew install --cask xquartz
brew install libpng
```

##### Debain/ubuntu

```bash
sudo apt install libx11-dev libxcursor-dev libpng-dev
```

##### ArchLinux/Manjaro

```bash
sudo pacman -S libx11 libxcursor libpng
```

##### Fedora/Fedora Silverblue/CentOS/RHEL

```bash
sudo dnf install libX11-devel libXcursor-devel libpng-devel
```

## Build Dependencies

-   [gcc](https://gcc.gnu.org/install/)
-   [make](https://www.gnu.org/software/make/)
-   [nodejs](https://nodejs.org/en/) (<=12.x.x)
-   [yarn](https://classic.yarnpkg.com/en/docs/install/)
-   [python](https://www.python.org/downloads/) (<=3.8)
-   [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

-   [puppeteer](https://www.npmjs.com/package/puppeteer)
-   [pngjs](https://www.npmjs.com/package/pngjs)
-   [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

-   [clickgen](https://pypi.org/project/clickgen/s)

## Build From Scratch

### ⚡ Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **main** and **dev** branches) and `pull request`(on **main** branch), You found theme resources in `artifact` section of **build**.GitHub **Actions** source is available inside [.github/workflows](https://github.com/ful1e5/apple_cursor/tree/main/.github/workflows) directory.

### Manual Build

```bash
make
```

#### Build `XCursor` theme

```bash
make unix
```

#### Customize `XCursor` size

```bash
make unix X_SIZES=22            # Only built '22px' pixel-size.
make unix X_SIZES=22 24 32      # Multiple sizes are provided with  ' '(Space)
```

#### Install `XCursor` theme

```bash
make install            # install as user
  # OR
sudo make install       # install as root
```

#### Build `Windows` theme

```bash
make windows
```

#### Customize `Windows Cursor` size

```bash
make windows WIN_SIZE=96            # Supports only one pixel-size
```

> For installation follow [these](#windows) steps.

<!-- Bug Report -->

# Bugs

Bugs 🐛 should be reported [here](https://github.com/ful1e5/apple_cursor/issues) on the Github issues page.

<!-- Help -->

# Getting Help

You can create a **issue**, I will help you. 🙂

<!-- Contributions and Suggestion -->

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.

<!-- Support -->

## Support

Give a **★** or Follow on [GitHub](https://github.com/ful1e5),That's work as **Steroid 💉** for me. 😉

> For more support

<a href="https://www.buymeacoffee.com/Nt7Wg4V" target="_blank">
  <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" >
</a>

<!-- Ninja  -->

<h1 align="center">
  ( `ω´ )۶▬ι═══════ﺤ
</h1>
<p align="center">
  <sub>I'm Using Katana </sub>
</p>
