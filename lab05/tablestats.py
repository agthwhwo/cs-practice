def read_rows():
    result = {}
    with open("events.csv", encoding="utf-8") as table:
        for name,line,num in (table.readline).split(','):
            result[line] = num
            
    return result


print(read_rows())


        
        
        
    
    
def count_types(rows):
    pass

def total_minutes(rows, kind):
    pass

def to_csv(counts):
    pass
    