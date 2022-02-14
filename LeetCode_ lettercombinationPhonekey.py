from itertools import product
def phonecomb(s):
    mappings = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    values =[mappings[c] for c in s]
    res = []

    for ele in product(* values):
        res.append(''.join(ele))

    if res != [""]:
        return res
    else:
        []


b = '23'
print(phonecomb(b))
