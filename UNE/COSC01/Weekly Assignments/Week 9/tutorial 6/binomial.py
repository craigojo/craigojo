def binomial_coeff(n, k):
  """Compute the binomial coefficient "n choose k".
  n: number of trials
  k: number of successes
  returns: int
  """

  return 1 if k == 0 else 0 if n == 0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)





# def binomial_coeff(n, k):
#   try:

#     if k == 0:
#       return 1
#     if n == 0:
#       return 0
#     else:
#       res = (binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1))
#       return res
#   except:
#     ValueError


# result = binomial_coeff(20, 3)
# print(result)




# def binomial_coeff(n, k):
#   """Compute the binomial coefficient "n choose k".
#   n: number of trials
#   k: number of successes
#   returns: int
#   """

#   if k == 0:
#     return 1
#   if n == 0:
#     return 0

#   res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
#   return res