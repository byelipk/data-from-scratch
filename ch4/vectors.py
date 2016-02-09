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
