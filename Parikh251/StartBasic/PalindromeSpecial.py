#L18 YT last code part

## MY CODE
# def palin(s):
#     s = s.lower()
#     ns = ""
#     for i in s:
#         if i.isalnum():
#             ns += i
#         else:
#             continue
#     if ns == ns[::-1]:
#         print("palindrome")
#     else:
#         print("not a palindrome")


## OTHER WAY
def palin(s):
    s = s.lower()
    r = s[::-1]
    n = len(s)  # or len(r),  its same
    i, j = 0
    while i<n and j<n:
        if s[i].isalnum() == False:
            i += 1
        elif r[j].isalnum() == False:
            j += 1
        elif s[i] == r[j]:
            i += 1
            j += 1
        else:
            return False

    return True


s = input()
if palin(s):
    print("Palindrome")
else:
    Print("Not a Palindrome")
