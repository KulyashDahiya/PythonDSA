def reverse(data):
    start_index = 0
    end_index = len(data) - 1

    data = list(data)

    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    return data

def is_palindrome(data):

    data1 = reverse(data)
    print(data1)
    data1 = ''.join(data1)
    print(data1)

    if data == data1:
        return True
    else:
        return False

if __name__ == '__main__':

    var1 = input("Type a word\n")
    print(is_palindrome(var1))

