import math
from Cryptodome.Util.number import long_to_bytes
from crypto import n, e

def fermat_factor(N):
    A = math.isqrt(N)
    if A * A < N:
        A += 1
    while True:
        B2 = A * A - N
        B = math.isqrt(B2)
        if B * B == B2:
            p = A + B
            q = A - B
            return p, q
        A += 1

with open("ciphertext.txt", "r") as f:
    c_hex = f.read().strip()
    c = int(c_hex, 16)

p, q = fermat_factor(n)
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

m = pow(c, d, n)
flag = long_to_bytes(m).decode("utf-8")

print("Flag:", flag)

with open("solution.txt", "w") as f:
    f.write(flag)

