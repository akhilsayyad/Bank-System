# print("hello")
n = 23

flag = False
for i in range(2,(int(n/2))):
    # print("hello there..................")
    if n%i == 0:
        # print(f"{n} is not prime")
        flag = True
        break
if flag == True:
    print("not prime number........")
else:
    print("prime number")


text = "HELLO WORLD !"

new_str = ""
for ch in text:
    if "A" <= ch <= "Z":
        new_char = chr(ord(ch)+32)
        new_str += new_char
    else:
        new_str += ch

print(new_str)

for i in range(1,5):
    for j in range(1,5):
        if j <= i:
            print("*",end=" ")
    print()