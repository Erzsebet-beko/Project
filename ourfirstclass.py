class Human():
    humans = 0

    def __init__(self, name, tall, age, sex):
        Human.humans+=1
        self.name = name
        self.tall = tall
        self.age = age
        self.sex = sex

    def get_info(self):
        print("Name: " + self.name)
        print("Tall: " + str(self.tall))
        print("Age: " + str(self.age))
        print("Sex: " + self.sex)

    def increase_age(self):
        if self.sex == "female":
            print("Forever young ;) - happy birtday")
        else:
            self.age+=1
            print("Age is increased - happy birtday " + str(self.age))

    def grow(self, cm):
        self.tall+= cm
        print("Grat you were grow " + str(self.tall))

    def get_existing_humans(self):
        print("Existing humans: " + str(Human.humans))


human1 = Human("Daniel", 186, 26, "male")
human1.get_info()
human1.increase_age()
human1.get_info()

print("======================================")

human2 = Human("Erzsebet", 170, 25, "female")
human2.get_info()
human2.increase_age()
human2.get_info()

print("======================================")

human1.grow(190)
human1.get_info()

print("======================================")

print(Human.humans)