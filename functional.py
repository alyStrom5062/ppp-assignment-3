def flat_sort(my_array):
    my_array = []
    for i in my_array:
        for key in i:
            my_array.append(key)
    return sorted(my_array)

# How does this solution ensure data immutability?
# Is this solution a pure function? Why or why not?

#       This solution is a pure functions because the result it gives is fully based on what it is given and nothing else.

# Is this solution a higher order function? Why or why not?

#       This solution is not a higher order function becaise it only contains for loops, array declaration, and a built in 
#       method. No other function is defined or dependent on this solution.

# Would it have been easier to solve this problem using a different programming style?

#       Functional programming is best for function-first, result after. It is unclear if there are multiple static arrays which could benefit
#       to be written as objects.

# Why in particular is functional programming a helpful paradigm when solving this problem?

#       Functional programming allows for a single program to be performed over and over again regardless of how many instances of my_array
#       occur. A function is like a machine which can produce what it is meant to make again and again.