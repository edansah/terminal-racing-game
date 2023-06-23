from racers import *
from time import sleep


def pick_racer() -> WackyRacer:
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
                print()
                print('=============================')
                print(f'You picked {racer_objects[choice].name}!')
                print('=============================\n\n')
                return racer_objects[choice]
                picked = True


def race_func(player_choice: WackyRacer):
    finished = False

    while not finished:

        for racer in racer_objects:
            race_length = 50
            race_turns = 0

        while racer.distance_travelled < race_length:
            sleep(0.4)
            race_turns += 1

            for racer in racer_objects:
                racer.distance_travelled += racer.new_speed()
                print(f'{racer.name} moved {str(racer.new_speed())} units in {racer.car_name}')
                print(f'Distance covered so far: {racer.distance_travelled}')
                print('-----------------------------------------------------------------')
                if racer.distance_travelled >= race_length:
                    if racer == player_choice:
                        print()
                        print()
                        print(f'Your pick, {racer.name}, won the race!')
                        print(f'Turns taken: {race_turns}')
                        print()
                        break
                    else:
                        print()
                        print()
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print(f'{racer.name} won the race! Better luck next time.')
                        print(f'Turns taken: {race_turns}')
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print()
                        break
        finished = True


def start_race():
    choice = pick_racer()
    started = False
    while not started:
        try:
            begin = input('Press ENTER to start the race')
            print()
            print()
            started = True
        except ValueError:
            print()
        if begin == '':
            race_func(choice)
        else:
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
    start_race()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
