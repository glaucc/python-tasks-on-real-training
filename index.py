a = ""
def func():
    global a
    a = str(input('Adinizi daxil edin: '))

def salamlama():
    print(f"Xos gelmisiniz, {a}")

func()
salamlama()
first = int(input("ilk reqemi daxil edin: "))
second = int(input("Ikinci reqemi daxil edin: "))

if first >= second:
    print("first value is greater")
else:
    print("second value is greater")

