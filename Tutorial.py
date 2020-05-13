"""
This shows basic commands and how to access Settings or Help centre
"""
#Basic Variables
Yes = (True, "True", "Y", "y", "Yes", "yes")
No = (False, "Flase", "N", "n", "No", "no")

def Want_tutral(x):
  if x in Yes:
    print("Lets begin the tutorial")
    print("Here is what we will be following:\n1. Basic commands\n2. Navigation\n3. Customization\n4. Help Centre")