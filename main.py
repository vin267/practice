class Dog:
    species = 'abcd'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return f'my name is {self.name}'

    def speak(self, sound):
        return f'{self.name} says {sound}'

buddy=Dog('buddy',9)

print(buddy.description())
print(buddy.speak('bow wow'))
print(buddy.species)

