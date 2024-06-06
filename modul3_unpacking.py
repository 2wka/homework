def print_params(a=1, b='строка', c=True):
    print(a,b,c)

print_params()
print_params('','','')
print_params(b='')
values_list = [True, 6, 'ананас']
values_dict ={'a': 'апельсин','b': False, 'c': 123}
print_params(*values_list)
print_params(**values_dict)