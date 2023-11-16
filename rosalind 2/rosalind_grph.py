


def rosalind_grph(fasta):
    with open(fasta) as f:
        lines = f.readlines()
    id = None
    for i in lines + ['>']:
        if i[0] == '>':
            if id != None:
                yield (id, ''.join(strings))
            id = i.strip()[1:]
            strings = []
        else:
            strings.append(i.strip())
    return strings

def result_grph():
    data = [(name, s[:3], s[-3:]) for (name, s) in rosalind_grph('rosalind_grph.txt')]
    for (namef, preff, sufff) in data:
        for (namet, preft, sufft) in data:
            if namef != namet and sufff == preft:
               print(namef, namet)
result_grph()