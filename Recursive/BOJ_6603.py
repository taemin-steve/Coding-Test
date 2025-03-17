# N = 10
# R = 3

# list = [1,2,3,4,5,6,7,8,9,10]

# choose = []

# def Combination(index, level):
#     if level == R:
#         print(choose)
#         return
        
#     for i in range(index, N):
#         choose.append(list[i])
#         Combination(i +1, level + 1)
#         choose.pop()
        
# Combination(0,0)

#==========================================================
        
# while True:
#     try:
#         N, *lst = input().split()
#         N = int(N)
        
#         R = 6
#         choose = []
        
#         def Combination(index, level):
#             if level == R:
#                 print(" ".join(choose))
#                 return
            
#             for i in range(index, N):

#                 choose.append(lst[i])
#                 Combination(i+1, level + 1)
#                 choose.pop()
                
#         Combination(0,0)
#         print()
        
#     except: 
#         break

# ====================================================

from itertools import combinations

while True :
    try:
        N, *lst = map(int, input().split())
        for c in combinations(lst, 6):
            print(" ".join(map(str, c)))
            
        print()
        
    except:
        break