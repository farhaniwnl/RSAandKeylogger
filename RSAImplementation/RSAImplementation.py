import random


def keys():
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def make_prime():
        n = random.randint(2, 1000000)
        if is_prime(n):
            return n
        else:
            return make_prime()

    p = make_prime()
    q = make_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    def gcd(phi, e):
        if e == 0:
            return phi
        return gcd(e, phi % e)

    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)
    def extended_gcd(e, phi):
        if e == 0:
            return (phi, 0, 1)
        else:
            gcd, x, y = extended_gcd(phi % e, e)
            return (gcd, y - (phi // e) * x, x)

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    return p, q, e, d, n

def encrypt(M, e, n):
    ciphertext = ""  # Initialize an empty string to store the ciphertext without spaces
    spaced_ciphertext = ""  # Initialize another string with spaces for decryption
    for char in M:
        encrypted_char = pow(ord(char), e, n)
        ciphertext += str(encrypted_char)
        spaced_ciphertext += str(encrypted_char) + " "  # Add a space between characters for separation
    return ciphertext, spaced_ciphertext.strip()  # Return both versions

def decrypt(ciphertext, d, n):
    message = ""  # Initialize an empty string to store the decrypted message
    char_codes = ciphertext[1].split()  # Split the spaced ciphertext into individual character codes
    for char_code in char_codes:
        decrypted_char = chr(pow(int(char_code), d, n))
        message += decrypted_char
    return message



if __name__ == "__main__":
    # Step 1: Get the message from the user
    message = input("Enter the message to encrypt: ")

    # Step 2: Generate RSA keys
    p, q, e, d, n = keys()

    print("Generated RSA parameters:")
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")

    # Step 3: Encrypt the message
    ciphertext = encrypt(message, e, n)
    print("Ciphertext:", ciphertext[0])

    # Step 4: Decrypt the ciphertext
    decrypted_message = decrypt(ciphertext, d, n)
    print("Decrypted Message:", decrypted_message)


