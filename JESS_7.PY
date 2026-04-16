def ShiftLeft3(A, B, C):
    # C->B, B->A, A->C
    return B, C, A

# Sinov
A, B, C = 1, 2, 3
A, B, C = ShiftLeft3(A, B, C)
print(f"Chapga siljish: {A}, {B}, {C}") # 2, 3, 1 chiqadi