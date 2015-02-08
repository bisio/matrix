# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    '''
    return [ (a1+b1,a2+b2)  for (ia,(a1,a2)) in enumerate(A)  for (ib,(b1,b2)) in enumerate(B) if ia==ib]



## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    return {v:k for (k,v) in d.items()}



## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    return [p+i for i in range(0,n)]

comprehension_with_row = [row(i,20) for i in range(0,15)]

comprehension_without_row = [ [i+j for j in range(0,20)]  for i in range(0,15)] 

p_function = {1:0.5,
              2:0.2,
              3:0.1,
              5:0.1,
              6:0.1}

def f1(x):
    return x+1


## 4: (Problem 4) Probability Exercise 1
Pr_f_is_even = sum( [p_function[x] for x in p_function.keys()  if f1(x) % 2 == 0] )
Pr_f_is_odd  = sum( [p_function[x] for x in p_function.keys()  if f1(x) % 2 == 1] )


def g(x):
    return x % 3

p_function_2 = {1:0.2,
                2:0.2,
                3:0.2,
                4:0.1,
                5:0.1,
                6:0.1,
                7:0.1}


## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = sum([ p_function_2[x] for x in p_function_2.keys() if g(x) == 1  ])
Pr_g_is_0or2 = sum([ p_function_2[x] for x in p_function_2.keys() if g(x) in [0,2]  ])

