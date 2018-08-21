#Made by Frost
 
#Degree of Static Indeterminacy 



#Degree of static indeterminacy of any structure is the number of extra equations required so as to find the support reactions and other remaining unknows in that structure 


#The degree of static indeterminacy is quite useful in civil engg so as to solve indeterminate structures. This is my attempt so as to calculate it with help of this code.




""" 
Input the type of structure it is,and on next line type in the number of members ,no of joints in it , no of reactions
eg:- truss 
     8 5 5
eg:- frame 
     9 8 6 
"""




#for truss
def truss(x,y,z) : 
    dst=(x+z)-2*y
    if dst<0 :
        print("Oops!! The structure is unstable")
    else :
        print("The degree of static indeterminacy is " + str(dst))



#for frame
def frame(x,y,z) :
   dsf= (3*x+z)-3*y
   if dsf<0:
      print("Oops!! The structure is unstable")
   else:
      print("The degree of static indeterminacy is " + str(dsf))






struct=input("Enter the type of structure: ")   
print("Enter the values of m,j,r:")

try :
    m,j,r = [int(x) for x in input().split()]
except EOFError :
    print("Please input values as given in the example  ")   #For Error handling
    
 
    
#to function
if struct == "truss":
         truss(m,j,r)
elif struct == "frame" :
         frame(m,j,r)
#else :
        # beam()