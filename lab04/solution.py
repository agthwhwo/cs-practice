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
    
