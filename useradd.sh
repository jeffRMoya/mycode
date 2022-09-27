#!/bin/bash

#This application will add a User to Linux
#That User will be added to a Group
#Will continue adding new Users until told otherwise

prompt(){
    echo "What do you want the userName to be?"
    read USSR
    echo "What group does the user belong to?"
    read GRP
}

makeUser(){
    echo "Making new user!"
    sudo useradd $USSR

    if id "$USSR" >/dev/null 2>&1; then
        echo "Hey dummy, $USSR  already exists"
    else
        echo "User $USSR created!"
    fi

    echo "Creating group $GRP (if need be) and adding $USSR to group $GRP"
    sleep 1
    echo "Adding $USSR to group $GRP"
    sleep 1
    sudo groupadd $GRP

    if id "$GRP" >/dev/null 2>&1; then
        echo "Hello, group $GRP has already been created!... Dummy"
    else
        echo "Operation successful"
    fi

    sleep 1
    sudo usermod -a -G $GRP $USSR
    echo "Done!"
}

finish(){
    echo "If you want to quit, type exit"
    read DONE
}

echo "Welcome to the user/group creation app"
echo "Here we will create users and groups"
echo "This app will also automatically add the user to a group"
echo "This app works with existing groups as well"
sleep 1

while [ "$DONE" != "exit" ]
do
    prompt
    makeUser
    finish
done

echo "Thanks for using the user/group creation app"
