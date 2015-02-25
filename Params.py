_VERSION="v0.1"
_VERSIONCODE="anot"
_LASTUPDATE="24.02.15"

_TABS10="										"
_TABS5="					"
_TABS2="		"
_TABS1="	"


class col:
    NORMAL= '\033[0m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def  px(normaltext):
    print(col.NORMAL +normaltext+col.NORMAL);
    return;
def  pxP(purpletext):
    print(col.PURPLE +purpletext+col.NORMAL);
    return;
def  pxB(bluetext):
    print(col.BLUE +bluetext+col.NORMAL);
    return;
def  pxG(greentext):
    print(col.GREEN +greentext+col.NORMAL);
    return;
def  pxY(yellowtext):
    print(col.YELLOW +yellowtext+col.NORMAL);
    return;
def  pxR(redtext):
    print(col.RED +redtext+col.NORMAL);
    return;
def  pxBLD(boldtext):
    print(col.BOLD +boldtext+col.NORMAL);
    return;
def  pxUND(underlinetext):
    print(col.UNDERLINE +underlinetext+col.NORMAL);
    return;





#import subprocess #Kabukta komut çalıştırmak için
#_PYEXECPREFIX='python ' #Ortam Eki
#subprocess.call (_PYEXECPREFIX + "Greeter.py",  shell=True)


#GEREKLİLER
#sudo pip install requests