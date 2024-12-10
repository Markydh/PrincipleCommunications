# 一维卷积 
import numpy as np

def convNew(A, B):
    # Initialize the output array C with zeros, size of the convolution result
    C = np.zeros(len(A) + len(B) - 1)
    
    # Perform the convolution
    for i in range(len(A)):
        C[i:i+len(B)] += A[i] * B  # Equivalent to the element-wise multiplication and shift
    
    return C

A = np.random.randn(100000)
B = np.random.randn(100000)