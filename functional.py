# don't need to focus on the functional paradigm assignment part.

# Functional Paradigm
# Implement a function that will flatten and sort a nested array of integers in ascending order, and which adheres to a functional programming paradigm. Input needs to be a matrix of integers. example [[5,9,7],[12,6,741,4],45,[6,65,2,31]]

def sort_asc_int(array): # takes in any array as a paramater
    new_array = [] # creates a new array to keep the function pure
    # since the array can contain other arrays, this makes sure to go to through each item and/or array within the original array, then each item inside the nested arrays.
    for item in array: 
        # checks to see if the item is only an integer
        if type(item) == int:
            new_array.append(item)
        # if the item is anything other than just a single integer do this:
        else:
            for i in item:
                new_array.append(i) # adds the individual items to the array
    # sorted() is a build in function that sorts in ascending order.         
    return sorted(new_array)


print(sort_asc_int([[5,9,7],[12,6,741,4],45,[6,65,2,31]]))


'''
How does this solution ensure data immutability?
    The original array, the argument of the function is not being changed. Instead a new array is being created, and it is only being created within the funciton itself.

Is this solution a pure function? Why or why not?
    Yes, the data that gets input into the function does not change. There is no global array that is being changed. 

Is this solution a higher order function? Why or why not?
    No. the solution is not a function, and the function sort_asc_int() does not take a function as an argument. 

Would it have been easier to solve this problem using a different programming style?
    Not really sure. It wasn't too difficult to figure this one out after I understood what flattening is and how to make it happen using for loops.

Why in particular is functional programming a helpful paradigm when solving this problem?
    Being able to use for loops within one function is all I needed, and I also didn't need to create a global array since the point of the function is to just sort the items in the nested array/matrix. 

'''
