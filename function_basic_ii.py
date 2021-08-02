# 1
def countdown(x):
    list = []
    for i in range(x, -1, -1):
        list.append(i)
    return list


print(countdown(5))

# 2


def newList(list):
    print(list[0])
    return list[1]


print(newList([1, 2]))

# 3


def first_plus_length(list):
    return list[0] + len(list)


print(first_plus_length([1, 2, 3, 4, 5]))

# 4


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0, len(list)):
        if list[i] > list[1]
        output.append(list[i])

    print(len(output))
    return output

# 5


def length_and_value(size, value):
    output = []
    for i in range(0, size,):
        output.append(value)

    return output
