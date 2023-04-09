color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for (i, each_element) in enumerate(color):
    if i not in (0,4,5):
        print(each_element)