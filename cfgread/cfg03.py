#!/usr/bin/env python3
## create file object in "r"ead mode
filename = input("What would you like to open?")


with open(filename, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.read()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

