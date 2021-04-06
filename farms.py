#!/usr/bin/env python3
# create the list called farms
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


# loop across the list vendors
for x in farms:
    print("The farm is:" + x.get("name"))  # each time through the loop print value of x
    farm = x.get("name")
    agriculture = x.get("agriculture")
    str(print(farm + agriculture))
print("\nOur loop has ended.")  # when the loop ends print this

