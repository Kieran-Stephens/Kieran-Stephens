import inflect
import csv
import ast
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="test"
)
mycursor = mydb.cursor()
p = inflect.engine()
with open('courriers.csv') as f:
    a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
with open('products.csv') as f:
    prdfile = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
with open('courriers.csv') as f:
    OrderFile = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
print1=[]


    

    
def NewOrder():
    
    f = input("Name of person ordering? ")
    b = input("Customer address? ")
    c = input("Customers phone number? ")
    d = input("name of courier? ")
    e = int(input("How many items do you want to insert? "))
    y=[]
    for n in range(e):
        Ordinal = p.ordinal(n+1)
        item = int(input(f"{Ordinal} item? "))
        y.append(item)
        
    update = {"customer_name": f,  "customer_address": b,  "customer_phone": c,  "courier": d,  "status": "preparing", "items": y}
    
    a.append(update)
    print(a)
    keys = a[0].keys()
    a_file = open("orders.csv", "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(a)
    
def UpdateOrder():    
    
    repeat = "Y"
    
    f=input("What is the customer name of the order you want to update? ")
    c = input(f"What is {f}'s phone number ? ")
    while repeat == "Y":
        b=input("what do you want to update? (e.g. customer_name, customer_phone etc.) ")
        e=input("What do you want to update it with? ")
        for n in range(len(a)):
            if a[n]['customer_name']==str(f):
                if a[n]['customer_phone'] == c:
                    a[n][b]=str(e)
                    
        repeat = input("Would you like to change another area in the order? (Y/N with capitals) ")
    print(a)
    keys = a[0].keys()
    a_file = open("orders.csv", "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(a)

def DeleteOrder():    
    
    f=input("What is the customer name of the order you want to delete? ")
    c = input(f"What is {f}'s phone number ? ")
    for n in range(len(a)):
        if a[n]['customer_name']==str(f):
                if a[n]['customer_phone'] == c:
                    a.remove(a[n])
                    break

    if a != []:
        keys = a[0].keys()
        a_file = open("orders.csv", "w")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
    else:
        a_file = open("orders.csv", "w")
        writer = csv.writer(a_file)
        row = ["customer_name","customer_address","customer_phone","courier","status","items"]
        writer.writerow(row)
    
    
    
def NewProduct():
    
        
    a=input("Name of Product? ")
    b = input(f"{a}'s price? (Please include £ sign and 2 decimal points) ")

    sql = "INSERT INTO products (name,price) VALUES (%s,%s)"
    val = (a,b)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f"New product with name {a} inserted.")

def UpdateProduct():
    
    repeat = "Y"
    f=input("What is the id of the product you want to update? ")
    while repeat == "Y":
        b=input("what do you want to update? (name or price) ")
        e=input("What do you want to update it with? ")
        sql = f"UPDATE products SET {b} = '{e}' WHERE id = {f}"
        mycursor.execute(sql)
        mydb.commit()
        print(f"Product with id {f} has been updated with {b} {e}")
        repeat = input("Would you like to change another area in the product? (Y/N with capitals) ")
    
def DeleteProduct():
    
    val=int(input("What is the id of the product you want to delete? "),)
    sql = "DELETE FROM products WHERE id = {}".format(val)
    mycursor.execute(sql)

    mydb.commit()

    print(f"Product with id {val} has been deleted")
    
def NewCourrier():
    
    a=input("Name of Courrier? ")
    b = input(f"{a}'s number? ")

    sql = "INSERT INTO courriers (name,phone) VALUES (%s,%s)"
    val = (a,b)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f"New courrier with name {a} inserted.")
        
def UpdateCourrier():
    repeat = "Y"
    f=input("What is the id of the Courriers you want to update? ")
    while repeat == "Y":
        b=input("what do you want to update? (name or number) ")
        e=input("What do you want to update it with? ")
        sql = f"UPDATE courriers SET {b} = '{e}' WHERE id = {f}"
        mycursor.execute(sql)
        mydb.commit()
        print(f"Courrier with id {f} has been updated with {b} {e}")
        repeat = input("Would you like to change another area in the order? (Y/N with capitals) ")
        
        
        

def DeleteCourrier():
    
    
    val=int(input("What is the id of the courrier you want to delete? "),)
    sql = "DELETE FROM courriers WHERE id = {}".format(val)
    mycursor.execute(sql)

    mydb.commit()

    print(f"Courrier with id {val} has been deleted")




def Choice():
    OorP = input("Products, Courriers or Orders? ")
    if OorP == "Orders":
        Orders()
    elif OorP == "Courriers":
        Courriers()
    elif OorP == "Products":
        Products()


def Orders():
    with open('orders.csv') as f:
        a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    
    
    for row in a:
        row["items"] = ast.literal_eval(row["items"])
        print(row)
    for row in a:
        print1.append(row)
    choice=input("choose your option: (1) delete, (2) update, (3)add new order: ")
    if choice=="3":
        NewOrder()
    if choice == "2":
        UpdateOrder()
    if choice == "3":
        DeleteOrder()

def Products():
    
    sql_select_Query = "select * from products"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of products in table: ", cursor.rowcount,"\n")

    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("price  = ", row[2],"\n")
    choice=input("choose your option: (1) delete, (2) update, (3)add new product: ")
    if choice=="3":
        NewProduct()
    if choice == "2":
        UpdateProduct()
    if choice == "1":
        DeleteProduct()
        
def Courriers():
    sql_select_Query = "select * from courriers"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of courriers in table: ", cursor.rowcount,"\n")

    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Number  = ", row[2],"\n")
    
    choice=input("choose your option: (1) delete, (2) update, (3)add new courrier: ")
    if choice=="3":
        NewCourrier()
    if choice == "2":
        UpdateCourrier()
    if choice == "1":
        DeleteCourrier()

Choice()