from racers import *


def sort_function():
    print('*********************************')
    print('*********************************')
    success = False
    while not success:
        try:
            sort_num = int(input(f'Sort racers by: \n'
                                 f'0: Racer name\n'
                                 f'1: Car name\n'
                                 f'2: Car number\n'
                                 f'3: No. of drivers\n'
                                 f': '))
        except ValueError:
            print('\n=============================')
            print('Please enter a valid integer.')
            print('=============================\n')

        else:
            if sort_num not in [0, 1, 2, 3]:
                print('\n=============================')
                print('Please enter a valid integer.')
                print('=============================\n')
            else:
                print()
                print()
                sorted_list = return_sorted_list(sort_num)
                for i in sorted_list:
                    i.show_registration()

                print()
                success = True


def return_car_numbers():

    for i in range(len(racer_objects)):
        print(racer_objects[i].power())



def pick_racer():
    pass


def greeting():
    print(f'=================================\n'
          f'---------------------------------\n'
          f'WELCOME TO WACKY RACERS: THE GAME\n'
          f'---------------------------------\n'
          f'=================================\n')
    print()


def main():
    greeting()
    sort_function()
    return_car_numbers()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

