import random

# check if its a matrix
def checkRec(matrix):
    length = len(matrix)
    for i in matrix:
        if len(i) != len(matrix[0]):
            return False, length, len(matrix[0])
        else:
            pass
    return True, length, len(matrix[0])



# show a matrix in a better way
def matrixShow(matrix):
    if_rec, len, wid = checkRec(matrix)
    if if_rec == True:
        for m in range(len):
            for n in range(wid):
                print(matrix[m][n], end = ' ')
            print('')
    else:
        return 0

# creare matrix
def matrixCreate(m, n, id = int(0), rand = False, randlist = [int(0),int(1)]):
    n_list = []
    matrix = []
    if rand == True:
        for i in range(m):
            n_list = []
            for j in range(n):
                n_list.append(random.choice(randlist))
            matrix.append(n_list)
    else:
        for i in range(n):
            n_list.append(id)
        for i in range(m):
            matrix.append(n_list)
    return matrix

def boat():
    listzero = []
    for i in range(50):
        listzero.append(int(0))
    listt = []
    matrix = []
    for i in range(46):
        listt.append(int(0))
    matrix.append(listzero)
    matrix.append([int(0),int(0),int(0),int(1)] + listt)
    matrix.append([int(0),int(1),int(0),int(1)] + listt)
    matrix.append([int(0),int(0),int(1),int(1)] + listt)
    for i in range(23):
        matrix.append(listzero)
    return matrix

def combinMat(mat_1, mat_2, m = 0, n = 0):
    mymat_1 = []
    for i in mat_1:
        mymat_1.append(i.copy())
    mat_1_check = checkRec(mat_1)
    mat_2_check = checkRec(mat_2)
    if mat_1_check[0] == False or mat_2_check[0] == False:
        return False, mat_1
    for m_i in range(len(mat_2)):
        for n_i in range(len(mat_2[0])):
            mymat_1[m_i + m][n_i + n] = mat_2[m_i][n_i]
    return mymat_1