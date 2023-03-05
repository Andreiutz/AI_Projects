import math

import numpy


# Probleme simple, dar cu dichis


# Problem 1
# Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text care conține mai multe cuvinte separate prin ” ” (spațiu).
# De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".

def get_last_word(text):
    words = text.lower().split(' ')
    last_word = words[0]
    for word in words:
        if word > last_word:
            last_word = word
    return last_word


# Problem 2
# Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
# De ex. distanța între (1,5) și (4,1) este 5.0

# V1
def get_euclidian_distance_v1(loc1, loc2):
    return round(math.dist(loc1, loc2), 2)


# V2
def get_euclidian_distance_v2(loc1, loc2):
    return round(math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2), 2)


# Problem 3
# Să se determine produsul scalar a doi vectori rari care conțin numere reale.
# Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
# De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.

def get_vector_product(a, b):
    return numpy.dot(a, b)


# Problem 4
# Să se determine cuvintele unui text care apar exact o singură dată în acel text.
# De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.

def only_one_appearance(text):
    dict = {}
    words = text.lower().split(' ')
    for word in words:
        if word in dict.keys():
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    result = []
    for word in dict.keys():
        if dict[word] == 1:
            result.append(word)
    return result


# Problem 5
# Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o singură
# valoare se repetă de două ori, să se identifice acea valoare care se repetă. De ex. în șirul [1,2,3,4,2] valoarea 2
# apare de două ori.

def get_duplicate(array):
    n = len(array)
    total_sum = 0
    for x in array:
        total_sum = total_sum + x
    return total_sum - n * (n - 1) // 2


# Problem 6
# Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul majoritar (care
# apare de mai mult de n / 2 ori). De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].

def get_majoritar(numbers):
    n = len(numbers)
    freqs = 10 * [0]
    for num in numbers:
        freqs[num] = freqs[num] + 1
        if freqs[num] > n // 2:
            return num
    return -1


# Problem 7
# Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
# De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.

def get_kst(numbers, k):
    numbers.sort()
    return numbers[len(numbers) - k]


# Problem 8
# Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. De ex. dacă n = 4,
# numerele sunt: 1, 10, 11, 100.

def generate_binary_v1(n):
    result = []
    for i in range(1, n + 1):
        result.append(bin(i)[2:])
    return result


# Problem 9
# Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)),
# să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.

# V1
def get_matrix_sums_v1(array, coordinates):
    sums = []
    for pair in coordinates:
        point1 = pair[0]
        point2 = pair[1]
        sum = 0
        for i in range(point1[0], point2[0] + 1):
            for j in range(point1[1], point2[1] + 1):
                sum = sum + array[i][j]
        sums.append(sum)
    return sums

# print(get_matrix_sums_v1([[0, 2, 5, 4, 1],
# [4, 8, 2, 3, 7],
# [6, 3, 4, 6, 2],
# [7, 3, 1, 8, 3],
# [1, 5, 7, 9, 4]], [[[1,1],[3,3]], [[2,2],[4,4]]]))

# V2 mai optim cu sume partiale dar extra memorie
def get_matrix_sums_v2(array, coordinates):
    sums = []

    newLine = [0] * len(array[0])
    array.insert(0, newLine)

    for i in range(0, len(array)):
        array[i].insert(0, 0)

    for i in range(1,len(array)):
        for j in range(1, len(array[0])):
            array[i][j] = array[i][j] + array[i-1][j] + array[i][j-1] - array[i-1][j-1]

    for pair in coordinates:
        point1 = pair[0]
        point2 = pair[1]

        #we add +1 to indexes since we bordered the array with zeros
        sums.append(array[point2[0]+1][point2[1]+1] - array[point2[0]+1][point1[1]] - array[point1[0]][point2[1]+1] + array[point1[0]][point1[1]])

    return sums



# Problema 10
# Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii,
# să se identifice indexul liniei care conține cele mai multe elemente de 1

def best_row_index(array):
    best_left = len(array[0])-1
    best_index = 0
    for i in range(0, len(array)):
        if array[i][best_left] == 1:
            best_index = i
            while array[i][best_left] == 1:
                best_left = best_left - 1
    return best_index

# Problem 11
# Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt
# complet înconjurate de 1.

def replace_elems(array):
    indexes = []
    index = 2
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j] == 0:
                if fill(i, j, array, index):
                    indexes.append(index)
                index = index + 1
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j] in indexes:
                array[i][j] = 1
            elif array[i][j] != 1:
                array[i][j] = 0
    return array

def fill(i, j, array, index):
    if i < 0 or i >= len(array) or j < 0 or j >= len(array[0]):
        return False
    elif array[i][j] != 0:
        return True
    else:
        array[i][j] = index
        result1 = fill(i-1, j, array, index)
        result2 = fill(i, j-1, array, index)
        result3 = fill(i+1, j, array, index)
        result4 = fill(i, j+1, array, index)
        return result1 and result2 and result3 and result4
