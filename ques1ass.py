#Ask user to input the password, and then call the fuction check_password_strength to check the pwd. 
def check_password_strength():
      SC=['!', '@', '#', '$', '%' ]
      x=str(input("Enter the password: "))
      
      if x.__len__() >= 8:
         #print("Length is Ok!")
         for i in x:
             if (i.isupper()) == True:
                for j in x:
                    if (j.islower()) == True:
                        for k in x:
                             if k in SC:
                                 return bool 
                             else:
                                  print('Input pwd has no special characters') 
                                  break 
                    else:
                         print("Input Pwd has no lowercase letter") 
                         break             
             else:
                  print("Input pwd has no uppercase letter")
                  break  
      else:
           print("The Password should be 8 characters long, Try again")

check_password_strength()