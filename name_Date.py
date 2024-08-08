letter = ''' 
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter_1 = letter.replace("<|Name|>","Sagar Kumar").replace ("<|Date|>","08-Aug-2024")
print(letter_1)