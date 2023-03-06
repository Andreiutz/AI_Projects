import lab_01


# Problem 1
def test_01():
    assert lab_01.get_last_word("Ana are mere rosii si galbene") == "si"
    assert lab_01.get_last_word("Zebra aaa") == "zebra"
    assert lab_01.get_last_word("abcd abce") == "abce"
    print("Test_01 Success")


# Problem 2
def test_02():
    assert lab_01.get_euclidian_distance_v1([1, 4], [5, 1]) == 5.0
    assert lab_01.get_euclidian_distance_v1([1, 1], [3, 3]) == 2.83

    assert lab_01.get_euclidian_distance_v2([1, 4], [5, 1]) == 5.0
    assert lab_01.get_euclidian_distance_v2([1, 1], [3, 3]) == 2.83
    print("Test_02 Success")


# Problem 3
def test_03():
    assert lab_01.get_vector_product([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
    print("Test_03 Success")


# Problem 4
def test_04():
    assert lab_01.only_one_appearance("ana are ana are mere rosii ana") == ['mere', 'rosii']
    assert lab_01.only_one_appearance("carte pauza masina") == ['carte', 'pauza', 'masina']
    assert lab_01.only_one_appearance("apa apa") == []
    print("Test_04 Success")


# Problem 5
def test_05():
    assert lab_01.get_duplicate([1, 2, 3, 4, 2]) == 2
    assert lab_01.get_duplicate([1, 1]) == 1
    assert lab_01.get_duplicate([1, 2, 3, 3]) == 3
    print("Test_05 Success")


# Problem 6
def test_06():
    assert lab_01.get_majoritar([1, 2, 3, 3, 3]) == 3
    assert lab_01.get_majoritar([1, 2, 3, 4, 5, 6]) == -1
    assert lab_01.get_majoritar([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2
    assert lab_01.get_majoritar([10, 11, 12, 13, 13, 13, 13]) == 13
    print("Test_06 Success")


# Problem 7
def test_07():
    assert lab_01.get_kst([7, 4, 6, 3, 9, 1], 2) == 7
    assert lab_01.get_kst([10, 12, 9, 3, 1, 8, 4], 4) == 8
    print("Test_07 Success")


# Problem 8
def test_08():
    assert lab_01.generate_binary_v1(4) == ['1', '10', '11', '100']
    assert lab_01.generate_binary_v1(7) == ['1', '10', '11', '100', '101', '110', '111']
    print("Test_08 Success")


# Problem 9
def test_09():
    assert lab_01.get_matrix_sums_v1(
        [[0, 2, 5, 4, 1],
         [4, 8, 2, 3, 7],
         [6, 3, 4, 6, 2],
         [7, 3, 1, 8, 3],
         [1, 5, 7, 9, 4]], [[[1, 1], [3, 3]], [[2, 2], [4, 4]]]
    ) == [38, 44]
    assert lab_01.get_matrix_sums_v1(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [[[0, 0], [2, 2]], [[0, 0], [1, 2]]]
    ) == [45, 21]
    assert lab_01.get_matrix_sums_v2(
        [[0, 2, 5, 4, 1],
         [4, 8, 2, 3, 7],
         [6, 3, 4, 6, 2],
         [7, 3, 1, 8, 3],
         [1, 5, 7, 9, 4]], [[[1, 1], [3, 3]], [[2, 2], [4, 4]]]
    ) == [38, 44]
    assert lab_01.get_matrix_sums_v2(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [[[0, 0], [2, 2]], [[0, 0], [1, 2]]]
    ) == [45, 21]
    print("Test_09 Success")


# Problem 10
def test_10():
    assert lab_01.best_row_index(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]
    ) == 1
    assert lab_01.best_row_index(
        [
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 1]
        ]
    ) == 2
    print("Test_10 Success")


# Problem 11
def test_11():
    assert lab_01.replace_elems(
        [
            [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        ]) == [
               [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
               [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
               [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
               [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    assert lab_01.replace_elems(
        [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 0]
        ]
    ) == [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0]
    ]
    print("Test_11 Success")



def test_all():
    test_01()
    test_02()
    test_03()
    test_04()
    test_05()
    test_06()
    test_07()
    test_08()
    test_09()
    test_10()
    test_11()


test_all()
