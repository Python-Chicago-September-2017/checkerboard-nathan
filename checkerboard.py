row = "*"
for i in range(0,8):
    for s in range(0,7):
        if row[s] == "*":
            row += " "
        else:
            row += "*"
    print row
    if row[0] == "*":
        row = " "
    else:
        row = "*"