class Matrix:
    def __init__(self, lst):
        self.mtrx = lst
        self.h = len(lst)
        self.w = len(lst[0])

    # Визначення розміру матриці
    def shape(self):
        return self.h, self.w

    # вивід на друк
    def __str__(self):
        res = ''
        for i in range(len(self.mtrx)):
            res += f'{self.mtrx[i]}\n'
        return res[:-1]

    # отримання значень по індексу
    def __getitem__(self, inx):
        return self.mtrx[inx]

    # додавання
    def __add__(self, other):
        if self.shape() == other.shape():
            sum = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.mtrx[i][j] + other.mtrx[i][j])
                sum.append(row)
            return Matrix(sum)
        else:
            if self.shape() < other.shape():
                k = other.shape()
                return self.bringing(k[0], k[1]) + other
            else:
                k = self.shape()
                return other.bringing(k[0], k[1]) + self

    # віднімання
    def __sub__(self, other):
        if self.shape() == other.shape():
            sub = []
            for i in range(self.h):
                row = []
                for j in range(self.w):
                    row.append(self.mtrx[i][j] - other.mtrx[i][j])
                sub.append(row)
            return Matrix(sub)
        else:
            if self.shape() < other.shape():
                k = other.shape()
                return self.bringing(k[0], k[1]) - other
            else:
                k = self.shape()
                return self - other.bringing(k[0], k[1])

    # Метод для створення нульової матриці
    @staticmethod
    def zeros(h, w, dtype=float):
        z = []
        for i in range(h):
            row = []
            for j in range(w):
                row.append(dtype(0))
            z.append(row)
        return Matrix(z)

    # Множення матриці на матрицю
    def dot(self, other):
        z = self.zeros(self.h, other.w, dtype=int)
        if self.w == other.h:
            for i in range(self.h):
                for j in range(other.w):
                    for k in range(other.h):
                        z[i][j] += self.mtrx[i][k] * other.mtrx[k][j]
            return z
        else:
            raise ValueError("operands could not be broadcast together with shapes")

    # Множення матриці на число
    def dot_const(self, const):
        res = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.mtrx[i][j] * const)
            res.append(row)
        return Matrix(res)

    # Транспонування матриці
    def transport(self):
        z = self.zeros(self.w, self.h)
        for i in range(self.h):
            for j in range(self.w):
                z[j][i] = self.mtrx[i][j]
        return z


    # Приведення матриці до заданого розміру додаванням нулів
    def bringing(self, h, w):
        z = self.zeros(h, w, dtype=int)
        for i in range(self.h):
            for j in range(self.w):
                z[i][j] = self.mtrx[i][j]
        return z

#################################################

a = Matrix([[1, 3, 3],
            [3, 4, 7],
            [3, 4, 7]])
b = Matrix([[1, 2, 3],
            [3, 4, 5]])

print(a)
print('*'*25)
print(b)
print('*'*25)
print(a + b)
print('*'*25)
print(a - b)
print('*'*25)
b = b.bringing(3, 3)
print(a.dot(b))
print('*'*25)
print(a.dot_const(2))
print('*'*25)
print(a.transport())
print('*'*25)
z = Matrix.zeros(3, 3, dtype=int)
print(z)
print('*'*25)
print(b[0][1])
print('*'*25)
print(b.shape())
print('*'*25)