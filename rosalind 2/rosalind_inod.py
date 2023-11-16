def rosalind_inod():
    with open("rosalind_inod.txt") as f:
      n = int(f.readline().strip())

    print(n-2)

rosalind_inod()
