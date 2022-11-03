def explosive_sum(memory: list) ->int :
    temp, current_index, pair_diff, sign_diff = 0, len(memory)-1, 1, 3  
    # pair diff means the diff between same sign, start from 1
    # sign diff means the diff between diff sign, start from 3

    isPair, isAdd = True, True 
    

    while current_index >= 0:
        if isPair: #check whether the current index is in the pair or not 
            if isAdd: #check whether the sign is '+' or '-' to add or minus the value
                temp += memory[current_index]
            else: 
                temp -= memory[current_index]
            current_index -= pair_diff #go to the second value of pair
                
            if current_index >= 0:
                if isAdd:
                    temp += memory[current_index]
                else:
                    temp -= memory[current_index]
                    
            else: break

            pair_diff += 1 #update the pair diff by increasing by 1 

            isPair = False # the next value after pair confirm not pair so update isPair to False

        else:
            current_index = current_index - sign_diff

            if current_index < 0: break

            sign_diff += 2 #update the sign_diff as it increases by 2

            isPair, isAdd = True, not isAdd #update isPair to True cause we ald change the index to pair location and invert the isAdd cause it's always one time plus and one time minus


    memory.append(temp)

            
    return memory

def exp_sum(number):
    memory = [1, 1, 2, 3]
    while len(memory) -1 < number: #because the number starts from 0 so it is directly same as index of array
        explosive_sum(memory)

    return memory[number] #print the last element of array which is what we want

print(exp_sum(20))


