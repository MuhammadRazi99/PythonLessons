def hamiltonian_visit():
    hamiltonian=[[1,2],[1,2]]



outputStr=[]
testCase=int(input())
for _ in range(testCase):
    no=int(input())
    outputStr.append(hamiltonian_visit(no))

for i in range(testCase):
    print(f"Case #{i+1}: {outputStr[i]}")