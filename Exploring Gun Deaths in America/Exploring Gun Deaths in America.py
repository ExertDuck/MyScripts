import csv

data = list(csv.reader(open("guns.csv", 'r')))

header_row = []
header_row.append(data[0])  #create header row
data = data[1:len(data)]    #remove header row from data

# create a dictionary with a count of numbers of deaths per year
years = [y[1] for y in data]    #list comp for years column
years_counts = {}

for e in years:
    if e in years_counts:
        years_counts[e] += 1
    else:
        years_counts[e] = 1

# no noticeable difference in deaths fro 2012 to 2014.
# let's look at it month on month
import datetime

dates = [datetime.datetime(year=int(e[1]),month=int(e[2]),day=1) for e in data]
date_counts = {}

for r in dates:
    if r in date_counts:
        date_counts[r] += 1
    else:
        date_counts[r] = 1
        
# How do gun deaths vary by gender and race?
sex_counts = {}

for r in data:
    if r[5] in sex_counts:
        sex_counts[r[5]] += 1
    else:
        sex_counts[r[5]] = 1

# Victims of gun violence are predominantly male
        
race_counts = {}

for r in data:
    if r[7] in race_counts:
        race_counts[r[7]] += 1
    else:
        race_counts[r[7]] = 1

# Whites are the largest race group How does racial distribution 
# correlate with normal demographics?

# Bringing in census data
census = [['Id', 'Year', 'Id', 'Sex', 'Id', 'Hispanic Origin',
           'Id', 'Id2', 'Geography', 'Total', 'Race Alone - White',
           'Race Alone - Hispanic', 'Race Alone - Black or African American',
           'Race Alone - American Indian and Alaska Native', 
           'Race Alone - Asian', 'Race Alone - Native Hawaiian and Other Pacific Islander',
           'Two or More Races'],['cen42010', 'April 1, 2010 Census', 'totsex',
            'Both Sexes', 'tothisp', 'Total', '0100000US', '', 'United States',
            '308745538', '197318956', '44618105', '40250635', '3739506', 
            '15159516', '674625', '6984195']]

mapping = {}
mapping["White"] = int(census[1][10])
mapping["Hispanic"] = int(census[1][11])
mapping["Black"] = int(census[1][12])
mapping["Native American/Native Alaskan"] = int(census[1][13])
mapping["Asian/Pacific Islander"] = int(census[1][14]) + int(census[1][15])

race_per_hundredk = {}
for e in race_counts:
    race_per_hundredk[e] = (race_counts[e]/mapping[e])*100000

races = [i[7] for i in data]
intents = [i[3] for i in data]
homicide_race_counts = {}
for i, race in enumerate(races):
    if race in homicide_race_counts and intents[i] == "Homicide":
            homicide_race_counts[race] += 1
    elif race not in homicide_race_counts and intents[i] == "Homicide":
        homicide_race_counts[race] = 1
        
for e in homicide_race_counts:
    homicide_race_counts[e] = (homicide_race_counts[e]/mapping[e])*100000
    
# Blacks have the highest homicide rate, then hispanics