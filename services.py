import time

inventory = [
    {
        'title' : 'arlekino',
        'author' : 'carlos rivera',
        'category' : 'comedy',
        'price' : 50,
        'quatity' : 12
    },
    {
        'title' : 'trava u doma',
        'author' : 'jennifer arango',
        'category' : 'adventure',
        'price' : 40,
        'quatity' : 21
    },
    {
        'title' : 'afterlife',
        'author' : 'daniel restrepo',
        'category' : 'action',
        'price' : 10,
        'quatity' : 30
    },
    {
        'title' : 'rose at nightfall',
        'author' : 'charlote arias',
        'category' : 'romance',
        'price' : 31,
        'quatity' : 6
    },
    {
        'title' : 'trinity',
        'author' : 'steve laurent',
        'category' : 'fantasy',
        'price' : 35,
        'quatity' : 25
    }
    
]

sales = []

# Option function
def number_input(text, type=float):

    # Input option validation
    while True:
        try:
            value =  type(input(text))
            return value
        except ValueError:
            print('[ERROR]: Invalid input. Please try again.')
            for countdown in range(2,0,-1):
                time.sleep(1)

# Add product function
def add_inventory():
    print('|===============[REGISTER INVENTORY]===============|')

    # Input validations
    while True:
        title = str(input('Enter the product title: '))

        if title.replace(" ", "").isalpha():
            break
        print("[ERROR]: The title can only contain letters. Please try again.")
        for countdown in range(2,0,-1):
            time.sleep(1)

    while True:
        author = str(input('Enter the author name: '))

        if author.replace(" ", "").isalpha():
            break
        print("[ERROR]: The author name can only contain letters. Please try again.")
        for countdown in range(2,0,-1):
            time.sleep(1)

    while True:
        category = str(input('Enter the category: '))

        if category .replace(" ", "").isalpha():
            break
        print("[ERROR]: The category can only contain letters. Please try again.")
        for countdown in range(2,0,-1):
            time.sleep(1)
    
    while True:
        try:
            price = int(input('Enter the product price: '))

            if price > 0:
                break
            else:
                print("[ERROR]: The price must be a number greater than 0.")
                for countdown in range(2,0,-1):
                    time.sleep(1)
        except ValueError:
            print("[ERROR]: You must enter a valid number.")
            for countdown in range(2,0,-1):
                time.sleep(1)

    while True:
        try:
            quatity = int(input('Enter the product quatity: '))

            if quatity > 0:
                break
            else:
                print("[ERROR]: The quantity must be a number greater than 0.")
                for countdown in range(2,0,-1):
                    time.sleep(1)
        except ValueError:
            print("[ERROR]: You must enter a valid number.")
            for countdown in range(2,0,-1):
                time.sleep(1)

    # Add product

    item = {
        'title' : title,
        'author' : author,
        'category' : category,
        'price' : price,
        'quatity' : quatity
    }
    
    inventory.append(item)
    print(f'[NOTICE]: Product added correctly')
    for countdown in range(2,0,-1):
        time.sleep(1)

def check_inventory():
    print('|===============[INVENTORY]===============|')
    for i, p in enumerate(inventory):
        print(f"[{i+1}] Titule: {p['title']} | Author: {p['author']} | Category: {p['category']} | Price: ${p['price']} | Quatity: {p['quatity']}")

def update_inventory():
    print('|===============[UPDATE INVENTORY]===============|')
    check_inventory()
    index = number_input('Select product number to update: ', int) - 1 

    if index not in range(len(inventory)):
        print("[ERROR]: You must enter a valid number.")
        return
    
    print("\n[NOTICE]: Leave fields blank if you want to keep some current data.\n")

    item = inventory[index]

    new_title = input(f'Input the new title: ({item['title']}): ' or item['title'])
    new_author = input(f'Input the new author: ({item['author']}): ' or item['author'])
    new_category = input(f'Input the new category: ({item['category']}): ' or item['category'])
    new_price = input(f'Input the new price: ({item['price']}): ' or item['price'])
    new_quatity = input(f'Input the new quatity: ({item['quatity']}): ' or item['quatity'])

    item['title'] = new_title
    item['autohr'] = new_author
    item['category'] = new_category
    item['price'] = new_price
    item['quatity'] = new_quatity

    print('[NOTICE]: Product updated successfully.')
    for countdown in range(2,0,-1):
        time.sleep(1)

def delete_inventory():
    print('|===============[DELETE INVENTORY]===============|')

    check_inventory()
    index = number_input('Select product number to delete: ', int ) - 1

    if index not in range(len(inventory)):
        print("[ERROR]: You must enter a valid number.")
        return
    
    delete = inventory.pop(index)
    print(f'[NOTICE]: Item {delete['title']} removed')
    for countdown in range(2,0,-1):
        time.sleep(1)

def register_sale():
    print('|===============[REGISTER SALE]===============|')

    while True:
        customer = str(input('Enter the customer name: '))

        if customer.replace(" ", "").isalpha():
            break
        print("[ERROR]: The customer name can only contain letters. Please try again.")
        for countdown in range(2,0,-1):
            time.sleep(1)

    check_inventory()

    index = number_input('Select product number sold: ', int) - 1

    if index not in range(len(inventory)):
        print("[ERROR]: You must enter a valid number.")
        return
    
    item = inventory[index]

    amount = number_input('Input the quantity sold: ' , int) 

    if amount > item['quatity']:
        print('[ERROR]: Insufficient quantity. The sale cannot be completed.')
        return
    
    
    discount = number_input('Input the discount applied (Enter 0 if not applicable): ')
    date = input('Input the sale date (D/M/Y): ')

    item['quatity'] -= amount

    total = ((item['price'] * amount) * (1 - discount / 100))
    

    sale = {
        'customer' : customer,
        'item' : item['title'],
        'quatity' : amount,
        'date' : date,
        'discount' : discount
    }

    sales.append(sale)
    print('[NOTCE]: Sale successfully registered')
    for countdown in range(2,0,-1):
        time.sleep(1)

def show_sales():
    print('|===============[SHOW SALES]===============|')

    for v in sales:
        print(f"DATE: {v['date']} - {v['item']} x{v['quatity']} | Customer: {v['customer']} | Total: ${v['total']}")

def top_3_items():
    print('|===============[TOP 3 ITEMS]===============|')

    count = {}

    for sale in sales:
        count[sale['title']] = count.get(sale['title'], 0) + sale['quatity']

    ranking = sorted(count.items(), key=lambda x: x[1], reverse=True)

    print(ranking[:3])

def sales_by_author():
    print('|===============[SALES BY AUTHOR]===============|')

    totales = {}

    for sale in sales:
        author = next(p['author'] for p in inventory if ['title'] == sale['item'])
        totales[author] = totales.get('author', 0) + sale['total']

    for author, total in totales.items():
        print(f'{author}: ${total}')

def calculate_net_and_gross_income():
    print('|===============[CALCULATE NET AND GROSS INCOME]===============|')

    gross_income = sum(v['total'] for v in sales)
    net_income = gross_income * 0.90

    print(f'Gross Income: ${gross_income}\n'
          f'Net Income (after 10%): ${net_income}')