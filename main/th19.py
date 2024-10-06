# -*- coding: utf-8 -*-
# Theme-Me/main/th19.py
# Credit by Zidan IDz
import os, sys, time, shutil
from support.echo import theme_me, abu, pxh, netral, putih, kuning, hijau, merah


def th19():
    os.system("clear")
    print(theme_me)
    print(f"         {abu}THEME-ME {pxh} 496 Gaming {netral}")
    print(f"{putih}({kuning}*{putih}) {abu}'username' and 'team name' will be displayed below the logo")
    username = input(f"\n{putih}enter username   {hijau}>{putih} ")
    while not username.strip() or '"' in username or "'" in username:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!!")
        username = input(f"\n{putih}enter username   {hijau}>{putih} ")
        continue
    time.sleep(0.5)
    team = input(f"\n{putih}enter team name  {hijau}>{putih}")
    while not team.strip() or '"' in team or "'" in team:
        print(f"{abu}({merah}X{abu}) must not be blank or contain quotation marks {merah}!!")
        team = input(f"\n{putih}enter team name  {hijau}>{putih}")
        continue
    file = "theme.py"
    fill = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[38;5;214m                      :?57:                   
                 .^!?YPGGGPY?~                
   .^^^^^~~!7?JY5PGGGGGPPGGGJ^:Y5YJ?7!!~~^:.  
   ?GGGGGGGGGGGGGGGPPPGGGP?~!JPGG55YYJ?!~:::~^
   ?GGGGGPPPPPPPPPPPGGGY~.^YGPY?^.  ..::^?YPG?
   JGPPPPPPPPPPPPPGGGJ^ .:::.. .:^^~~~~!YGGGGJ
   JGPPPPPPPPPPGGGP5~                .~?PGPPGJ
   ^PGPPPPPPPGG5?~:.    :~!.       .!J5PGPPPGJ
    !GGPPPPPGP!         ^~:         :!5GGPPPG?
     !PGGPPPG! ^!77!~.                 !5GPPG7
      ^YGGGGGY5GGGGGGP!                .75GGP^
        ^?5PGGGGPPPPPGG!                ~PGGY 
           ^7YPGGGPPPPGP.                JGG~ 
     ^^.     :~7YPGPPPGG:                ^GJ  
     :PPYJJ?JJY5PPPPPPG5.                75.  
      ^PGGGGGGGGGPPGGGP^                .5^   
       ^PGGGPPPPPPPP57.          ^      :^    
        :YPGGGGGGPY?~            J^           
          :^~~!!!~:.            .P7           
                          ..    7GJ7^         
                       .  77   ^GGJ~          
                 :^~!7YP^^GJ  ^5J^            
                 :!YPGGGYPG! .~:              
                    .~?YPY7  '''
run(logo)
print('''              \033[97m Username : \033[30;48;5;208m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''')  """
    with open(file, "w") as y:
        y.write(fill)
    of = "theme.py"
    into = os.path.join(os.environ["HOME"], "..", "usr", "etc", "theme.py")
    und = os.path.join(os.environ["HOME"], "..", "usr", "etc", "motd")
    if os.path.exists(into):
        os.remove(into)
    elif os.path.exists(und):
        os.remove(und)

    while True:
        try:
            shutil.move(of, into)
            break
        except Exception as e:
            with open(file, "w") as y:
                y.write(fill)
            time.sleep(1)
