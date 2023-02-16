# Searches a sales data .csv file and prints results based on input
# Alternate version

def main():
    while True:
        criteria = input('Search by invoice id (id) or customer last name (lname)? ').lower()
        if criteria == 'lname' or criteria == 'id': break
        print("ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search\n")

    if criteria == 'id':
        search_idx = 0
    else:
        search_idx = 2

    sales_data = open('sales_data.csv', 'r')
    search_term = input('Enter your search term: ')
    next(sales_data)
    print()

    total_records = 0
    for data in sales_data:
        tokens = data.split(',')

        if tokens[search_idx].lower() == search_term.lower():
            print(data.strip())
            total_records += 1

    sales_data.close()

    if total_records == 1:
        print('\n1 record found')
    else:
        print(f'\n{total_records} records found')

main()