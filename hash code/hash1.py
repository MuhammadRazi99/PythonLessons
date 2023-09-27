from collections import defaultdict
def check_eligibility():
    pass
def swapPositions(list, pos1, pos2):
    first_ele = list.pop(pos1)  
    second_ele = list.pop(pos2-1)
    list.insert(pos1, second_ele) 
    list.insert(pos2, first_ele) 
    return list
def bubble_sort(pro): 
    for i in range(ProNo):
        already_sorted = True
        for j in range(ProNo - i - 1):
            if pro[j][2] < pro[j+1][2]:
                pro=swapPositions(pro,j,j+1)
                already_sorted = False
            elif pro[j][2] == pro[j+1][2]:
                if pro[j][1] > pro[j+1][1]:
                    pro=swapPositions(pro,j,j+1)
                    already_sorted = False
        if already_sorted:
            break
    return pro
with open("hash code/input_data/a_an_example_in.txt","r") as file:
    line1 = file.readline().split()
    ConNo = int(line1[0])
    ProNo = int(line1[1])
    con = {}
    for _ in range(ConNo):
        line = file.readline().split()
        name = line[0]
        skills ={}
        for _ in range(int(line[1])):
            skill = file.readline().split()
            skills[skill[0]]=int(skill[1])
        con[name]=skills
    pro = []
    for _ in range(ProNo):
        line = file.readline().split()
        skills = {}
        for _ in range(int(line[4])):
            skill = file.readline().split()
            skills[skill[0]] = int(skill[1])
        pro.append([x for x in line[:-1]]+[skills])
        
pro=bubble_sort(pro)
for i in range(pro):
    for j in range(len(pro[i][4].value())):
        if check_eligibility()==False:
            pro=swapPositions(pro,)
