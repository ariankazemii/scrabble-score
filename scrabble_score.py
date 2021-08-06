def score(word):
    
    values = {'AEIOULNRST':1,
              'DG':2,
              'BCMP':3,
              'FHVWY':4,
              'K':5,
              'JX':8,
              'QZ':10}
    total = 0
    
    word = word.upper()

    for letter in word :
        for key,value in values.items():
            if letter in key :
                total += value
                
    return total
