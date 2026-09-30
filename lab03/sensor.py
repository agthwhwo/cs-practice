threshold = float(input())
n = int(input())
errors = 0
excess = 0
max_num = -10**10
sum_num = 0

for i in range(n):
    s = input()

    if s == 'error':
        errors += 1
    else:
        temperature = float(s)

        sum_num += temperature
        max_num = max(max_num, temperature)

        if temperature > threshold:
            excess += 1

print(n, errors, excess, f'{max_num:.1f}', f'{(sum_num / (n - errors)):.1f}', sep='\n')