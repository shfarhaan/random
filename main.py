# Answer to question 18 Find the last occurrence of an element in a list
# Given a list and an element, write a program to find the last occurrence of the element in the list.
my_list = [1, 5, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]
element = 5
last_occurrence_index = len(my_list) - my_list[::-1].index(element) - 1
print("Last occurrence of the element is at index:", last_occurrence_index)
print("Length: ", len(my_list))

print("Reverse Order: ", my_list[::-1])

print("Index element: ", my_list[::-1].index(element) )

