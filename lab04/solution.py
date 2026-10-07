names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names, scores):
    num = 0
    index = 0
    for i in range(len(scores)):
        if scores[i] > num:
            num = scores[i]
            index = i

    return names[index]

print(winner(names,scores))
