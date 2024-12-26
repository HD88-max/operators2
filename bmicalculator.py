weight = float(input("Enter your weight "))
height = float(input("Enter your height in metres "))
BMI = weight/ (height)**2
print("Your BMI is {0}".format(BMI))
if BMI < 18.5:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 34.5:
    print("You are overweight")
else:
    print("You are obese")

