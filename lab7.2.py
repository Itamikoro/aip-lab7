ns = [37, 4, 72, 11, 36, 4, 34, 11]
prover = set()
povtor = set()
for i in ns:
    if i in prover:
        povtor.add(i)
    else:
        prover.add(i)
print(povtor)