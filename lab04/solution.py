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

def average(scores: list[float]) -> float:
    if len(scores) != 0:
        return round(sum(scores) / len(scores),2)
    else:
        return 0

def ranking(names, scores):
    index_list = list(range(len(names)))
    index_list.sort(key=lambda i: scores[i],reverse=True)
    return [names[i] for i in index_list]


def above_average(names, scores):
    result = list()
    average_num = average(scores)
    for i in range(len(names)):
        if scores[i] > average_num:
            result.append(names[i])

    return result

if __name__ == "__main__":
    names =  ["Аня", "Боря", "Вика"]
    scores = [7.0,   9.0,    9.0]
    print(winner(names,scores))
    print(average(scores))
    print(ranking(names,scores))
    print(above_average(names,scores))
