# customerNo=int(input())
# customerGuide={}
# for i in range(customerNo):
#     like=list(input().split(' '))
#     customerGuide.update({f"like{i+1}":like})
#     dislike=list(input().split(' '))
#     customerGuide.update({f"dislike{i+1}":dislike})
# #like=set()
# i=0
# no=customerGuide.get(f"like{i}")
# no=int(no[0])
# print(no)
# # for i in range(customerNo):
# #     for j in range()
# #     like.add(customerGuide.values())
from collections import defaultdict

def checkClients(clients,ing):
    count = 0
    for x in clients:
        sat = True
        for i in x[0]:
            if i not in ing:
                sat = False
                break
        if sat:
            for i in x[1]:
                if i in ing:
                    sat = False
                    break
        if sat:
            count +=1
    return count
        
if _name_ == '_main_':
    with open('test_sets/c.txt','r') as file:
        n = int(file.readline())
        count = defaultdict(lambda:0)
        clients=[]
        for _ in range(n):
            like = file.readline().split()
            dislike = file.readline().split()
            clients.append([like[1:],dislike[1:]])
            try:
                for i in like[1:]:
                    count[i] = count[i]+1
                for i in dislike[1:]:
                    count[i] = count[i]-1
            except IndexError:
                pass
        final_count = count.copy()
        
        for x in clients:
            like = x[0]
            dislike = x[1]
            try:
                failures  = 0
                success = 0
                for i in like:
                    if count[i]<= 0:
                        failures += 1
                for i in dislike:
                    final_count[i] = final_count[i]+(0.001*failures)
                    if count[i]>=1:
                        success +=1
                for i in like:
                    final_count[i] = final_count[i]-(0.001*success)
            except IndexError:
                print('err')
        # print(sorted(list(count.items()),key = lambda x : x[1]))
        count = final_count
        # print(final_count)
        final = [x for x,y in count.items() if y>0] 
        
        print(f"{len(final)} {' '.join(final)}") 
        # print(len([x for x, y in count.items() if y == 0]))
        # print(checkClients(clients,final))