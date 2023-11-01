import random


def keys():
    def is_prime(n):
        if n < 2:
            return False       # This function determines if the parameter is a prime number or not
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def make_prime():
        n = random.randint(2, 1000000)
        if is_prime(n):                                 # This function generates a prime number recursively (if the
                                                        # is not prime, run function again)
            return n
        else:
            return make_prime()

    p = make_prime()
    q = make_prime()                          #generate the p and q prime values
    n = p * q                                 #generate n = p*q
    phi = (p - 1) * (q - 1)                   #generate phi = (p - 1) * (q - 1)

    def gcd(phi, e):
        if e == 0:
            return phi                #
        return gcd(e, phi % e)                #This function finds the gcd between two parameters recursively
                                              # (if e is not 0, continue running the funciton with phi % e until gcd is found

    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)
    def extended_gcd(e, phi):
        if e == 0:
            return (phi, 0, 1)                 #This funciton determines the modular multiplicative inverse (Euclidean algo) to find d
                                               #SOURCE: https://stackoverflow.com/questions/16310871/how-to-find-d-given-p-q-and-e-in-rsa

        else:
            gcd, x, y = extended_gcd(phi % e, e)
            return (gcd, y - (phi // e) * x, x)

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    return p, q, e, d, n

def encrypt(M, e, n):
    ciphertext = []  # empty list to store chars
    for char in M:
        encrypted_char = pow(ord(char), e, n) #store char by calculation method C = M^e (mod n)
        ciphertext.append(encrypted_char)
    return ciphertext

def decrypt(ciphertext, d, n):
    message = ''  # Create an empty string to store the decrypted message
    for char in ciphertext:
        decrypted_char = chr(pow(char, d, n)) #decrypt char by calculating M = C^d (mod n)
        message += decrypted_char  # append each char to  message
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
    print("Ciphertext:", ciphertext)

    # Step 4: Decrypt the ciphertext
    decrypted_message = decrypt(ciphertext, d, n)
    print("Decrypted Message:", decrypted_message)


