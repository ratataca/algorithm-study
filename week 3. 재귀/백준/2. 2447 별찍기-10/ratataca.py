def star(n, unit):
    out = []
    if n == 3:
        return unit
    else:
        for i in unit:
            out.append(i*3)
        for i in unit:
            out.append(i + " " * len(unit) + i)
        for i in unit:
            out.append(i*3)
        return star(n//3, out)

n = int(input())
unit = ['***', '* *', "***"]
result = star(n, unit)

for i in result:
    print(i)