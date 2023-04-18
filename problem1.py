#Sushant Sushant
#22077514

#printing the greeting message.
print("WELCOME TO THE AMANDO SHOPPING SITE")

shopping_cart= {}
#shopping_cart is a dictionary.

option=0
#taking the options for the menu.
while(option!=4):
   
  print("1. Add product to cart. ")
  print("2. Search the product. ")
  print("3. Delete the product from the cart.")
  print("4. Quit.")


  option = int(input("Enter option between 1-4: "))
  
#giving the commands for the working of options.
  
  if option == 1:
     if len(shopping_cart) < 5:
       #pn = input for product name.   pb =  input for product brand.
            pn = input("Enter product name: ")
            pb = input("Enter product brand: ")
       #adding the product to the dictionary.
            shopping_cart.update({pn:pb})
            print("You added following items to the cart.")
       #this will be displayed when the user will try to add more than           5 items in the cart.
     else:
            print("Cart is full.")
      
    
    
  elif option == 2:
    #s = input for the product to be searched.
       s= input("Enter the item to be searched: ")
    #searching the products in the cart 
       if s in shopping_cart:
            b= shopping_cart[s]
            print(s,":",shopping_cart[pn])
         #if the prodct is alredy saved in the cart then it will be               displayed.
       else:
            print("No product exists with this name.")
         #if the item is wrong or which is not saved by the user, it               will not be displayed and a message will be displayed "No               product exists with this name."
  
  elif option == 3:
     if len(shopping_cart) > 0:
       #d = input for the product to be deleted.
        d = input("Enter the product name to be deleted: ")
       
        if d in shopping_cart:
            shopping_cart.pop(d)
            print("Product deleted from cart successfully.")
        else:
             print("No product exists with this name.")
#if the item entered which is to be deleted is in the cart then it will be deletd (.pop) and if the item is not there, it will show             "No product exists with this name."
     else:
            print("Cart is empty, no item is found.")
 #if the user has deleted all the items from the cart and he again try to do so then  it will show "Cart is empty, no item is found.""
      
  elif option == 4:
      print("Exiting.")

#exiting the program
          
