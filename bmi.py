print('\nBMI weight guide \n')
weight = float(input('Please enter your weight(kg): '))
height = float(input('Please enter your height(meter): '))
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5 :
    print('Your BMI number is ', bmi, 'Underweight.')
elif bmi >= 25 and bmi < 29.9 :
    print('Your BMI number is ', bmi, 'Overweight')  
elif bmi >= 30 :
    print('Your BMI number is ', bmi, 'Obese')    
else:
    print('Your BMI number is ', bmi, 'Healthy')
