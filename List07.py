def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    sikl=0
    while len(list1)>sikl:
        if list1[sikl]==0:
            list1[sikl]=False
        sikl+=1
    return list1