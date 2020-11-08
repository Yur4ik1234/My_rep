print("first constant", None)
print("first constant", False)

print(hex(64), "is 64 in hex \n")

print(help(hex), "\n")

clock = 4
if clock+1 == 5:
    print("clock\n")
else:
    print("not clock")

for i in range(6):
    print(" Hello world!!!")



    with open("README.md", "w") as f:
        f.write("Write info to file")

square = lambda a: a*a
print(square(3))


try:
    value = input("Enter a number: ")
    x = int(value)
except ValueError as e:
    print(e)
finally:
    print("Everything is OK")
