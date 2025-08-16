
# if-elif- else

# age= 18

# if age>18:
#     print("hii")
# elif age<18:
#     print("fuck off")
# else:
#     print("😁")    



# while

# count =1;

# while count<10:
#     print(count )
#     count+=1

#*****************************************************  for loop   **************************

# for i in range(1,6):
#     print(i)

    
    # range(start, stop) generates numbers, stop is exclusive.


#*****************************************************  Break Continue   **************************


# for num in range(1, 6):
#     if num == 3:
#         continue  # skip 3
#     if num == 5:
#         break     # stop loop
#     print(num)


# #              *****************************************************  Break Continue   **************************


# def hello():
#     print("hii")

# hello()

# #              *****************************************************  2️⃣ Function with Parameters & Return   **************************



# def add(a,b):
#     return a+b

# total = add(5,5)
# print(total)

# def greet(name="hello"):
#     print(f"name: {name} " )

# greet()
# greet("hii")



# #              *****************************************************  4️⃣ *args and **kwargs   ********************************

# def sum_all(*args):
#     return sum(args)


# print(sum_all(1,2,3,4,5))


# def user(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key} : {value}")


# user(name="Prem",age=22)

# *args → many positional arguments as a tuple.

# **kwargs → many keyword arguments as a dictionary.



x = 10  # Global variable

def change_x():
    global x
    x = 20  # Changes global x
    print("Inside function:", x)

change_x()
print("Outside function:", x)
