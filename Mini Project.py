products = []
products.append("Rice")
products.append("coke") 
print(products)

def mainmenuoption():
    option = input("What is your menu option? ")
    if option == "0":
        exit()
    elif option == "1":
        print(products)

    elif option == "2":
        products.append(input("What is your new product? "))
    elif option == "3":
        for i in range(len(products)):
            print(f'{i} {products[i]}')
        index = input("Choose a product index. ")
        newProduct = input("What is your new product? ")
        products[int(index)] = newProduct
    elif option == "4":
        for i in range(len(products)):
            print(f'{i} {products[i]}')
        index = input("What is the index of the product you want to delete? ")
        del products[int(index)]
        
        
    print(products)    
mainmenuoption()

