def sum_args(*args):
    return sum(args)
def sub_args(x,*args):
    return(x-sum(args))
def multi(*args):
    total =1
    for n in args:
        total = total*n
    return(total)
def dev(x,*args):
    total=1
    for n in args:
        total = total*n
    return(x*1/total)
