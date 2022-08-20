#Function named hello() that prints a greeting to the user
def hello():
    print('Hello!')

hello()


#Function named pack() that returns a single list with 
# 3 arguments inside as list elements
def pack(x, y, z):
    return [x, y, z]
   
print(pack("orange, sandwich, chips"))

#Function named eat_lunch() that accepts a list of any length
def eat_lunch(my_lst):
 if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

eat_lunch([])
eat_lunch(["sushi"])
eat_lunch(["cookie", "orange"])