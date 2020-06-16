# CASH: GENERIC MODE (CORRECTIONS)
n = int(input("Insert total number of cash denominations: "))

if n <= 1:
    print("The number of denominations should be at least two")
    

else: 
    categories = []
    categories.append(int(input("Insert your first denomination  ")))

i = n - 1
while i > 0:
  categories.append(int(input("Insert another denomination  ")))
  i -= 1

categ = categories.sort(reverse = True)
print("Your cash denominations are ", categories)

u = input("Your total change is: ")
m = round(float(u)*100)

if m <= 0:
    print("The change should be positive")
if m < min(categories):
    print("Sorry! I can't give you change!")

else: 
    cant = []

    for i in range (n):
        cant.append((int(m/categories[i-n])* (categories[i-n])))
    
        if m >= categories[i-n]: 
            print("I give you", int(m/categories[i-n]),"coin(s) of",categories[i-n],"c")
            m %= categories[i-n]
           
    def sumlist(cant):
       sum = 0
       for i in cant:
        sum = sum + i
       return sum
   
    
    if (float(u) - sumlist(cant)/100) == 0:
     print("Your change is exact!")
    if (float(u) - sumlist(cant)/100) > 0:
     print("Sorry! I Owe you",int((float(u)*100 - sumlist(cant))),"cents")