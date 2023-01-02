###########################################################

    #  Computer Project #9

    #

    #  Algorithm

    #     the program prompts the user for prices and security file and opens them
    #     read_file() function is then used to create a set of company names and the master dictonary consisting the data of company with company code as the key  
    #     add_price() function uses the master list and prices file pointer as parameters to update the prices in the master list
    #   the program asks the user for the company symbol which along with master list is used in get_max_price_of_company() to find the maximum value price for the company along with the date 
    #   find_max_company_price() uses the get_max_price_of_company() to return the company with most value along with the company code
    #   get_average_price_of_company() is similar to get_max_price_of_company(), the difference is that it does not uses the max() and calculates the average price of the specific companies
    #   display_list() displays the list of items in 3 columns in centre with total of 35 character space, every 4th item is added to the new line

###########################################################

import csv
#options for the menu
MENU = '''\nSelect an option from below:
            (1) Display all companies in the New York Stock Exchange
            (2) Display companies' symbols
            (3) Find max price of a company
            (4) Find the company with the maximum stock price
            (5) Find the average price of a company's stock
            (6) quit
    '''
#welcome banner printed at start of the program
WELCOME = "Welcome to the New York Stock Exchange.\n"

def open_file():
    '''This function is going to ask the user for the price and security file. The function will keep looping until each file is open.'''
    while True:
        price_file_name = input("\nEnter the price's filename: ")
        try:
            price_fp = open(price_file_name, 'r')
            break
        except:
            print("\nFile not found. Please try again.")
    while True:
        security_file_name = input("\nEnter the security's filename: ")
        try:
            security_fp = open(security_file_name, 'r')
            return price_fp, security_fp
        except:
            print("\nFile not found. Please try again.")
            

def read_file(securities_fp):
    '''This function uses the securities file pointer to create the dictionary of companies data with their code as the key. A empty list is added in the dictionary to add the prices later on.'''
    company_name_set = set()
    company_dict = dict()
    security_reader = csv.reader(securities_fp)
    next(security_reader)
    for line in security_reader:
        company_data = [line[1], line[3], line[4], line[5], line[6], []]
        company_name_set.add(line[1])
        company_dict[line[0]] = company_data
    return company_name_set, company_dict
        
def add_prices (master_dictionary, prices_file_pointer):
    '''This function uses the master dictonary and price file pointer to add the prices in the empty list of index 5 in master list. The master dictionary is modified and no values are returned'''

    price_reader = csv.reader(prices_file_pointer)
    next(price_reader)
    for line in price_reader:
        price_data = [line[0], float(line[2]), float(line[3]), float(line[4]), float(line[5])]
        if line[1] in master_dictionary:
            master_dictionary[line[1]][5].append(price_data)
        else:
            continue
    
def get_max_price_of_company (master_dictionary, company_symbol):
    '''This function uses master dictionary and company symbol prompted from used to find the max price value of that company along with the date on which it reached the maximum value.'''
    if company_symbol in master_dictionary:
        company_high_price = []
        price_list = master_dictionary[company_symbol][5]
        if price_list:
            for line in price_list:
                tup = (line[4], line[0])
                company_high_price.append(tup)
            max_price = max(company_high_price)
            return max_price
    return (None, None)

def find_max_company_price (master_dictionary):
    '''This function uses the get_max_price_of_company to calculate the highest company value and find the company name. It returns the value in form of string and float'''
    max_company_price_list = []
    for key in master_dictionary:
        max_price = get_max_price_of_company(master_dictionary, key) 
        if None in max_price:
            continue
        max_company_price_list.append((max_price[0], key))
    max_company_price = max(max_company_price_list)
    return max_company_price[::-1]

def get_avg_price_of_company (master_dictionary, company_symbol):
    '''This function is similar to get_max_price_of_company, just instead of using max(), the sum() and len() is used to find the average price of the company '''
    if company_symbol in master_dictionary:
        average_high_price_list = []
        price_list = master_dictionary[company_symbol][5]
        if price_list:
            for line in price_list:
                average_high_price_list.append(line[4])
            if average_high_price_list:
                avg_price = (sum(average_high_price_list))/(len(average_high_price_list))
                return round(avg_price, 2)
    return 0.0
            
def display_list (lst):  # "{:^35s}"
    '''This function takes a list as parameter and displays it in the form of 3 columns and a new line is added after every 3 item in the list. It also does not create a new line if there are less than 3 items in last line'''
    for index, items in enumerate(lst):
        print("{:^35s}".format(items), end = '')
        if (index + 1)%3 == 0:
            print()
    
#main function runs the program using the other functions
def main():
    #printing welcome message
    print(WELCOME)
    #calls the open file function to get the file pointers of each specific files
    price_fp, security_fp = open_file()
    #read_file function is called to create a set of company names and a master list 
    securities_set, master_dictionary = read_file(security_fp)
    #this function is used to modify the master list and add the prices in the empty list of the dictionary
    add_prices(master_dictionary, price_fp)

    #while the statement is true
    while True:
        #it will keep printing the Menu and ask for options until the user quits the program
        print(MENU)
        #prompts the user to enter an option
        option = int(input("\nOption: "))
        
        #if the user enters option 6, it quits the program
        if option == 6:
            print("\n")
            break
        #when option 1 is entered, list of companies is displayed using the display_list function
        elif option == 1:
            print("\n{:^105s}".format("Companies in the New York Stock Market from 2010 to 2016"))
            display_list(sorted(list(securities_set)))
            print("\n")

        #if the option 2 is selected, the company symbols are displayed in sorted format using the display_list function
        elif option == 2:
            print("\ncompanies' symbols:")
            display_list(sorted(list(master_dictionary.keys())))
            print("\n")
        
        #when option 3 is prompted, it finds the maximum price of the company symbol entered
        elif option == 3:
            while True:
                #the user is asked for the company symbol
                company_symbol = input("\nEnter company symbol for max price: ")
                #if the company symbol is correct, it runs the get_max_price_of_company function
                if company_symbol in master_dictionary:
                    company_max_price, max_price_date = get_max_price_of_company(master_dictionary, company_symbol)
                    #if the value is none, it prints about no prices being in the company
                    if company_max_price == None:
                        print("\nThere were no prices.")
                    else:
                        #prints the max value of stock and date it was highest on
                        print("\nThe maximum stock price was ${:.2f} on the date {:s}/\n".format(company_max_price, max_price_date))
                    break
                else:
                    print("\nError: not a company symbol. Please try again.")
        #if option 4 is entered, the company with highest stock price is calculated
        elif option == 4:
            #find_max_company_price function is called for it
            max_price_company_name, company_max_price = find_max_company_price(master_dictionary)
            #prints the comapny name with its stock value
            print("\nThe company with the highest stock price is {:s} with a value of ${:.2f}\n".format(max_price_company_name, company_max_price))
        #when option 5 is entered, it finds the average stock value of the company
        elif option == 5:
            while True:
                #ask user to enter the company symbol
                company_symbol = input("\nEnter company symbol for average price: ")
                #if the entered symbol is in master dictionary, the average is calculated
                if company_symbol in master_dictionary:
                    company_avg_price = get_avg_price_of_company(master_dictionary, company_symbol)
                    #if the average is none, no values are printed
                    if company_avg_price == None:
                        print("\nThere were no prices.")
                    else:
                        print("\nThe average stock price was ${:.2f}.\n".format(company_avg_price))
                    break
                else:
                    #if no symbol exists in dictionary, it asks the user to enter the symbol again
                    print("\nError: not a company symbol. Please try again.")
        #if an invalid option is entered, the user is asked to select the option until they enters the right option
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__": 
    main() 
