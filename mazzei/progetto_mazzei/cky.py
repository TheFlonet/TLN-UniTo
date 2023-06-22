def cky(words: list[str], grammar: list[tuple]) -> bool:
    sentence = ['']
    sentence.extend(words)
    table = [[set() for _ in range(len(sentence))] for _ in range(len(sentence))]
    back = {}

    for j in range(1, len(sentence)):
        prods = find_terminal_productions(sentence[j], grammar)
        for elem in prods:
            table[j - 1][j].add(elem[0])
            if (j, j, elem[0]) in back:
                back[(j, j, elem[0])].append(elem[1][0])
            else:
                back[(j, j, elem[0])] = elem[1][0]
        for i in range(j - 2, -1, -1):
            for k in range(i + 1, j):
                prods = find_non_terminal_productions(table[i][k], table[k][j], grammar)
                for prod in prods:
                    table[i][j].add(prod[0])
                    if (i + 1, j, prod[0]) in back:
                        back[(i + 1, j, prod[0])].extend([
                            (prod[1][0], (i + 1, k, prod[1][0])),
                            (prod[1][1], (k + 1, j, prod[1][1]))
                        ])
                    else:
                        back[(i + 1, j, prod[0])] = [
                            (prod[1][0], (i + 1, k, prod[1][0])),
                            (prod[1][1], (k + 1, j, prod[1][1]))
                        ]

    if 'S' in table[0][len(words)]:
        print_productions(back, (1, len(words), 'S'))
    return 'S' in table[0][len(words)]


def find_non_terminal_productions(bs: set, cs: set, grammar: list[tuple]) -> list[tuple]:
    heads = list()
    for rule in grammar:
        for b in bs:
            for c in cs:
                if len(rule[1]) == 2 and rule[1][0] in b and rule[1][1] in c:
                    heads.append(rule)
    return heads


def find_terminal_productions(word: str, grammar: list[tuple]) -> list[tuple]:
    heads = list()
    for rule in grammar:
        if len(rule[1]) == 1 and rule[1][0] == word:
            heads.append(rule)
    return heads


def print_productions(back: dict[tuple], cell: tuple, indent: int = 0):
    print(' ' * indent + cell[2], end=' -> ')
    if type(back[cell]) is str:
        print(back[cell])
        return
    for prod in back[cell]:
        print(prod[0], end=' ')
    print()
    for prod in back[cell]:
        print_productions(back, prod[1], indent + 4)
