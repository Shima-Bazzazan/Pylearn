import qrcode


PRODUCTS = []

def read_from_database_store():
    file =open("G:\python_project\pylearn7\sessions\session_06\database.txt" , "r")
    for line in file :
        line = line.rstrip()
        result = line.split(",")
        my_dict = {"code" : result[0] ,"name" : result[1] ,"price": result[2] ,"count" : result[3] }
        PRODUCTS.append(my_dict)     
    file.close()


def show_menu():
    print()
    print("1_ Add")
    print("2_ Edit")
    print("3_ Remove")
    print("4_ Search")
    print("5_ Show list")
    print("6_ Buy")
    print("7_ QRcode generator")
    print("8_ Exit")


def add():
     code = input("Please enter code: ") 
     name = input("Please enter name: ")
     price = input("Please enter price: ") 
     count = input("Please enter count: ")
     new_product={"code":code, "name":name, "price":price, "count":count}
     PRODUCTS.append(new_product)

def edit():
    edit_character="y"
    while (edit_character == "y"):
        product_code=input("Please enter the product's code you want to edit: ")
        for product in PRODUCTS:
            if product['code']== product_code:
                edited_item= int(input("Please type the item number that you want to edit:\n1) name\n2) price\n3) count\n"))
                if edited_item==1:
                    product['name']=input("Please enter New name for this code: ")
                elif edited_item==2:
                    product['price']=input("Please enter New price for this code: ")
                elif edited_item==3:
                    product['count']=input("Please enter New count for this code: ")
                print(product)
                break
        else:
            print("The product code you enter is not exist!")
        edit_character = input("Do you want to continue?(y/n) ")
    print("The list has been edited")


def remove():
    remove_character="y"
    while (remove_character == "y"):
        felag=0
        product_code=input("Please enter the product's code you want to delete: ")
        for product in PRODUCTS:
            if product['code']== product_code:
                felag=1
                temp=PRODUCTS.index(product)
                PRODUCTS.pop(temp)
                print(f"{product['name']} is removed, from products")
        if felag==0:
            print("Ops! There is no such product")
        remove_character = input("Do you want to continue?(y/n) ")
    print("The item has been removed")


def search():
    user_input=input("Please enter your keyword: ")
    for product in PRODUCTS:
        if product['code']==user_input or product['name']==user_input:
            print(product["code"],",",product["name"],",",product["price"])
            break
    else:
        print('Sorry! not found')


def show_list():
    for row in PRODUCTS:
        print(row["code"],"\t\t",row["name"],"\t\t",row["price"])


def buy():
     read_from_database_store()
     shopping_list = [] 
     total_price = 0
     felag=0
     while (felag==0) :
        product_code = input("Please enter product's code: ")
        for product in PRODUCTS :
            if product["code"] == str(product_code) :
                user_count = int(input("How many " + product["name"] + " do you want to buy? "))
                if int(product["count"]) < user_count :
                    print("The request is excessive")
                    break
                elif  int(product["count"]) >= user_count :
                    product["count"] = int(product["count"]) - user_count
                    user_product = {"product_code" : product["code"] , "product_name" : product["name"] , "product_price" : product["price"] , "product_count" : user_count}
                    shopping_list.append(user_product)
                    print("Product added to your shopping list")
                    total_price += int(product["price"]) * user_count

                    choice = input("Do you want to continue shopping?(y/n) ")
                    if choice == "y" :
                         break 
                    elif choice == "n" :
                         print("code \t\t name \t\t price \t\t count ")
                         for user_product in shopping_list :
                             print(str(user_product["product_code"])  + "\t\t" + user_product["product_name"] + "\t\t" + str(user_product["product_price"]) + "\t\t" + str(user_product["product_count"]) )
                         print("Ttal Price : " , total_price)
                         felag=1
                         break

        else :
            print ("Sorry! product not found")
            break


def write_to_database_store():
    f = open("G:\python_project\pylearn7\sessions\session_06\database.txt", "w")
    f = open("G:\python_project\pylearn7\sessions\session_06\database.txt", "a")
    for product in PRODUCTS:
        line = str(product["code"] +","+ product["name"] +","+ product["price"] +","+ str(product["count"]))
        f.write(line.strip()+"\n")
    f.close()


def make_qrcode() :
     print("choose a code from below list: ")
     show_list()
     user_code = str(input("\nEnter product's code number to create qrcode:"))
     for product in PRODUCTS :
         if user_code == product["code"] :
             product_info =("code=" + product["code"] +" \t\t "+ "name=" + product["name"] +" \t\t "+"price=" + product["price"] +" \t\t "+ "count=" + product["count"])
             print(product_info)
             img = qrcode.make(product_info)
             img.save("product_qrcode_store.png")


print("Welcome to my Store ")
print("Loading . . . ")
read_from_database_store()
print("Data loaded.")

while True :
    show_menu()
    user_choice = int(input("\nPlease enter your choice: "))

    if user_choice == 1 :
        add()
    elif user_choice == 2 :
        edit()     
    elif user_choice == 3 :
        remove()
    elif user_choice == 4 :
        search()
    elif user_choice == 5 :
        show_list()
    elif user_choice == 6 :
        buy()
    elif user_choice == 7 :
        make_qrcode()    
    elif user_choice == 8 :
        write_to_database_store()
        exit(0)
    else :
        print("Try again")