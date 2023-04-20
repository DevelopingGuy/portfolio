# Code by Ash

import qrcode
from PIL import Image

print("""

        (             )  (                                                                
   (    )\ )   (   ( /(  )\ )         (                                       )           
 ( )\  (()/(   )\  )\())(()/(   (     )\ )      (           (   (       )  ( /(      (    
 )((_)  /(_))(((_)((_)\  /(_))  )\   (()/(     ))\  (      ))\  )(   ( /(  )\()) (   )(   
((_)_  (_))  )\___  ((_)(_))_  ((_)   /(_))_  /((_) )\ )  /((_)(()\  )(_))(_))/  )\ (()\  
 / _ \ | _ \((/ __|/ _ \ |   \ | __| (_)) __|(_))  _(_/( (_))   ((_)((_)_ | |_  ((_) ((_) 
| (_) ||   / | (__| (_) || |) || _|    | (_ |/ -_)| ' \))/ -_) | '_|/ _` ||  _|/ _ \| '_| 
 \__\_\|_|_\  \___|\___/ |___/ |___|    \___|\___||_||_| \___| |_|  \__,_| \__|\___/|_|   
                                                                                         
""")

data = input("Input the data of the qr code (links, phone numbers, emails): ")

img = qrcode.make(data)
type(img)
img.save("output.png")

print("Output has been saved as output.png")

im = Image.open(r"output.png") 
im.show()
