print('\n\nBMI weight guide \n')
weight = float(input('Please enter your weight(kg): '))
height = float(input('Please enter your height(meter): '))
bmi = weight / (height * height)
if bmi < 18.5 :
    print('Underweight.')
elif bmi >= 25 and bmi < 29.9 :
    print('Overweight')  
elif bmi >= 30 :
    print('Overweight')    
else:
    print('Healthy')
print(bmi)