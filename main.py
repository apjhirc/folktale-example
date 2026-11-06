import time,sys,os
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
