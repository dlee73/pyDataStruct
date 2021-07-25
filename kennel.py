class Kennel:

    def __init__(self, kennel_name="", spaces=None) -> object:
        if spaces is None:
            spaces = []
        self.kennel_name = kennel_name
        self.spaces = spaces

    def birth(self):
        self.spaces.append(Dog(name="baby", age=0, id_num=self.create_id(), kennel=self.kennel_name))
        print(self)

    def __str__(self):
        l = ""
        for dog in self.spaces:
            l = l + "%s\n" % dog.__str__()
        return l


    def id(self, idnumber):
        return self.spaces[idnumber-1]

    def name(self, dogname):
        for x in self.spaces:
            if x.name == dogname:
                return self.id(x.id_num)

    def create_id(self):
        if len(self.spaces) == 0:
            return 1
        else:
            return self.spaces[len(self.spaces) - 1].id_num + 1

    def intake_new_dog(self, name, age):
        self.spaces.append(Dog(name=name, age=age, kennel=self.kennel_name, id_num=self.create_id()))
        print(self)

    def intake_existing_dog(self, dog):
        dog.id_num = self.create_id()
        dog.kennel = self.kennel_name
        self.spaces.append(dog)
        print(self)

    def remove_dog(self, dog):
        dog.kennel = None
        self.spaces.remove(self.name(dog))
        print(self)


class Dog:
    def __init__(self, name, age, id_num=0, kennel=None, owner=None, stray=False):
        self.name = name
        self.age = age
        self.id_num = id_num
        self.kennel = kennel
        self.owner = owner
        self.stray = stray

    def __str__(self):
        return "Name: {}, Age: {}, Kennel: {}, ID: {}".format(self.name, self.age, self.kennel, self.id_num)

    def change_name(self, newname):
        self.name = newname

    def change_age(self, newage):
        self.age = newage

    def set_kennel(self, kennel):
        self.kennel = kennel
        self.kennel.intake_existing_dog(self)



mcgrady = Kennel(kennel_name="Mcgrady")
steve = Dog(name="Steve", age=9)
mcgrady.intake_existing_dog(steve)
lila = Dog(name="Lila", age=9)
print(steve)
print(mcgrady)




