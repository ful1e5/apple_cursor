#!/bin/bash
# A script for preparing binaries of Apple Cursors, created by Abdulkaiz Khatri.

version="v2.0.1"

error() (
  set -o pipefail
  "$@" 2> >(sed $'s,.*,\e[31m&\e[m,' >&2)
)

get_config_file() {
  local key="${1}"
  local cfg_file="build.toml"

  if [[ $key == *"Right"* ]]; then
    cfg_file="build.right.toml"
  fi

  echo $cfg_file
}

with_version() {
  local comment="${1}"
  echo "$comment ($version)."
}

if ! type -p ctgen >/dev/null; then
  error ctgen
  exit 127 # exit program with "command not found" error code
fi

declare -A names
names["macOS"]=$(with_version "macOS cursors")
names["macOS-White"]=$(with_version "White macOS cursors")

# Cleanup old builds
rm -rf themes bin

# Building Apple XCursor binaries
for key in "${!names[@]}"; do
  comment="${names[$key]}"
  cfg=$(get_config_file key)

  ctgen "$cfg" -p x11 -d "bitmaps/$key" -n "$key" -c "$comment" &
  PID=$!
  wait $PID
done

# Building Bibata Windows binaries
for key in "${!names[@]}"; do
  comment="${names[$key]}"
  cfg=$(get_config_file key)

  ctgen "$cfg" -p windows -s 16 -d "bitmaps/$key" -n "$key-Small" -c "$comment" &
  ctgen "$cfg" -p windows -s 24 -d "bitmaps/$key" -n "$key-Regular" -c "$comment" &
  ctgen "$cfg" -p windows -s 32 -d "bitmaps/$key" -n "$key-Large" -c "$comment" &
  ctgen "$cfg" -p windows -s 48 -d "bitmaps/$key" -n "$key-Extra-Large" -c "$comment" &
  PID=$!
  wait $PID
done

# Compressing Binaries
mkdir -p bin
cd themes || exit

for key in "${!names[@]}"; do
  tar -cJvf "../bin/${key}.tar.xz" "${key}" &
  PID=$!
  wait $PID
done

# Compressing Bibata.tar.xz
cp ../LICENSE .
tar -cJvf "../bin/macOS.tar.xz" --exclude="*-Windows" . &
PID=$!
wait $PID

# Compressing Bibata-*-Windows
for key in "${!names[@]}"; do
  zip -rv "../bin/${key}-Windows.zip" "${key}-Small-Windows" "${key}-Regular-Windows" "${key}-Large-Windows" "${key}-Extra-Large-Windows" &
  PID=$!
  wait $PID
done

cd ..

# Copying License File for 'bitmaps'
cp LICENSE bitmaps/
zip -rv bin/bitmaps.zip bitmaps
