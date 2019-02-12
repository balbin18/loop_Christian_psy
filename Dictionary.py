contacts = {}

while True:
    print('1. Add number')
    print('2. Search number')
    print('3. Print contacts')

    user_choice = input('Select: ')

    if user_choice == '1':
        name = input('\nEnter name: ')
        number = input('Enter number: ')
        print()

        contacts[name] = number
    elif user_choice == '2':
        search = input('\nSearch: ')
        print('{} - {}'.format(search, contacts[search]))
        print()
    elif user_choice == '3':
        print()
        print(contacts)
        print()
    else:
        print('\nInvalid choice')

     
        print("1 - Add Number")
        print("2 - Search Number")

dict_phone = {}
while True:
    choices = (input ("Enter Choices: "))

    if choices == "1":
        name = input("Enter name: ")
        p_num = input("Enter #: ")
        dict_phone[name] = p_num

    elif choices == "2":
        dict_phone[name] = p_num
        Search = input("Enter name: ")
        print(dict_phone[Search])
    else:
        break
