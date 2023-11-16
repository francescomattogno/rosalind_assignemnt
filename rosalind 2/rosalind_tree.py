def rosalind_tree():
 fasta = "rosalind_tree.txt"

 with open(fasta, "r") as f:
    n = int(f.readline())
    adjacency_list = [line.strip().split(" ") for line in f]

 s_trees = [] 
 nodi = set()
 for i, j in adjacency_list:
    if i in nodi or j in nodi:
        for st in s_trees:
            if i in st or j in st:
                s_trees[s_trees.index(st)].append(i)
                s_trees[s_trees.index(st)].append(j)
                nodi.add(i), nodi.add(j)
    else:
        s_trees.append([i,j])
        nodi.add(i), nodi.add(j)

 l = len(s_trees)
 for i in range(l):
    for j in range(l):
        if i==j:
           break
        if len(set(s_trees[i] + s_trees[j])) < len(s_trees[i]) + len(s_trees[j]):
            s_trees[i] = list(set(s_trees[i] + s_trees[j]))
            s_trees[j] = []
 s_trees = [i for i in s_trees if i]


 result = (n -len(nodi)) + len(s_trees) - 1
 print(result)

rosalind_tree()