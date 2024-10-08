def is_prime(func):
    def wrapper(*elems, **pelems):
        result = func(*elems, **pelems)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print('Composite num')
                    return result
            print('Prime num')
        elif result == 1:
            print('Neutral num')
        return result
    return wrapper


@is_prime
def sum_three(n1, n2, n3):
    return n1 + n2 + n3


res = sum_three(2, 3, 6)
print(res)
