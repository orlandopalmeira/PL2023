with open("part1.txt","w") as left:
    with open("processos.txt") as ds:
        for line in ds:
            line = line.split("::")[:5]
            left.write('::'.join(line) + '\n')

with open("part2.txt","w") as right:
    with open("processos.txt") as ds:
        for line in ds:
            line = line.split("::")[5:]
            right.write('::'.join(line))