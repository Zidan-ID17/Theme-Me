#coding utf-8
import os, sys, time, requests, shutil, subprocess

def teks(c):
    for n in c + '\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)
        
def load(duration=24, interval=0.1):
    animation_chars = "|/-\\"
    num_frames = int(duration / interval)
    for i in range(num_frames):
    	sys.stdout.write("\r{}[{}∆{}] Please Wait {}\033[0m".format(putih, hijau, putih, animation_chars[i % len(animation_chars)]))
    	sys.stdout.flush()
    	time.sleep(interval)

gelap= ' \033[38;5;240m'
merah=  '\033[91m'
hijau= '\033[92m'
kuning= '\033[93m'
biru= '\033[94m'
ungu= '\033[95m'
abu= '\033[90m'
putih= '\033[97m'
oren= '\033[38;5;208m'
pxm= '\033[97;41m'
mxp= '\033[91;47m'
pxm= '\033[97;41m'
pxa= '\033[97;100m'
bebas= '\033[0m'
        
logo = """
{}████████╗██╗  ██╗███████╗{}███╗   ███╗███████╗
{}╚══██╔══╝██║  ██║██╔════╝{}████╗ ████║██╔════╝
{}   ██║   ███████║█████╗  {}██╔████╔██║█████╗  
{}   ██║   ██╔══██║██╔══╝  {}██║╚██╔╝██║██╔══╝  
{}   ██║   ██║  ██║███████╗{}██║ ╚═╝ ██║███████╗
{}   ╚═╝   ╚═╝  ╚═╝╚══════╝{}╚═╝     ╚═╝╚══════╝
{}               .: B E T A :.

{} • {}Author: {} ZidanIDz {}
{} • {}Github: https://github.com/Zidan-ID17 
{}———————————————————————————————————————————""".format(merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, abu, kuning, putih, pxm, bebas, kuning, putih, abu)

daftar = """{}
     Some List of HTML & CSS Color Codes
┏━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ White   : #FFFFFF ┃ Light Coral    : #F08080 ┃
┃ Red     : #FF0000 ┃ Crimson        : #DC143C ┃
┃ Green   : #00FF00 ┃ Gainsboro      : #DCDCDC ┃
┃ Blue    : #0000FF ┃ Misty Rose     : #FFE4E1 ┃
┃ Yellow  : #FFFF00 ┃ Lavender Blush : #FFF0F5 ┃
┃ Magenta : #FF00FF ┃ Seashell       : #FFF5EE ┃
┃ Maroon  : #800000 ┃ Honeydew       : #F0FFF0 ┃
┃ Purple  : #800080 ┃ Mint Cream     : #F5FFFA ┃
┃ Indigo  : #4B0082 ┃ Brown          : #A52A2A ┃
┃ Gold    : #FFD700 ┃ Old Lace       : #FDF5E6 ┃
┗━━━━━━━━━┻━━━━━━━━━┻━━━━━━━━━━━━━━━━┻━━━━━━━━━┛
 """.format(abu)

def tanya():
	time.sleep(2.5)
	entah = input(" \n{} Want to Try Again ? {}(Y/N) > ".format(putih, kuning))
	if entah.lower() == "Y"or entah.lower() == "y":
		pintu()
	elif entah.lower() == "N" or entah.lower() == "n":
		time.sleep(2.5)
		print("\n{} Bye Bye 👋\n".format(putih))
		sys.exit()
	else:
		time.sleep(2.5)
		print("\n{}  Bye Bye 👋\n".format(putih))
		sys.exit()
		
def subscribe():
	time.sleep(2.5)
	os.system('xdg-open https://www.youtube.com/@ZeyShyy.')
	os.system("clear")
	print(logo)
	time.sleep(2.5)
	ini = input("\n\n{}Press Enter to Return {}> ".format(putih,kuning))

def selesai():
	os.system("clear")
	print(logo)
	print("\n\n{}[{}✓{}] Successfully Changed Termux Appearance \n[{}~{}] Open a New Session to See Changes".format(putih, hijau, putih, hijau, putih))
	print("\n\n{}[{}*{}] If You Want to Exit Press CTRL + Z".format(abu, kuning, abu))
	ini = input("\n{}Press Enter to Return {}> ".format(putih,kuning))
	halaman1()
		
def pintu():
    time.sleep(2.5)
    os.system('clear')
    teks(logo)
    print("\n{} For Tokens, you can check YouTube Zeyshyy {}".format(pxa, bebas))
    kode = input("{}Enter Token {}>{} ".format(putih, hijau, putih))
    if kode.lower() == "oh37dvla2gd85v0bt1":
    	time.sleep(2.5)
    	print("\n{} Login Successfully [{}✓{}]".format(putih, hijau, putih))
    	time.sleep(2.5)
    	halaman1()
    else:
    	time.sleep(2.5)
    	print("\n{} Login Failed [{}X{}]".format(putih, merah, putih))
    	tanya()
    
                    
page1 = """
       {}        [ {}PAGE {}1{}/{}2{} ] 
╔════════════—•[{} THEME-ME {}{}]•—═════════════•
╠═══•[{}01{}]{} Infernal Reaper {}
╠═══════════════════════•[{}02{}] {}Team Liquid {}
╠═══•[{}03{}]{} Todak   {}
╠═══════════════════════•[{}04{}] {}Wings Gaming  {}
╠═══•[{}05{}] {}Blacklist{}
╠═══════════════════════•[{}06{}] {}Onic  {}
╠═══•[{}07{}] {}Fnatic {}
╠═══════════════════════•[{}08{}] {}Faze Clan {}
╠═══•[{}09{}] {}MegaStars {}
╠═══════════════════════•[{}10{}] {}Ninjas in Pyjamas{}
║———————————————————————————————————————————
╠═══•[{}30{}] {}See All Theme Examples {}Page 1{}
╠═══•[{}40{}] {}Original Theme {}
╠═══•[{}50{}] {}Next Page {}
╠═══•[{}99{}] {}Subscribe YouTube Channel {} ZeyShyy {} {}
╚═══•[{}00{}] {}Exit Program 
""".format(merah, putih, kuning, putih, kuning, merah, pxa, bebas, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih,  merah, putih, merah, putih,  merah, putih, merah, putih, merah, putih, merah, putih, merah,putih, merah, putih, kuning, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih,pxm, bebas,  merah, oren, merah, putih, )                      

def halaman1():
	time.sleep(2.5)
	os.system('clear')
	teks(logo)
	print(page1)
	pilih = input("{}Enter Choice {}>{} ".format(putih, hijau, putih))
	if pilih.lower() == "1" or pilih.lower() == "01":
		pilih1()
		load()
		selesai()
	elif pilih.lower() == "2" or pilih.lower() == "02":
		pilih2()
		load()
		selesai()
	elif pilih.lower() == "3" or pilih.lower() == "03":
		pilih3()
		load()
		selesai()
	elif pilih.lower() == "4" or pilih.lower() == "04":
		pilih4()
		load()
		selesai()
	elif pilih.lower() == "5" or pilih.lower() == "05":
		pilih5()
		load()
		selesai()
	elif pilih.lower() == "6" or pilih.lower() == "06":
		pilih6()
		load()
		selesai()
	elif pilih.lower() == "7" or pilih.lower() == "07":
		pilih7()
		load()
		selesai()
	elif pilih.lower() == "8" or pilih.lower() == "08":
		pilih8()
		load()
		selesai()
	elif pilih.lower() == "9" or pilih.lower() == "09":
		pilih9()
		load()
		selesai()
	elif pilih.lower() == "10":
		pilih10()
		load()
		selesai()
	elif pilih.lower() == "30":
		time.sleep(2.5)
		os.system("clear")
		print(logo1+logo2+logo3+logo4+logo5+logo6+logo7+logo8+logo9+logo10)
		ini = input("\n{}Press Enter to Return {}> ".format(putih,kuning))
		halaman1()
	elif pilih.lower() == "40":
		time.sleep(2.5)
		semula()
		load()
		selesai()
	elif pilih.lower() == "50":
		halaman2()
	elif pilih.lower() == "99":
		subscribe()
		halaman1()
	elif pilih.lower() == "00" or pilih.lower() == "0":
		time.sleep(2.5)
		print("\n{} Bye Bye 👋\n".format(putih))
		sys.exit()
	else:
		time.sleep(0.3)
		print("{}".format(kuning))
		print(" "+pilih+"{} is not Available in the Options [{}!{}]".format( putih, merah, putih))
		time.sleep(2.5)
		halaman1()
	
logo1 = """\n  \033[97;41m Infernal Reaper \033[0m
\033[91m                  ...:::::::::...
              ..:::\033[97maad8888888baa\033[91m:::..
           .::::\033[97md\033[91m:?\033[97m88888888888\033[91m?::\033[97m8b\033[91m::::.
         .:::\033[97md8888\033[91m:?\033[97m88888888\033[91m??\033[97ma888888b\033[91m:::.
       .:::\033[97md8888888a8888888aa8888888888b\033[91m:::.
      ::::\033[97mdP\033[91m::::::::\033[97m88888888888\033[91m::::::::\033[97mYb\033[91m::::
     ::::\033[97mdP\033[91m:::::::::\033[97mY888888888P\033[91m:::::::::\033[97mYb\033[91m::::
    ::::\033[97md8\033[91m:::::::::::\033[97mY8888888P\033[91m:::::::::::\033[97m8b\033[91m::::
   .::::\033[97m88\033[91m::::::::::::\033[97mY88888P\033[91m::::::::::::\033[97m88\033[91m::::.
   :::::\033[97mY8baaaaaaaaaa88P\033[91m:\033[97mT\033[91m:\033[97mY88aaaaaaaaaad8P\033[91m:::::
   :::::::\033[97mY88888888888P\033[91m::\033[97m|\033[91m::\033[97mY88888888888P\033[91m:::::::
   ::::::::::::::::\033[97m888\033[91m:::\033[97m|\033[91m:::\033[97m888\033[91m::::::::::::::::
   `:::::::::::::::\033[97m8888888888888b\033[91m::::::::::::::'
    :::::::::::::::\033[97m88888888888888\033[91m::::::::::::::
     :::::::::::::\033[97md88888888888888\033[91m:::::::::::::
      ::::::::::::\033[97m88\033[91m::\033[97m88\033[91m::\033[97m88\033[91m:::\033[97m88\033[91m::::::::::::
       `::::::::::\033[97m88\033[91m::\033[97m88\033[91m::\033[97m88\033[91m:::\033[97m88\033[91m::::::::::'
         `::::::::\033[97m88\033[91m::\033[97m88\033[91m::\033[97mP\033[91m::::\033[97m88\033[91m::::::::'
           `::::::\033[97m88\033[91m::\033[97m88\033[91m:::::::\033[97m88\033[91m::::::'
              ``:::::::::::::::::::''
                   ``:::::::::''
""" 
 
logo2 = """\n  \033[30;47m Team Liquid \033[0m
\033[90m                    ..:^^^^^^::.                    
              .::^:::^::...!~^^:^^^::.              
        .:::::^:::\033[37m7YPB?\033[90m...~\033[37m@@&BPY7!\033[90m^^^^^^::..       
    ^^^^^^~\033[37m!?J:\033[90m...\033[37mJ@@@#\033[90m:..\033[37m?@@@P!B@@&BPY?!\033[90m~^^:^^^.   
   .!....\033[37m7&@@@B!\033[90m...\033[37m?@@@Y\033[90m..\033[37m!&5\033[90m~. \033[37m5@@@@@@@@&#G5\033[90m~.!:   
   .!.....~\033[37m5&@@@5\033[90m^..!\033[37m&@G\033[90m^.:^..:\033[37mY@@@@@@@@@@@@@\033[90mJ !:   
   .!.~!:.  ^\033[37mJB@@&Y\033[90m:.^^.......:!\033[37mYB@@@@@@@@@@@\033[90mJ !:   
   .!.?\033[37m@#P?\033[90m~. .~\033[37mYBY:\033[90m..............^\033[37mJG&@@@@@@@\033[90mJ !:   
   .!.7\033[37m@@@@@#PJ\033[90m~.................\033[37m!!\033[90m..\033[37mP@@@@@@@\033[90mJ !:   
   .!.:^\033[37m!?YPG##7.\033[90m................\033[37m^7^\033[90m.\033[37m!&@@@@@@\033[90mJ !:   
   .!.::.....::............\033[37m^:\033[90m.........\033[37m!&@@@@@\033[90m?.!:   
   .!.!\033[37m&#####7\033[90m.............\033[37m?? \033[90m.........~\033[37m#@@@@\033[90m?.!.   
    !.~\033[37m&#BGPY\033[90m:.............\033[37m7@J\033[90m~:........^\033[37mB@@@\033[90m!.!.   
    !:.:.. .................\033[37mP@@&BJ\033[90m....:!::\033[37mB@&\033[90m^.!    
    ~^.:\033[37m!?5BP\033[90m................\033[37m7P&@@Y\033[90m.^7~^^\033[37mY&@G\033[90m.^~    
    .7.^\033[37m&@@@5\033[90m..................^\033[37m5@@Y7P@B#@@@\033[90m!.!.    
     ^~.\033[37m7G?\033[90m^.....................\033[37m!G@@@@@@@@?\033[90m.~^     
      ^~....\033[37m^?\033[90m.....................\033[37m?#@@@@B!\033[90m.~^      
       :~^\033[37m.:5@7\033[90m.....................:\033[37mY&G7\033[90m::~:       
         :~^\033[37m:^!\033[90m.......................\033[37m::\033[90m:^:         
           .:^^^:..................:^^^:.           
               :^^^^::........::^^^:.               
                   .:^^^^::^^^^:.                   
                        .::.                        
"""

logo3 = """\n  \033[30;47m Todak \033[0m
\033[37m            YJ:                            
            ?@&J.                          
            !@@@#7                   .:^:  
            !@@@@@Y             .^7JYJ~:   
            7@@@@@@P.^~^.  :~?5B#BY!.      
            J@@@@@@@&@@@#PB&@@#J~!~        
            G@@@@@@@@@@@@@@@@5^.J@@#Y^     
          .5@@@@@@@@@@@@@@@P~7P&@@@@@@5:   
         :B@@@@@@@@@@@@@B5! :YB@@@@@@@@&7  
       :!#@@@@@@@@@@#&@G       ^Y&@@@@@@@? 
     ~5G@@@@@@@@@&&#:Y@B         ^B@@@@@@@~
   :7?^:#@@@@@@@P^#! .B#.         :&@@@@@@G
   ^.  ^@@@@@@@J :G   :G:          5@@@@@@@
       ^@@@@@@7  .!    ::          5@@@@@@@
        B@@@@Y.^                  ^&@@@@@@G
        7@@@@:7@!          .     ^#@@@@@@@~
         Y@@@~~@@P^   :!JYJ!.  ^5@@@@@@@@7 
          J@@#^!J7!?P##P?!~~7YB@@@@@@@@&!  
           ^P@@P5#@@B?~?G&@@@@@@@@@@@&5:   
             ~Y&@@@?^5&@@@@@@@@@@@@BJ:     
               ^@@&.?@@@@@@@@@&#P?^        
                J@@Y !7????7!~:.           
                 P@@!                      
                 .P@@!                     
                   J@@!                    
                    ~B@?                   
                      7B5.                 
                        7?.
"""

logo4= """\n  \033[30;47m Wings Gaming \033[0m
\033[97m?!:                                              :!?
~YJ?!^.                                      .:!?JY!
 ^?YY5YJ7~.                ..            .^!?YYYYJ^ 
   ~?5PGBBBPY7^.       ^YPGG57:     .^7JPGBBGG5J~.  
    .:~?5B#@@@@#57.   !BBBBB5.   .!5B@@@@&BPJ!^.    
    ^?YYJJJYP&@@@@B7  ?BGPPGP.  !B@@@@&G5J?JJYJ^    
      :7YPGGB&&&&###? .Y57?5!  7###&&@&BBGPY7^      
         :7???J##BGGP. ..  .  .5GGB##Y???7:         
          :!YPB###BGP. .^!!:. .5GB###BGY7:          
              .^!?JY57J555555J7YYY?!^:              
                   ^G#BGGPPGGB#G:                   
                  !#@&#BBGGBB#&@#!                  
                 ~@@#!5&####&J?&@@!                 
                 .JP: B@&PP@@5 ~GJ:                 
                     ^&@&:^&@#.                     
                      ~G5  5P^                      
"""

logo5= """\n  \033[30;47m Blacklist \033[0m
\033[97m                ^Y!                                 
             !G&@@@#~                               
             @@@@@@@@#~                             
             &@@@@@@@@@#~                           
             &@@@@@@@@@@@#~                         
             &@@@&:Y@@@@@@@&!      ^Y&#             
             &@@@&  .5@@@@@@B^ :J#@@@@&             
             &@@@&    .Y#Y~~?G@@@@@@@@#             
             &@@@&     .7P&@@@@@@@@&Y^              
             &@@@& .~P&@@@@@@@@&P~. .?Y             
             &@@@@&@@@@@@@@@G7. .!G&@@&             
             &@@@@@@@@@@B?: .~5&@@@@@@#             
             &@@@@@@#Y^  ^Y#@@@@@@@@@@#             
             @@@&5~. :?B@@@@@@@@@#@@@@#             
             Y!. .!G&@@@@@@@@#Y^ .@@@@#             
             .~P&@@@@@@@@&P~.    .@@@@#             
             &@@@@@@@&G7.        .@@@@#             
             &@@@@B?:            .@@@@#             
             &#J:                .@@@@#             
                                 .@@@@#             
                                 .@@@@#             
                                 .@@@@&             
                                 .@@&P~             
                                  ?:                
"""

logo6= """\n  \033[30;43m Onic \033[0m
\033[93m
                     :^^^^^^:..  ..                 
                     ^JPBBGGGGP5JJP5?~.             
                .:^~!77JGBBBPY5GBBBBBBGJ^           
              ~YPBBBBP5YYYYYY?:.~JGBGGGBB5~         
               :~?5GBP?^.    ..   .?GGYY5PGP55555PJ.
        .^!?Y5PGPP55YYJJ7:     .7Y55GBGGPPPBBBBBBY. 
    .^7YPGBBPJ7~^:.        .^!?YPBBBBGBBBBBBGPP5!   
   .7YPGBBBB5?~:         ^?PBBBBBBGGGGGGBBBB57:     
       .:~!J5BBBPY!.    :~?PBBGGGGGGGGGBBY7^.       
      .:!?Y5PPY7~:.  :75GBBBGGGGGGGGGGGBJ           
   :7YPBBBGJ~.       :7PBBGGGGGGGGGGGGB5            
 ^JPGGGGGGGP55Y!   ^JPBBGGGGGGGGGGGGGBP.            
 ......:7PBBGJ: :?PBBBBBGGGGGGGGGGGGBG:             
      .7JJJ7. ~5BBP55PGBBBGGGBBBBGGBG~              
            !PB5!^~7. .~JGBBBBYJYBBB!               
          JGBB? ^PBJ     ~GBBJ  JBB?                
          ^~^^  :~~:      ^~~.  ^^^
"""

logo7 = """\n  \033[97;48;5;202m Fnatic \033[0m
\033[38;5;208m                         :~~:                            
                         ~77~                            
             ..::::^^^^^::...:^^^^^^:::..                
       .:^~~!!!!!!!7!!!!!!..!!!!!!!!!!!!!!~~^:.          
     .~!777!!!!!!!!~!!!!!!:.!!!!!!~!!!!!!!777!!!:        
     :!!~^^::....   ^!!!!!. !!!!!^   ....::^^~!!:        
      ..           .!!!!!^  ^!!!!!.           ..         
                   ~!!!!!.  .!!!!!~                      
                 .~!!!!!: .. :!!!!!^                     
            .:^~!!!!!!!^ :!!: :!!!!!^                    
           ^!!~~!!!!!!^  ^!!~  :!!!!!~.                  
           .  .~!!!!!:   ~!!~   :!!!!!~:                 
         ::.:^!!!!!~.    ~!!~    .~!!!!!^:.::            
        :!!!!!!!!!:      ~!!~      :~!!!!!!!7^           
        ^!!!!!!!:        ~!!~        :!!!!!!!~           
        :!!!!~:          ~!!~          :~!!!!^           
         ~!^:            :!!^            :^!~.           
"""

logo8= """\n  \033[97;41m Faze Clan \033[0m
\033[91m
  ..................................................     
  ^77777777777777777777777777777777777777777777777!:     
   .!???????????????????????????????????????????!:       
     .^::::::::::::::::7??????!^^^^^^^^^^^^^^^^:         
                       !??????^                          
          ^~~~~~~~~~~~~7??????^                          
           ^7?????????????????^                          
             ^7???????????????^                          
               ........!??????~.................         
                       ~???????7?????????????7~.         
                       ~????????????????????~.           
                       ~??????????77777777~.             
                       ~???????7~.                       
                       ~?????!:                          
                       ~??7~.                            
                       ~!:                               
"""

logo9 ="""\n  \033[97;41m MegaStars \033[0m
\033[31m
      ~.                                  .~        
     .&&G?:                            :?G&&.       
     .#&&&&BY~.                    .~YB&&&&#.       
     .#&&######5!.              :7P#######&#.       
     .####G?G#####G?^       .^JG#####G?G##&#.       
     .####Y  .!5B####BY~..!5B####B5!.  Y####.       
     .####5      ^JG####BB###BPJ^.     Y####.       
     .####5  ^5!.   :75BBBB##G!.       Y####.       
     .####5  ~###P?:   .~YGBB##BP7:    Y####.       
     .####Y  :PB####GY~.   :?PB####B^  Y####.       
     .####G~.  .~YB####B57:   .!5B##!  Y####.       
      5######P7.   :?P#####GJ^    ^Y^  Y####.       
        ^JG#####GJ^   .!5B####B5!.     ?##&#.       
      7:   .7P#####B5!.   ^JG#####G?^   .~5B.       
     .&&BJ^   .~YB#####G?:   :7P#####B5~.           
     .#&&&&#5!.   :?P######5^   .~5##&&&&GJ.        
      .~5B&&&&#G?:   .~5BB5!.   :?G#&&&&B5!.        
          :?G&&&&&B5~.      .~5B&&&&#G?:            
             .!5#&&&&#P7.:7P#&&&&#5!.               
                .^JG##########GJ^                   
                    .!5B##B5!.                      
                       .~~.                         
"""

logo10 = """\n  \033[30;42m Ninjas in Pyjamas \033[0m
\033[38;5;120m        .!~.                                             
         :5BPJ!^.   ^?YPGGGGGGPYJ!^.         .~:         
           7B##BG5?~^^!?JJ??JY5PB##B5?:   .~JGJ.         
            ^P######BPY7^.      .^!Y57::!YG##J           
           ~^.JP?~~!?5G##BPJ!^.       JB##B#J            
          ?B#!       ::^!JPB#BG5?~:   .PBB#J             
         J##5:    ~?P#BY^ ^BBB5GB#BP? .P##J :            
        !#BP.   .Y##GJ~:^7G#B!  ?B#B^.5BY! ^G!           
        P##~   .YP?^ :?PB#BY~ .7B#G^ ~~:  :G#5           
       :BBG.   .::. ^B#BB#B5?5B#B5^ .^?7  :BBB.          
       :BBB:  ^75J.:Y?^:^!JPBBY!:.~JG#5.  :BBB.          
        P#G: YB#5. .:~JG5?: ..:!YB##P?.   !#B5           
        !B^ Y##5.:75G#B57^.^?PB#B5!^.    .P##~           
         : Y##P. ?GB##BY7^.^7JJ~::7!    :5##?            
          J#BBP.   :~?5G##B5?~^?5B5.    7#B7             
         J#B##BJ       .^!JPB####B!^~7PJ ^~              
        J##GY7::75Y7^.      .^7JPB######P:               
      .JGJ~.   :?5B##BP5JJ??JJ?!^^~?5GB##B7              
      :~.         .^!JYPGGGGGGPY?^   .^!JPBY:            
                          ..              :~!.           
"""

def pilih1():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue 
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
[91m                  ...:::::::::...
              ..:::[97maad8888888baa[91m:::..
           .::::[97md[91m:?[97m88888888888[91m?::[97m8b[91m::::.
         .:::[97md8888[91m:?[97m88888888[91m??[97ma888888b[91m:::.
       .:::[97md8888888a8888888aa8888888888b[91m:::.
      ::::[97mdP[91m::::::::[97m88888888888[91m::::::::[97mYb[91m::::
     ::::[97mdP[91m:::::::::[97mY888888888P[91m:::::::::[97mYb[91m::::
    ::::[97md8[91m:::::::::::[97mY8888888P[91m:::::::::::[97m8b[91m::::
   .::::[97m88[91m::::::::::::[97mY88888P[91m::::::::::::[97m88[91m::::.
   :::::[97mY8baaaaaaaaaa88P[91m:[97mT[91m:[97mY88aaaaaaaaaad8P[91m:::::
   :::::::[97mY88888888888P[91m::[97m|[91m::[97mY88888888888P[91m:::::::
   ::::::::::::::::[97m888[91m:::[97m|[91m:::[97m888[91m::::::::::::::::
   `:::::::::::::::[97m8888888888888b[91m::::::::::::::'
    :::::::::::::::[97m88888888888888[91m::::::::::::::
     :::::::::::::[97md88888888888888[91m:::::::::::::
      ::::::::::::[97m88[91m::[97m88[91m::[97m88[91m:::[97m88[91m::::::::::::
       `::::::::::[97m88[91m::[97m88[91m::[97m88[91m:::[97m88[91m::::::::::'
         `::::::::[97m88[91m::[97m88[91m::[97mP[91m::::[97m88[91m::::::::'
           `::::::[97m88[91m::[97m88[91m:::::::[97m88[91m::::::'
              ``:::::::::::::::::::''
                   ``:::::::::''     '''
run(logo)
print('''             \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''           \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))
				
def pilih2():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue 
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[90m                    ..:^^^^^^::.                    
              .::^:::^::...!~^^:^^^::.              
        .:::::^:::\033[37m7YPB?\033[90m...~\033[37m@@&BPY7!\033[90m^^^^^^::..       
    ^^^^^^~\033[37m!?J:\033[90m...\033[37mJ@@@#\033[90m:..\033[37m?@@@P!B@@&BPY?!\033[90m~^^:^^^.   
   .!....\033[37m7&@@@B!\033[90m...\033[37m?@@@Y\033[90m..\033[37m!&5\033[90m~. \033[37m5@@@@@@@@&#G5\033[90m~.!:   
   .!.....~\033[37m5&@@@5\033[90m^..!\033[37m&@G\033[90m^.:^..:\033[37mY@@@@@@@@@@@@@\033[90mJ !:   
   .!.~!:.  ^\033[37mJB@@&Y\033[90m:.^^.......:!\033[37mYB@@@@@@@@@@@\033[90mJ !:   
   .!.?\033[37m@#P?\033[90m~. .~\033[37mYBY:\033[90m..............^\033[37mJG&@@@@@@@\033[90mJ !:   
   .!.7\033[37m@@@@@#PJ\033[90m~.................\033[37m!!\033[90m..\033[37mP@@@@@@@\033[90mJ !:   
   .!.:^\033[37m!?YPG##7.\033[90m................\033[37m^7^\033[90m.\033[37m!&@@@@@@\033[90mJ !:   
   .!.::.....::............\033[37m^:\033[90m.........\033[37m!&@@@@@\033[90m?.!:   
   .!.!\033[37m&#####7\033[90m.............\033[37m?? \033[90m.........~\033[37m#@@@@\033[90m?.!.   
    !.~\033[37m&#BGPY\033[90m:.............\033[37m7@J\033[90m~:........^\033[37mB@@@\033[90m!.!.   
    !:.:.. .................\033[37mP@@&BJ\033[90m....:!::\033[37mB@&\033[90m^.!    
    ~^.:\033[37m!?5BP\033[90m................\033[37m7P&@@Y\033[90m.^7~^^\033[37mY&@G\033[90m.^~    
    .7.^\033[37m&@@@5\033[90m..................^\033[37m5@@Y7P@B#@@@\033[90m!.!.    
     ^~.\033[37m7G?\033[90m^.....................\033[37m!G@@@@@@@@?\033[90m.~^     
      ^~....\033[37m^?\033[90m.....................\033[37m?#@@@@B!\033[90m.~^      
       :~^\033[37m.:5@7\033[90m.....................:\033[37mY&G7\033[90m::~:       
         :~^\033[37m:^!\033[90m.......................\033[37m::\033[90m:^:         
           .:^^^:..................:^^^:.           
               :^^^^::........::^^^:.               
                   .:^^^^::^^^^:.                   
                        .::.                        '''
run(logo)
print('''               \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''             \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih3():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[37m            YJ:                            
            ?@&J.                          
            !@@@#7                   .:^:  
            !@@@@@Y             .^7JYJ~:   
            7@@@@@@P.^~^.  :~?5B#BY!.      
            J@@@@@@@&@@@#PB&@@#J~!~        
            G@@@@@@@@@@@@@@@@5^.J@@#Y^     
          .5@@@@@@@@@@@@@@@P~7P&@@@@@@5:   
         :B@@@@@@@@@@@@@B5! :YB@@@@@@@@&7  
       :!#@@@@@@@@@@#&@G       ^Y&@@@@@@@? 
     ~5G@@@@@@@@@&&#:Y@B         ^B@@@@@@@~
   :7?^:#@@@@@@@P^#! .B#.         :&@@@@@@G
   ^.  ^@@@@@@@J :G   :G:          5@@@@@@@
       ^@@@@@@7  .!    ::          5@@@@@@@
        B@@@@Y.^                  ^&@@@@@@G
        7@@@@:7@!          .     ^#@@@@@@@~
         Y@@@~~@@P^   :!JYJ!.  ^5@@@@@@@@7 
          J@@#^!J7!?P##P?!~~7YB@@@@@@@@&!  
           ^P@@P5#@@B?~?G&@@@@@@@@@@@&5:   
             ~Y&@@@?^5&@@@@@@@@@@@@BJ:     
               ^@@&.?@@@@@@@@@&#P?^        
                J@@Y !7????7!~:.           
                 P@@!                      
                 .P@@!                     
                   J@@!                    
                    ~B@?                   
                      7B5.                 
                        7?.  '''
run(logo)
print('''              \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih4():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[97m?!:                                              :!?
~YJ?!^.                                      .:!?JY!
 ^?YY5YJ7~.                ..            .^!?YYYYJ^ 
   ~?5PGBBBPY7^.       ^YPGG57:     .^7JPGBBGG5J~.  
    .:~?5B#@@@@#57.   !BBBBB5.   .!5B@@@@&BPJ!^.    
    ^?YYJJJYP&@@@@B7  ?BGPPGP.  !B@@@@&G5J?JJYJ^    
      :7YPGGB&&&&###? .Y57?5!  7###&&@&BBGPY7^      
         :7???J##BGGP. ..  .  .5GGB##Y???7:         
          :!YPB###BGP. .^!!:. .5GB###BGY7:          
              .^!?JY57J555555J7YYY?!^:              
                   ^G#BGGPPGGB#G:                   
                  !#@&#BBGGBB#&@#!                  
                 ~@@#!5&####&J?&@@!                 
                 .JP: B@&PP@@5 ~GJ:                 
                     ^&@&:^&@#.                     
                      ~G5  5P^             '''
run(logo)
print('''               \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''             \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih5():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[97m                ^Y!                                 
             !G&@@@#~                               
             @@@@@@@@#~                             
             &@@@@@@@@@#~                           
             &@@@@@@@@@@@#~                         
             &@@@&:Y@@@@@@@&!      ^Y&#             
             &@@@&  .5@@@@@@B^ :J#@@@@&             
             &@@@&    .Y#Y~~?G@@@@@@@@#             
             &@@@&     .7P&@@@@@@@@&Y^              
             &@@@& .~P&@@@@@@@@&P~. .?Y             
             &@@@@&@@@@@@@@@G7. .!G&@@&             
             &@@@@@@@@@@B?: .~5&@@@@@@#             
             &@@@@@@#Y^  ^Y#@@@@@@@@@@#             
             @@@&5~. :?B@@@@@@@@@#@@@@#             
             Y!. .!G&@@@@@@@@#Y^ .@@@@#             
             .~P&@@@@@@@@&P~.    .@@@@#             
             &@@@@@@@&G7.        .@@@@#             
             &@@@@B?:            .@@@@#             
             &#J:                .@@@@#             
                                 .@@@@#             
                                 .@@@@#             
                                 .@@@@&             
                                 .@@&P~             
                                  ?:           '''
run(logo)
print('''              \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih6():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[93m                     :^^^^^^:..  ..                 
                     ^JPBBGGGGP5JJP5?~.             
                .:^~!77JGBBBPY5GBBBBBBGJ^           
              ~YPBBBBP5YYYYYY?:.~JGBGGGBB5~         
               :~?5GBP?^.    ..   .?GGYY5PGP55555PJ.
        .^!?Y5PGPP55YYJJ7:     .7Y55GBGGPPPBBBBBBY. 
    .^7YPGBBPJ7~^:.        .^!?YPBBBBGBBBBBBGPP5!   
   .7YPGBBBB5?~:         ^?PBBBBBBGGGGGGBBBB57:     
       .:~!J5BBBPY!.    :~?PBBGGGGGGGGGBBY7^.       
      .:!?Y5PPY7~:.  :75GBBBGGGGGGGGGGGBJ           
   :7YPBBBGJ~.       :7PBBGGGGGGGGGGGGB5            
 ^JPGGGGGGGP55Y!   ^JPBBGGGGGGGGGGGGGBP.            
 ......:7PBBGJ: :?PBBBBBGGGGGGGGGGGGBG:             
      .7JJJ7. ~5BBP55PGBBBGGGBBBBGGBG~              
            !PB5!^~7. .~JGBBBBYJYBBB!               
          JGBB? ^PBJ     ~GBBJ  JBB?                
          ^~^^  :~~:      ^~~.  ^^^   '''
run(logo)
print('''              \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih7():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[38;5;208m                         :~~:                            
                         ~77~                            
             ..::::^^^^^::...:^^^^^^:::..                
       .:^~~!!!!!!!7!!!!!!..!!!!!!!!!!!!!!~~^:.          
     .~!777!!!!!!!!~!!!!!!:.!!!!!!~!!!!!!!777!!!:        
     :!!~^^::....   ^!!!!!. !!!!!^   ....::^^~!!:        
      ..           .!!!!!^  ^!!!!!.           ..         
                   ~!!!!!.  .!!!!!~                      
                 .~!!!!!: .. :!!!!!^                     
            .:^~!!!!!!!^ :!!: :!!!!!^                    
           ^!!~~!!!!!!^  ^!!~  :!!!!!~.                  
           .  .~!!!!!:   ~!!~   :!!!!!~:                 
         ::.:^!!!!!~.    ~!!~    .~!!!!!^:.::            
        :!!!!!!!!!:      ~!!~      :~!!!!!!!7^           
        ^!!!!!!!:        ~!!~        :!!!!!!!~           
        :!!!!~:          ~!!~          :~!!!!^           
         ~!^:            :!!^            :^!~.     '''
run(logo)
print('''               \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''             \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih8():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[91m
  ..................................................     
  ^77777777777777777777777777777777777777777777777!:     
   .!???????????????????????????????????????????!:       
     .^::::::::::::::::7??????!^^^^^^^^^^^^^^^^:         
                       !??????^                          
          ^~~~~~~~~~~~~7??????^                          
           ^7?????????????????^                          
             ^7???????????????^                          
               ........!??????~.................         
                       ~???????7?????????????7~.         
                       ~????????????????????~.           
                       ~??????????77777777~.             
                       ~???????7~.                       
                       ~?????!:                          
                       ~??7~.                            
                       ~!:           '''
run(logo)
print('''              \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))


def pilih9():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[31m
      ~.                                  .~        
     .&&G?:                            :?G&&.       
     .#&&&&BY~.                    .~YB&&&&#.       
     .#&&######5!.              :7P#######&#.       
     .####G?G#####G?^       .^JG#####G?G##&#.       
     .####Y  .!5B####BY~..!5B####B5!.  Y####.       
     .####5      ^JG####BB###BPJ^.     Y####.       
     .####5  ^5!.   :75BBBB##G!.       Y####.       
     .####5  ~###P?:   .~YGBB##BP7:    Y####.       
     .####Y  :PB####GY~.   :?PB####B^  Y####.       
     .####G~.  .~YB####B57:   .!5B##!  Y####.       
      5######P7.   :?P#####GJ^    ^Y^  Y####.       
        ^JG#####GJ^   .!5B####B5!.     ?##&#.       
      7:   .7P#####B5!.   ^JG#####G?^   .~5B.       
     .&&BJ^   .~YB#####G?:   :7P#####B5~.           
     .#&&&&#5!.   :?P######5^   .~5##&&&&GJ.        
      .~5B&&&&#G?:   .~5BB5!.   :?G#&&&&B5!.        
          :?G&&&&&B5~.      .~5B&&&&#G?:            
             .!5#&&&&#P7.:7P#&&&&#5!.               
                .^JG##########GJ^                   
                    .!5B##B5!.                      
                       .~~.         
'''
run(logo)
print('''              \033[97m Username : \033[97;41m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def pilih10():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print(daftar)
	time.sleep(0.4)
	print("{}({}*{}) {}HTML Color Code for the cursor color to be displayed ".format(putih, kuning, putih, abu))
	color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
	while not color.strip() or '"' in color or "'" in color:
		print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
		color = input("\n{}Enter Color Code {}>{} ".format(putih, hijau, putih))
		continue
	time.sleep(0.6)
	file1 = "bash.bashrc"
	isi = """#Created with the THEME-ME coded by Zidan IDz
#Subscribe YouTube Zeyshyy
#
clear
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
python $HOME/../usr/etc/theme
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\\n\[\e[97;100m\] \[\e[91m\]●\[\e[93m\]●\[\e[92m\]●\e[30m\]\w\[\e[0m\] \[\e[92m\]'
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion
echo -e '\e[4 q'
echo -ne '\033]12;"""+color+"""\007'   """ 
	with open(file1, 'w') as file:
		file.write(isi)
		print("\n{}------------------------------------------------".format(putih))
		print('{}({}*{}) {}"Username" & "Team Name" will be displayed below the theme logo'.format(putih, kuning, putih, abu))
		username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
		while not username.strip() or '"' in username or "'" in username:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			username = input("\n{}Enter Username   {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
		while not team.strip() or '"' in team or "'" in team:
			print("{}({}X{}) Input must not be empty or contain quotation marks ({}!{})".format(abu, merah, abu, merah, abu))
			team = input("\n{}Enter Team Name  {}>{} ".format(putih, hijau, putih))
			continue
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "theme"
		isi = """#Created with the THEME-ME coded by Zidan IDz 
import os, sys, time

def run(a):
    for n in a + '\\n':
        sys.stdout.write(n)
        sys.stdout.flush()
        time.sleep(0.1/100)

logo = '''
\033[32m        .!~.                                             
         :5BPJ!^.   ^?YPGGGGGGPYJ!^.         .~:         
           7B##BG5?~^^!?JJ??JY5PB##B5?:   .~JGJ.         
            ^P######BPY7^.      .^!Y57::!YG##J           
           ~^.JP?~~!?5G##BPJ!^.       JB##B#J            
          ?B#!       ::^!JPB#BG5?~:   .PBB#J             
         J##5:    ~?P#BY^ ^BBB5GB#BP? .P##J :            
        !#BP.   .Y##GJ~:^7G#B!  ?B#B^.5BY! ^G!           
        P##~   .YP?^ :?PB#BY~ .7B#G^ ~~:  :G#5           
       :BBG.   .::. ^B#BB#B5?5B#B5^ .^?7  :BBB.          
       :BBB:  ^75J.:Y?^:^!JPBBY!:.~JG#5.  :BBB.          
        P#G: YB#5. .:~JG5?: ..:!YB##P?.   !#B5           
        !B^ Y##5.:75G#B57^.^?PB#B5!^.    .P##~           
         : Y##P. ?GB##BY7^.^7JJ~::7!    :5##?            
          J#BBP.   :~?5G##B5?~^?5B5.    7#B7             
         J#B##BJ       .^!JPB####B!^~7PJ ^~              
        J##GY7::75Y7^.      .^7JPB######P:               
      .JGJ~.   :?5B##BP5JJ??JJ?!^^~?5GB##B7              
      :~.         .^!JYPGGGGGGPY?^   .^!JPBY:            
                          ..              :~!.   '''
run(logo)
print('''              \033[97m Username : \033[30;42m """+username+""" \033[0m''')
print('''            \033[97m Team :\033[90m """+team+""" \033[0m''') """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "theme"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'theme')
			shutil.move(source_path, destination_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			os.remove(file_path)
			file_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			with open(file_path, 'w') as new_file:
				new_file.write("  ")
				print("\n{}[{}!{}] Currently Changing the Appearance of Termux ".format(putih, hijau, putih))

def semula():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	file1 = "bash.bashrc"
	isi = """#Created with the motd-ME coded by Zidan IDz
# Command history tweaks:
# - Append history instead of overwriting
#   when shell exits.
# - When using history substitution, do not
#   exec command immediately.
# - Do not save to history commands starting
#   with space.
# - Do not save duplicated commands.
shopt -s histappend
shopt -s histverify
export HISTCONTROL=ignoreboth

# Default command line prompt.
PROMPT_DIRTRIM=2
PS1='\[\e[0;32m\]\w\[\e[0m\] \[\e[0;97m\]\$\[\e[0m\] '
# Handles nonexistent commands.
# If user has entered command which invokes non-available
# utility, command-not-found will give a package suggestions.
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
    command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found '$1'
    }
fi

[ -r /data/data/com.termux/files/usr/share/bash-completion/bash_completion ] && . /data/data/com.termux/files/usr/share/bash-completion/bash_completion  """ 
	with open(file1, 'w') as file:
		file.write(isi)
		time.sleep(0.6)
		source_path = "bash.bashrc"
		destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'bash.bashrc')
		shutil.move(source_path, destination_path)
		file2 = "motd"
		isi = """ Welcome to Termux!

 Docs:       https://termux.dev/docs
 Donate:     https://termux.dev/donate
 Community:  https://termux.dev/community

 Working with packages:

  - Search:  pkg search <query>
  - Install: pkg install <package>
  - Upgrade: pkg upgrade

 Subscribing to additional repositories:

  - Root:    pkg install root-repo
  - X11:     pkg install x11-repo

 For fixing any repository issues,
 try 'termux-change-repo' command.

 Report issues at https://termux.dev/issues

 """
		with open (file2, 'w') as file:
			file.write(isi)
			source_path = "motd"
			destination_path = os.path.join(os.environ['HOME'], '..', 'usr', 'etc', 'motd')
			shutil.move(source_path, destination_path)
			print("\n{}[{}!{}] Currently Changing Appearance to Original ".format(putih, hijau, putih))
				
page2 = """
       {}        [ {}PAGE {}2{}/{}2{} ] 
╔════════════—•[{} THEME-ME {}{}]•—═════════════•
╠═══•[{}11{}]{} -- {}
╠═══════════════════════•[{}12{}] {}-- {}
╠═══•[{}13{}]{} --   {}
╠═══════════════════════•[{}14{}] {}--  {}
╠═══•[{}15{}] {}--{}
╠═══════════════════════•[{}16{}] {}--  {}
╠═══•[{}17{}] {}-- {}
╠═══════════════════════•[{}18{}] {}-- {}
╠═══•[{}19{}] {}-- {}
╠═══════════════════════•[{}20{}] {}--{}
║———————————————————————————————————————————
╠═══•[{}30{}] {}See All Theme Examples {}Page 2{}
╠═══•[{}40{}] {}Original Theme {}
╠═══•[{}50{}] {}Previous Page{}
╠═══•[{}99{}] {}Subscribe YouTube Channel {} ZeyShyy {} {}
╚═══•[{}00{}] {}Exit Program 
""".format(merah, putih, kuning, putih, kuning, merah, pxa, bebas, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih,  merah, putih, merah, putih,  merah, putih, merah, putih, merah, putih, merah, putih, merah,putih, merah, putih, kuning, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih, merah, putih,pxm, bebas,  merah, oren, merah, putih, )                      

def halaman2():
	time.sleep(2.5)
	os.system("clear")
	teks(logo)
	print(page2)
	pilih = input("{}Enter Choice {}>{} ".format(putih, hijau, putih))
	if pilih.lower() == "11":
		maaf()
	elif pilih.lower() == "12":
		maaf()
	elif pilih.lower() == "13":
		maaf()
	elif pilih.lower() == "14":
		maaf()
	elif pilih.lower() == "15":
		maaf()
	elif pilih.lower() == "16":
		maaf()
	elif pilih.lower() == "17":
		maaf()
	elif pilih.lower() == "18":
		maaf()
	elif pilih.lower() == "20":
		maaf()
	elif pilih.lower() == "30":
		maaf()
	elif pilih.lower() == "40":
		time.sleep(2.5)
		semula()
		load()
		selesai()
	elif pilih.lower() == "50":
		halaman1()
	elif pilih.lower() == "99":
		subscribe()
		halaman2()
	elif pilih.lower() == "0" or pilih.lower() == "00":
		time.sleep(2.5)
		print("\n{} Bye Bye 👋\n".format(putih))
		sys.exit()
	else:
		time.sleep(0.3)
		print("{}".format(kuning))
		print(" "+pilih+"{} is not Available in the Options [{}!{}]".format( putih, merah, putih))
		time.sleep(2.5)
		halaman2()

def maaf():
	time.sleep(2.5)
	os.system("clear")
	print(logo)
	print("\n{}[{}*{}] Sorry, Theme has not been added ".format(putih, kuning, putih))
	print("{}[{}!{}] Theme will be added when the video reaches 500 likes".format(putih, kuning, putih))
	print("{}[{}∆{}] You Can Also Provide Theme Suggestions in Video Comments ".format(putih, kuning, putih))
	print("\n{}[{}*{}] Press 1 to open Video ".format(abu, putih, abu))
	ini = input("\n{}Press Enter to Return {}> ".format(putih,kuning))
	if ini.lower() == "1" or ini.lower() == "01":
		os.system('xdg-open https://www.youtube.com/@ZeyShyy.')
		time.sleep(0.8)
		os.system("clear")
		print(logo)
		time.sleep(2.5)
		ini = input("\n\n{}Press Enter to Return {}> ".format(putih,kuning))
		halaman2()
	else:
		time.sleep(2.5)
		halaman2()
		

pintu()