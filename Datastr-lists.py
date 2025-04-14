
#activity1
#Create an empty list
empty_list = []
print()

# A list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Use * operator
triples = [1, 2, 3] * 3
print(triples)

#reverse the given list
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList,"\n")

#activity 2 program to check first and last character is same 
# function to check whether 
# first and last character of words match
def match_words(words):
	ctr = 0
	lst = []
	for word in words:
		if len(word) > 1 and word[0] == word[-1]:
			ctr += 1
			lst.append(word)
	
	print("List of words with first and last character same\n", lst)
	return ctr
	
count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count)

#activity3 :
L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", L)
  
# variable to store the sum of 
# the list
count = 0
  
# Finding the sum
for i in L:
    count += i
      
# divide the total elements by
# number of elements
avg = count/len(L)
  
print("sum = ", count)
print("average = ", avg)

# Sorting the elements of the list
L.sort()
 
# printing the first element
print("Smallest element is:", L[0])

# printing the last element
print("Largest element is:", L[-1])

#activity4 :
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")



list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


#activity4
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")



list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)


#activity5
# Example string
my_string = "Hello, how are you?"

# Split the string into words
split_string = my_string.split()

print("Split string:", split_string)

#acp 

def square_and_split(start, end):
    # Create a list of square values
    square_values = [x**2 for x in range(start, end + 1)]

    # Filter even and odd square values
    even_squares = [x for x in square_values if x % 2 == 0]
    odd_squares = [x for x in square_values if x % 2 != 0]

    # Print results
    print(f"\nSquare values from {start} to {end}: {square_values}")
    print(f"Even square values: {even_squares}")
    print(f"Odd square values: {odd_squares}")

# Get user input for range
start_range = int(input("Enter the starting number of range: "))
end_range = int(input("Enter the ending number of range: "))

# Call the function
square_and_split(start_range, end_range)



