n = input()

rev = ""
for i in n:
    rev = rev + i

if rev == n:
    print("palindrome")
else:
    print("not a palindrome")



# if n[::-1] == n:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")