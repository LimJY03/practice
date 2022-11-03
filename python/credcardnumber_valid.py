import re

def validate_cred_card(card: str):
    output = 'Valid'
    
    if '-' in card:
        output = 'Valid' if re.fullmatch("^[456]\d{3}(-\d{4}){3}", card) else 'Invalid'
    
    if output == 'Valid':
        output = 'Invalid' if re.search(r'([0-9])\1{3,}', re.sub('-', '', card)) or not re.fullmatch('^[456]\d{15}', re.sub('-', '', card)) else 'Valid'
    
    return output
    

num_test = int(input())
for i in range(num_test):
    print(validate_cred_card(str(input())))


    
    