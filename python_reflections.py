#Prompt 1: Functional Programming 
#this function will flatten and sort an array of integers in ascending order
def flatten_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_sort([[1,2,3],[4,5,6],[7,8,9]]))

#this solution ensures data immutability by defining the array as a variable. this ensures it can only return the specified data type.
#this is a pure function, it will always return the same output for a given input.
#this is not a higher order function as it does not take another function as an argument nor does it return a function.
#this is probably the simplest solution to the given prompt, so functional programming is the best way to solve it.
#functional programming maintains clean code when dealing with many simple calculations, and keeps the data immutable which means it can be used again elswhere in a program.