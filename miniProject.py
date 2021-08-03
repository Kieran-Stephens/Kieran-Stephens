
import inflect
import unittest
import patch from mock
import mysql.connector
from collections import defaultdict
d = defaultdict(list)
from itertools import groupby
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="test"
)
mycursor = mydb.cursor()
p = inflect.engine()





    

    
def NewOrder():
    
    f = input("Name of person ordering? ")
    b = input(f"{f}'s address? ")
    c = input(f"{f}'s phone number? ")
    d = input("Courriers id? ")
    HowMany = int(input("How Many items do you want to insert in the order? "))
    
    
    status = "preparing"
    
    
        
    
    
    sql = "INSERT INTO orders (customer_name,customer_address,customer_phone,courrierID,status) VALUES (%s,%s,%s,%s,%s)"
    val = (f,b,c,d,status)
    
    try:
        mycursor.execute(sql,val)
        mydb.commit()
        
        sql = "SELECT max(orderID) from orders"
        cursor = mydb.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        H = records[0][0]
        for n in range(HowMany):
            Ordinal = p.ordinal(n+1)
            item = input(f"{Ordinal} item id you want to insert? ")
            
            sql = f"INSERT INTO OrderProducts VALUES ({H},{item})"

            mycursor.execute(sql)
            mydb.commit()
        
        print(f"New order with customer_name {f} inserted.")
    except mysql.connector.errors.IntegrityError:
        print("Courrier ID doesnt exist, please check courriers for valid IDs.")
    
    
def UpdateOrder():    
    
    repeat = "Y"
    f=input("What is the id of the order you want to update? ")
    while repeat == "Y":
        b=input("what do you want to update? (customer_name, customer_address) ")
        if b == "orderID":
            print("You cannot change the orderID")
        if b=="items":
            HowMany = int(input("How Many items do you want to update in the order? "))
            for n in range(HowMany):
                Ordinal = p.ordinal(n+1)
                item = input(f"{Ordinal} items id you want to change? ")
                Change = int(input("What do you want to change it with? "))
                sql = f"UPDATE OrderProducts SET ProductID = '{Change}' WHERE orderID = {f} and ProductID = {item}"
            
                mycursor.execute(sql)
                mydb.commit()
                print(f"Item with id {item} in Order with id {f} has been updated with item with id {Change}")
                
                
        else:
            e=input("What do you want to update it with? ")

            sql = f"UPDATE orders SET {b} = '{e}' WHERE orderID = {f}"
            try:
                mycursor.execute(sql)
                mydb.commit()
                print(f"Order with id {f} has been updated with {b} {e}")
            except mysql.connector.errors.IntegrityError:
                print("Courrier ID doesnt exist, please check courriers for valid IDs.")
        repeat = input("Would you like to change another area in the product? (Y/N with capitals) ")

def DeleteOrder():    
    

    val=int(input("What is the id of the order you want to delete? "))
    sql = "DELETE FROM OrderProducts WHERE orderID = {}".format(val)
    sql2 = "DELETE FROM orders WHERE orderID = {} ".format(val)
    mycursor.execute(sql)
    mycursor.execute(sql2)
    mydb.commit()

    print(f"Order with id {val} has been deleted")
    
    
def TrackOrder():
    OrderID = input("What is your order ID? ")
    sql = f"SELECT status from orders WHERE orderID = {OrderID}"
    cursor = mydb.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    print("The Status of order with ID ",OrderID," is: ",records[0][0])
    
    

    
    
    
    
    
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
    f=input("What is the ID of the product you want to update? ")
    while repeat == "Y":
        b=input("what do you want to update? (name or price) ")
        e=input("What do you want to update it with? ")
        sql = f"UPDATE products SET {b} = '{e}' WHERE ProductID = {f}"
        mycursor.execute(sql)
        mydb.commit()
        print(f"Product with id {f} has been updated with {b} {e}")
        repeat = input("Would you like to change another area in the product? (Y/N with capitals) ")
    
def DeleteProduct():
    
    val=int(input("What is the id of the product you want to delete? "),)
    sql = "DELETE FROM products WHERE ProductID = {}".format(val)
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
        sql = f"UPDATE courriers SET {b} = '{e}' WHERE CourrierID = {f}"
        mycursor.execute(sql)
        mydb.commit()
        print(f"Courrier with id {f} has been updated with {b} {e}")
        repeat = input("Would you like to change another area in the order? (Y/N with capitals) ")
        
        
        

def DeleteCourrier():
    
    
    val=int(input("What is the id of the courrier you want to delete? "),)
    sql = "DELETE FROM courriers WHERE CourrierID = {}".format(val)
    mycursor.execute(sql)

    mydb.commit()

    print(f"Courrier with ID {val} has been deleted")




def Choice():
    OorP = input("Products, Courriers or Orders? ")
    if OorP == "Orders":
        Orders()
    elif OorP == "Courriers":
        Courriers()
    elif OorP == "Products":
        Products()


def Orders():
    sql_select_Query = "select * from orders ORDER BY status"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of products in table: ", cursor.rowcount,"\n")
    list1 = []
    mycursor = mydb.cursor()



    sql = """SELECT orders.orderID,products.ProductID
    FROM ((orders
    INNER JOIN OrderProducts ON orders.orderID = OrderProducts.orderID)
    INNER JOIN products ON OrderProducts.ProductID = products.ProductID)
    """
    cursor = mydb.cursor()
    cursor.execute(sql)
    items = cursor.fetchall()
    print("Total number of products in table: ", cursor.rowcount,"\n")
    itemsList=[]
    from itertools import groupby
    from operator import itemgetter
    
    sorter = sorted(items, key=itemgetter(0))
    grouper = groupby(sorter, key=itemgetter(0))
    
    res = {k: list(map(itemgetter(1), v)) for k, v in grouper}
    
    print(res)
    for row in records:
        indexForItem=int(row[0])
        print("orderID = ", row[0])
        print("customer_name = ", row[1])
        print("customer_address  = ", row[2])
        print("customer_phone  = ", row[3])
        print("courrierID  = ", row[4])
        print("status  = ", row[5])
        print("items = ",res[indexForItem],"\n")       
    choice=input("choose your option: (1) delete, (2) update, (3)add new order, (4)track product inventory: ")
    if choice=="3":
        NewOrder()
    if choice == "2":
        UpdateOrder()
    if choice == "1":
        DeleteOrder()
    if choice == "4":
        TrackOrder()

def Products():
    
    sql_select_Query = "select * from products"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of products in table: ", cursor.rowcount,"\n")

    for row in records:
        print("ProductId = ", row[0], )
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
        print("CourrierId = ", row[0], )
        print("name = ", row[1])
        print("number  = ", row[2],"\n")
    
    choice=input("choose your option: (1) delete, (2) update, (3)add new courrier: ")
    if choice=="3":
        NewCourrier()
    if choice == "2":
        UpdateCourrier()
    if choice == "1":
        DeleteCourrier()
    
Choice()