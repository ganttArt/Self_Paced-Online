#!/usr/bin/env python3
import sys
import os
from operator import itemgetter

#--------------------------------------------------------------------------
def send_thank_you_letter(donor_name, donation_amt):
    print(f'\nDear {donor_name}\n'
         'Thank you for a recent donation to our Foundation in the amount of $' + f'{donation_amt}\n'
         '\nSincerely'
         '\nBill & Melinda Gates')


#-----------------------------------------------------------------------------
def send_thank_you_add_new_donation():
    donor_name =input('\n\nPlease enter name of donor:  ')
    donation_amt = input('\nEnter the amount > ')
    if donor_name in list_of_donors:
        list_of_donors[donor_name].append(float(donation_amt))

    # New donor
    else:
        list_of_donors[donor_name] = []
        list_of_donors[donor_name].append(float(donation_amt))
    # send thank you letter to the the donor name user just entered
    send_thank_you_letter(donor_name, donation_amt)


#----------------------------------------------------------------------------
def create_thank_you_files():
    for donor_name in list_of_donors.keys():
        #donor_name = each_donor['name']
        total_donation = sum(list_of_donors[donor_name]) #sum(each_donor['donation'])
        thks_letter = open('{name}.txt'.format(name = donor_name), 'w')
        thks_letter.write('Dear {name}, \n'
                          'Thank you for your generosity to our Foundation in the total amount of ${amt}'.format(name = donor_name,
                                                                                                                 amt = total_donation))
        thks_letter.close()

#----------------------------------------------------------------------------
def thank_you_menu_selection():
    user_selection = input('\n\nTHANK-YOU MENU\nChoose from one of options below:\n\
        L) List current donors\n\
        T) Send Thank-you letter (or Add donor and Send one)\n\
        F) Create Thank-you files\n\
        M) Back to MAIN MENU\n\
        Q) Quit the program\n\
        Please type L, T, F, M, or Q: ')
    return user_selection


#-------------------------------------------------------------------------
def thank_you_letter():
    while True:
        # use of dictionary where 'key' is the menu choice and 'value' is function to call
        thank_you_menu_function = {
        'L': create_report,
        'T': send_thank_you_add_new_donation,
        'F': create_thank_you_files,
        'M': main,
        'Q': quit_program
    }
        thank_you_selection = thank_you_menu_selection().upper()
        thank_you_menu_function.get(thank_you_selection, invalid_thank_you_menu)()
        #invalid_menu is to handle non-of-above choices


#--------------------------------------------------------------------------
def sort_donor_list(unsorted_list):
    sorted_donation_list = []
    for d in unsorted_list:
        total_donation =  sum(unsorted_list[d])
        number_of_donation = len(unsorted_list[d])
        average = total_donation / number_of_donation
        sorted_donation_list.append([d, total_donation, number_of_donation, average])
    #
    sorted_donation_list = sorted(sorted_donation_list, key = itemgetter(1), reverse = True)

    return sorted_donation_list


#------------------------------------------------------------------------------
def create_report():
    sorted_list = sort_donor_list(list_of_donors)
    report_header = ['Donor Name', 'Total Donation Amt', 'Num of Donation',  'Avg Per Donation']
    print('\n\n{:<25}{:>20}{:>20}{:>20}'.format(*report_header))
    print('-'*90)
    for donor in sorted_list:
        print('{:<26}${:>15,.2f}{:>15}{:>25,.2f}'.format(donor[0], donor[1], donor[2], donor[1] / donor[2]))
    print('\n\n')

def test_create_report():
    for key, item in list_of_donors.items():
        print("{:<20}: {}".format(key, item))


#------------------------------------------------------------------------------
def init_donor_list():
    # create initial list of donors and their donations
    global list_of_donors
    list_of_donors = {'William Boeing': [12.86, 2.00, 3.00, 4.00, 5.00],
                      'Steve Jobs':     [6.00, 7.00, 8.00],
                      'Paul Allen':     [9.00, 10.00, 11.00],
                      'Charles Flint':  [12.00, 13.00, 14.00],
                      'Thomas Edison':  [15.00, 16.00, 17.00]  }


#------------------------------------------------------------------------------
def main_menu_selection():
    response = input('\n\nMAIN MENU\nChoose from one of the options below:\n\
        T) THANK-YOU MENU\n\
        R) Create a Report\n\
        Q) Quit the program\n\
        Please type T, R, or Q: ')
    return response


#------------------------------------------------------------------------------
def quit_program():
    print('Bye!')
    sys.exit()


#-----------------------------------------------------------------------------
def invalid_menu():
    print('\nNot a valid option!\n\n')
    main()


#-----------------------------------------------------------------------------
def invalid_thank_you_menu():
    print('\nNot a valid option!\n\n')
    thank_you_menu_selection()


#------------------------------------------------------------------------------
def main():
    # use of dictionary where 'key' is the menu choice and 'value' is function to call
    main_menu_options = {
        'T': thank_you_letter,
        'R': create_report,
        'Q': quit_program
    }
    while True:
        init_donor_list()
        main_menu_action = main_menu_selection().upper()
        main_menu_options.get(main_menu_action, invalid_menu)() #invalid_menu is to handle
                                                                # non-of-above choices


#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()