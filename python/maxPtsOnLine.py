from math import floor





def maxPtsOnLine(arr2d):
    count = 0
    for i in range(len(arr2d)-1):
        for j in range(len(arr2d[i])-1):
            if(j==0):
                for i in range(len(arr2d)-1):
                    # check whether it's going right, pos x
                    if(arr2d[i+1][j] - arr2d[i][j] > 0):
                        distance_x = arr2d[i+1][j] - arr2d[i][j]
                        print('going right, pos x')
                    elif(arr2d[i+1][j] - arr2d[i][j] == 0):
                        distance_x = arr2d[i+1][j] - arr2d[i][j]
                        print('on the same x axis')
                    # check whether it's going left, neg x
                    else:
                        distance_x = arr2d[i+1][j] - arr2d[i][j]
                        print('going left, neg x')
        
            # check whether it's going up, positive y
            if(arr2d[i+1][j] - arr2d[i][j] > 0):
                distance_y = distance_x = arr2d[i+1][j] - arr2d[i][j]
                print('going up, pos y')
            elif(arr2d[i+1][j] - arr2d[i][j] == 0):
                distance_y = distance_x = arr2d[i+1][j] - arr2d[i][j]
                print('on the same y axis')
            else:
                distance_y = distance_x = arr2d[i+1][j] - arr2d[i][j]
                print('going down, neg y')

        if abs(distance_y) == distance_x:
            count += 1
                
    return count

print(maxPtsOnLine([[1, 1],[2, 2],[2, 3],[3, 3],[3, 5]]))



# def solution3(arr2d):
#     def gradient (x1,x2,y1,y2) :
#         grad = (y2 - y1) / (x2 - x1)
#         return grad

#     count = 0
#     max = 0
#     same = 0
#     for i in range(len(arr2d)-1):
#         dict = {}
#         j = i+1
#         for j in range(len(arr2d)-1):
#             # check duplicates
#             # if arr2d[j][0] - arr2d[i][0] == 0 & arr2d[j][1]-arr2d[i][1] == 0:
#             #     same += 1
#             # else:
#             #     continue
#             if arr2d[i][0] - arr2d[j][0] != 0:
#                 m = gradient(arr2d[i][0], arr2d[j][0], arr2d[i][1], arr2d[j][1])
#             else:
#                 m = 'Infinity'
#             if m not in dict:
#                 dict[m] = 1
#             else: 
#                 dict[m] += 1
            
             
#             # for x in dict:
                
#             #     if(dict[x] + same + 1 > max):
#             #         max = dict[x] + same + 1
                
#             #     return max
                    
       
#     # if max > count:
#     #     count = max   
        
#     return count
    
# print(solution3([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(maxPtsOnLine([[1,1], [2,2], [3,3], [3,4],[5,5]]))
