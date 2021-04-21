#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pandas
import pandas as pd
import pyexcel

# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt


# Request data from user
# Data for Name a challenge you overcame
def challenges():
    input_situation = input("\nWhat was the situation? ")
    input_challenge = input("How did you process this challenge? ")
    input_solution = input("What was your solution? ")
    input_resolution = input("How was it resolved? ")
    d = {"Situation": input_situation, "Task": input_challenge, "Action": input_solution, "Result": input_resolution}
    return d

# Data for Name a failure you overcame
def failure():
    input_event = input("\nWhat went wrong? ")
    input_response = input("How did you handle it? ")
    input_action = input("What was your solution? ")
    input_ending = input("How did it all end? ")
    d = {"Situation": input_event, "Task": input_response, "Action": input_action, "Result": input_ending}
    return d

# Use user input to create data for excel
def main():
    """Runtime code"""

    # Runtime
    mylistdict = []  # this will be our list we turn into a *.xls file
    

    while True:
        # determine if user is adding a new question
        new_entry = input("\nWhich interview question would you like to answer? (Short Responses Please) \n 1. Tell me about a time you overcame a challenge.\n 2. Tell me about a time you overcame failure.\n -->  ")

        # determine how to handle user input
        if new_entry == '1':
            result = challenges()

        elif new_entry == '2':
            result = failure()

        else:
            print("Sorry, that is not an option")
            continue # restart the loop

        # building out our list we want to place into xls
        mylistdict.append(result)
    
        keep_going = input("\nWould you like to answer another interview question? Enter to continue, or enter 'q' to quit: ")
        if keep_going.lower() == 'q':
           break

    # ask for the name of the xls file to be saved
    filename = input("\nWhat would you like to name this file? ")



    # use pandas to create a dataframe
    df = pd.DataFrame(mylistdict)
    print(df)

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
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    
    # save table
    fig.tight_layout()
    plt.savefig(f'output/{filename}.png')

    # display where the file has been created
    print("The file " + filename + " has been saved in *.xls, *.xlsx, *.json, and *.png formats!")


# this runs when the program is called
if __name__ == "__main__":
    main()
