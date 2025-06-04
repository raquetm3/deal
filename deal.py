# Deal or No Deal Game
# Rules - 26 cases, pick one case
#first round - pick 6 cases, then get a deal, take deal, or no deal (counter offer?)    (How is the deal calculated)
# second round - 5 cases, then deal
# third round - 4 cases, then deal
# fourth round - 3 cases then deal
# fifth round - 2 cases then deal
# sixth round - 1 case then deal
# next rounds - 1 case then deal until two cases are left
# when 2 are left, stick with yours, or pick the other one

#$12,275.30 + (0.748 * E) - (2714.74 * C) - (0.40 * M) + (.0000006986 * E^2) + (32.623 * C^2)  E = mean of all remaining values    C = number of cases remaining
# M = max value on the board

# Counter offer...can only do it once per game, if accepted game ends, if not keep playing
# Range for counteroffer...?
import time
import sys
import random
from pyfiglet import Figlet
import re

class Case:
    def __init__(self, number, value):
        self.number = number
        self.value = value

    def number(self):
        return self.number

    def value(self):
        return self.value

    def __str__(self):
        return f"Case number: {self.number}  Case Value: {self.value}"


Case_Values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
cases = []
for _ in range(1,27):
    case = Case(number=_, value="")
    value = random.choice(Case_Values)
    case.value = value
    cases.append(case)
    Case_Values.remove(value)



def main():
    # Start Game
    start()

    # Choose Case
    cases_remaining = [case.number for case in cases]
    choice = choosecase(cases_remaining)
    your_case = cases[choice - 1]

    cases_remaining = [case.number for case in cases if case != your_case ]
    values_remaining = [case.value for case in sorted(cases, key=lambda x: x.value)]

    # guessing cases, then deal
    countered = False
    for x in range(1,10):
        cases_remaining, values_remaining = gameround(x, cases_remaining, values_remaining, cases)
        counter = deal(x, your_case, cases_remaining, values_remaining, countered)
        if counter == True:
            countered = True

    finalchoice(your_case, cases_remaining, cases)





def start():
    f = Figlet(font='rectangles')
    print(f.renderText('Deal or No Deal!'))
    while True:
        ready = input("\nReady to start? (y/n) ").lower().strip()
        if ready == "y":
            break
        if ready == "n":
            print("Take your time.")
        else:
            print("Input must be 'y' or 'n'!")


def choosecase(cases_remaining):   #Returns case number
    # returns case choice as an int
    while True:
        choice = input("\nWhich case would you like to pick? (1-26) ").strip()
        pattern = r"^[1-9]$|^1[0-9]$|^2[0-6]$"
        try:
            match = re.search(string=choice, pattern=pattern)
            if match:
                choice = int(choice)
                if choice in cases_remaining:
                    return choice
                else:
                    print("You must choose a case that's available!")
            else:
                raise ValueError
        except ValueError:
            print("You must choose a number between 1 and 26!")


def gameround(n, cases_remaining, values_remaining, cases):
    x = n
    if n > 6:
        n = 6
    print(f"\nWe are ready to start Round {x}! You will pick {7-n} case(s)!")
    wait(1)
    for x in range(7 - n):
        print(f"\nCases Remaining: {cases_remaining}")
        print(f"\nValues Remaining: {values_remaining}")
        wait(1)
        print(f"\nYou have {7-n-x} case(s) left to pick this round.")
        wait(1)
        guess = choosecase(cases_remaining)
        for case in cases:
            if guess == case.number:
                print(f"You picked Case {case.number}")
                wait(1)
                print(f"That case contained the value ${case.value}!")
                wait(1)
                cases_remaining.remove(case.number)
                values_remaining.remove(case.value)
                break

    return cases_remaining, values_remaining

def deal(n, your_case, cases_remaining, values_remaining, countered):
    if n < 9:
        print(f"Values Remaining: {values_remaining}")
        wait(1)
        print("The banker is calling in to offer you a deal...")
        wait(1)
        # average * (round # /9)
        sum = 0
        for value in values_remaining:
            sum += value

        deal = round(((sum / len(cases_remaining)) * (n / 9)), 2)
        while True:
            choice = input(f"\nThe banker is offering you ${deal:.2f}. Do you accept? (y/n/counter)) ").strip().lower()
            if choice == "y":
                print(f"You have made a deal for ${deal:.2f}!")
                wait(1)
                print(f"Your case contained the value ${your_case.value}")
                wait(1)
                if your_case.value > deal:
                    sys.exit("Too bad, you made a bad deal!")
                else:
                    sys.exit("Nice job! You made a good deal!")
            elif choice == "n":
                print("No Deal! You will move on to the next round!")
                wait(1)
                return False
            elif choice == "counter":
                if countered == False:
                    counteroffer(deal, your_case)
                    return True
                else:
                    print("You can only counteroffer once per game!")
            else:
                print("Input must be 'y' or 'n' or 'counter'!")
    else:
        print(f"Values Remaining: {values_remaining}")
        pass

def finalchoice(your_case, cases_remaining, cases):
    print(f"\nThere are only two cases remaining. Your case, Case {your_case.number}, and Case {cases_remaining[0]}.")
    wait(1)
    while True:
        choice = input("Do you want to stick with your case, or switch cases? (stick/switch) ").strip().lower()
        if choice == "stick":
            print(f"You decide to stick with Case {your_case.number}")
            wait(1)
            print(f"Your case contains ${your_case.value}!")
            wait(1)
            for case in cases:
                if cases_remaining[0] == case.number:
                    print(f"Case {case.number} holds the value ${case.value}!")
                    wait(1)
                    if your_case.value > case.value:
                        sys.exit("Nice job! You made the right call!")
                    else:
                        sys.exit("Too bad, you should have switched cases!")

        elif choice == "switch":
            print(f"You decide to swap Case {your_case.number} for Case {cases_remaining[0]}")
            wait(1)
            for case in cases:
                if cases_remaining[0] == case.number:
                    print(f"Case {case.number} holds the value ${case.value}!")
                    wait(1)
                    print(f"Case {your_case.number} holds the value ${your_case.value}!")
                    wait(1)
                    if case.value > your_case.value:
                        sys.exit("Nice job! You made the right call!")
                    else:
                        sys.exit("Too bad, you should not have switched cases!")

        else:
            print("You must input 'stick' or 'switch'!")


def counteroffer(deal, your_case):
    while True:
        try:
            offer = float(input("What is your counteroffer? (Enter a dollar amount with no commas) ").strip())
        except ValueError:
            print("You must enter a number!")
        else:
            pattern = r"^[1-9]\d*(\.\d{1,2})?$"
            match = re.search(string=str(offer), pattern=pattern)
            if match:
                if offer <= float(f"{(deal*1.2):.2f}"):
                    print(f"The banker accepts your counter offer of ${offer:.2f}!")
                    wait(1)
                    print(f"Your case contained the value ${your_case.value}")
                    wait(1)
                    if your_case.value > offer:
                        sys.exit("Too bad, you made a bad deal!")
                    else:
                        sys.exit("Nice job! You made a good deal!")
                else:
                    print("The banker refuses your counter offer")
                    wait(1)
                    break
            else:
                print("The number you entered is invalid")


def wait(n):
    time.sleep(n)

if __name__ == "__main__":
    main()
