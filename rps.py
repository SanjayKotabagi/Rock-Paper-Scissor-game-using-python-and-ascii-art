import random as r
import os
import time

rock = '''
    _______
---'   ____)
      (_____)
ROCK   (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
PAPER     _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
SCISSORS _________)
      (____)
---.__(___)
'''

pcc = '''
                    _           _          
  _ __   ___    ___| |__   ___ (_) ___ ___ 
 | '_ \ / __|  / __| '_ \ / _ \| |/ __/ _ \\
 | |_) | (__  | (__| | | | (_) | | (_|  __/
 | .__/ \___|  \___|_| |_|\___/|_|\___\___|
 |_|                                       
'''
usc = '''
                             _           _          
  _   _ ___  ___ _ __    ___| |__   ___ (_) ___ ___ 
 | | | / __|/ _ \ '__|  / __| '_ \ / _ \| |/ __/ _ \\
 | |_| \__ \  __/ |    | (__| | | | (_) | | (_|  __/
  \__,_|___/\___|_|     \___|_| |_|\___/|_|\___\___|
                                                    
'''


youwin = '''
        ============================================
        __   _____  _   _  __        _____ _   _ 
        \ \ / / _ \| | | | \ \      / /_ _| \ | |
         \ V / | | | | | |  \ \ /\ / / | ||  \| |
          | || |_| | |_| |   \ V  V /  | || |\  |
          |_| \___/ \___/     \_/\_/  |___|_| \_|
        ============================================                                  
        '''

pcwin = '''
    ============================================
     ____   ____  __        _____ _   _ 
    |  _ \ / ___| \ \      / /_ _| \ | |
    | |_) | |      \ \ /\ / / | ||  \| |
    |  __/| |___    \ V  V /  | || |\  |
    |_|    \____|    \_/\_/  |___|_| \_|
    ============================================
    '''



def result(user,pc):
    global rock,paper,scissors,usc,pcc
    print(usc)
    if user == 1:
        print(rock)
        print(pcc)
        if pc == 1:
            print(rock)
            return 1,1
        elif pc == 2:
            print(paper)
            return 0,1
        elif pc == 3:
            print(scissors)
            return 1,0

    if user == 2:
        print(paper)
        print(pcc)
        if pc == 1:
            print(rock)
            return 1,0
        elif pc == 2:
            print(paper)
            return 1,1
        elif pc == 3:
            print(scissors)
            return 0,1

    if user == 3:
        print(scissors)
        print(pcc)
        if pc == 1:
            print(rock)
            return 0,1
        elif pc == 2:
            print(paper)
            return 1,0
        elif pc == 3:
            print(scissors)
            return 1,1

def sboard():
    global pcb,ub,pcscore,uscore
    u,p = ub,pcb
    a,b = uscore,pcscore
    print("====| USER |================| PC |======")
    for i in range(len(pcb)-1):
        print("\t{} \t\t\t{}".format(u[i],p[i]))
    print("========================================")
    print("====| {}  |================| {} |======".format(a,b))
    dummy = input("ENTER ANY KEY CONTINUE : ")


pcscore = 0
uscore = 0
pcb = []
ub = []
while True:
    time.sleep(3)
    os.system('cls')
    print('''
    ======================================================================================
             ______                   _______                          _______                  
        -----'   ___)              ---'   ____)_____                ---'   ____)____
                (_____)                       _______)                        ______)
        ROCK     (____)            PAPER     __________)           SCISSORS _________)
                 (___)                      _________)                    (____)
        ------.__(__)               ---.___________)               ---.__(___)                                             
    ======================================================================================
                                YOUR SCORE {}  VS COMPUTER SCORE {}
    ======================================================================================
    '''.format(uscore,pcscore))
    user = int(input("Choose \n1. Rock \n2. Paper \n3. Scissor \n4. Exit \n5. Score Board\n>>>"))
    if user != 1 and user != 2 and user != 3 and user != 4 and  user != 5: 
        print("CHOOSE VALID OPTION :)")
        continue
    if user == 4:
        break
    if user == 5:
        sboard()
        continue
    pc = r.randint(1,3)
    us , pcs = result(user,pc)
    pcb.append(pcs)
    ub.append(us)
    if pcs == us :
        print("======================= DRAW =======================")
    elif pcs == 1 :
        print("======================= PC WINS =======================")
    elif us == 1 :
        print("======================= YOU WIN =======================")
    pcscore += pcs
    uscore += us


if uscore >= pcscore:
        print(youwin)
else:
    print(pcwin)



    

