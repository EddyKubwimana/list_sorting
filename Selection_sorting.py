

# second algorithm focus on finding a smallest number and arrange the rest compared to that number
def selection_sort (listname):
    index = 0
    while index != len(listname):
        for item in range(index, len(listname)):
            if listname[item] < listname[index]:
                listname[index], listname[item] = listname[item], listname[index]
        index = index+1
    return listname




