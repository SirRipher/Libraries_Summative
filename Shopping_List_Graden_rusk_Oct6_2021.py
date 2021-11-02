#--------
#Shopping List
#October 6 2021
#Graden rusk
#--------

##----Functions start here----##
import time
from Shopping_List_Libraries import Adding_Deleting_to_Lists, List_shopping


def View():
    print()
    Things = List_shopping.Item#prints out the list
    print(f"You got {Things}")
    time.sleep(.5)
    Total = sum(List_shopping.Item.values())#addss the sum of the items
    print(f"The Total is {Total}$")
    money = List_shopping.random(1)
    print(f"looks like you only get {money} to spend today.")
    if money >= Total:
        print("Congrats on staying in the limit.")
    else:
        print("Looks like somebody is gonna starve this month. Just kidding.")
    View_has_been_called = True
    pass
    start(View_has_been_called)
    
def start():#start function
    play = True # makes play equal true
    if play == True:#checks to see if play is equal to true
        print()
        time.sleep(.5)
        print("What would you like to do? Please select a number.")
        print("""1. Add to the list.
2. Delete from the list.
3. View the list.
4. Quit.""")
        
        try:#plays this if options is a number
            options = int(input(">>>" )) 
            
            if options == 1:#checks for 1=1
                Adding_Deleting_to_Lists.item_add()
                #plays Adding function
            if options == 2:#checks for 2=2
                Adding_Deleting_to_Lists.item_delete()#plays delete funct
            if options == 3:#checks for 3=3
                View()#plays View funct
            else:
                print("Have you looked at the list?")
                choice = input(">>>" )
                if choice == 'yes' or choice == 'y' or choice == 'Yes':
                    play == False#will end the list entirely
                else:
                    print("You should view your items.")
                    View()
                
        except:
            start()

#----Code Starts Here----#
print("Welcome to your Shopping list.")
start()
