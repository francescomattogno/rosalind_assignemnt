def rosalind_nwck(z, x, y):
    x_index = z.find(x)
    y_index = z.find(y)
    t = [i for i in z[min(x_index, y_index):max(x_index, y_index)] if i in [')','(',',']]
    par = ''
    result=0
    for i in t:
        par += i
    while '(,)' in par:
        par = par.replace('(,)','')
    if par.count('(') == len(par):
        result= len(par)
    elif par.count(')') == len(par):
        result= len(par)
    elif par.count(',') == len(par):
        result= 2
    else:
        result= par.count(')') + par.count('(') + 2
    print(result)

def nwck_final():
    with open('rosalind_nwck.txt', 'r') as f:
        tree = [line.strip().replace(';','') for line in f.readlines() if len(line.strip()) > 0]
    for i in range(0, len(tree), 2):
        z = tree[i]
        x, y = tree[i+1].split(' ')
        print(rosalind_nwck(z,x,y), end=" ")
    print()

nwck_final()


#sorry but i can't understand why before the numbers, that turns out to be correct, i get this 'none'