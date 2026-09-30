porog = float(input())
n = int(input())
errors, excess, max_num, sum_num = 0, 0, -10000000000, 0

for _ in range(n):
    s = input()

    if s == 'error':
        errors += 1
    else:
        temperature = float(s)

        sum_num += temperature
        max_num = max(max_num, temperature)

        if temperature > porog:
            excess += 1

print(n, errors, excess, f'{max_num:.1f}', f'{(sum_num / (n - errors)):.1f}', sep='\n')