import re
def mix_strings(s1, s2):
    
    new_s1 = re.sub('[^a-z]', '', s1)
    new_s2 = re.sub('[^a-z]', '', s2)
    
    count = 0
    dict_s1 = {}
    dict_s2 = {}
    arr = ''
    substr = ''
    arr = []


    for i in new_s1:
        if i in dict_s1:
            dict_s1[i] += 1
        else:
            dict_s1[i] = 1

    for i in new_s2:
        if i in dict_s2:
            dict_s2[i] += 1
        else:
            dict_s2[i] = 1

    dict_s1 = {k: v for k, v in sorted(dict_s1.items(), key=lambda item: (-item[1], item[0]))}

    dict_s2 = {k: v for k, v in sorted(dict_s2.items(), key=lambda item: (-item[1], item[0]))}

    dict_s1 = dict(filter(lambda x: x[1] > 1, dict_s1.items()))
    dict_s2 = dict(filter(lambda x: x[1] > 1, dict_s2.items()))

        


    for i in set(list(dict_s1.keys()) + list(dict_s2.keys())):
        if i in dict_s1 and i in dict_s2:

            if dict_s1[i] > dict_s2[i]:
                arr.append('1:' + i*dict_s1[i]) 
                    
            elif dict_s1[i] == dict_s2[i]:
                arr.append('=:' + i*dict_s2[i])
            else:
                arr.append('2:' + i*dict_s2[i])
        else:
            if i in dict_s1:
                arr.append('1:' + i*dict_s1[i])
            else:
                arr.append('2:' + i*dict_s2[i])

    print(dict_s1, dict_s2)

    arr = sorted(arr, key=lambda x: (-len(x), x[0], ord(x[2:3])))
    

    
   

    return '/'.join(arr)  
    


if __name__ == '__main__':

    print(mix_strings("my&friend&Paul has heavy hats! &", "my friend John has many many friends &"))
    print(mix_strings('mmmmm m nnnnn y&friend&Paul has heavy hats! &', "my frie n d Joh n has ma n y ma n y frie n ds n&"))
    print(mix_strings("Are the kids at home? aaaaa fffff", "Yes they are here! aaaaa fffff"))
