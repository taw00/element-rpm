#!/usr/bin/env bash

# QT5 + GNOME + Wayland has issues
# https://bugreports.qt.io/browse/QTBUG-68619

# Electron + KDE Plasma has issues
# https://github.com/electron/electron/issues/12791
# https://github.com/taw00/riot-rpm/issues/16

# I wrote this little wrapper script that attempts to bypass these issues until
# they are fixed. The workarounds involve setting environment variables so that
# the application is forced to operate in a manner that is different than it
# would by default.

# Note that QT programs will currently "do the right thing" without intervention
# but they will post a somewhat cryptic warning message
#   "Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway."
# We control that explicitely here so that this message doesn't crop up.

# How this script it used.
# 1. It is called from the commandline instead of calling the application directly, or,
# 2. It is called from <application>.desktop (which is used by your window
#    manager open the application), and...
# 3. If you use this as a template for your own application, you flip on
#    the relevant flag below if your application is a QT5 application or an
#    Electron-based application.

# This can be "qt5" or "electron" or "neither"
type_of_application=electron

_XDG_SESSION_TYPE=$XDG_SESSION_TYPE
_XDG_CURRENT_DESKTOP=$XDG_CURRENT_DESKTOP
_QT_QPA_PLATFORM=$QT_QPA_PLATFORM

noisy=0
echoerr() {
    if [ $noisy -ne 0 ]
    then
        printf "%s\n" "$*" >&2;
    fi
}

if [ "$type_of_application" = "qt5" ]
then
    force_gnome_wayland=0
    if [ $force_gnome_wayland -ne 0 ] ; then noisy=1 ; fi
    
    if [ "$XDG_CURRENT_DESKTOP" = "GNOME" ] && [ "$XDG_SESSION_TYPE" = "wayland" ]
    then
        if [ $force_gnome_wayland -ne 0 ]
        then
            # Experimental. wayland is still problematic.
            echoerr "\
## We have elected to force this QT5-based application to work with wayland and not fall back to x11.
"
            _QT_QPA_PLATFORM=wayland
        else
            _XDG_SESSION_TYPE=x11
            unset _QT_QPA_PLATFORM
        fi

    else
        echoerr "\
## Desktop session is not gnome+wayland, carry on!
"
    fi

elif [ "$type_of_application" = "electron" ]
then
    force_kde=0
    if [ $force_kde -ne 0 ] ; then noisy=1 ; fi
    if [ "$XDG_CURRENT_DESKTOP" = "KDE" ]
    then
        if [ $force_kde -eq 0 ]
        then
            _XDG_CURRENT_DESKTOP=Unity
        else
            # Experimental. kde is still problematic.
            echoerr "\
## We have elected to force this electron-based application to work as by default with KDE.
"
        fi
    else
        echoerr "\
## Desktop session is not KDE, carry on!
"
    fi
fi

echoerr "\
XDG_SESSION_TYPE -->    $XDG_SESSION_TYPE to $_XDG_SESSION_TYPE
XDG_CURRENT_DESKTOP --> $XDG_CURRENT_DESKTOP to $_XDG_CURRENT_DESKTOP
QT_QPA_PLATFORM -->     $QT_QPA_PLATFORM to $_QT_QPA_PLATFORM
"

XDG_CURRENT_DESKTOP=$_XDG_CURRENT_DESKTOP XDG_SESSION_TYPE=$_XDG_SESSION_TYPE QT_QPA_PLATFORM=$_QT_QPA_PLATFORM /usr/bin/env riot "$@"

