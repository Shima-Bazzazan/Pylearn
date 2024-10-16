
import qrcode
import sqlite3


def menu():
     print("1. Add") 
     print("2. Edit")
     print("3. Delete")
     print("4. Search")
     print("5. Show")   
     print("6. Buy")
     print("7. Qrcode")
     print("8. Exit")


def add():
     code = input("Please enter product's code: ") 
     name = input("\nPlease enter product's name: ")
     price = input("\nPlease enter product's price: ") 
     count = input("\nPlease enter product's count: ")

     cursor.execute(f"INSERT INTO STORE (id,name,price,count) VALUES({code} , '{name}' , {price} , {count})")
     cursor.commit()



def edit():
    id = int(input("Please enter your product's ID:"))
    temp= str(input("Which product's feature do you want to edit? (id/name/price/count): "))

    if temp =="id":
        new_id = int(input("Please enter new product's id: "))
        cursor.execute(f"UPDATE store set {temp}={new_id} WHERE id = {id}")
        cursor.commit()        
    elif temp =="name":
        new_name = str(input("Please enter new product's name: "))
        cursor.execute(f"UPDATE store set {temp}='{new_name}' WHERE id = {id}")
        cursor.commit() 
    elif temp =="price" :
        new_price = int(input("enter new product's price: "))
        cursor.execute(f"UPDATE store set {temp}={new_price} WHERE id = {id}")
        cursor.commit() 
    elif temp =="count" :
        new_count = int(input("Please enter new product's count: "))
        cursor.execute(f"UPDATE store set {temp}={new_count} WHERE id = {id}")
        cursor.commit() 



def delete():
    user_input = input("Please enter your product's ID you want to delete: ") 
    cursor.execute(f"DELETE from store where id = {user_input}")
    cursor.commit()
    print("Removed successfully!")
    show()



def search():
    user_choice = str(input("Which field do you want to search based on ? (ID/name): "))
    if user_choice=="id" :
        id = int(input("enter product;s ID:"))
        for row in cursor.execute(f"SELECT * FROM store WHERE ID={id}"):
            print (row)
    elif user_choice == 'name' :
        name = str(input("Please enter product's name: "))
        for row in cursor.execute(f"SELECT * FROM store WHERE name={name}"):
            print (row)



def show():
    print("\n(code , name , price , count)")
    for row in cursor.execute("SELECT * FROM store"):
        print(row)
    print("")



def buy():
    user_product = str(input("Please enter your product's name: "))
    user_count = int(input("How many of this product do you buy? "))
    for row in cursor.execute(f"SELECT count FROM store WHERE name='{user_product}'").fetchall():
        count = (row[0])
    remain = int(count) - user_count
    if remain >= 0 :
        connection.execute(f"UPDATE store set count={remain} WHERE name = '{user_product}'")
        connection.commit() 
    elif remain < 0 :
        print("There are not enough of this product to buy!")


def make_qrcode() :
    id = int(input("\nPlease enter product's ID to create Qrcode: "))
    user_product = cursor.execute(f"SELECT * FROM store WHERE id={id} ").fetchall()
    img = qrcode.make(user_product)
    img.save("product_qrcode.png")



print("'Welcome to my store'")
global connection
global cursor
connection = sqlite3.connect("store.db")
cursor = connection.cursor()

while True :
    menu()
    user_choice = int(input("\nPlease enter your choice: "))

    if user_choice == 1 :
        add()
    elif user_choice == 2 :
        edit()     
    elif user_choice == 3 :
        delete()
    elif user_choice == 4 :
        search()
    elif user_choice == 5 :
        show()
    elif user_choice == 6 :
        buy()
    elif user_choice == 7 :
        make_qrcode()    
    elif user_choice == 8 :
        connection.close()
        exit(0)
    else :
        print("This value is not valid!")     