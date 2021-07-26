import inflect
import csv
p = inflect.engine()



OorP = input("Products, Courriers or Orders? ")
print1=[]

if OorP == "Orders":
    with open('orders.csv') as f:
        a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    
    for i in a:
        
        print1.append(i)
    for i in print1:
        print(i)
    
        
    choice=input("choose your option: (1) delete, (2) update, (3)add new order: ")
    if choice=="3":
        
        f = input("Name of person ordering? ")
        b = input("Customer address? ")
        c = input("Customers phone number? ")
        d = input("name of courier? ")
        e = int(input("How many items do you want to insert? "))
        y=[]
        for n in range(e):
            Ordinal = p.ordinal(n+1)
            item = input(f"{Ordinal} item")
            y.append(item)
            
        update = {"customer_name": f,  "customer_address": b,  "customer_phone": c,  "courier": d,  "status": "preparing", "items": f}
        
        a.append(update)
        print(a)
        keys = a[0].keys()
        a_file = open("orders.csv", "wb")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
        
        
    if choice=="2":
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
        textfile3= open("orders.csv","wb")
        for order in a:
            textfile3.write(str(order)+"\n")
    if choice == "1":
        f=input("What is the customer name of the order you want to delete? ")
        c = input(f"What is {f}'s phone number ? ")
        for n in range(len(a)):
            if a[n]['customer_name']==str(f):
                    if a[n]['customer_phone'] == c:
                        a.remove(a[n])
                        break
    
        keys = a[0].keys()
        a_file = open("orders.csv", "wb")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
    
    
    
elif OorP == "Products":
    with open('products.csv') as f:
        a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    
    for i in a:
        print(i)

    choice=input("choose your option: (1) delete, (2) update, (3)add new order: ")
    if choice=="3":
        
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
    if choice=="2":
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
    if choice == "1":
        a=input("What is the name of the product you want to delete? ")
        for n in range(len(a)):
            if a[n]['name']==str(a):
                a.remove(a[n])
                break
        print(a)
        keys = a[0].keys()
        a_file = open("products.csv", "wb")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
    
elif OorP == "Courriers":   
    with open('courriers.csv') as f:
        a = [{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)]
    
    for i in a:
        print(i)

    choice=input("choose your option: (1) delete, (2) update, (3)add new order: ")
    if choice=="3":
        
        e = input("Name of Courrier? ")
        b = input(f"{e}'s number? ")
        
        update = {"name": e,  "price": b}
        a.append(update)
        print(a)
        keys = a[0].keys()
        a_file = open("courriers.csv", "wb")
        dict_writer = csv.DictWriter(a_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(a)
        
    if choice=="2":
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
    if choice == "1":
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








