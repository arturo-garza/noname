import random


religions = {
    1: "Jewish",
    2: "Baha’i",
    3: "Muslim",
    4: "Buddhist",
    5: "Sikh",
    6: "Christian",
    7: "Other",
    8: "Hindu",
    9: "Jain",
    10: "Prefer not to say",
}


class Applicant:

     def __init__(self):
         self.gender = "M" if random.random() < 0.5 else "F"  # TODO add more
         self.yearofbirth = random.randint(1970, 2000)
         self.religion = None if random.random() < 0.5 else religions[random.randint(1,10)]

class HiringManager:

    def __init__(self):
        pass

    def process(self, applicant):
        return (random.random() < 0.333)

