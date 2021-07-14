import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    exp_list = np.exp(L)
    sum_exp = sum(exp_list)
    result = []
    for i in exp_list:
        result.append(i*1.0/sum_exp)
    return result

print(softmax([5,6,7]))