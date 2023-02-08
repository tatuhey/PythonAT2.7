# Raihan Khalil Abdillah
# AT2.7 Question 1
# Linear Search Method

# Linear Search in Python

# Linear search algorithm defined in a function
def linearSearch(fruitlist, input):
    for i in fruitlist:
        if (i == input):
            print(fruitlist.index(input))


fruitlist = ["mango", "watermelon", "apple", "orange", "grape", "banana"]
input = str(input("Enter fruit to search in the list: "))

# calling the function
linearSearch(fruitlist, input)
