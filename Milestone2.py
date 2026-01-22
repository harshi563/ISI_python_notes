# 16 Jan ; Task 1
'''If units<=100 
Then bill= units*2 
If units <= 300
Then bill= units*3
Otherwise 
Then bill= units*5'''
unit=float(input("Enter the units: "))

if(unit<=100):
    unit=unit*2
elif(unit<=300):
    unit=unit*3
else:
    unit=unit*5
print(f"The Bill is = {unit}")


