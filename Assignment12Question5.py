from typing import List
from copy import copy, deepcopy


def find_max_matches(compatible: List[List[bool]]):
    x = len(compatible)
    y = len(compatible[0])
    array1 = deepcopy(compatible)
    array2 = deepcopy(compatible)
    option1 = ""
    option2 = ""
    num1 = 0
    num2 = 0

    # ------------------ Option 2 --------------------3 cycle check first
    cycle3 = "There is no length 3 cycle"
    for i in range(0, x):
        for j in range(0, y):
            if i != j and array2[i][j]:
                for x in range(0, len(array2[j])):
                    if array2[j][x] and array2[x][i] and i != x:
                        cycle3 = "Length 3 cycle: " + str(i) + "->" + str(j) + " and " + str(j) + "->" + str(x) + " and " + str(x) + "->" + str(i) + "\n"
                        alreadyDonated(array2, i)
                        alreadyDonated(array2, j)
                        alreadyDonated(array2, x)
                        num2 += 6
                        option2 = option2 + cycle3

    cycle2 = "There is no length 2 cycle"
    for i in range(0, x):
        for j in range(0, y):
            if y > i != j < x:
                # runs throw all the relation and check if there is a true i,j and j,i (2 cycle)
                if array2[i][j] and array2[j][i]:
                    cycle2 = "Length 2 cycle: " + str(i) + "->" + str(j) + " and " + str(j) + "->" + str(i) + "\n"
                    alreadyDonated(array2, i)
                    alreadyDonated(array2, j)
                    num2 += 4
                    option2 = option2 + cycle2

    # ------------------ Option 1 --------------------2 cycle check first
    cycle2 = "There is no length 2 cycle"
    for i in range(0, x):
        for j in range(0, y):
            if y > i != j < x:
                # runs throw all the relation and check if there is a true i,j and j,i (2 cycle)
                if array1[i][j] and array1[j][i]:
                    cycle2 = "Length 2 cycle: " + str(i) + "->" + str(j) + " and " + str(j) + "->" + str(i) + "\n"
                    alreadyDonated(array1, i)
                    alreadyDonated(array1, j)
                    num1 += 4
                    option1 = option1 + cycle2

    cycle3 = "There is no length 3 cycle"
    for i in range(0, x):
        for j in range(0, y):
            if i != j and array1[i][j]:
                for x in range(0, len(array1[j])):
                    if array1[j][x] and array1[x][i] and i != x:
                        cycle3 = "Length 3 cycle: " + str(i) + "->" + str(j) + " and " + str(j) + "->" + str(x) + " and " + str(x) + "->" + str(i) + "\n"
                        alreadyDonated(array1, i)
                        alreadyDonated(array1, j)
                        alreadyDonated(array1, x)
                        num1 += 6
                        option1 = option1 + cycle3

    if num1 > num2:
        print(option1)
    else:
        print(option2)

# function that set the donator a false on all of his relation after he donated
def alreadyDonated(compatible: List[List[bool]], donated: int):
    for i in range(0, len(compatible[donated])):
        compatible[donated][i] = False

def main():

    a = [[True, True, False, False],
         [True, False, True, True],
         [True, False, True, False],
         [False, True, False, False],
         [False, False, False, False]]
    find_max_matches(a)


if __name__ == '__main__':
    main()