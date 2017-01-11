#"life": 0.1, "game": 0.5, "style": 0.25, "job": 0.2, "boss": 0.05, "mother": 0.8
import numpy as np
advervb = ["Firstly,", "Secondly,", "Thirdly,", "Fourthly,"]
lines = ["life","game","style","job","boss","mother"]
prob = np.array([0.1, 0.5, 0.25, 0.2, 0.05])
prob /= np.sum(prob[0:2])

for i in range(4):
    print(advervb[i] + " I love my " + lines[np.random.randint(0, 5)])


