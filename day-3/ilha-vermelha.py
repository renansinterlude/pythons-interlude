print('''
        ,,;;;;;,,
      ,;;:::::::;;,
     ,;;::' , ':::;,
     ;;::  /(   ::;;
     ;;:: |  \  ::;;
     ';;::.\c/.::;;'
      ';:::'-,:::;'
        '';| |;''
           '-,
           | |
           '-,
           | |
           '-,
           | |
           '-,
           | |
          /`"`\
       .-'.  _.'-.
      `._  `    _.'
         `"---"`

''')
print("Bem vindo à Ilha Vermelha.")
print("Você acordou dentro de um casebre numa colina de uma ilha paradisíaca e sua missão é chegar até a costa e escapar.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

escolha1 = input('Você abriu a porta e viu que é quase fim de tarde.\nDuas trilhas estão diante de você, uma levando à uma floresta e outra a uma pedreira.\n\nEscolha ir para "floresta" ou "pedreira:"\n')
escolha1 = escolha1.lower();
if escolha1 == "pedreira":
  print("\nNa pedreira, você encontra uma tirolesa e uma escadaria. Ambas levam até a costa da ilha.\nO sol está se pondo, tingindo tudo ao seu redor de vermelho e logo você ficará sem luz. \nVocê checa a tirolesa e vê que seu gancho está enferrujado e a corda gasta.\nA escada parece segura, porém demorada.")
  escolha2 = input('\nEscolha descer pela "tirolesa" ou "escadaria": \n')
  escolha2 = escolha2.lower()
  if escolha2 == "tirolesa":
    print("\nA tirolesa range com seu peso, mas você consegue chegar na costa sem problemas.\nVocê avista um barco a motor, uma canoa e uma lancha. Você está sentindo muita dor de cabeça. ")
    escolha3 = input('\nEscolha o "barco", a "canoa" ou a "lancha" para ir embora da Ilha vermelha: \n').lower()
    if escolha3 == "barco":
      print("\nVocê dá partida no barco e ele avança rapidamente pelo mar.\nNão demora muito até você avistar um porto. Você desembarca e descobre estar na Bélgica.\nPor sorte, você fala flamengo fluentemente e consegue ajuda para regressar pro seu país.\nEnquanto viaja de volta, só consegue se perguntar como diabos foi parar naquela ilha, de qualquer forma.\nVocê decide parar de beber.")
      print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢀⣠⣴⠾⢛⠋⠉⠀⠀⠈⠉⠙⠛⢷⣦⡄⠀⠀
        ⠀⠀⢀⣴⡿⡫⠖⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡄⠀
        ⠀⢠⡿⠋⠎⠀⠀⠀⣠⣴⡶⢶⡶⢤⡀⠀⠀⠀⠀⢸⣿⠀
        ⢠⡟⠀⠀⠀⠀⢠⢾⡿⠉⠀⠀⠁⠀⠹⡄⠀⠀⠀⠀⣿⡇
        ⣾⠁⠀⠀⠀⠀⢺⡟⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⠁
        ⣿⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⢠⡟⠀
        ⣿⠀⠀⠀⣀⣰⣿⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⣠⠃⣸⠁⠀
        ⠛⠋⠛⠻⠽⠟⠁⠀⠀⢀⣤⡴⠞⠉⠀⠀⠚⣁⡼⠃⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠁⠀⠀⣠⠴⠚⠋⠉⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⢻⢠⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣾⣇⣭⣿⣧⣄⣸⡇⠧⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠐⠲⡍⢳⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣷⢇⠀⠀⠀⠀⠉⢨⡇⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠹⣧⡓⠂⠀⢀⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      ''')
    elif escolha3 == "lancha":
      print("Você dá partida na lancha e seu motor explode.\nVocê morreu carbonizado.")
      print('''
                   _.-^^---....,,--       
               _--                  --_  
              <                        >)
              |                         | 
               \._                   _./  
                  ```--. . , ; .--''       
                        | |   |             
                     .-=||  | |=-.   
                     `-=#$%&%$#=-'   
                        | ;  :|     
               _____.,-#%&$@%#&#~,._____
      ''')
    else:
      print("\nVocê consegue remar por algum tempo antes de desmaiar. Seu corpo desequilibra a canoa e você cai no mar.\nVocê morre despedaçado por uma orca.")
      print('''
                                       __
                                   _.-~  )
                        _..--~~~~,'   ,-/     _
                     .-'. . . .'   ,-','    ,' )
                   ,'. . . _   ,--~,-'__..-'  ,'
                 ,'. . .  (@)' ---~~~~      ,'
                /. . . . '~~             ,-'
               /. . . . .             ,-'
              ; . . . .  - .        ,'
             : . . . .       _     /
            . . . . .          `-.:
           . . . ./  - .          )
          .  . . |  _____..---.._/ _______
    ~---~~~~----~~~~             ~~
      ''')
  else:
    print("\nNo segundo degrau descido, um dos enormes tijolos de concreto escorrega e você rola até o final das escadas.\nVocê morreu a cabeça numa rocha")
    print('''
                                  ____
                          __,---'     `--.__
                       ,-'                ; `.
                      ,'                  `--.`--.
                     ,'                       `._ `-.
                     ;                     ;     `-- ;
                   ,-'-_       _,-~~-.      ,--      `.
                   ;;   `-,;    ,'~`.__    ,;;;    ;  ;
                   ;;    ;,'  ,;;      `,  ;;;     `. ;
                   `:   ,'    `:;     __/  `.;      ; ;
                    ;~~^.   `.   `---'~~    ;;      ; ;
                    `,' `.   `.            .;;;     ;'
                    ,',^. `.  `._    __    `:;     ,'
                    `-' `--'    ~`--'~~`--.  ~    ,'
                   /;`-;_ ; ;. /. /   ; ~~`-.     ;
  -._                   ; ;  ; `,;`-;__;---;      `----'
  `--.__             ``-`-;__;:  ;  ;__;
  ...     `--.__                `-- `-'
  
    ''')
  

else:
  print("\nVocê escuta um farfalhar nas folhas e depois um beliscão na perna.\nVocê morreu picado por uma cobra.")
  print('''
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣄⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡖⣻⠉⢿⣿⠆⠈⠙⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡚⠒⠊⠙⠂⠀⠀⢆⣱⡘⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠛⠳⣖⠒⠒⢙⡤⣿⣷⠃⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢻⠆⠤⠤⡗⣿⢻⣼⢀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠸⣼⣏⡒⢲⠟⡟⣾⡾⣎⢾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢸⡴⢻⠃⠀⡜⢸⣻⠴⠛⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣰⣰⣷⠏⠀⢰⠃⣿⣷⢳⣰⣤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⣯⣿⣟⠢⢤⣇⣸⣿⡽⣧⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣭⠓⠌⠉⡛⠉⣿⣼⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣰⠁⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠐⠁⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣼⠏⢰⢦⡀⠀⠀⠀⠀⠀⣀⡠⠤⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⡀⠀⠀⣸⡟⠀⠈⢯⡓⠦⢤⡤⠴⠚⠁⠀⠀⠀⠀⠀⢘⠍⠳⡄⠀⠀⠀⠀
  ⠀⠀⢀⣠⠤⠖⠒⡒⠒⠢⢤⡗⢤⡉⢺⠒⣿⡃⣀⣀⣠⠽⠷⠒⠛⠉⠉⣉⣉⣛⣛⣛⣛⡉⠀⠀⣸⠀⠀⠀⠀
  ⢀⡴⠋⠀⠀⢠⠊⠀⠀⠀⢸⡇⢄⡈⠛⣏⣿⠉⠁⠀⢀⣠⠤⠖⠚⠉⠉⠀⠀⠀⠓⠦⣄⠉⠙⠚⠯⣄⡀⠀⠀
  ⡜⠀⠀⠀⠀⢸⣤⡶⠦⢤⣼⣇⠀⠈⢉⣧⢿⣧⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠉⢦⠀
  ⣇⠀⠀⠀⠀⠈⠳⣄⣀⣀⣈⣿⠑⠢⠤⠼⡞⣿⡄⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠒⠒⢿⡇⠀⠀⠀⠀⠸⡆
  ⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠈⠐⠂⠙⣖⠻⣤⣠⣤⡶⠞⠋⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⢸⠇
  ⠀⠈⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠈⠢⠀⠉⠓⠦⠤⢤⣀⣠⠤⠤⠤⠒⠚⠉⠀⠀⠀⠀⠀⣠⡟⠁
  ⠀⠀⠀⠀⠈⠙⠓⠲⠶⠶⠶⠶⠞⠛⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠴⠞⠋⠀⠀⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  ''')
