import random


check1 = True
check2 = True
hold_decision = "nothing for now"

print("-----------WELCOME TO DICE SIMULATION-------------")

dice_no = input("How many dice would you like to throw(write '<number>-HOLD' to continue with same dies) : ")

if(len(dice_no) > 1):
    hold_decision = dice_no[2:]

if(hold_decision == "HOLD"):
    dice_no = int(dice_no[0])

    while check1 == True:

        for i in range(dice_no):

            print(f"dice {i+1} had : {random.randint(1,6)}")

        again = input("Do you want to roll again? (Y/N) : ")
        if again == 'Y':
            check1 = True
        else:
            break
else:
    dice_no = int(dice_no[0])

    

    while check1 == True:

            for i in range(dice_no):

                print(f"dice {i+1} had : {random.randint(1,6)}")

            again = input("Do you want to roll again? (Y/N) : ")

            if again == 'Y':

                dice_no = int(input("How many dies? : "))
                check1 = True

            else:
                break