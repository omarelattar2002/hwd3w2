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
string1 = "123 Real Street, Apt. 2, Springfield, OR 43498"
string2 = "My Phone Number is(555)555-4231"

def get_nums(string1):
    nums = []

    for num in string1:
        if num.isdigit():
            nums.append(num)
    return nums    

string1 = "123 Real Street, Apt. 2, Springfield, OR 43498"

print(get_nums(string1))
print(get_nums(string2))


#Excecise 3
digits = "123"
digits2 = "99"

def convert(digits):
    numbers = int(digits) + 1
    return str(numbers)


print(convert(digits))
print(convert(digits2))