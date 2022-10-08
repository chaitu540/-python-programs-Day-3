def reverse(str):
    string="".join(reversed(str))
    return string
s=str(input("Enter a string:"))

print("The reversed string using reversed() is:",reverse(s))
