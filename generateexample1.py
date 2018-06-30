import csv
import models
import random

class BadHiringManager(models.HiringManager):

    def process(self, applicant):
        if applicant.gender == "F":
            return (random.random() < 0.10)
        else:
            return (random.random() < 0.333)


applicants = []

for i in range(1,1000):
    applicants.append(models.Applicant())


hiring_managers = {
    1: models.HiringManager(),
    2: models.HiringManager(),
    3: models.HiringManager(),
    4: models.HiringManager(),
    5: BadHiringManager(),
}


with open('example1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        "Gender",
        "Hiring Manager ID",
        "Decision"
    ])
    for applicant in applicants:

        hiring_manager_id = random.randint(1, 5)


        writer.writerow([
            applicant.gender,
            hiring_manager_id,
            "True" if hiring_managers[hiring_manager_id].process(applicant) else "False"
        ])


