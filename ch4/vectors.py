# A three-dimensional vector (height, weight, age)
height_weight_age_vector = [34,56,12]

# A four-dimensional vector (exam1, exam2, exam3, exam4)
exam_grades_vector = [87, 59, 98, 89]

# Custom functions that will allow us to perform
# arithmetic on vectors.
#
# Vector addition
# Vectors sum componentwise. This means that if we
# add two vector of equal length, their sum will
# be the sum of each dimension added together.
#
# v1 = [1,2]
# v2 = [3,4]
# v1 + v2 => [(v1[0] + v2[0]), (v1[1] + v2[1])] => [4, 6]

# vector_add([1,2], [2,1])
# => [3,3]
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

# vector_subtract([1,2], [2,1])
# => []
def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v,w)]

# vector_sum([[1,2,3], [1,2,3]])
# => [2,4,6]
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

# scalar_multiply(2, [2,4,6])
# => [4, 8, 12]
def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of
    the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

# dot([1,2], [2,1])
# => 4
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# sum_of_squares([1,2,3,4])
# => 30
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


import math

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

# distance([1,2], [1,2])
# => 0.0
def distance(v, w):
    return magnitude(vector_subtract(v, w))


# Matricies
#
# Matrices are important to us for several reasons.
# First, we can use a matrix to represent a data set
# consisting of multiple vectors, simply by considering
# each vector as a row of the matrix. For example, if
# you had the heights, weights, and ages of 1,000 people
# you could put them in a 1, 000 × 3 matrix:
A = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]

B = [
    [4,5,6],
    [4,5,6],
    [4,5,6]
]

# Second, we can use an n × k matrix to represent a
# linear function that maps k-dimensional vectors to
# n-dimensional vectors.
#
# Third, matrices can be used to represent binary relationships.
friendships = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], # user 0
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0], # user 1
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], # user 2
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0], # user 3
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], # user 4
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0], # user 5
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 6
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0], # user 7
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1], # user 8
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]] # user 9

# friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
#                  (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# If there are very few connections, this is a much more
# inefficient representation, since you end up having to
# store a lot of zeroes. However, with the matrix representation
# it is much quicker to check whether two nodes are
# connected — you just have to do a matrix lookup
# instead of (potentially) inspecting every edge:
friendships[0][2] == 1 # True, 0 and 2 are friends
friendships[0][8] == 1 # False, 0 and 8 are not friends

friends_of_five = [
    i
    for i, is_friend in enumerate(friendships[5])
    if is_friend
]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
    whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)   # given i, create a list
    for j in range(num_cols)] # [entry_fn(i, 0), ... ]
    for i in range(num_rows)] # create one list for each i

def is_diagonal(i, j):
    return 1 if i == j else 0
