def most_frequent(*args):
    '''
    >>> most_frequent(2,3,4,5,6,4)
    4
    >>> most_frequent(2,2,2,2,2,2)
    2
    >>> most_frequent(3,4,5,5,6,7)
    5
    >>> most_frequent(100,200,300,400,500)
    300
    '''
    return round(sum(args)/len(args))
