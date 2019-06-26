#!/bin/bash
# python3.7 -m pip install -r requirements.txt
# uncomment when requirements.txt is done
read -p $'Does a \'tokens.txt\' file already exist? [y/n] ' tokensexist
if [ $tokensexist = 'y' ]; then
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
