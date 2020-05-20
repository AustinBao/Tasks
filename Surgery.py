import random
import sys


class Surgeon:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    def surgery(self, recipeint, organ_donor):
        death = random.randint(0, 9)
        if death == 1:
            print("Uh oh " + recipeint.first + " " + recipeint.last + " your body rejected the new organ")
        else:
            new_recipient = recipeint.numberoforgans + 1
            new_organdonor = organ_donor.numberoforgans - 1

            print("everything went smoothly")
            print(recipeint.first + ' ' + recipeint.last + " you now have " + str(new_recipient) + ' ' + recipeint.type)
            print(organ_donor.first + ' ' + organ_donor.last + " you now have " + str(new_organdonor) + ' ' + organ_donor.type)


class Patient:
    def __init__(self, first, last, numberoforgans, type):
        self.first = first
        self.last = last
        self.numberoforgans = numberoforgans
        self.type = type


# never found a need for kidney class
class Kidney:
    pass


patient_a = Patient('Adam', 'Cole', 0, 'Kidney')
patient_b = Patient('Mary', 'Jones', 2, 'Kidney')

patient_c = Patient('Mike', 'Man', 0, 'Heart')
patient_d = Patient('Andy', 'Man', 1, 'Heart')

surgeon_1 = Surgeon('Scott', 'James')
surgeon_1.surgery(patient_a, patient_b)
surgeon_1.surgery(patient_c, patient_d)
