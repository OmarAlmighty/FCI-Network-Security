import random


# Function to generate a super-increasing sequence for the public key
def generate_super_increasing_sequence(k):
    sequence = [random.randint(1, 100)]
    while len(sequence) < k:
        next_element = sum(sequence) + random.randint(1, 100)
        sequence.append(next_element)
    return sequence


# Function to generate the private key from the public key
def generate_public_key(super_increasing, n, r):
    return [(r * element) % n for element in super_increasing]


# Function to encrypt the plaintext using the private key
def knapsack_encrypt(plaintext, public_key):
    # Convert character to 8-bit binary
    ptxt_bits = [int(bit) for bit in format(ord(plaintext), '08b')]
    encrypted_message = sum(a * x for a, x in zip(public_key, ptxt_bits))
    return encrypted_message


# Function to decrypt the ciphertext using the super-increasing sequence
def knapsack_decrypt(ciphertext, super_increasing, r, n):
    # Compute modular multiplicative inverse of r
    r_inv = pow(r, -1, n)
    decrypted_sum = (r_inv * ciphertext) % n

    # Solve knapsack problem
    bits = []
    for w in reversed(super_increasing):
        if decrypted_sum >= w:
            bits.append(1)
            decrypted_sum -= w
        else:
            bits.append(0)

    # Reverse bits to get correct order and convert to character
    bits = bits[::-1]
    char_code = int("".join(map(str, bits)), 2)
    return chr(char_code)

# Ensure n is sufficiently large and r is coprime with n
# This is the GCD algorithm
def is_coprime(x, y):
    while y:
        x, y = y, x % y
    return x==1


# Parameters
k = 8  # Number of elements in the super-increasing sequence
# Generate super-increasing sequence and ensure n is large enough
super_increasing = generate_super_increasing_sequence(k)
n = sum(super_increasing) * 2 + random.randint(100, 1000)  # Make n sufficiently large

# Ensure r is coprime with n
r = random.randint(2, n - 1)
while not is_coprime(r, n):
    r = random.randint(2, n - 1)

# Generate keys
puk = generate_public_key(super_increasing, n, r)

plaintext = "g"
ciphertext = knapsack_encrypt(plaintext, puk)
decrypted_message = knapsack_decrypt(ciphertext, super_increasing, r, n)

print("Super-increasing sequence:", super_increasing)
print("Private Key:", puk)
print("Original Message:", plaintext)
print("Encrypted Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)
