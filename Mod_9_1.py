def apply_all_func(int_float_list, *funcs):
    results = {}
    for func in funcs:
        func_name = func.__name__
        result = func(int_float_list)
        results[func_name] = result
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
