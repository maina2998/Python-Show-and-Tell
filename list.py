


def sum_list(items):#writing program to sum all the items in a list
    sum_numbers = 0#declaring our number as zero
    for x in items:#each number in item
        sum_numbers += x#finding the total sum of items
    return sum_numbers#this returns the sum of numbers
print(sum_list([1,2,-8]))#this prints the sum of the declared numbers


def multiply_list(items):#writing program to multiply all the items in a list
    multiply_numbers = 1#declaring our number as zero
    for x in items:#each number in item
        multiply_numbers*=x#finding the total multiply of items
    return multiply_numbers#this returns the mutiply of numbers
print(multiply_list([1,2,-8]))#this prints the mutiply of the declared numbers
