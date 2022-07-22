

FONTCONFIG_FILE="{PREFIX}/lib/fonts/fonts.conf"
ONTCONFIG_PATH="{PREFIX}/lib/fonts/"

VK_ICD_FILENAMES="/usr/share/vulkan/icd.d/nvidia_icd.json"



WINEPREFIX	=	"{PREFIX}"
WINELOADER	=	"{PREFIX}/lib/loader/bin/wine"
WINESERVER	=	"{PREFIX}/lib/loader/bin/wineserver"

WINEARCH		=	"win64"
WINEDLLOVERRIDES="winemenubuilder.exe=d"
WINEDEBUG="-all"


STAGING_WRITECOPY="1"
STAGING_RT_PRIORITY_SERVER="1"
STAGING_RT_PRIORITY_SERVER="90"
STAGING_RT_PRIORITY_BASE="90"

fc-cache -fv



SCR_PATH="/mnt/volumes/btrnvv1/opt/cellar/photoshopCCV19/"
CACHE_PATH="/home/hoefkens/.cache/photoshopCCV19"
RESOURCES_PATH="$SCR_PATH/resources"


notify-send "Photoshop CC" "Photoshop CC launched." -i "/mnt/volumes/btrnvv1/opt/cellar/photoshopCCV19/launcher/AdobePhotoshop-icon.png"



**os.environ,
'WINEDEBUG' 			: '-all',
'WINEARCH'				:	'win64',
'WINEPREFIX' 			:	'/opt/Adobe/PhotoshopCC/prefix',
'WINELOADER'			:	'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wine',
'WINESERVER'			:	'/opt/btrwin/lib/loaders/wine/lutris-6.21-6-x86_64/bin/wineserver',
'FONTCONFIG_FILE' : '/opt/btrwin/lib/fonts/fonts/fonts.conf',
'FONTCONFIG_PATH' : '/opt/btrwin/lib/fonts/fonts/',
'SCR_PATH'				:	'/opt/Adobe/PhotoshopCC',
'RESOURCES_PATH'	:	'/opt/Adobe/PhotoshopCC/resources',
'CACHE_PATH'			: '/home/hoefkens/.cache/photoshopCCV19'
}




wineserver -p 300 -d0 &
wineserver -p 5000 -d0 &

/wineserver -p 300 -d0 &
sudo setcap cap_sys_nice+ep $WINESERVER


$WINESERVER  --debug=0 --persistent=10
$WINEBIN/wine start /unix '/mnt/volumes/btrnvv1/opt/cellar/Games/drive_c/Tools/MSIAfterburner/MSIAfterburner.exe'
nohup /mnt/btrnvv1/opt/lib/loaders/wine/5/lutris-5.21-2-x86_64/bin/wineserver --debug=0 --persistent=10  &
sudo setcap cap_sys_nice+ep /mnt/btrnvv1/opt/lib/loaders/wine/5/lutris-5.21-2-x86_64/bin/wineserver

WINEPATH="/bin/winepath --windows"


\



winetricks



# /mnt/volumes/btrnvv1/opt/lib/loaders/wine/lutris-GE-Proton7-14-x86_64/bin/wine64 start $1












fc-cache -fv




WINESERVER_OPTS=""
WINESERVER_OPTS="${WINESERVER_OPTS} --debug=0"
WINESERVER_OPTS="${WINESERVER_OPTS} --persistent=10"
######### WINEBINS
# EXEC=$($WINEBIN/winepath --windows $1)

sudo setcap cap_sys_nice+ep $WINESERVER

STAGING_WRITECOPY="1"
STAGING_RT_PRIORITY_SERVER="1"
STAGING_RT_PRIORITY_SERVER=90


$WINEBIN/wineserver --debug=0 --persistent=10 &
# $WINEBIN/wineserver $WINESERVER_OPTS &



 
 
 




bin/wine64 "start /unix $1 "



# $WINEBIN/wine64 start /unix $2 $3
# $WINEBIN/wine64 winelauncher $EXEC $3 $4










##### file rgb.reg
REGEDIT4

[HKEY_CURRENT_USER\Control Panel\Desktop]
"FontSmoothing"="2"
"FontSmoothingGamma"=dword:00000578
"FontSmoothingOrientation"=dword:00000001
"FontSmoothingType"=dword:00000002



wine regedit rgb.reg || winetricks settings fontsmooth=rgb


#### FILE : ~/.config/fontconfig/fonts.conf

<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

<fontconfig>

    <match target="font">
        <edit mode="assign" name="embeddedbitmap"><bool>false</bool></edit>

        <edit mode="assign" name="antialias">  <bool>true</bool></edit>
        <edit mode="assign" name="autohint">   <bool>false</bool></edit>
        <edit mode="assign" name="hinting">    <bool>true</bool></edit>

        <edit mode="assign" name="hintstyle"><const>hintslight</const></edit>

        <edit mode="assign" name="rgba"><const>rgb</const></edit>

        <edit mode="assign" name="lcdfilter"><const>lcddefault</const></edit>
    </match>

</fontconfig>


winecfg
sudo fc-cache -fv

