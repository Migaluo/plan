def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)  # 递归的方法写阶乘


def fact(n):
    if n==1:
       return 1
    else:
        return n*fact(n-1)    # 普通方法