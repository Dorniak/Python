import numpy as np
activities = ["Singing in the shower", "Laughing", "Active sex", "Banging your head on a wall", "Brushing your teeth", "Pushing a shopping trolley", "Watching TV", "Smoking", "Dancing", "Hugging", "Whipping your head back and forth on a song", "Kissing", "Walking your dog", "Chewing gum", "Missing one night of sleep", "Texting"]
calories = [15, 30, 200, 150, 10, 100, 65, 10, 55, 70, 50, 3,  100, 11,  161,  40]
durations = [3,  10,  30,  60,  3,  30, 60,  3, 10, 60,  3, 1,   30, 60, 60*8,  60]
c_d = [calories[k]/durations[k] for k in range(len(calories))]
order = np.argsort(c_d)
for i in range(len(calories)):
    print(activities[order[i]]+" %d %d" % (calories[order[i]], durations[order[i]]))