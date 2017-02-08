# -*- coding: utf-8 -*-

print("Welcome to the Lucky Number!")

lucky_number = raw_input("Pick a number between 0 and 100,000: ")

while lucky_number == "18765":
    print("Congratulations! You have won an unlimited supply of cocoa!")
    break

else:
    print("Two more guesses...")
    lucky_number = raw_input("Pick a number between 0 and 100,000: ")

    while lucky_number == "18765":
        print("Congratulations! You have won an unlimited supply of cocoa!")
        break

    else:
        print("One more guess... ")
        lucky_number = raw_input("Pick a number between 0 and 100,000: ")

        while lucky_number == "18765":
            print("Congratulations! You have won an unlimited supply of cocoa!")
            break

        else:
            print("Sorry, wrong number... Better luck next time!")