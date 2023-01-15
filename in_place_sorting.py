# in place sorting
def sort(listname):
    '''
    Sorts an array in ascending order
    Do in place sorting which takes O(1)
    Overal time complexity O(n log n)
    '''
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(listname)):

            if listname[i] < listname[i - 1]:
                swap = False
                swapper = listname[i]
                listname[i] = listname[i - 1]
                listname[i - 1] = swapper
    return listname

#Test
numbers = [1,8,9,0,0, 6, 8, 8, 10, 3, 11, 20]
print(sort(numbers))
