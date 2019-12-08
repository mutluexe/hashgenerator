import hashlib
import sys
import io
def main():

    with io.open(sys.argv[1], "r", encoding='utf-8', errors='ignore') as file:
        f1 = file.readlines()
    for data in f1:
        print(encrypt_string(data))

    file.close()

def encrypt_string(string):
    sha_signature = \
        hashlib.sha256(string.encode('utf-8', errors='ignore')).hexdigest()
    return sha_signature

if __name__ == "__main__":

    main()
