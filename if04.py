def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0 and b>0 and c>0:
        return 3
    if a>0 and b>0 and c<0 or b>0 and a<0 and c>0 or b<0 and a>0 and c>0:
        return 2
    if a<0 and b<0 and c>0 or a>0 and b<0 and c<0 or b>0 and a<0 and c<0:
        return 1
    else:
        return 0
print(main(-3,-9,5))