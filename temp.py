import shelve
from kennel import*

shelf = open("testshelve.dir")

for x in shelf:
    x.birth()

shelf.close()