'''
Unfinished
Integer Lightweight Softmax implementation using python. Assumes 8-bit quantized input.
'''
import numpy as np

def i_exp(X_q, S, z, n):
  '''
  Integer-only Exponential function (i-exp). [Algorithm 2 in paper]
  X_q = quantized input
  S = scale
  z,n = normalization parameters
  '''
  # coefficients derived from second order polynomial
  a = 0.3581
  b = 1.353
  c = 0.344
  q_b = (b/S)
  q_c = c/a*(S**2)
  S_l = a*(S**2)
  X_q_l = (X_q + q_b)**2 + q_c
  X_out = X_q_l << n - z 
  S_out = S_l / (2**n)

  return X_out, S_out
  
def norm_helper(X_q, S, b):
  '''
  Normalization function [Algorithm 1, function-I in paper]
  X_q = quantized input
  S = scale
  b = bit-width
  '''
  X_q = X_q - (2**b - 1)
  n = 32
  X_q_ln = np.round(-1*np.log(2/S))
  X_q = np.maximum(X_q, n*X_q_ln)
  z = np.round(X_q / X_q_ln)
  X_n = X_q - z*X_q_ln
  
  return X_n, z, n
  

def ils_helper(x, S, z, n):
  '''
  Helper function to calculate efficient softmax.
  x = 1 entry of quantized input
  S = scale
  b = bit-width
  '''
  total = np.sum(i_exp(X-q))
  return 2 << np.log2(total) - np.log2(i_exp(x, S, z, n))


def ils(X_q, S, b):
  '''
  Integer Lightweight Softmax function. [Algorithm 1 in paper]
  X_q = quantized input
  S = scale
  b = bit-width
  '''
  X_q_temp,z,n = norm_helper(X_q, S, b)
  X_exp,S_iexp = i_exp(X_q_temp,S,z,n)
  result = "FINISH THIS STEP"

  

  ## ensure ints are 32 bit < 2^31 or clip them
  ## try plotting function and compare to regular softmax
  