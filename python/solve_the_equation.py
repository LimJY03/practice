# https://leetcode.com/problems/solve-the-equation/


def solveEquation(equation: str) -> str:
    lhs, rhs = equation.split('=')
    lhs = lhs.replace('-', '+-')
    rhs = rhs.replace('-', '+-')
    lhs_term = lhs.split('+')
    rhs_term = rhs.split('+')
    
    def get_coefficient(arr: list) -> list:
        coef_arr, num_arr = [], []
        for i in range(len(arr)):
            if 'x' not in arr[i]:
                if len(arr[i]) == 0:
                    continue
                num_arr.append(int(arr[i]))
            else:
                if arr[i] == 'x':
                    coef_arr.append(1)
                elif arr[i] == '-x':
                    coef_arr.append(-1)
                else:   
                    coef_arr.append(int(arr[i].strip('x')))
        return coef_arr, num_arr
    lhs_coef, lhs_num = get_coefficient(lhs_term)
    rhs_coef, rhs_num = get_coefficient(rhs_term)
    
    total_coef, total_num = 0 , 0
    total_coef += sum(lhs_coef) -(sum(rhs_coef))
    total_num += -(sum(lhs_num)) + sum(rhs_num)
    print(total_coef, total_num)
    if (lhs_coef == rhs_coef):
        if total_num == 0:
            val_x =  'Infinite Solution'
        else:
            val_x = 'No Solution'

   
    else:
        val_x = total_num/total_coef if total_num % total_coef != 0 else total_num//total_coef 
        
    
    print(val_x)


# solveEquation('x+5-3+x=6+x-2')
# solveEquation('x=x+5')
solveEquation('-x=-1')


