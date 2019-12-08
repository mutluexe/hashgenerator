import hashlib
import sys
def main():

    with open(sys.argv[1], "r") as file:
        f1 = file.readlines()
    for data in f1:
        print(encrypt_string(data))

def encrypt_string(string):
    sha_signature = \
        hashlib.sha256(string.encode()).hexdigest()
    return sha_signature

if __name__ == "__main__":

    main()
