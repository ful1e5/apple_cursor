#! /bin/bash

# auto-install patch by @luizoti on Bibata Cursror => https://github.com/ful1e5/Bibata_Cursor/commit/eb84f27919e433f9b72e7ef9f6444d4a7d276ba9
INPUT=$1

ROOT_UID=0
DEST_DIR=
URL="https://github.com/ful1e5/apple_cursor/releases/download/1.0.1-beta/macOSBigSur.tar"
macOSBigSur="./macOSBigSur"
DOWNLOAD_FILE_NAME="$macOSBigSur.tar"

cd "$( dirname "${BASH_SOURCE[0]}" )" || exitt

# Destination directory
if [ "$UID" -eq "$ROOT_UID" ]; then
  DEST_DIR="/usr/share/icons"
else
  DEST_DIR="$HOME/.icons"
fi

echo -e "\e[1m\n+---------------------------------------------+"
echo -e "|     macOSBigSur Cursor Installer Script     |"
echo -e "+---------------------------------------------+\n\e[0m"



# -------------------- Color print Functions --------------------
show_question() {
  echo -e "\033[1;34m$@\033[0m"
}

show_dir() {
  echo -e "\033[1;32m$@\033[0m"
}

show_error() {
  echo -e "\033[1;31m$@\033[0m"
}

end() {
  echo -e "\nExiting...\n"
  exit 0
}

# -------------------- Helpers --------------------
continue() {
  case ${INPUT} in
    '-a' )
      :
      ;;
    '-h' )
      echo "  -a - Auto-install for all users!"
      ;;
    * )
      show_question "\nDo you want to continue? (Y)es, (N)o : \n"
      read INPUT
      case $INPUT in
       ( [Yy]* ) ;;
       ( [Nn]* ) end;;
       ( * ) show_error "\nSorry, try again."; continue;;
      esac
      ;;
  esac
}

replace() {
  show_question "\nFound an existing installation. Replace it? (Y)es, (N)o :\n" 
  read INPUT
  case $INPUT in
    ( [Yy]* ) rm -rf "$@/macOSBigSur*" 2>/dev/null;;
    ( [Nn]* ) ;;
    ( * ) show_error "\tSorry, try again."; replace $@;;
  esac

}


# For download the package
function download {
    echo -e "\nDownloading macOSBigSur Theme..."
    url=$1
    filename=$2

    if [ -x "$(which wget)" ] ; then
        curl -o $2 -fL $url
    elif [ -x "$(which curl)" ]; then
        wget -q $url -O $2 --show-progress
    else
        show_error "Could not find curl or wget, please install one." >&2
    fi

    if [ $? -eq 0 ]; then
       echo "Downloading Complete"
    else
        show_error "Downloading... FAIL"
    fi
}


# unpack 
function unpack {
    echo -e "\nUnpacking Theme..."
    file=$1
    dir=${file%.*}

    echo "$dir"
    # creating dir and extract .tar file content to it
    mkdir "$dir" && tar -xvf "$file" -C "$dir"

    # remove .tar file
    rm -rf $file

    if [ $? -eq 0 ]; then
        echo "Unpacking Complete"
    else
        show_error "Unpacking Theme... FAIL"
    fi
}   

install() {

  # Cecking old version exits or not
  if [ -f "$DOWNLOAD_FILE_NAME" ] || [ -f "$macOSBigSur" ]; then
      echo -e "\nmacOSBigSur.tar file already exists"
      show_question "\nDownload Fresh Theme OR Continue with existing file? (D)ownload File (recommended), (E)xisting File : \n "
        read INPUT
        case $INPUT in
        ( [Dd]* ) download $URL $DOWNLOAD_FILE_NAME;;
        ( [Ee]* ) ;;
        ( * ) show_error "\nSorry, try again."; continue;;
        esac
  else
      download $URL $DOWNLOAD_FILE_NAME
  fi


  # unpack file
  unpack $DOWNLOAD_FILE_NAME

  # Show destination directory
  echo -e "\nmacOSBigSur Cursor Theme will be installed in:\n"
  show_dir "\t$DEST_DIR"
  if [ "$UID" -eq "$ROOT_UID" ]; then
    echo -e "\nIt will be available to all users."
  else
    echo -e "\nTo make them available to all users, run this script as root."
  fi

  continue


  # Check destination directory
  if [ ! -d $DEST_DIR ]; then
    mkdir -p $DEST_DIR
  elif [[ -d $DEST_DIR/macOSBigSur ]]; then
    replace $DEST_DIR
  fi

  echo -e "\nInstalling macOSBigSur..."
  
  # Copying files
  cp -rf $macOSBigSur $DEST_DIR
  chmod -R 755 $DEST_DIR/macOSBigSur

  echo "Installation complete!"
  echo "Do not forget you have to set macOSBigSur Cursor"
}

remove() {

  # PREVIEW

  # Show installation directory
  if [[  -d $DEST_DIR/macOSBigSur ]]; then
    echo -e "\nmacOSBigSur Theme installed in:\n"
    show_dir "\t$DEST_DIR"
    if [ "$UID" -eq "$ROOT_UID" ]; then
      echo -e "\nIt will remove for all users."
    else
      echo -e "\nIt will remove only for current user."
    fi

    continue
  
  else
    show_error "\nmacOSBigSur Cursor is not installed in:\n"
    show_dir "\t$DEST_DIR\n"
    end
  fi

  echo -e "\nRemoving macOSBigSur..."
  rm -rf $DEST_DIR/macOSBigSur

  echo "Removing complete"
  echo "I hope to see you soon."
}

main() {
  # Cases
  case ${INPUT} in
  '-a' )
    install
    ;;
  '-h' )
    echo "  -a - Auto-install for all users!"
    ;;
  * )
    show_question "What you want to do: (I)nstall, (R)emove : \n"
    read INPUT
    case $INPUT in
      ( [Ii]* ) install;;
      ( [Rr]* ) remove;;
      ( * ) show_error "\nSorry, try again."; main;;
    esac
    ;;
  esac 

  # Remove directory
  rm -rf macOSBigSur
}

( cd /tmp/ && main )