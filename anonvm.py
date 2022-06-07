from os import name, system
try:
    system('pkg install python3')
except:
    print("Exception error occurred")
    exit()
system('pip install colorama')
from colorama import Fore
from time import sleep
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN
green2 = Fore.LIGHTGREEN_EX
white = Fore.WHITE
def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.01)
    print()
if name == 'nt':
    print(f'{red}[!] {white}this tool works on linux systems only ! ')
    exit()
else:
    system('clear')
banner = f'''
{red} █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗    ██╗   ██╗███╗   ███╗
{red} ██╔══██╗████╗  ██║██╔═══██╗████╗  ██║    ██║   ██║████╗ ████║ 
{red} ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║    ██║   ██║██╔████╔██║
{red} ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║    ╚██╗ ██╔╝██║╚██╔╝██║
{red} ██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║     ╚████╔╝ ██║ ╚═╝ ██║
{red} ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝      ╚═══╝  ╚═╝     ╚═╝ 
{Fore.CYAN}
[{blue}!{cyan}] Coded By ANON_DARKPHANTOM
[{blue}!{cyan}] Select The Linux OS To Install

[01]{blue} - {red}Ubuntu{cyan}    [07]{blue} - {red}openSUSE Leap{cyan}
[02]{blue} - {red}Debian{cyan}    [08]{blue} - {red}openSUSE Tumbleweed{cyan}
[03]{blue} - {red}Kali{cyan}      [09]{blue} - {red}BlackArch{cyan}
[04]{blue} - {red}Fedora{cyan}    [10]{blue} - {red}Alpine{cyan}
[05]{blue} - {red}Void{cyan}      [11]{blue} - {red}Developer{cyan}
[06]{blue} - {red}CentOS{cyan}    [12]{blue} - {red}Exit{cyan}

'''
SlowPrint(banner)
def x10():
    global os
    try:
        os = input(f'{cyan}[{blue}!{cyan}] Please Enter The OS Code To Install It : ')
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()
    if os == '1' or os == '01':
        try:
            system('clear')
            print(f'''{white}
                            .:/+oossssoo+/:.`
                        `:+ssssssssssssssssss+:`
                      -+sssssssssssssss{white}y{red}ssssssss+-
                    .osssssssssssss{white}yy{red}ss{white}mMmh{red}ssssssso.
                   /sssssssss{white}ydmNNNmmd{red}s{white}mMMMMNdy{red}sssss/
                 `+ssssssss{white}hNNdy{red}sssssss{white}mMMMMNdy{red}ssssss+`
                 +sssssss{white}yNNh{red}ss{white}hmNNNNm{red}s{white}mMmh{red}s{white}ydy{red}sssssss+
                -sssss{white}y{red}ss{white}Nm{red}ss{white}hNNh{red}ssssss{white}y{red}s{white}hh{red}ss{white}mMy{red}sssssss-
                +ssss{white}yMNdy{red}ss{white}hMd{red}ssssssssss{white}hMd{red}ss{white}NN{red}sssssss+
                sssss{white}yMMMMMmh{red}sssssssssssss{white}NM{red}ss{white}dMy{red}sssssss
                sssss{white}yMMMMMmhy{red}ssssssssssss{white}NM{red}ss{white}dMy{red}sssssss
                +ssss{white}yMNdy{red}ss{white}hMd{red}ssssssssss{white}hMd{red}ss{white}NN{red}sssssss+
                -sssss{white}y{red}ss{white}Nm{red}ss{white}hNNh{red}ssssssss{white}dh{red}ss{white}mMy{red}sssssss-
                 +sssssss{white}yNNh{red}ss{white}hmNNNNm{red}s{white}mNmh{red}s{white}ymy{red}sssssss+
                  +ssssssss{white}hNNdy{red}sssssss{white}mMMMMmhy{red}ssssss+
                   /sssssssss{white}ydmNNNNmd{red}s{white}mMMMMNdh{red}sssss/
                    .osssssssssssss{white}yy{red}ss{white}mMmdy{red}sssssso.
                      -+sssssssssssssss{white}y{red}ssssssss+-
                        `:+ssssssssssssssssss+:`
                            .:/+oossssoo+/:.


                ''')
            system(
                'pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh')
        except:
            print(f"{red}Exception occured")
    elif os == '2' or os == '02':
        try:
            system('clear')
            print(f'''{white}
                       _,met$$$$$gg.
                    ,g$$$$$$$$$$$$$$$P.
                  ,g$$P"        """Y$$.".
                 ,$$P'              `$$$.
                ',$$P       ,ggs.     `$$b:
                `d$$'     ,$P"'   {red}.{white}    $$$
                 $$P      d$'     {red},{white}    $$P
                 $$:      $$.   {red}-{white}    ,d$$'
                 $$;      Y$b._   _,d$P'
                 Y$$.    {red}`.{white}`"Y$$$$P"'
                {white} `$$b      {red}"-.__
                {white}  `Y$$
                   `Y$$.
                     `$$b.
                       `Y$$b.
                          `"Y$b._
                              `"""

                    ''')
            system(
                'pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '3' or os == '03':
        try:
            system('clear')
            print(f'''
                {white}..............
                            ..,;:ccc,.
                          ......```;lxO.
                .....````..........,:ld;
                           .`;;;:::;,,.x,
                      ..```.            0Xxoc:,.  ...
                  ....                ,ONkc;,;cokOdc`,.
                 .                   OMo           `:{red}dd{white}o.
                                    dMc               :OO;
                                    0M.                 .:o.
                                    ;Wd
                                     ;XO,
                                       ,d0Odlc;,..
                                           ..`,;:cdOOd::,.
                                                    .:d;.`:;.
                                                       'd,  .`
                                                         ;l   ..
                                                          .o
                                                            c
                                                            .`
                                                             .


                ''')
            system(
                'pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh')
        except:
            print(f"{red}Exception occured")
    elif os == '4' or os == '04 ':
        try:
            system('clear')
            print(f'''
                {cyan}          /:-------------:\\
                {cyan}       :-------------------::
                {cyan}     :-----------{white}/shhOHbmp{cyan}---:\\
                {cyan}   /-----------{white}omMMMNNNMMD  {cyan}---:
                {cyan}  :-----------{white}sMMMMNMNMP{cyan}.    ---:
                {cyan} :-----------{white}:MMMdP{cyan}-------    ---\\
                {cyan},------------{white}:MMMd{cyan}--------    ---:
                {cyan}:------------{white}:MMMd{cyan}-------    .---:
                {cyan}:----    {white}oNMMMMMMMMMNho{cyan}     .----:
                {cyan}:--     .{white}+shhhMMMmhhy++{cyan}   .------/
                {cyan}:-    -------{white}:MMMd{cyan}--------------:
                {cyan}:-   --------{white}/MMMd{cyan}-------------;
                {cyan}:-    ------{white}/hMMMy{cyan}------------:
                {cyan}:--{white} :dMNdhhdNMMNo{cyan}------------;
                {cyan}:---{white}:sdNMMMMNds:{cyan}------------:
                {cyan}:------{white}:://:{cyan}-------------::
                {cyan}:---------------------://


                ''')
            system(
                'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh')
        except:
            print(f"{red}Exception occured")
    elif os == '5' or os == '05':
        try:
            system('clear')
            print(f'''
                {green2}
                                __.;=====;.__
                            _.=+==++=++=+=+===;.
                             -=+++=+===+=+=+++++=_
                        .     -=:``     `--==+=++==.
                       _vi,    `            --+=++++:
                      .uvnvi.       _._       -==+==+.
                     .vvnvnI`    .;==|==;.     :|=||=|.
                {green}+QmQQm{green}pvvnv; {green}_yYsyQQWUUQQQm #QmQ#{green}:{green}QQQWUV$QQm.
                {green} -QQWQW{green}pvvo{green}wZ?.wQQQE{green}==<{green}QWWQ/QWQW.QQWW{green}(: {green}jQWQE
                {green}  -$QQQQmmU`  jQQQ@{green}+=<{green}QWQQ)mQQQ.mQQQC{green}+;{green}jWQQ@'
                {green}   -$WQ8Y{green}nI:   {green}QWQQwgQQWV{green}`{green}mWQQ.jQWQQgyyWW@!
                {green}     -1vvnvv.     `~+++`        ++|+++{green2}
                      +vnvnnv,                 `-|===
                       +vnvnvns.           .      :=-
                        -Invnvvnsi..___..=sv=.     `
                          +Invnvnvnnnnnnnnvvnn;.
                            ~|Invnvnvvnvvvnnv]+`
                               -~|[*1]*|~


                               ''')
            system(
                'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Void/void.sh && bash void.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '6' or os == '06':
        try:
            system('clear')
            print(f'''{green2}
                                 ..
                               .PLTJ.
                              <><><><>
                     {green}KKSSV' 4KKK {green}LJ{red} KKKL.'VSSKK
                     {green}KKV' 4KKKKK {green}LJ{red} KKKKAL 'VKK
                     {green}V' ' 'VKKKK {green}LJ{red} KKKKV' ' 'V
                     {green}.4MA.' 'VKK {green}LJ{red} KKV' '.4Mb.
                {red}   . {green}KKKKKA.' 'V {green}LJ{red} V' '.4KKKKK {blue}.
                {red} .4D {green}KKKKKKKA.'' {green}LJ{red} ''.4KKKKKKK {blue}FA.
                {red}<QDD ++++++++++++  {blue}++++++++++++ GFD>
                {red} 'VD {blue}KKKKKKKK'.. {green}LJ {green}..'KKKKKKKK {blue}FV
                {red}   ' {blue}VKKKKK'. .4 {green}LJ {green}K. .'KKKKKV {blue}'
                     {blue} 'VK'. .4KK {green}LJ {green}KKA. .'KV'
                     {blue}A. . .4KKKK {green}LJ {green}KKKKA. . .4
                     {blue}KKA. 'KKKKK {green}LJ {green}KKKKK' .4KK
                     {blue}KKSSA. VKKK {green}LJ {green}KKKV .4SSKK
                {green}              <><><><>
                               'MKKM'
                                 ''


                ''')
            system(
                'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '7' or os == '07':
        try:
            system('clear')
            print(f'''{green}
                           .;ldkO0000Okdl;.
                       .;d00xl:^```````^:ok00d;.
                     .d00l`                'o00d.
                   .d0Kd'{green}  Okxol:;,.          {green}:O0d.
                  .OK{green}KKK0kOKKKKKKKKKKOxo:,      {green}lKO.
                 ,0K{green}KKKKKKKKKKKKKKK0P^{green},,,{green}^dx:{green}    ;00,
                .OK{green}KKKKKKKKKKKKKKKk`{green}.oOPPb.{green}`0k.{green}   cKO.
                :KK{green}KKKKKKKKKKKKKKK: {green}kKx..dd {green}lKd{green}   `OK:
                dKK{green}KKKKKKKKKOx0KKKd {green}^0KKKO` {green}kKKc{green}   dKd
                dKK{green}KKKKKKKKKK;.;oOKx,..{green}^{green}..;kKKK0.{green}  dKd
                :KK{green}KKKKKKKKKK0o;...^cdxxOK0O/^^'  {green}.0K:
                 kKK{green}KKKKKKKKKKKKK0x;,,......,;od  {green}lKk
                 `0K{green}KKKKKKKKKKKKKKKKKKKK00KKOo^  {green}c00`
                  `kK{green}KKOxddxkOO00000Okxoc;``   {green}.dKk`
                    l0Ko.                    .c00l`
                     `l0Kk:.              .;xK0l`
                        `lkK0xl:;,,,,;:ldO0kl`
                            `^:ldxkkkkxdl:^`


                    ''')
            system(
                'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '8' or os == '08':
        try:
            system('clear')
            print(f'''{cyan}
                                                     ......
                     .,cdxxxoc,.               .:kKMMMNWMMMNk:.
                    cKMMN0OOOKWMMXo. ;        ;0MWk:.      .:OMMk.
                  ;WMK;.       .lKMMNM,     :NMK,             .OMW;
                 cMW;            'WMMMN   ,XMK,                 oMM'
                .MMc               ..;l. xMN:                    KM0
                'MM.                   'NMO                      oMM
                .MM,                 .kMMl                       xMN
                 KM0               .kMM0. .dl:,..               .WMd
                 .XM0.           ,OMMK,    OMMMK.              .XMK
                   oWMO:.    .;xNMMk,       NNNMKl.          .xWMx
                     :ONMMNXMMMKx;          .  ,xNMWKkxllox0NMWk,
                         .....                    .:dOOXXKOxl,


                    ''')
            system(
                'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '9' or os == '09':
        try:
            system('clear')
            print(f'''{white}
                                   00
                                   11
                                  ===={red}
                                  .{white}//{red}
                                 `o{white}//{red}:
                                `+o{white}//{red}o:
                               `+oo{white}//{red}oo:
                               -+oo{white}//{red}oo+:
                             `/:-:+{white}//{red}ooo+:
                            `/+++++{white}//{red}+++++:
                           `/++++++{white}//{red}++++++:
                          `/+++oooo{white}//{red}ooooooo/`
                         ./ooosssso{white}//{red}osssssso+`
                        .oossssso-`{white}//{red}`/ossssss+`
                       -osssssso.  {white}//{red}  :ssssssso.
                      :osssssss/   {white}//{red}   osssso+++.
                     /ossssssss/   {white}//{red}   +ssssooo/-
                   `/ossssso+/:-   {white}//{red}   -:/+osssso+-
                  `+sso+:-`        {white}//{red}       `.-/+oso:
                 `++:.             {white}//{red}            `-/+/
                 .`                {white}/{red}                 `/


                    ''')
            system(
                'pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '10':
        try:
            system('clear')
            print(f'''{cyan}
                       .hddddddddddddddddddddddh.
                      :dddddddddddddddddddddddddd:
                     /dddddddddddddddddddddddddddd/
                    +dddddddddddddddddddddddddddddd+
                  `sdddddddddddddddddddddddddddddddds`
                 `ydddddddddddd++hdddddddddddddddddddy`
                .hddddddddddd+`  `+ddddh:-sdddddddddddh.
                hdddddddddd+`      `+y:    .sddddddddddh
                ddddddddh+`   `//`   `.`     -sddddddddd
                ddddddh+`   `/hddh/`   `:s-    -sddddddd
                ddddh+`   `/+/dddddh/`   `+s-    -sddddd
                ddd+`   `/o` :dddddddh/`   `oy-    .yddd
                hdddyo+ohddyosdddddddddho+oydddy++ohdddh
                .hddddddddddddddddddddddddddddddddddddh.
                 `yddddddddddddddddddddddddddddddddddy`
                  `sdddddddddddddddddddddddddddddddds`
                    +dddddddddddddddddddddddddddddd+
                     /dddddddddddddddddddddddddddd/
                      :dddddddddddddddddddddddddd:
                       .hddddddddddddddddddddddh.


                ''')
            system(
                'pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh')
        except:
            print(f"{red}Exception occurred")
    elif os == '11':
        try:
            system('xdg-open https://anon-d46kph4tom.github.io/ ')
        except:
            print(f"{red}Exception occurred")
    elif os == '12':
        exit()
    elif os == "exit" or os == "quit" or os == "q":
        SlowPrint("Goodbye!")
        exit()
    else:
        print(f"{red}Invalid option!{cyan}")
        x10()
if __name__ == "__main__":
    x10()