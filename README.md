<!-- Branding -->
<p align="center">
    <img src="https://imgur.com/17W62gp.png" width="120" alt="macOS Big Sur" />
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
    <img alt="Puppeteer version" src="https://img.shields.io/github/package-json/dependency-version/ful1e5/apple_cursor/puppeteer">
  </a>

  <a href="https://github.com/ful1e5/clickgen">
    <img alt="Clickgen" src="https://img.shields.io/badge/theme%20builder-clickgen-FD0542" />
  </a>
  
  <!-- Second Row -->
  <br />
  <a href="https://github.com/ful1e5/apple_cursor/releases">
    <img alt="Apple Cursor release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/ful1e5/apple_cursor?include_prereleases" />
  </a>

  <a href="https://github.com/ful1e5/apple_cursor/blob/master/LICENSE">
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

Enjoy upcoming **[macOS BigSur](https://www.apple.com/macos/big-sur-preview/)** Cursor Theme for `Windows` and `Linux` with _HiDPi Support_ 🎉

#### Cursor Sizes: 24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96

#### Colors:

- ![#000000](https://placehold.it/15/000/000000?text=+) `#000000`
- ![#fffff](https://placehold.it/15/fff/000000?text=+) `#fffff`
- ![#13A3F5](https://placehold.it/15/13A3F5/000000?text=+) `#13A3F5`
- ![#4DCB2C](https://placehold.it/15/4DCB2C/000000?text=+) `#4DCB2C`
- ![#FED103](https://placehold.it/15/FED103/000000?text=+) `#FED103`
- ![#FE9D0C](https://placehold.it/15/FE9D0C/000000?text=+) `#FE9D0C`
- ![#F2493C](https://placehold.it/15/F2493C/000000?text=+) `#F2493C`
- ![#B75DCC](https://placehold.it/15/B75DCC/000000?text=+) `#B75DCC`

#### Preview:

<!-- Preview -->

<p align="center">
  <img title="macOS Big Sur" src="https://imgur.com/BA0gkrO.png">
  </br>
  <sub>macOS Big Sur</sub>
</p>

<!-- Build Dependencies -->

# Dependencies

## Runtime Dependencies

- libxcursor-dev
- libx11-dev
- libpng-dev (<=1.6)

#### Install Runtime Dependencies

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
  sudo dnf install libx11-devel libxcursor-devel libpng-devel
```

## Build Dependencies

- nodejs (<=12.x.x)
- yarn
- python (<=3.6)
- pip3

<!-- Install -->

# Install

## Basic Installation

Download latest `stable` & `development` from [here](https://github.com/ful1e5/apple_cursor/releases) according to your **OS**.

### Linux/X11

<!-- Install Video  -->
<p align="center">
  <video src="https://i.imgur.com/zIF1JkH.mp4" width="75%" autoplay loop preload></video>
</p>

```bash
# Unpack
mkdir macOSBigSur && tar -xvf macOSBigSur.tar -C macOSBigSur
# For local users
mv macOSBigSur ~/.icons/
# For all users
sudo mv macOSBigSur /usr/share/icons/
```

### Windows

1. Open the `settings` app.
2. **Goto** `Devices` -> `Mouse` -> `Additional Mouse Options`.
3. **Goto** the `pointers` tab.
4. Replace each cursor in the currently applied cursor set with the corresponding cursor in the `mac OsBigSur Windows Theme` folder.
5. Click "**save as**" and type in the desired name.
6. Click "**apply**" and "**ok**".

## Manual Install

> Make sure you have installed all [Build dependencies](#build-dependencies).

### ⚡ Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **master** and **dev** branchs) and `pull request`(on **master** branch), You found theme resources in `artifact` section of **build**.You found all **Actions** in [.github/workflows](https://github.com/ful1e5/apple_cursor/tree/master/.github/workflows) directory.

### Build

```bash
# This command setup python virtual environment && install all packages
yarn setup
# Build & Unpack built cursor theme
yarn compile && yarn unpack
```

After build `bitmaps` and `packages` are generated at project root directory.

### Install Build Cursor

All builded cursor packages are available inside `packages` directory.

```bash
cd ./packages
# Unpack .tar archive
mkdir macOSBigSur && tar -xvf macOSBigSur.tar -C macOSBigSur
# clean old version & install new build version to local user (recommended)
rm -rf ~/.icons/macOSBigSur && cp macOSBigSur ~/.icons/
```

<!-- Bug Report -->

# Bugs

Bugs 🐛 should be reported [here](https://github.com/ful1e5/apple_cursor/issues) on the Github issues page.

<!-- Help -->

# Getting Help

You can create a **issue**, I will help you. 🙂

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
<p align="center">I'm Using Katana </p>
