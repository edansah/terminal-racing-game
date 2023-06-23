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


def race_function(player_choice: WackyRacer):
    finished = False
    race_length = 20
    race_loop = 0

    while not finished:
        for racer in racer_objects:
            while racer.distance_travelled < race_length:
                sleep(0.5)
                race_loop += 1

                for contestant in racer_objects:
                    contestant.distance_travelled += contestant.new_speed()
                    print(f'{contestant.name} moved {contestant.new_speed()} units.\n'
                          f'Distance travelled: {contestant.distance_travelled} units\n'
                          f'-----------------------------------------------------', end='')
                    print()
                    if contestant.distance_travelled >= race_length:
                        if contestant == player_choice:
                            print()
                            print(f'You won with {contestant.name}, congratulations!\n'
                                  f'Loops taken: {race_loop}')
                        else:
                            print()
                            print(f'{contestant.name} won!\n'
                                  f'Loops taken: {race_loop}')

                        finished = True
                        break




def start_race():
    choice = pick_racer()
    started = False
    while not started:
        try:
            begin = input('Press ENTER to start the race')
            print()
            print()
        except ValueError:
            print()
        if begin == '':
            race_function(choice)
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
