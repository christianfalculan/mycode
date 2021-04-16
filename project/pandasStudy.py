#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pandas
import pandas as pd

# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt

# Request data from user
# Data for new employee
def new_employee():
    input_name = input("\nWho is this new hire? ")
    input_position = input("What is their position? ")
    input_phonenumber = input("What is their contact information? ")
    input_thoughts = input("Are they cool? ")
    d = {"Name": input_name, "Position": input_position, "Phonenumber": input_phonenumber, "Thoughts": input_thoughts}
    return d

# Data for new clients
def new_client():
    input_client = input("\nWhat is the name of the new client? ")
    input_value = input("How much business do they provide? ")
    input_poc = input("Who is their point of contact? ")
    input_number = input("What is their number to be reached? ")
    d = {"Client": input_client, "Value": input_value, "POC": input_poc, "Number": input_number}
    return d

# Use user input to create data for excel
def main():
    """Runtime code"""

    # Runtime
    mylistdict = []  # this will be our list we turn into a *.xls file
    

    while True:
        # determine if user is adding a new employee or client
        new_entry = input("\nIs this a new employee or client? ")

        # determine how to handle user input
        if new_entry == 'employee':
            result = new_employee()

        elif new_entry == 'client':
            result = new_client()

        else:
            print("Sorry, that is not an option")
            continue # restart the loop

        # building out our list we want to place into xls
        mylistdict.append(result)
    
        keep_going = input("\nWould you like to add another? Enter to continue, or enter 'q' to quit: ")
        if keep_going.lower() == 'q':
           break

    # ask for the name of the xls file to be saved
    filename = input("\nWhat would you like to name this file? ")



    # use pandas to create a dataframe
    df = pd.DataFrame(mylistdict)

    # save out "old" Excel format (*.xls)
    df.to_excel(f"output/{filename}.xls")

    # save out "new" Excel format (*.xlsx)
    df.to_excel(f"output/{filename}.xlsx")

    # save out to JSON format (*.json)
    df.to_json("output/{filename}.json")


    #### Working on table visualizations (excel view without excel)
    # define figure and axes
    fig, ax = plt.subplots()

    # hide the axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    # create a table
    table = ax.table(cellText=df.values)#, colLabels=df.keys)

    # save table
    fig.tight_layout()
    plt.savefig(f'output/{filename}.png')

    # display where the file has been created
    print("The file " + filename + " has been saved in *.xls, *.xlsx, *.json, and *.png formats!")


# this runs when the program is called
if __name__ == "__main__":
    main()
