# Apple Cursor

Enjoy macOS cursors for `Windows` and `Linux` with _HiDPI Support_ .

[![Build](https://github.com/ful1e5/apple_cursor/workflows/build/badge.svg)](https://github.com/ful1e5/apple_cursor/actions?query=workflow%3Abuild)
[![CodeFactor](https://www.codefactor.io/repository/github/ful1e5/apple_cursor/badge)](https://www.codefactor.io/repository/github/ful1e5/apple_cursor)
[![Twitter](https://img.shields.io/badge/twitter-ful1e5-blue)](https://twitter.com/ful1e5)

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

### Quick install

- macOSBigSur: [https://www.pling.com/p/1408466](https://www.pling.com/p/1408466)
- macOSBigSur-White: [https://www.pling.com/p/1616779](https://www.pling.com/p/1616779)
- macOSMonterey: [https://www.pling.com/p/1648124](https://www.pling.com/p/1648124)
- macOSMonterey-White: [https://www.pling.com/p/1648129](https://www.pling.com/p/1648129)

#### Preview:

> Check Figma file [here](https://www.figma.com/file/OZw8Ylb9xPFw9h1uZYSMFa/Mac-Cursor?node-id=0%3A1)

<p align="center">
  <img title="macOSMonterey" src="https://imgur.com/bmS0fRT.png">
  </br>
  <sub>macOSMonterey Cursors</sub>
</p>

<p align="center">
  <img title="macOSMonterey White" src="https://imgur.com/s0nqcje.png">
  </br>
  <sub>macOSMonterey White Cursors</sub>
</p>

<p align="center">
  <img title="macOSBigSur" src="https://imgur.com/Q022eSp.png">
  </br>
  <sub>macOSBigSur Cursors</sub>
</p>

<p align="center">
  <img title="macOSBigSur White" src="https://imgur.com/SFVR945.png">
  </br>
  <sub>macOSBigSur White Cursors</sub>
</p>

### Manual Install

> Note: replace name according package name.

#### Linux/X11

##### macOSMonterey

```bash
# extract `macOSMonterey.tar.gz`
tar -xvf macOSMonterey.tar.gz

# For local users
mv macOSMonterey ~/.icons/

# For all users
sudo mv macOSMonterey /usr/share/icons/
```

##### macOSBigSur

```bash
# extract `macOSBigSur.tar.gz`
tar -xvf macOSBigSur.tar.gz

# For local users
mv macOSBigSur ~/.icons/

# For all users
sudo mv macOSBigSur /usr/share/icons/
```

#### Windows

##### macOSMonterey

1. unzip `macOSMonterey-Windows.zip` file
2. Open `macOSMonterey-Windows/` in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open _Control Panel > Personalization and Appearance > Change mouse pointers_, and select **MacOSMonterey Cursors**.
5. Click '**Apply**'.

##### macOSBigSur

1. unzip `macOSBigSur-Windows.zip` file
2. Open `macOSBigSur-Windows/` in Explorer, and **right click** on `install.inf`.
3. Click 'Install' from the context menu, and authorize the modifications to your system.
4. Open _Control Panel > Personalization and Appearance > Change mouse pointers_, and select **MacOSBigSur Cursors**.
5. Click '**Apply**'.

### Uninstall

#### Windows

1. Go to **Registry Editor** by typing the same in the _start search box_.
2. Expand `HKEY_CURRENT_USER` folder and expand `Control Panel` folder.
3. Go to `Cursors` folder and click on `Schemes` folder - all the available custom cursors that are installed will be listed here.
4. **Right Click** on the name of cursor file you want to uninstall; for eg.: _macOSMonterey Cursors_ and click `Delete`.
5. Click '**yes**' when prompted.

# Dependencies

## External Libraries

- libxcursor
- libx11
- libpng (<=1.6)

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

- [gcc](https://gcc.gnu.org/install/)
- [make](https://www.gnu.org/software/make/)
- [nodejs](https://nodejs.org/en/) (<=12.x.x)
- [yarn](https://classic.yarnpkg.com/en/docs/install/)
- [python](https://www.python.org/downloads/) (<=3.8)
- [pip3](https://pip.pypa.io/en/stable/installing/)

### Node Packages

- [puppeteer](https://www.npmjs.com/package/puppeteer)
- [pngjs](https://www.npmjs.com/package/pngjs)
- [pixelmatch](https://www.npmjs.com/package/pixelmatch)

### PyPi Packages

- [clickgen](https://pypi.org/project/clickgen/s)

## Build From Scratch

### Auto Build (using GitHub Actions)

GitHub Actions is automatically runs on every `push`(on **main** and **dev** branches) and `pull request`(on **main** branch), You found theme resources in `artifact` section of **build**.GitHub **Actions** source is available inside [.github/workflows](https://github.com/ful1e5/apple_cursor/tree/main/.github/workflows) directory.

### Manual Build

> Check **[Makefile](./Makefile)** for more targets.

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

# Bugs

Bugs should be reported [here](https://github.com/ful1e5/apple_cursor/issues) on the Github issues page.

# Getting Help

You can create a **issue**, I will help you. 🙂

# Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md), any suggestions for features and contributions to the continuing code masterelopment can be made via the issue tracker or code contributions via a `Fork` & `Pull requests`.
