import math

def i_exp(X_q, S, z, n):

  a = 0.3581
  b = 1.353
  c = 0.344
  q_b = (b/S)
  q_c = c/a*(S**2)
  S_l = a*(S**2)
  
  X_q_l = (X_q + q_b)**2 + q_c
  X_out = n-z
  S_out = S_l / (2**n)
  return X_out, S_out
  
def norm(X_q, S, b):
  X_q = X_q - (2**b - 1)
  n = 32
  X_q_ln = -1*math.log(2/S)
  X_q = max(X_q, n*X_q_ln)
  z = X_q / X_q_ln
  X_n = X_q - z*X_q_ln
  
  return X_n, z, n
  
def ils(X_q, S, b):
  X_q_temp,z,n = norm(X_q, S, b)
  X_exp,S_iexp = i_exp(X_q_temp,S,z,n)
  X_out = 
  

  ## ensure ints are 32 bit < 2^31 or clip them
  ## try plotting function anad compare to regular softmax
  