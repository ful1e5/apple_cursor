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

Enjoy upcoming **[macOS BigSur](https://www.apple.com/macos/big-sur-preview/)** Cursor Theme for `Windows` and `Linux` with _HiDPi Support_ 🎉.

<!-- Table Of Content -->
<details>
 <summary><strong>Table of Contents</strong> (click to expand)</summary>

- [Apple Cursor](#apple-cursor)
  - [Cursor Sizes](#cursor-sizes)
  - [Colors](#colors)
  - [Quick Install For Linux](#quick-install)
  - [Manual Install](#manual-install)
    - [Linux Install](#linux/x11)
    - [Windows Install](#windows)
  - [Cursors Preview](#preview)
- [Dependencies](#dependencies)
  - [Runtime Dependencies](#runtime-dependencies)
  - [Build Dependencies](#build-dependencies)
- [Build From Scrach](#build-from-scratch)
  - [⚡ Auto Build (using GitHub Actions)](#⚡-auto-build-using-gitHub-actions)
  - [Manual build](#manual-build)
    - [Setup Python Environment](#setup-python-environment)
    - [Compile Theme using yarn](#using-yarn)
    - [Compile Theme using npm](#using-npm)
  - [Install Build Theme](#install-build-theme)
- [Bugs](#bugs)
- [Getting Help](#getting-help)
- [Contributing](#contributing)
- [Support ✨](#support)

</details>

#### Cursor Sizes

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

##### via curl

```bash
bash <(curl -s "https://raw.githubusercontent.com/ful1e5/apple_cursor/master/scripts/install.sh")
```

##### via wget

```bash
bash <(wget -qO- "https://raw.githubusercontent.com/ful1e5/apple_cursor/master/scripts/install.sh")
```

### Manual Install

#### Linux/X11

<!-- Install Video  -->
<!-- <p align="center">
  <video src="https://i.imgur.com/zIF1JkH.mp4" width="75%" autoplay loop preload></video>
</p> -->

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
3. Click 'Install' from the context menu, and authorise the modifications to your system.
4. Open _Control Panel > Personalisation and Appearance > Change mouse pointers_, and select **MacOSBigSur Cursors**.
5. Click '**Apply**'.

#### Preview:

> Detailed Cursors Informations inside [src/svgs/README.md](https://github.com/ful1e5/apple_cursor/blob/master/src/svg/README.md)

<!-- Preview -->

<p align="center">
  <img title="macOS Big Sur" src="https://imgur.com/BA0gkrO.png">
  </br>
  <sub>macOSBigSur Cursors 🍎</sub>
</p>

<!-- Build Dependencies -->

# Dependencies

## Runtime Dependencies

- libxcursor-dev
- libx11-dev
- libpng-dev (<=1.6)

#### Install Runtime Dependencies

##### macOS

```bash
brew cask install xquartz libpng
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
sudo dnf install libx11-devel libxcursor-devel libpng-devel
```

## Build Dependencies

- [nodejs](https://nodejs.org/en/) (<=12.x.x)
- [yarn](https://classic.yarnpkg.com/en/docs/install/) / [npm](https://docs.npmjs.com/cli/install.html)
- [python](https://www.python.org/downloads/) (<=3.6)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

#### devDependencies

- [@types/puppeteer](https://www.npmjs.com/package/@types/puppeteer)
- [@types/pngjs](https://www.npmjs.com/package/@types/pngjs)
- [@types/pixelmatch](https://www.npmjs.com/package/@types/pixelmatch)
- [nodemon](https://www.npmjs.com/package/nodemon)
- [ts-node](https://www.npmjs.com/package/ts-node)
- [tslint](https://www.npmjs.com/package/tslint)
- [typescript](https://www.npmjs.com/package/typecript)

#### dependencies

- [puppeteer](https://www.npmjs.com/package/puppeteer)
- [pngjs](https://www.npmjs.com/package/pngjs)
- [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

- [clickgen](https://pypi.org/project/clickgen/s)
- [Pillow](https://pypi.org/project/Pillow/)

## Build From Scratch

### ⚡ Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **master** and **dev** branches) and `pull request`(on **master** branch), You found theme resources in `artifact` section of **build**.GitHub **Actions** available inside [.github/workflows](https://github.com/ful1e5/apple_cursor/tree/master/.github/workflows) directory.

### Manual Build

#### Setup python environment

```bash
python3 -m pip install --upgrade pip                 # Update pip to latest
python3 -m pip3 install virtualenv                   # Install python virtual environment
virtualenv venv                                      # Create new virtualenv named `venv`
source venv/bin/activate                             # Activate virtualenv

# For Deactivate virtualenv
deactivate
```

#### Compile From Source

> Make sure your [python environment](#setup-python-environment) setup and `virtualenv` is **active**.

##### Using yarn

```bash
yarn install                                         # Install all Node Packages
yarn py_install                                      # Install all PyPi Packages
yarn compile                                         # Compile the cursor theme
```

##### Using npm

```bash
npm install                                          # Install all Node Packages
npm py_install                                       # Install all PyPi Packages
npm compile                                          # Compile the cursor theme
```

After build `bitmaps` and `themes` directory are generated at project **root**.

### Install Build Theme

All builded cursor themes are available inside `themes` directory.

#### Linux

```bash
cd ./themes
rm -rf ~/.icons/macOSBigSur && cp macOSBigSur ~/.icons/   # installing Theme to local user(recommend)
```

#### Windows

1. unzip `macOSBigSur_Windows.zip` file
2. Open the `settings` app.
3. **Goto** `Devices` -> `Mouse` -> `Additional Mouse Options`.
4. **Goto** the `pointers` tab.
5. Replace each cursor in the currently applied cursor set with the corresponding cursor in the `macOSBigSur_Windows` folder.
6. Click "**save as**" and type in the desired name.
7. Click "**apply**" and "**ok**".

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
