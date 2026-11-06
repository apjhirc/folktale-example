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
