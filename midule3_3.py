def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
#print_params(5,6,7,true) выходит ошибка, так как на выходе аргументов больше
print_params(b=25)
print_params(c=[1,2,3])

values_list = [1,False,'slovo']
values_dict = {'a':3, 'b':8, 'c':5}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = (25,'proverka')
print_params(*values_list_2,42)