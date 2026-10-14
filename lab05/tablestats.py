def read_rows(lines):
    rows = []
    header = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        fields = [value.strip() for value in line.split(",")]

        if head is None:
            head = fields
            continue

        if len(fields) != len(head):
            continue

        row = {}

        for i in range(len(head)):
            row[head[i]] = fields[i]

        rows.append(row)

    return rows

    
def count_types(rows):
    counts = {}

    for row in rows:
        kind = row["тип"]

        if kind not in counts:
            counts[kind] = 0

        counts[kind] += 1

    return counts

def total_minutes(rows,kind):
    total = 0.0

    for row in rows:
        if row["тип"] != kind:
            continue

        value = row["минуты"].replace(",", ".")

        try:
            total += float(value)
        except ValueError:
            continue

    return round(total, 1)


def to_csv(counts):
    pass
    