#--------
#Shopping List
#October 6 2021
#Graden rusk
#--------
from Shopping_List_Libraries import List_shopping

def item_add():#Adding function
    adding = input("What item do you want to add?\n>>>" ).lower()
    costing = float(input("what is the cost, or age, or grade?\n>>>" ))
    List_shopping.Item[adding] = (costing)
    start()

def item_delete():
    print("What do you want to delete from the list?")
    print("No capitals please")
    delete = input(">>>" )#allows them to type in what they want
    if delete in List_shopping.Item:#checks for delete in the Item list
        print(f"{delete} is being deleted.")
        del List_shopping.Item[delete]#deletes the Item from the list
        start()
    else:
        print("That's not in the list.")
        start()#uses the start funct
