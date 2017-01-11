import numpy
lines = ["life","game","style","job","boss","mother"]
advervb = ["Firstly,", "Secondly,", "Thirdly,", "Fourthly,"]

for i in range(1,5):
    r = numpy.random.randint(0,5)
    print(advervb[i-1] +" I love my " + lines[r])
