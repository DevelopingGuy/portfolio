# Code by Ash

import random

print("""

 (                                                                                                
 )\ )                                  (      (                                       )           
(()/(    )          (  (         (     )\ )   )\ )      (           (   (       )  ( /(      (    
 /(_))( /(  (   (   )\))(    (   )(   (()/(  (()/(     ))\  (      ))\  )(   ( /(  )\()) (   )(   
(_))  )(_)) )\  )\ ((_)()\   )\ (()\   ((_))  /(_))_  /((_) )\ )  /((_)(()\  )(_))(_))/  )\ (()\  
| _ \((_)_ ((_)((_)_(()((_) ((_) ((_)  _| |  (_)) __|(_))  _(_/( (_))   ((_)((_)_ | |_  ((_) ((_) 
|  _// _` |(_-<(_-<\ V  V // _ \| '_|/ _` |    | (_ |/ -_)| ' \))/ -_) | '_|/ _` ||  _|/ _ \| '_| 
|_|  \__,_|/__//__/ \_/\_/ \___/|_|  \__,_|     \___|\___||_||_| \___| |_|  \__,_| \__|\___/|_|   
                                                                                                  
""")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

lenght = int(input("Lenght of the password: "))

print("Here is your newly generated password ^^ :")

password = ""

for c in range(lenght):
    password += random.choice(chars)

print(password)
