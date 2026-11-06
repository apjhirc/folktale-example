import time,sys,os,random
from shutil import get_terminal_size
from random import randint
health = 10
dragon_hp = 10
round = 1
chosen = None

questions = [
    {'q': 'Who built the Anping Fort?', 'a1': 'Tsai Ing-wen', 'a2': 'Zheng Chenggong', 'a3': 'Confucius', 'a4': 'Dutch East India Company (VOC)', 'ans': 'a4'},
    {'q': 'What was the original name of Anping Fort?', 'a1': 'Fort Zeelandia', 'a2': 'Fort Provintia', 'a3': 'Fort San Domingo', 'a4': 'Fort Santiago', 'ans': 'a1'},
    {'q': 'In which year did the Dutch arrive in Anping?', 'a1': '1600', 'a2': '1624', 'a3': '1662', 'a4': '1895', 'ans': 'a2'},
    {'q': 'Who defeated the Dutch and took control of Anping in 1662?', 'a1': 'Chiang Kai-shek', 'a2': 'Sun Yat-sen', 'a3': 'Zheng Chenggong (Koxinga)', 'a4': 'Confucius', 'ans': 'a3'},
    {'q': 'Which city is Anping District part of?', 'a1': 'Taipei', 'a2': 'Kaohsiung', 'a3': 'Taichung', 'a4': 'Tainan', 'ans': 'a4'},
    {'q': 'What is Anping Old Street famous for?', 'a1': 'Traditional snacks and historic shops', 'a2': 'Snowboarding', 'a3': 'Skyscrapers', 'a4': 'Hot springs', 'ans': 'a1'},
    {'q': 'What is the Anping Tree House famous for?', 'a1': 'Its glass roof', 'a2': 'Banyan tree roots covering an old warehouse', 'a3': 'Its underground tunnels', 'a4': 'Its golden walls', 'ans': 'a2'},
    {'q': 'What was the Anping Tree House originally used as?', 'a1': 'A royal palace', 'a2': 'A school', 'a3': 'A warehouse', 'a4': 'A military hospital', 'ans': 'a3'},
    {'q': 'Which European country controlled Anping during the 17th century?', 'a1': 'France', 'a2': 'Spain', 'a3': 'Portugal', 'a4': 'Netherlands', 'ans': 'a4'},
    {'q': 'What is a famous traditional snack in Anping?', 'a1': 'Shrimp rolls', 'a2': 'Sushi', 'a3': 'Pizza', 'a4': 'Hamburgers', 'ans': 'a1'},
    {'q': 'Which seafood ingredient is especially associated with Anping?', 'a1': 'Salmon', 'a2': 'Oysters', 'a3': 'Tuna', 'a4': 'Lobster', 'ans': 'a2'},
    {'q': 'What is the Anping Old Fort also known as?', 'a1': 'Chihkan Tower', 'a2': 'Eternal Golden Castle', 'a3': 'Fort Zeelandia', 'a4': 'Fort San Domingo', 'ans': 'a3'},
    {'q': 'What is the main purpose of Anping Harbor historically?', 'a1': 'Mining gold', 'a2': 'Growing tea', 'a3': 'Manufacturing cars', 'a4': 'Maritime trade and transportation', 'ans': 'a4'},
    {'q': 'Which famous Anping landmark was built during the Qing dynasty to defend the coast?', 'a1': 'Eternal Golden Castle', 'a2': 'Taipei 101', 'a3': 'Chihkan Tower', 'a4': 'Anping Tree House', 'ans': 'a1'},
    {'q': 'What is another name for the Eternal Golden Castle?', 'a1': 'Fort Zeelandia', 'a2': 'Erkunshen Battery', 'a3': 'Fort Provintia', 'a4': 'Fort San Domingo', 'ans': 'a2'},
    {'q': 'What kind of trees cover the Anping Tree House?', 'a1': 'Pine trees', 'a2': 'Cherry trees', 'a3': 'Banyan trees', 'a4': 'Maple trees', 'ans': 'a3'},
    {'q': 'What is Anping famous for producing as a traditional preserved food?', 'a1': 'Chocolate', 'a2': 'Cheese', 'a3': 'Kimchi', 'a4': 'Preserved fruits', 'ans': 'a4'},
    {'q': 'Which Anping attraction is known for its beautiful sunset views?', 'a1': 'Yuguang Island', 'a2': 'Alishan', 'a3': 'Sun Moon Lake', 'a4': 'Taroko Gorge', 'ans': 'a1'},
    {'q': 'What is the traditional local name for the Anping area before it became known as Anping?', 'a1': 'Danshui', 'a2': 'Tayouan (Dayuan)', 'a3': 'Lukang', 'a4': 'Hengchun', 'ans': 'a2'},
    {'q': 'What is Anping especially important for in Taiwan history?', 'a1': 'It was the first place with an airport', 'a2': 'It was the tallest city', 'a3': 'It was an early center of European settlement and trade', 'a4': 'It was the first place with a railway', 'ans': 'a3'}
]




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

def blockText(text):
    width = len(text) + 12
    border = "═" * width
    blank = " " * width
    padding = " " * 6

    return (
        f"╔{border}╗\n"
        f"║{blank}║\n"
        f"║{padding}{text}{padding}║\n"
        f"║{blank}║\n"
        f"╚{border}╝"
    )

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
    global round,dragon_hp,health
    print(f"Round: {round} Health: [{getHP('p')}] DRAGON HP: [{getHP('d')}]".rjust(get_terminal_size().columns))
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
    
    chosen = randint(0,len(questions)-1)

    typingPrint("Please Choose The Best Response\n")
    print(blockText(questions[chosen]["q"]))

    print(f'Option A: {questions[chosen]["a1"]}')
    print(f'Option B: {questions[chosen]["a2"]}')
    print(f'Option C: {questions[chosen]["a3"]}')
    print(f'Option D: {questions[chosen]["a4"]}')

    ans = input('Input Your Answer Ex:A ) >> ')

    if ans == 'A':
        ans = 'a1'
    if ans == 'B':
        ans = 'a2'
    if ans == 'C':
        ans = 'a3'
    if ans == 'D':
        ans = 'a4'

    if ans == questions[chosen]["ans"]:
        round += 1
        dragon_hp -= 1
        battle()
    else:
        health -= 1
        round += 1
        battle()




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

while round < 10:
    if health != 0:
        battle()
        round += 1
    else:
        break

#end()
