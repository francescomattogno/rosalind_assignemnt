from Bio import Phylo
from io import StringIO

def distancecalc(tree, n_1, n_2):
    commonancestor = tree.commonancestor(n_1, n_2)
    dist = tree.dist(commonancestor, n_1) + tree.dist(commonancestor, n_2)
    return dist

def rosalind_nkew(tree):
    lines = tree.strip().split('\n')
    nodes = lines[-1] 
    nodes = nodes.strip().split()
    return tuple(nodes)

input = """paste file content here"""

s_tree = input.strip().split('\n\n')

for i, s_tree in enumerate(s_tree):
    o_tree = StringIO(tree)
    trees = Phylo.parse(o_tree, "newick")
    nodes = rosalind_nkew(s_tree)
    tree = next(trees) 
    distance = distancecalc(tree, *nodes)
        
    print(int(distance), end=" ")