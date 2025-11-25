import time
from services import (
    add_inventory,
    check_inventory,
    update_inventory,
    delete_inventory,
    register_sale,
    show_sales,
    top_3_items,
    sales_by_author,
    calculate_net_and_gross_income
)

def menu():
    while True:
        opcion = input('|=============[National Bookstore]=============|\n'
                    '|1. Add Inventory\n'
                    '|2. Check Inventory\n'
                    '|3. Update Inventory\n'
                    '|4. Delete Inventory\n'
                    '|5. Register Sale\n'
                    '|6. Show Sales\n'
                    '|7. Top 3 Items\n'
                    '|8. Sales by author\n'
                    '|9. Calculate net and gross income\n'
                    '|10. Exit\n'
                    '[OPTION]: ')
                    
        if opcion < "1" and opcion > "10":
            print('[ERROR]: Invalid input. Please try again.')
            for countdown in range(2,0,-1):
                time.sleep(1)
        elif opcion == "1":
            add_inventory()
        elif opcion == "2":
            check_inventory()
        elif opcion == "3":
            update_inventory()
        elif opcion == "4":
            delete_inventory()
        elif opcion == "5":
            register_sale()
        elif opcion == "6":
            show_sales()
        elif opcion == "7":
            top_3_items()
        elif opcion == "8":
            sales_by_author()
        elif opcion == "9":
            calculate_net_and_gross_income()
        else:
            print('[WARNING]: Exiting the program')
            for countdown in range(3,0,-1):
                print(f'[COUNTDOWN] {countdown}...')
                time.sleep(1)
            print('[NOTICE]: Program completed.')
            break

menu()