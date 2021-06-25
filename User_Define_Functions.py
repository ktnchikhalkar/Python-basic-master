################################################################################
    
# User defined functions   #named functions

 
def add_numbers(x,y):
   sum = x + y
   return sum



def avg_number(x, y):
    print("Average of ",x," and ",y, " is ",(x+y)/2)
    
avg_number(3, 4)



## Define a function with conditional statement
    
def max_num(num1,num2,num3):
    
    if num1 >= num2 and num1 >= num3:
        
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3
    
print (max_num(400,60,1150))




def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")


evenOdd(2) 
evenOdd(3)


############### Lambda expressions ########################################

def cube(y):                      #user define function
    return y*y*y; 
  
 # lambda functions are anonymous expression i.e (function without any name)

g = lambda x: x*x*x 
print(g(7)) 

  

#filter function will filter the elements or items that satisfies the condition

list1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list1 = list(filter(lambda x: (x%2 != 0) , list1)) 
print(final_list1)


# map function will helps to apply the condition to all elements one by one

list2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list2 = list(map(lambda x: x*2 , list2)) 
print(final_list2) 