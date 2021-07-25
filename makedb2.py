from kennel import *
import shelve

with shelve.open("dogdb") as db:
    db["Steve"] = Dog("Steve", 5)
