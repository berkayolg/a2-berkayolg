from hashlib import sha256

def create_hash(password):                      #Taken from https://bitbucket.org/damienjadeduff/hashing_example/raw/master/hash_password.py
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()

def take_comment():
    comment = input("Enter your comment: ")
    password = input("Enter your password: ")
    return password

inputL = list()
comment = ""
len = 0
passwordHash = create_hash("GoodPassword")
inputL.append(comment)
falsePass = False
while comment != "quit":
    if falsePass is False and comment != "":
        print("Previously entered comments: ")
    for i in range(1, len+1):
        print(i, ". ", inputL[i])

    password = take_comment()
    if passwordHash == create_hash(password):
        inputL.append(comment)
        len += 1
        continue
    else:
        falsePass = True
        print("I am sorry i can't let you do this")


