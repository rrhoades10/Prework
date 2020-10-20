a_list = [1, 2, 3, 4, 5, 6, 7]


def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True


is_consecutive(a_list)
