#!/bin/bash
if [ "$(uname)" == "Darwin" ]; then
    if [[ $(command -v brew) == "" ]]; then
        echo "installing Homebrew"
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    else
        echo "updating Homebrew"
        brew update
    fi
    if ! brew info python3 &>/dev/null; then
        echo "installing python3.7 and pip3 via Homebrew"
        brew install python3
    else
        echo "upgrading python3.7 via Homebrew"
        brew upgrade python3
    fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    echo "updating package list"
    sudo apt-get update
    echo "upgrading installed packages"
    sudo apt-get upgrade
    if [[ $(command -v python3.7) == "" ]]; then
        echo "installing python3.7 prerequesites via apt-get"
        sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
        echo "installing python3.7 via source"
        wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
        tar -xf Python-3.7.3.tar.xz
        cd Python-3.7.3
        ./configure --enable-optimizations
        make -j$(nproc)
        sudo make altinstall
        echo "removing python3.7 installation files"
        cd ..
        rm -rf Python-3.7.3*
    fi
    if [[ $(command -v pip3) == "" ]]; then
        echo "installing pip3"
        sudo apt-get install python3-pip
    fi
fi
python3.7 -m pip install -r requirements.txt
tokenslocation=$PWD/tokens.txt
if [ -f "$tokenslocation" ]; then
    read -p $'Would you like to delete the old \'tokens.txt\' file and make a new one? [y/n] ' resettokens
    if [ $resettokens = 'y' ]; then
        rm tokens.txt
        touch tokens.txt
        read -sp $'Please input your discord token:' d_token
        echo $d_token >> tokens.txt
    fi
else
    touch tokens.txt
    read -sp $'Please input your discord token:' d_token
    echo $d_token >> tokens.txt
fi
