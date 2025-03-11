# while True:
#     try : 
#         N = int(input())

#         arr = '-' * pow(3, N)

#         def Canto(arr):
#             if len(arr) == 1:
#                 return '-'
#             else:
#                 length = int(len(arr)/3)
#                 return Canto(arr[0:length]) + ' ' * length + Canto(arr[(length * 2):])

#         print(Canto(arr))
    
#     except : 
#         break

while True:
    try : 
        N = int(input())
        arr = []
        
        for i in range(N + 1):
            if i == 0 : 
                arr.append("-")
            else : 
                arr.append(arr[i-1] + ' ' * pow(3,i - 1) + arr[i-1])       
        
        print(arr[N])
    
    except : 
        break
