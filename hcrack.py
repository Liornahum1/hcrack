import hashlib,argparse

#Create parser and parse arguments
parser = argparse.ArgumentParser("hcrack",description="Simple hash cracker supporting md5,sha1,sha224,sha256,sha384,sha512")

parser.add_argument("-H","--hash",help="Enter hash string")
parser.add_argument("-w","--wordlist",help="Wordlist to use in order to crack")


args = parser.parse_args()

#Check if the hash is md5 hash
if len(args.hash) == 32:
    print("Starting md5 hash cracking!")
    try:
        with open(args.wordlist,"r") as fl:
            for word in fl:
                word = word.replace('\n','')
                hash_res = hashlib.md5(word.encode()).hexdigest()               
                if hash_res == args.hash:
                    print(f"Hash Cracked:{word}")
    except FileNotFoundError:
        print("File not cound!")

#Check if the hash is sha1 hash
elif len(args.hash) == 40:
    print("Starting sha1 hash cracking!")
    try:
        with open(args.wordlist,"r") as fl:
            for word in fl:
                word = word.replace('\n','')
                hash_res = hashlib.sha1(word.encode()).hexdigest()
                if hash_res == args.hash:
                    print(f"Hash Cracked:{word}")
    except FileNotFoundError:
        print("File not cound!")

#Check if the hash is sha224 hash
elif len(args.hash) == 56:
    try:
        print("Starting sha224 hash cracking!")
        with open(args.wordlist,"r") as fl:
            for word in fl:
                word = word.replace('\n','')
                hash_res = hashlib.sha224(word.encode()).hexdigest()
                if hash_res == args.hash:
                    print(f"Hash Cracked:{word}")
    except FileNotFoundError:
        print("File not cound!")
    
#Check if the hash is sha256 hash
elif len(args.hash) == 64:
    try:
        print("Starting sha256 hash cracking!")
        with open(args.wordlist,"r") as fl:
            for word in fl:
                word = word.replace('\n','')
                hash_res = hashlib.sha256(word.encode()).hexdigest()
                if hash_res == args.hash:
                    print(f"Hash Cracked:{word}")
    except FileNotFoundError:
        print("File not cound!")

#Check if the hash is sha384 hash
elif len(args.hash) == 96:
    try:
        print("Starting sha384 hash cracking!")
        with open(args.wordlist,"r") as fl:
            for word in fl:
                word = word.replace('\n','')
                hash_res = hashlib.sha384(word.encode()).hexdigest()
                if hash_res == args.hash:
                    print(f"Hash Cracked:{word}")
    except FileNotFoundError:
        print("File not cound!")

#Check if the hash is sha512 hash
elif len(args.hash) == 128:
    try:
        print("Starting sha512 hash cracking!")
        with open(args.wordlist,"r") as fl:
            for word in fl:
                word = word.replace('\n','')
                hash_res = hashlib.sha512(word.encode()).hexdigest()
                if hash_res == args.hash:
                    print(f"Hash Cracked:{word}")
    except FileNotFoundError:
        print("File not cound!")
