def calc_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

def catgorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal Weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    elif 30.0 <= bmi:
        return "Obese"
    else:
        print("Input a valid weight and height")

def main():
    weight = float(input("What is you weight(kg): "))
    height = float(input("What is your height(Meters): "))
    bmi = calc_bmi(weight, height)
    category = catgorize_bmi(bmi)

    print(f"Your BMI is {bmi}")
    print(f"You are {category}")

main()