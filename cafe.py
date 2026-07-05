menu = ['cake', 'matcha', 'water', 'milkshake'] 

stock = {'cake': 2,
         'matcha': 4,
         'water': 1,
         'milkshake': 2}

price = {'cake': 5,
         'matcha': 6,
         'water': 2,
         'milkshake': 5}

total_stock = 0

for item in menu:
    item_value = (stock[item] * price[item])
    total_stock = total_stock + item_value

print(f"£{total_stock}") 
    

