
# def fact(n):
#     ans=1
#     for i in range(1,n+1):
#         ans=ans*i
#     print(ans)
# fact(5)

print("---------------------------")

def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)
        print(n)

# Example usage
print_numbers(5)