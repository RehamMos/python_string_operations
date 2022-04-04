from string_ops import *


string = "This is an example. Return the nth occurrence of example in this example string."

print("Testing Function 'find the required word based on occurrence' ")
print('-'*50)

print(find_nth_occurrence("example", string, 1))
print(find_nth_occurrence("example", string, 2))
print(find_nth_occurrence("example", string, 3))


print('#'*50)

print("Testing Function 'Simple String Matching'")
print('-'*50)
print(solve("code*s","codewars"))
print(solve("codewar*s","codewars"))
print(solve("code*warrior","codewars"))
print(solve("c","c"))
print(solve("*s","codewars"))
print(solve("*s","s"))
print(solve("s*","s"))
print(solve("aa","aaa"))
print(solve("aa*","aaa"))
print(solve("aaa","aa"))
print(solve("aaa*","aa"))
print(solve("*","codewars"))

print('#'*50)
print("Testing Function 'Is it a palindrome?'")
print('-'*50)

print(is_palindrome('a'))
print(is_palindrome('aba'))
print(is_palindrome('Abba'))
print(is_palindrome('malam'))
print(is_palindrome('walter'))
print(is_palindrome('kodok'))
print(is_palindrome('Kasue'))
print('#'*50)
print("Testing Function 'Repeated Substring'")
print('-'*50)
print(f("ababab"))
print(f("abcde"))