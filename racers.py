from random import randint


# Opens the .csv in read-only mode
# Reads contents into one big string
# Splits string by newline, converting it to a list. One line = a contestant
# Omit the .csv 's index using a for loop
# Split each line by commas, turning each contestant into a list
# Each item in the new lists is a property of the contestants, i.e. name etc.
# Append these to a new list and return list
def process_contestant_csv(csv_file: str) -> list:
    contestants = open(csv_file, 'r')
    contestants = contestants.read()
    contestants = contestants.split('\n')

    clean_racer_list = []

    for i in range(1, len(contestants)):
        racer = contestants[i].split(',')
        clean_racer_list.append(racer)

    return clean_racer_list


# Data cleaned, hence ready to create class
class WackyRacer:
    def __init__(self, racer_info):
        racer_name, car_name, car_num, passengers, power = racer_info
        self.name = racer_name
        self.car_name = car_name
        self.car_num = car_num
        self.passengers = passengers
        self.power = power
        # Gives WackyRacer object a random speed between 1 and 10
        self.speed = randint(1, 10)
        self.distance_travelled = 0

    def show_registration(self):
        print(f'Contestant name: \t{self.name}\n' 
              f'Car name: \t\t\t{self.car_name}\n'
              f'Car number: \t\t{self.car_num}\n'
              f'No. of drivers: \t{self.passengers}\n'
              f'Power: \t\t\t\t{self.power}\n')

    def new_speed(self) -> int:
        return randint(1, self.speed)

    # Used for sorting
    def return_properties(self) -> list:
        return [self.name, self.car_name, self.car_num, self.passengers]


# Returns list of WackyRacer objects
def create_racer_objects(cleaned_list: list) -> list:
    the_racers = []

    for i in range(len(cleaned_list)):
        my_racer = WackyRacer(cleaned_list[i])
        the_racers.append(my_racer)
    return the_racers


# Returns list of car numbers
def return_car_numbers() -> list:
    car_num_list = []
    for _ in racer_objects:
        car_num_list.append(_.car_num)

    return car_num_list


racers_data = process_contestant_csv('contestants.csv')
racer_objects = create_racer_objects(racers_data)


# sorted takes an iterable and returns a list
def return_sorted_list(sort_number: int) -> list:
    return sorted(racer_objects, key=lambda racer: racer.return_properties()[sort_number], reverse=False)


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