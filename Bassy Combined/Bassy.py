"""
Hi, I am Assisstant, your personal Bassy [Big Hero 6 Refrence]
I will help note down your tasks, create alarms and open files.
I'm still in Beta testing, so please don't hate me.
"""
import Tutorial

#Basic Variables
Yes = (True, "True", "Y", "y", "Yes", "yes")
No = (False, "Flase", "N", "n", "No", "no")
#--------------------------------------------------

#Greeting after opening up for the first time/system reboot
print("Hello, I am Assisstant, your personal Bassy:]\nWhat should I call you???")
Admin_Name = input()
print(Admin_Name +", that's a beautiful name.")
print ("What do you want the command to call on me to be?")
Command_word = input()
#----------------------------------------------------------------------------------------------------------------------

#Tutorials?
print("Do you want to have a small tutorial?")
answer = input()
if answer in Yes:
    print("Shall we proceed?")
elif answer in No:
    print("You can call on me by your chosen command...zzzz")
else:
    print ("That is an invalid name...")
    #A command for it to ask again if the person wants a tutorial#
#----------------------------------------------------------------------------------------------------------------------

#Finally, the Tutral
if answer in Yes:
    Want_tutral(answer)
elif answer in No:
    print("Sleepin Yo")
    #Module Sleepin_yo
