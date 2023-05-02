import sys

def encode(s, key):
    s = s.upper()
    encoded = ""
    count = 0
    for c in s:
        ordd = ord(c)
        if ordd < 65 or ordd > 90:
            continue
        if count%50 == 0 and len(encoded) != 0:
            encoded += "\n"
        elif count%5 == 0 and len(encoded) != 0:
            encoded += " "
        encoded += chr(65 + (ord(c)-65+key) % 26)
        count += 1
    return encoded
 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please enter two arguments")
        sys.exit(1)
    print(encode(sys.argv[1], int(sys.argv[2])))
    sys.exit(0)