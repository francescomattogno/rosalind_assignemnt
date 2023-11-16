

codondict = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


def readile():
    file = open('rosalind_splc.txt', 'r')
    seqs = file.readlines()
    i=1
    tempString=''
    list1 =[]
    while(i<len(seqs)):
        if(seqs[i].__contains__('>')):
            list1.append(tempString)
            tempString=''
            i+=1
        elif(i==len(seqs)-1):
            list1.append(seqs[i])
            i+=1
        else:
            tempString +=seqs[i]
            i+=1
    list1[0] = list1[0].replace('\n', '')
    i=1
    while (i < len(list1)):
        list1[i] = list1[i].replace('\n','')
        list1[0] = removeIntrons(list1[0],list1[i])
        i+=1
    list1[0] = list1[0].replace('T','U')
    return list1[0]


def removeIntrons(dna, intron):
    dna = dna.replace(intron, '')
    return dna


def rosalind_splc(rna):
    i = 0
    protein = ""
    rna = rna.replace("\n","")
    while (i < len(rna)):
        if(codondict[rna[i:i+3]]== 'STOP'):
            break
        protein += codondict[rna[i:i + 3]]
        i += 3
    protein = protein.replace('STOP','')
    print(protein)

rosalind_splc(readile())