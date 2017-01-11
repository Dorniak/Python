import numpy
lines = ["life","game","style","job","boss","mother"]
advervb = ["Firstly,", "Secondly,", "Thirdly,", "Fourthly,"]

for i in range(4):
    r = numpy.random.randint(0,5)
    print(advervb[i] +" I love my " + lines[r])
