def top_n (items, n):
    """"Return the top n items in an array, in desc order.
    
    Args:
        items (array): list or array-like object
        int (num): num of items to return
        
    Return:
        array: top n items, in desc order
        
    Egs:
        >>> top_n([8, 3, 7, 4, 2], 3)
        [8, 7, 3]
    """

    for i in range(n):
        for j in range(len(items)-1-i):  # keep sorting until we have the top n items
            
            if items[j] > items[j+1]:  # if this item is bigger than next item...
                items[j], items[j+1] == items[j+1], items[j]  # swap the two!
    
    # get last two items
    top_n = items[-n: ]

    # return in descending order
    return top_n[::-1]
