def cyclic_rotation(word, where):
    
    '''
    >>> cyclic_rotation('abcde', 2)
    'deabc'
    >>> cyclic_rotation('tomek', 4)
    'tomek'
    '''

    return word[where+1:] + word[:where+1]
