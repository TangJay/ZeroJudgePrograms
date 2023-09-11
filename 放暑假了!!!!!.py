import sys

for i in sys.stdin:
    i = int(i)
    if (i and not (i & (i - 1))) == 1:
        print("Yes")
    else:
        print("No")
