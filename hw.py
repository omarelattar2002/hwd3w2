#Excercise 1
p_nums = [1, 3, 5, 7, 8]
n_nums = []

def convert_list(p_nums):

    for num in p_nums:
        n_nums.append(-num)
    return n_nums

print(convert_list(p_nums))


p_nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]
n_nums = []

def convert_list(p_nums):

    for num in p_nums:
        n_nums.append(-num)
    return n_nums


print(convert_list(p_nums))

#Excecise 2
str = "123 Real Street, Apt. 2, Springfield, OR 43498"

def get_nums(str):
    nums = []

    for num in str:
        if num.isdigit():
            nums.append(num)
        return nums    

str = "123 Real Street, Apt. 2, Springfield, OR 43498"

print(get_nums(str))


#Excecise 3
digits = "123"

def convert(digits):
    numbers = int(digits) + 1
    return str(numbers)


print(convert(digits))