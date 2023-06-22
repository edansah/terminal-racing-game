from racers import *


def sort_function():
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
            print('Non-number given.')
            print('=============================\n')

        else:
            if sort_num not in [0, 1, 2, 3]:
                print('\n=================================')
                print('Please enter a valid sorting number.')
                print('===================================\n')
            else:
                print()
                print()
                sorted_list = return_sorted_list(sort_num)
                print('=============================\n\n')
                for i in sorted_list:
                    i.show_registration()

                print()
                success = True


def return_car_numbers() -> list:
    car_num_list = []
    for car in racer_objects:
        car_num_list.append(car.car_num)

    return car_num_list


def pick_racer():
    car_numbers = return_car_numbers()

    picked = False
    while not picked:
        try:
            choice = int(input('Select a racer by entering their car number: '))
        except ValueError:
            print('\n=============================')
            print('Please enter a valid integer.')
            print('=============================\n')
        else:
            if str(choice) not in car_numbers:
                print('\n=============================')
                print('Please select a valid car number from the following:')
                print(car_numbers)
                print('=============================\n')
            else:
                print()
                print('=============================')
                print(f'You picked {racer_objects[choice].name}!')
                print('=============================\n')
                picked = True


def greeting():
    print(f'=================================\n'
          f'---------------------------------\n'
          f'WELCOME TO WACKY RACERS: THE GAME\n'
          f'---------------------------------\n'
          f'=================================\n')
    print()


def start_race():
    finished = False


def main():
    greeting()
    sort_function()
    pick_racer()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
