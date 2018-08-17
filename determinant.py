import random

class Matrix:
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.table = []

        for i in range(self.height):
            tmp_row = []
            for j in range(self.width):
                tmp_row.append(random.randint(1,10))
            self.table.append(tmp_row)

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                print(str(self.table[i][j]).rjust(4,' '),end=' |')
            print('')

    def det(self):
        if self.width!=self.height:
            return False
        if self.width == 1:
            return self.table[0][0]

        sum = 0
        coeff = 1
        for k in range(self.width):
            M2 = Matrix(self.width-1,self.height-1)
            for i in range(1,self.height):
                j2 = 0
                for j in range(self.width):
                    if j!=k:
                        M2.table[i-1][j2] = self.table[i][j]
                        j2+=1
            sum += coeff*self.table[0][k]*M2.det()
            coeff=-coeff
        return sum

M1 = Matrix(8,8)

M1.draw()

print(M1.det())