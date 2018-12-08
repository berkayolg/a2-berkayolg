inputL = list()

comment = ""
len = 0
while comment != "quit":
    inputL.append(comment)
    if comment != "":
        print("Previously entered comments: ")
    for i in range(1, len+1):
        if comment != "":
            print("1. ", inputL[i])

    comment = input("Enter your comment: ")
    len += 1


