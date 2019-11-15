def poker_hand(hand):
    '''
    >>> poker_hand([1,1,1,1,1])
    'five'
    >>> poker_hand([2,2,2,2,3])
    'four'
    >>> poker_hand([1,1,1,2,3])
    'three'
    >>> poker_hand([2,2,3,3,4])
    'twopairs'
    >>> poker_hand([1,2,2,3,4])
    'pair'
    >>> poker_hand([1,1,2,2,2])
    'fullhouse'
    >>> poker_hand([1,2,3,4,5])
    'nothing'
    '''
    hand_dic = {}
    for num in hand:
        if num in hand_dic:
            hand_dic[num] += 1
        else:
            hand_dic[num] = 1
    if len(hand_dic) == 5:
        answer = 'nothing'
    if len(hand_dic) == 4:
        answer = 'pair'
    if len(hand_dic) == 3:
        for el in hand_dic.values():
            if el == 3:
                answer = 'three'
                break
            else:
                answer = 'twopairs'
    if len(hand_dic) == 2:
        for el in hand_dic.values():
            if el == 4:
                answer = 'four'
                break
            else:
                answer = 'fullhouse'
    if len(hand_dic) == 1:
        answer = 'five'
    return answer

