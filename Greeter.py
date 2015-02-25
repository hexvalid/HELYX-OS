import Params
_SPLASH= ("Greeter splashed")

_LOGOS1=("██╗  ██╗███████╗██╗  ██╗   ██╗    ██╗  ██╗")
_LOGOS2=("██║  ██║██╔════╝██║  ╚██╗ ██╔╝    ╚██╗██╔╝")
_LOGOS3=("███████║█████╗  ██║   ╚████╔╝█████╗╚███╔╝ ")
_LOGOS4=("██╔══██║██╔══╝  ██║    ╚██╔╝ ╚════╝██╔██╗ ")
_LOGOS5=("██║  ██║███████╗███████╗██║       ██╔╝ ██╗")
_LOGOS6=("╚═╝  ╚═╝╚══════╝╚══════╝╚═╝       ╚═╝  ╚═╝")
_LOGOSX1=("╔══════════════════════════════════")
_LOGOSX2=("║")
_LOGOSX3=("╚══════════════════════════════════")

def splash():
    print  (_SPLASH)
    print  (_LOGOS1)    
    print  (_LOGOS2)
    print  (_LOGOS3)
    print  (_LOGOS4)
    print  (_LOGOS5)
    print  (_LOGOS6)
    print  (_LOGOSX1)
    print  (_LOGOSX2+"═══Versiyon:         "+Params._VERSION)
    print  (_LOGOSX2+"═══Versiyon Kodu:    "+Params._VERSIONCODE)
    print  (_LOGOSX2+"═══Son düzenlenleme: "+Params._LASTUPDATE)
    print  (_LOGOSX3)

