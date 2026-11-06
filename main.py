import time,sys,os
from shutil import get_terminal_size

health = 10
dragon_hp = 10

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  print()


def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value


def enterToContinue():
    print("\n\n")
    print(r"""
╔══════════════════════════════════════╗
║                                      ║
║      Press enter to continue...      ║
║                                      ║
╚══════════════════════════════════════╝
""")

    input()

def clearScreen():
  os.system("clear")

def getHP(character):
    if character == 'd':
        if dragon_hp != 10:
            return ("█"*dragon_hp+' '*(10-dragon_hp))
        else:
            return ("█"*dragon_hp)
    else:
        if health != 10:
            return ("█"*health+' '*(10-health))
        else:
            return ("█"*health)




def battle():
    print(f"Health: [{getHP('p')}] DRAGON HP: [{getHP('d')}]".rjust(get_terminal_size().columns))
    print(r"""
                                               / \                 / \
                                  ____________/   \_______________/   \
                             ____/                                     \__
                        ____/       /\                    /\             \
                   ____/           /  \__________________/  \             \
                  /                /                         \             \
                 /________________/                           \_____________\
                                                __
                                         ___.--'  '--.__
                                    _.-''    _    _     ''-._
                                  .'        (o)  (o)         '.
                                 /             __              \
                                /       ___.--'  '--.__         |
                               |    _.-'     ______    '-.     /
                               | .-'      .-'      '-.    \___/
                                \|       /  /\  /\    \    |
                                 \       \_/  \/  \___/   /
                                  '.__                  _.'
                                      '---.________.---'
                                            /    \
                                           /      \__________
                                          /                  \____
                                         /                        '--.
                                        /                             \
                                       /_______________________________/

      O
     /|\                                      >>>  >>>  >>>
  ==/ | \==================================> >>>  >>>  >>>
     / \                                      >>>  >>>  >>>
    /   \
""")


clearScreen()
#typingPrint("Hello")
print(r"""
                   / \  //\
      |\___/|      /   \//  \\
      /0  0  \__  /    //  | \ \
     /     /  \/_/    //   |  \  \
     @_^_@'/   \/_   //    |   \   \
     //_^_/     \/_ //     |    \    \
  ( //) |        \///      |     \     \
( / /) _|_ /   )  //       |      \     _\
( // /) '/,_ _ _/  ( ; -.   |    _ _\.-~        .-~~~^-.
(( / / )) ,-{        _      `-.|.-~-.           .~         `.
(( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
(( /// ))      `.   {            }                   /      \  \
 (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
            ///.----..>        \             _ -~             `.  ^-`  ^-_
              ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                 /.-~

╔═════ Press enter to continue... ═════╗
║                                      ║
║         The Dragon of Anping         ║
║                                      ║
╚══════════════════════════════════════╝

""")

input()
clearScreen()

print(r'''
                 /\                 /\
                /  \____     ____/  \
               /  /     \___/     \  \
          ____/  /   /\       /\   \  \____
         /      /___/  \_____/  \___\      \
         \____       .-"""-.       ____  /
              \     /  o o  \     /
               \___|    ^    |___/
                   \  \___/  /
                    '._===_.'
                       ||\
                       || \     FIRE!!!
                       ||  \>>>>>>>>>>>>>>>
                      /  \     >>>>>>>>>>>>>>>>
                     /____\       >>>>>>>>>>>>>>>
                                   \  |  /
                                    \ | /
                                 .---\|/---.
                                /  BOOOOM!  \
                               (  *  *  *   )
                                \___   ____/
                                    \ /
             ANPING                  V
        _        _       _       _       _
       | |      | |     | |     | |     | |
    ___| |______| |_____| |_____| |_____| |___
   |   ANPING OLD FORT   |                   |
   |  []  []  []  []   |  []  []  []  []     |
   |___________________|_____________________|
      /\/\    /\/\       /\/\       /\/\
     /____\  /____\     /____\     /____\
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')


typingPrint("RLong: From now on, Anping belongs to me! Hahaha!")
time.sleep(0.5)
typingPrint("\nYou have to stop it.")
enterToContinue()

clearScreen()
typingPrint("Ryan: Hi adventurer!\nI'm Ryan. As you can see. Anping is being attacked by the evil dragon.")
time.sleep(0.1)
typingPrint("Ryan: In this game, you have to answer some questions about Anping to defeat RLong.")
time.sleep(0.1)
typingPrint("Ryan: Let's go!")

enterToContinue()
battle()
