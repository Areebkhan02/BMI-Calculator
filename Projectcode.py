import stdiomask
import random

user_age = eval(input("Enter age: "))
user_height = eval(input("Enter height: "))
user_weight = eval(input("Enter weight: "))
extra_medical = str(input(
    "Enter any medical problem/maternity you facing right now (Enter No or NO if not): ")).lower()

count = 0


def BMI_calculator(age=0, height=0, weight=0, extra_medical="no"):
    height = height * 12
    weight = weight * 2.205
    BMI = round(703 * weight / (height**2), 2)
    weight = weight / 2.205
    if age > 60 or age < 10:
        return "Sorry ! our program is not for your specified age !"
    if extra_medical.lower() != "no":
        return "Sorry ! our program is not for you !"

    if BMI < 18.5:
        print("The person BMI ({}) is below the range ! Subscribe to our program to get better guidance. ".format(BMI))
        return Callback("Underweight", age, weight)
    elif BMI > 18.5 and BMI < 24.9:
        return Callback("Normal", age, weight)
    elif BMI > 25:
        print("The person BMI ({}) is above the range ! Subscribe to our program to get better guidance. ".format(BMI))
        return Callback("Overweight", age, weight)
    return BMI


def Callback(condition, age, weight):
    global user_height
    global count
    if count % 4 == 0 or count == 0:
        credit_card = eval(input("Enter credit card number (11 digit): "))
        credit_card = str(credit_card)
        while len(credit_card) != 11:
            print("Invalid credit card !")
            credit_card = eval(input("Enter credit card number (11 digit): "))
            credit_card = str(credit_card)
        credit_pin = stdiomask.getpass(
            prompt='Enter credit card pin (4 digit): ')
        credit_pin = str(credit_pin)
        while len(credit_pin) != 4:
            print("Invalid credit card pin !")
            credit_pin = stdiomask.getpass(
                prompt='Enter credit card pin (4 digit): ')
            credit_pin = str(credit_pin)
        print("30 $ have been deducted from your account {0} !".format(
            "*" * 7 + str(credit_card[7:])))

    count += 1
    if condition == "Overweight":
        if age <= 18:
            print("-------------------- Monthly Schedule --------------------")
            print("month {}".format(count))
            print("Breakfast: 2 apples and 1 glass of milk ")
            print("Lunch: Porridge ")
            print("Dinner: Grilled Steak ")
            print("Do 15 pushups everyday !")

            # LIKH LE YAHAN PE

            steps = str(int(random.uniform(5000, 6000)))
            print("Do walk {}00 steps weekly !".format(steps[:2]))
            loss_weight = eval(input("How much weight (kg) you lost: "))
            new_weight = weight - loss_weight
            print("You lost {} kg of weight. Now your weight is {} kg".format(loss_weight, new_weight))
            BMI_calculator(age, user_height, new_weight)

        elif age > 18 and age <= 45:
            print("-------------------- monthly Schedule --------------------")
            print("month {}".format(count))
            print("Breakfast: 3 pears and 1 glass of mangomilkshake ")
            print("Lunch: grilled fish ")
            print("Dinner: baked potatoes ")
            print("Do 25 pushups everyday !")

            steps = str(int(random.uniform(5000, 6000)))
            print("Do walk {}00 steps weekly !".format(steps[:2]))
            loss_weight = eval(input("How much weight (kg) you lost: "))
            new_weight = weight - loss_weight
            print("You lost {} kg of weight. Now your weight is {} kg".format(loss_weight, new_weight))
            BMI_calculator(age, user_height, new_weight)

        elif age > 45 and age <= 60:

            print("-------------------- monthly Schedule --------------------")
            print("month {}".format(count))
            print("Breakfast: 1 fruitcake ")
            print("Lunch: chucken currry ")
            print("Dinner: baked buns ")
            print("Do 5 squats everyday !")

            steps = str(int(random.uniform(5000, 6000)))
            print("Do walk {}00 steps weekly !".format(steps[:2]))
            loss_weight = eval(input("How much weight (kg) you lost: "))
            new_weight = weight - loss_weight
            print("You lost {} kg of weight. Now your weight is {} kg".format(loss_weight, new_weight))
            BMI_calculator(age, user_height, new_weight)

    elif condition == "Underweight":
        if age <= 18:
            print("-------------------- monthly Schedule --------------------")
            print("month {}".format(count))
            print("Breakfast: 5 pears and 2 glass of mangomilkshake ")
            print("Lunch: broasted chicken ")
            print("Dinner: baked potatoes with mayo sauce")
            print("Do 25 squats everyday !")

            steps = str(int(random.uniform(5000, 6000)))
            print("Do walk {}00 steps weekly !".format(steps[:2]))
            gain_weight = eval(input("How much weight (kg) you gain: "))
            new_weight = weight + gain_weight
            print("You gain {} kg of weight. Now your weight is {} kg".format(gain_weight, new_weight))
            BMI_calculator(age, user_height, new_weight)

        elif age > 18 and age <= 45:
            print("-------------------- monthly Schedule --------------------")
            print("month {}".format(count))
            print("Breakfast: 3 cups of sogi with sugar ")
            print("Lunch: Biryani ")
            print("Dinner: baked troaters with mayo sauce")
            print("Do 35 squats everyday !")

            steps = str(int(random.uniform(5000, 6000)))
            print("Do walk {}00 steps weekly !".format(steps[:2]))
            gain_weight = eval(input("How much weight (kg) you gain: "))
            new_weight = weight + gain_weight
            print("You gain {} kg of weight. Now your weight is {} kg".format(gain_weight, new_weight))
            BMI_calculator(age, user_height, new_weight)

        elif age > 45 and age < 60:
            print("-------------------- monthly Schedule --------------------")
            print("month {}".format(count))
            print("Breakfast: 1 cups of sogi with sugar ")
            print("Lunch: Whole grain ")
            print("Dinner: Pata with red sauce")
            print("Do 7 squats everyday !")

            steps = str(int(random.uniform(5000, 6000)))
            print("Do walk {}00 steps weekly !".format(steps[:2]))
            gain_weight = eval(input("How much weight (kg) you gain: "))
            new_weight = weight + gain_weight
            print("You gain {} kg of weight. Now your weight is {} kg".format(gain_weight, new_weight))
            BMI_calculator(age, user_height, new_weight)

    return "-------------------------------------------------------\nYour BMI is in the satisfied range !! Enjoy !\n-------------------------------------------------------"


print(BMI_calculator(user_age, user_height, user_weight, extra_medical))
# https://rawgit.com/mmmovania/Physijs_Tutorials/master/MultipleBoxes.html
