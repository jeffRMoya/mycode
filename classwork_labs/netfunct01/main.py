#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# function to connect to commands
def devicereboot(devices): # devices== dict
    for ip in devices.keys(): # looping through the dict
        print(f'{crayons.green("Connecting to...")} {ip}')
    print("REBOOTING NOW!")
    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    with open("devicemd.json", "r") as devicemdfile:
        devicecmd = json.load(devicemdfile)

    print("Welcome to the {crayons.blue('Network')} Device Command Pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd) # call function to connect to IPs
# call our main function
main()

