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

def smoker_cost():
    smoking_cost = []
    non_smoking_cost = []
    index = 0
    total_smokers = []
    total_non_smokers = []
    

    for status in smoker:
        if 'yes' in status:
            smoking_cost += charges[index]
            total_smokers += 1
            index += 1
        else:
            non_smoking_cost += charges[index]
            total_non_smokers += 1
            index += 1
    avg_cost_smoker = smoking_cost/total_smokers
    avg_cost_non = non_smoking_cost/total_non_smokers

    print('The average cost for a smoker = {}'.format(round(avg_cost_smoker),2))
    print('The average cost for a non smoker = {}'.format(round(avg_cost_non),2))




average_age()
sex_count()
smoker_cost()
