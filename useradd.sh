#!/bin/bash

#This application will add a User to Linux
#That User will be added to a Group
#Will continue adding new Users until told otherwise

prompt(){
    read -p "Enter the new username: "  USSR
    read -p "Enter the new user's group: " GRP
}

makeUser(){
    echo "Making new user!"

    if id "$USSR" >/dev/null 2>&1; then
        echo "Hey dummy, $USSR  already exists"
    else
        sudo useradd "$USSR"
        echo "User $USSR created!"
    fi

    echo "Creating group $GRP (if need be) and adding $USSR to group $GRP"
    sleep 1

    if grep -q $GRP /etc/group; then
        echo "Hello, group $GRP has already been created!... Dummy"
    else
        sudo groupadd $GRP
        echo "Operation successful"
    fi

    if id -nG "$USSR" | grep -qw "$GRP"; then
        echo "$USSR already belongs to group $GRP"
    else
        echo "Adding $USSR to group $GRP"
        sudo usermod -aG $GRP $USSR
    fi

    sleep 1
    echo "Done!"
}

finish(){
    echo "If you want to quit, type exit"
    read DONE
}

echo "**Welcome to the Person Creation App**" | figlet
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

echo "Thanks for Playing God!!" | figlet
