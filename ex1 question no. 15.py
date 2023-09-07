n_terms = int(input("number of terms in the Fibonacci sequence: "))
sequence = [0, 1]

if n_terms <= 0:
    print("Positive number.")
elif n_terms == 1:
    print("Fibonacci sequence:")
    print(sequence[0])
else:
    print("Fibonacci sequence:")
    for i in range(2, n_terms):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    for term in sequence:
        print(term, end=" ")