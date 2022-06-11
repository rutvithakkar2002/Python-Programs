import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
mul=(lambda a,b:a*b)(a,b)
print(sys.argv[0])
print(mul)
print(len(sys.argv))
