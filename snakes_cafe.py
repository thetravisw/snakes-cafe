import sys


#create menu list
menu = [["Drinks",[["Cold Beer","7"],["Warm Beer","5"],["Cocktails","9"],["Cobra Venom","10"]]],["Apps",[["Pulled Pork Sliders","12"],["Beer Batter Oyster Fry","18"],["Grilled Rattlesnake Tacos","16"]]],["Entrees",[["Anaconda Soup","35"],["Dry Aged House NY Strip","55"],["Pan Seared Yellowfin","40"]]],["Desserts",[["Pat's Salmon Cookies","11"],["Creme Brulee","16"],["Strawberry Short-Snake","14"]]]]
  
# print the menu

MenuSize=0
print("""
***********************************
Welcome to Snakes on a Plane, 
The finest of in-flight dining.

"I [never get] tired of these Mother$%&#ing Snakes 
On this Mother@!#$ing Plane!" ~~ Samuel L Jackson
***********************************

""")

# Print the Menu
OrderMenu = []
for i in range (0,len(menu)):
  print(menu[i][0]) #prints the menu categories
  for j in range (0,len(menu[i][1])):
    MenuSize += 1
    print(f"{MenuSize}  {menu[i][1][j][0]}    {menu[i][1][j][1]}")  #prints menu item and price
    OrderMenu.append([menu[i][1][j][0],0])
  print ("""
  """)

print("""
To Order, enter an item number.  To quit, type 'Q' To Complete your Order type 'Done'""")

# infinte while loop for taking orders
while True:
  MenuItem = input("Your order: ")
  
  # Exit Out
  if MenuItem == "Q" or MenuItem == "Done":
    break


  # Check for valid entry and handle errors
  try:
    OrderNum = int(MenuItem)
    if OrderNum<1 or OrderNum > len(OrderMenu)-1:
      print("Wrong number.  It's ok though, math is hard.")
    else:
      OrderNum = int(MenuItem)
      # We have an acceptble input.   Add item to order and print the acknowledgement.
      OrderMenu[OrderNum-1][1] += 1  #I attempted to put this in the Try/Catch block above, thus avoiding the If statement.   Unfortunately, Python doesn't throw an error for me when attempting to do this with an OrderNum <1
      print("""


      your current order is:""")
      for i in range (0, len(OrderMenu)-1):
        print(f"{i+1}:  ({OrderMenu[i][1]}x) " + OrderMenu[i][0])
      print("Choose your next item, or type Q to quit, or Done to finish the transaction")
  except:
    print("Why U no read?  Input a menu item number, 'Q' to quit, or 'Done' to finish")
  

