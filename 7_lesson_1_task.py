class Matrix:
    def __init__(self, mat_1, mat_2):
        self.mat_1 = mat_1
        self.mat_2 = mat_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.mat_1)):

            for el in range(len(self.mat_2[i])):
                matr[i][el] = self.mat_1[i][el] + self.mat_2[i][el]

        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in matr]))



my_matrix = Matrix([[4, 7, 8],
                    [10, 65, 45],
                    [54, 76, 89]],
                   [[98, 23, 12],
                    [65, 76,54],
                    [76, 32, 76]])

print(my_matrix.__add__())