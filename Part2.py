import numpy
lines = ["life","game","style","job","boss","mother"]
words = [lines[numpy.random.randint(0,5)] for i in range(4)]
for i in range(4):
    print("I love my "+ words[i])



# for i in range(3):
#     r = numpy.random.randint(0,5)
#     print("I love my " + lines[r])
