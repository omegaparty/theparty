import csv
from csv import DictReader

age = []
sex = []
bmi = []
children =[]
smoker = []
region = []
charges = []


with open('insurance.csv', newline= '') as insurance_data:
    data = DictReader(insurance_data, delimiter = ',')
    for row in data:
        age.append(int(row['age']))
        sex.append(row['sex'])
        bmi.append(float(row['bmi']))
        children.append(int(row['children']))
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(float(row['charges']))
    
def average_age():
    print('The average age is {}'.format(round(sum(age)/len(age))))

def sex_count():
    male = 0
    female = 0
    for gender in sex:
        if 'male' == gender:
            male+=1
        else:
            female+=1
    print('Total Males {}'.format(male))
    print('Total Females {}'.format(female))

average_age()
sex_count()


