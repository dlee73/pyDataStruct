import shelve
from kennel import *

db = shelve.open("dogdb")

for key in db:
    print(db["%s" % key])

db.close()

