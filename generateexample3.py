import csv
import models
import random

class BadHiringManager(models.HiringManager):

    def process(self, applicant):
        age = 2018 - applicant.yearofbirth
        if applicant.gender == "F":
            if age < 25:
                return (random.random() < 0.50)
            elif age < 35:
                return (random.random() < 0.30)
            else:
                return (random.random() < 0.20)
        else:
            if age < 25:
                return (random.random() < 0.20)
            elif age < 35:
                return (random.random() < 0.30)
            else:
                return (random.random() < 0.50)


applicants = []

for i in range(1,10000):
    applicants.append(models.Applicant())


hiring_managers = {
    1: models.HiringManager(),
    2: BadHiringManager(),
    3: models.HiringManager(),
    4: models.HiringManager(),
    5: models.HiringManager(),
}


with open('example3.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Gender",
        "YearOfBirth",
        "Hiring Manager ID",
        "Decision"
    ])
    for applicant in applicants:

        hiring_manager_id = random.randint(1, 5)

        writer.writerow([
            applicant.gender,
            applicant.yearofbirth,
            hiring_manager_id,
            "True" if hiring_managers[hiring_manager_id].process(applicant) else "False"
        ])


