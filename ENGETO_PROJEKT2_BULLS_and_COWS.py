"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Adam Šimůnek
email: adam.simunek@seznam.cz
discord: adamsim2
"""

#import
from random import randint
from time import time

#help
separator = "-"*54
title = "PROJEKT_1.py: první projekt do Engeto Online Python Akademie"

#users functions
def introduction():
    print(title, separator," ", "Hi there!", separator, "I've generated a random 4 digit number for you.", "Let's play a bulls and cows game.", separator, sep= "\n")

def generate_4_digit_list():
    digit_list = list()
    digit_list.append(randint(1,9))
    while len(digit_list) < 4:
        new_digit = randint(0, 9)
        if new_digit not in digit_list:
            digit_list.append(new_digit)
    return digit_list

def number_validation (players_number):
    if players_number is "":
        print("enter a 4 digit number", separator, sep="\n")
    elif (str(players_number)[0]) is "0":
        print("number '0' can not be selected as first digit", separator, sep="\n")
    elif players_number.isdigit() == False:
        print("enter only digit symbols", separator, sep="\n")     
    elif len(players_number) != 4:
        print("your number does not have 4 digits", separator, sep="\n")
    elif len(set(players_number)) != 4:
        print("your number contains two or more same digits", separator, sep="\n")
    else: 
        players_number_list = [int(digit) for digit in str(players_number)]
        invalid_players_number = False
        return (players_number_list)

def BC_one_round(generated_number_list, players_number_list):
    print(">>>", players_number)
    result = {"bulls": 0, "cows":0}
    players_number_list = [int(digit) for digit in str(players_number)]
    digit_index = 0
    for digit in players_number_list:
        if digit == generated_number_list[digit_index]:
            result["bulls"] = result["bulls"] + 1
        elif digit in generated_number_list:
            result["cows"] = result["cows"] + 1
        digit_index = digit_index + 1
    result_values = list(result.values())
    if 1 not in result_values:
        print(f'bulls: {result_values[0]}, cows: {result_values[1]}')
    elif result["bulls"] == 1 and result["cows"] != 1:
        print(f'bull: {result_values[0]}, cows: {result_values[1]}')
    elif result["bulls"] != 1 and result["cows"] == 1:
        print(f'bulls: {result_values[0]}, cow: {result_values[1]}')
    else:
        print(f'bull: {result_values[0]}, cow: {result_values[1]}')



if __name__ == "__main__":
    #introdution to program
    introduction()
    
    #generating of 4 digit number
    digit_list = generate_4_digit_list()

    #game process
    count_guesses = 0
    lap_times = list()
    failure = True
    while failure:
        #check validity of players number
        invalid_players_number = True
        while invalid_players_number:
            players_number = input("Enter a number:")
            players_number_list = number_validation(players_number)
            if players_number_list != None:
                invalid_players_number = False
        lap_times.append(time())

        #check players guess      
        if digit_list == players_number_list:
            print(">>>", players_number)
            failure = False
        else:
            #another game-lap
            BC_one_round(digit_list, players_number_list)
            print(separator)      
        
        #counting game-laps
        count_guesses = count_guesses + 1

    #total game-time
    total_time = lap_times[-1] - lap_times[0]
    print(separator)
    
    #results + time of single game-laps
    print(f"""
Correct, you've guessed the right number in {count_guesses} guesses! 
Final time: {round(total_time, 2)} s.
{separator}
LAP TIMES:
lap n. 0: stop-watch activated (first valid guess)""")  
    lap = 1
    lap_time_0 = float(lap_times[0])
    for lap_time in lap_times[1:]:
        lap_time_new = lap_time - lap_time_0
        print(f"lap n. {lap}: {round(lap_time_new, 2)} s.")
        lap = lap + 1
        lap_time_0 = lap_time


        



            
        

