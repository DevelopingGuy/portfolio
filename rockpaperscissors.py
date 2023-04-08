# Code by Ash

import random

print("""

 (                     (                             (                                  
 )\ )              )   )\ )                          )\ )                               
(()/(           ( /(  (()/(    )           (   (    (()/(     (                (        
 /(_)) (    (   )\())  /(_))( /(  `  )    ))\  )(    /(_)) (  )\  (   (    (   )(   (   
(_))   )\   )\ ((_)\  (_))  )(_)) /(/(   /((_)(()\  (_))   )\((_) )\  )\   )\ (()\  )\  
| _ \ ((_) ((_)| |(_) | _ \((_)_ ((_)_\ (_))   ((_) / __| ((_)(_)((_)((_) ((_) ((_)((_) 
|   // _ \/ _| | / /  |  _// _` || '_ \)/ -_) | '_| \__ \/ _| | |(_-<(_-</ _ \| '_|(_-< 
|_|_\\\___/\__| |_\_\  |_|  \__,_|| .__/ \___| |_|   |___/\__| |_|/__//__/\___/|_|  /__/ 
                                 |_|                                                   

""")

def play():
    user = input("Press 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It\'s a tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"
    
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True 

while True:
    print(play())