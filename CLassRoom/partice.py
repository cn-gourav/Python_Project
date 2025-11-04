# user input 
# a = int(input("Enter a Number : "))

# i = 1
# while(i <= a):
#     num = i
#     # increase order 
#     while(num <= a):
#         print("*" ,end = " ")
#         num = num + 1

#     print(end = "\n")
#     i = i+1


# *
# **
# ***
# ****


user = int(input("Enter a Number : "))
i=1
while(i<=user):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
    