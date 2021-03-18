from datetime import datetime
from dataclasses import dataclass

@dataclass
class Pet:
    def __init__(self,species,breed,name,color,gender,owner,address,birthdate):
        try:
            self.species = species
        except:
            print("invalid data type")
        try:
            self.breed = breed
        except:
            print("invalid data type")
        try:
            self.name = name
        except:
            print("invalid data type")
        try:
            self.color = color
        except:
            print("invalid data type")
        try:
            self.gender = gender
        except:
            print("invalid data type")
        try:
            self.owner = owner
        except:
            print("invalid data type")
        try:
            self.address = address
        except:
            print("invalid data type")
        try:
            self.birthdate = datetime.strptime(birthdate,"%b %d %Y")
        except:
            print("invalid data type")

    def getAge(self,age):
        self.age = age

    def __str__(self):
        print(self.name + ",",str(self.age) + ",",self.species + ",",self.color)

@dataclass
class Dog(Pet):
    def __init__(self,breed,name,color,gender):
        super(Dog,self).__init__(species = "None",breed = breed,name= name,color = color,
                                 gender = gender,owner = "None", address = "None", birthdate = "None")

class Puppy(Dog):
    def getAge(self,age):
        ageMonths = age*12
        self.age = ageMonths
        print("age: " + str(self.age) + " months")

    def play(self):
        string = str(('(___()', "'", "`", ";", "\"", "n",   "/",",    /", "`", "\"", "n      \\\\\"", "--\\\\"))
        return string

cat = Pet("cat","maine coon","Max","orange","male","Owner","Address","Jun 1 2005")
cat.getAge(5)
cat.__str__()

dog_1 = Dog("husky","Mars","black","male")
dog_1.getAge(5)
dog_1.__str__()

puppy_1 = Puppy("boxer","Mars","brown","male")
puppy_1.getAge(1)
puppy_1.__str__()