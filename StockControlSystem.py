import time

storage1, storage2 = {} , {}

def storage1_add(item, quantity) :
    if item in storage1:
        storage1[item] += quantity
        print (f"{quantity} units of {item} added to stock.")
    else :
        storage1[item] = quantity
        print(f"{quantity} units of {item} added to stock ")

def storage1_remove(item, quantity) :
    if item in storage1 : 
        if storage1[item] - quantity >= 0:
            storage1[item] -= quantity
            print(f"{quantity} units of {item} removed from stock.")
        else:
            print(f"Error: Not enough {item} in stock ")
    else:
        print(f"Error: {item} not in stock")

def storage2_add(item, quantity) :
    if item in storage2 :
        storage1[item] += quantity
        print (f"{quantity} units of {item} added to stock.")
    else :
        storage2[item] = quantity
        print(f"{quantity} units of {item} added to stock ")

def storage2_remove(item, quantity) : 
    if item in storage2 : 
        if storage2[item] - quantity >= 0:
            storage2[item] -= quantity
            print(f"{quantity} units of {item} removed from stock.")
        else:
            print(f"Error: Not enough {item} in stock ")
    else:
        print(f"Error: {item} not in stock")        
   
def show_total_items_storage1():
    print(storage1)

def show_total_items_storage2():
    print(storage2)
    

def show_total_items():
    Total_Storage = storage1 | storage2
    print(Total_Storage)


while True:
    print("  __________________________________")
    print(" |                                  |")
    print(" |       STOCK CONTROL SYSTEM       |")
    print(" |__________________________________|")
    print(" ")
    print("   1. Add Item in Storage(1)")
    print("   2. Remove Item in Storage(1)")
    print("   3. Add Item in Storage(2)")
    print("   4. Remove item in Storage(2)")
    print("   5. Show Total Items in Storage(1)")
    print("   6. Show Total Items in Storage(2)")
    print("   7. Show Total Items")
    print("   8. Quit")
    print(" ")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Write the name of item: ")
        quantity = int(input("Enter the quantity: "))
        storage1_add(item,quantity)
    elif choice == 2:
        item = input("Write the name of item: ")
        quantity = int(input("Enter the quantity: "))    
        storage1_remove(item, quantity)
    elif choice == 3:
        item = input("Write the name of item: ")
        quantity = int(input("Enter the quantity: "))
        storage2_add(item, quantity)
    elif choice == 4:
        item = input("Write the name of item: ")
        quantity = int(input("Enter the quantity: "))
        storage2_remove(item, quantity)    
    elif choice == 5:
        show_total_items_storage1()
    elif choice == 6:
        show_total_items_storage2()
    elif choice == 7:
        show_total_items()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Try Again")

