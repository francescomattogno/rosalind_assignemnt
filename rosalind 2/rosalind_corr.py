f=open("rosalind_corr.txt", "r")
list=[]
list2=[]
q=[]
correct=[]
def point_mut_count(no_mut, mut):
	count = 0
	for i in range(len(no_mut)):
		if mut[i] != no_mut[i]:
			count +=1
	return count
def complement(text):
	new_text= ""
	for i in text:
		if i == "A":
			new_text+="T"
		elif i == "C":
			new_text+="G"
		elif i == "G":
			new_text+="C"
		else:
			new_text+="A"
	return new_text[::-1]
def rosalind_corr():
    for i in f.readlines():
        if not i.startswith(">"):
            list.append(str(i.replace("\n", "")))
    for i in list:
        if list.count(i)>1:
           correct.append(i)
        elif complement(i) in list:
           correct.append(i)
        else:
           q.append(i)
    for i in q:
        c=0
        for j in correct:
            if point_mut_count(i, j)==1:
                if c==0:
                   c=1
                   list2.append(str(i)+"->"+str(j))
                elif point_mut_count(i, complement(j))==1:
                    if c==0:
                        c=1
                        list2.append(str(i)+"->"+str(complement(j)))
    for i in list2:
        print(i)

rosalind_corr()

