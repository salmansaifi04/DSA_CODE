## print first N natural numbers

def natural_numbers(n):
    if n>0:
        natural_numbers(n-1)
        print(n, end= " ")

# natural_numbers(3)
# print()

def natural_num_rev_order(n):
    if n>0:
        print(n, end=" ")
        natural_num_rev_order(n-1)
# natural_num_rev_order(10)
# print()

def odd_numbers(n):
    if n>0:
        odd_numbers(n-1)
        print(2*n-1, end=" ")
    
# odd_numbers(10)
# print()

def even_numbers(n):
    if n>0:
        even_numbers(n-1)
        print(2*n, end=" ")
# even_numbers(10)
# print()

def odd_number_reverse(n):
    if n>0:
        print(2*n-1, end=" ")
        odd_number_reverse(n-1)
# odd_number_reverse(10)
# print()

def even_number_reverse(n):
    if n>0:
        print(2*n, end= " ")
        even_number_reverse(n-1)
even_number_reverse(10)
print()