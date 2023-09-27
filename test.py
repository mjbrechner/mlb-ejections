import pandas as pd

ejections = pd.read_csv("ejections.csv")

ejections['REASON'] = ejections['REASON'].str.lower()

ejections.EJECTEENAME[0]

ejectee_list = []
for i in ejections['EJECTEE'].unique():
    ejectee_list.append(i)
ejectee_list

ejectee_dic = {}
for x in range(len(ejections)):
    ejectee_dic[x] = ejections.EJECTEENAME[x]
ejectee_dic

ejections.EJECTEENAME.value_counts()

pmc = ('P' or 'M' or 'C')


player_ejections = ejections[ejections['JOB'] == 'P']
manager_ejections = ejections[ejections['JOB'] == 'M']
coach_ejections = ejections[ejections['JOB'] == 'C']
trainer_ejections = ejections[ejections['JOB'] == 'T']
other_ejections = ejections[ejections['JOB'] == 'N']
#other_ejections.EJECTEENAME.value_counts()

print(other_ejections)

