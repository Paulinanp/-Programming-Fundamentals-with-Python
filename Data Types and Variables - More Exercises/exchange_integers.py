a = int(input())
b = int(input())

print(f"Before: \n"
      f"a = {a} \n"
      f"b = {b}")

c = b
b = a
a = c

print(f"After:\n"
      f"a = {a}\n"
      f"b = {b}")