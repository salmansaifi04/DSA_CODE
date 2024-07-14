# sum of first N natural numbers

def natural_number_sum(n):
    if n == 1:
        return 1
    else:
        return n+natural_number_sum(n-1)

# print(natural_number_sum(4))

## odd number sum
def odd_number_sum(n):
    if n == 1:
        return 1
    else:
        return 2*(n-1)+odd_number_sum(n-1)
    
# print(odd_number_sum(3))

## even number sum calculate
def even_number_sum(n):
    if n == 1:
        return 2
    else:
        return 2*n + even_number_sum(n-1)

# print(even_number_sum(2))

## factorial 
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

# print(fact(3))

## squares 
def squares_of_natural_number(n):
    if n == 0:
        return 0
    else:
        return n*n + squares_of_natural_number(n-1)

print(squares_of_natural_number(2))


# 50 30 10 40 80 70 100  (root, left tree, right tree) -> Preorder
# 10 30 40 50 70 80 100  (Left tree, root, right tree) -> Inorder 
# 10 40 30 70 100 80 50  (Left tree, right tree, root) -> Post order