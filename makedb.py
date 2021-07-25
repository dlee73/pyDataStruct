from kennel import Dog, Kennel
import shelve

villa = Kennel(kennel_name="Villa")
bob = Dog(name="Bob", age=4)

villa.intake_existing_dog(bob)
villa.intake_new_dog(name="Henriette", age=7)
villa.intake_new_dog(name="Harvey", age=8)
villa.intake_new_dog(name="Murray", age=7)

villa.occupants()

with shelve.open('dogdb') as db:
    for dog in villa.spaces:
        db[dog.name] = dog

print(open('dogdb.dir').read())


