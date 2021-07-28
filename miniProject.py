import inflect
import csv
import ast 
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
    if choice == "1":
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
    
        
    e = input("Name of Product? ")
    b = input(f"Price of {e}? ")
        
    update = {"name": e,  "price": b}
    a.append(update)
    print(a)
    keys = a[0].keys()
    a_file = open("products.csv", "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(a)

def UpdateProduct():
    
    repeat = "Y"
    
    f=input("What is the name of the Product you want to update? ")
    while repeat == "Y":
        b=input("what do you want to update? (name or price) ")
        e=input("What do you want to update it with? ")
        for n in range(len(a)):
            if a[n]['name']==str(f):
                a[n][b]=str(e)
        repeat = input("Would you like to change another area in the order? (Y/N with capitals) ")
    print(a)
    keys = a[0].keys()
    a_file = open("products.csv", "wb")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(a)
    
def DeleteProduct():
    
    x=input("What is the name of the product you want to delete? ")
    for n in range(len(a)):
        if a[n]['name']==str(x):
            a.remove(a[n])
            break
    print(a)
    if a != []:
        keys = a[0].keys()
        a_file = open("products.csv", "w")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
    else:
        a_file = open("products.csv", "wb")
        writer = csv.writer(a_file)
        row = ["name","price"]
        writer.writerow(row)
    
def NewCourrier():
    
        
    e = input("Name of Courrier? ")
    b = input(f"{e}'s number? ")
    
    update = {"name": e,  "price": b}
    a.append(update)
    print(a)
    keys = a[0].keys()
    a_file = open("courriers.csv", "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(a)
        
def UpdateCourrier():
        repeat = "Y"
        
        f=input("What is the name of the Courriers you want to update? ")
        while repeat == "Y":
            b=input("what do you want to update? (name or number) ")
            e=input("What do you want to update it with? ")
            for n in range(len(a)):
                if a[n]['name']==str(f):
                    a[n][b]=str(e)
            repeat = input("Would you like to change another area in the order? (Y/N with capitals) ")
        
        
        keys = a[0].keys()
        a_file = open("courriers.csv", "wb")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
def DeleteCourrier():
    e=input("What is the name of the Courrier you want to delete? ")
    for n in range(len(a)):
        if a[n]['name']==str(e):
            a.remove(a[n])
            break
    print(a)
    if a != []:
        keys = a[0].keys()
        a_file = open("courriers.csv", "wb")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
    else:
        a_file = open("courriers.csv", "wb")
        writer = csv.writer(a_file)
        row = ["name","number"]
        writer.writerow(row)




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
    
    a = prdfile
    
    for i in a:
        print(i)
    choice=input("choose your option: (1) delete, (2) update, (3)add new product: ")
    if choice=="3":
        NewProduct()
    if choice == "2":
        UpdateProduct()
    if choice == "1":
        DeleteProduct()
        
def Courriers():
    with open('courriers.csv') as f:
        a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    
    for i in a:
        print(i)
    choice=input("choose your option: (1) delete, (2) update, (3)add new courrier: ")
    if choice=="3":
        NewCourrier()
    if choice == "2":
        UpdateCourrier()
    if choice == "1":
        DeleteCourrier()

Choice()