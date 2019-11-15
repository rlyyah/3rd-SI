def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as er:
        print(er)
    else:
        print('good index lul')
    finally:
        print('arrr, thanks!')
list_t = [1,2,3]

print_list_element(list_t, 4)


import logging

logging.basicConfig(filename='age.log', level=logging.ERROR)

age = None
while age == None:
    try:
        user_age = int(input('Enter your age: '))
    except ValueError as err:
        logging.error(err)
        print('you were very very bad this year!')
    else:
        age = user_age
        print(f"Apparently, you are {age} years old.")
