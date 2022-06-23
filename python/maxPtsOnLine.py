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

print(maxPtsOnLine([[1,1], [2,2], [3,3], [3,4],[5,5]]))
