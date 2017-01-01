# Riot - Front-end client for the decentralized, secure, messaging and
#        data-transport protocol, Matrix.org
#
# https://riot.im/
# https://github/taw00/riot-web-srpm
#
# t0dd@protonmail.com


# Release bump is the base release number - i.e., we tend to "bump" this often.
# Recommend including the date for experimental builds
# for example 20160405.0, 20160405.1, 20160405.2, 20160406.0, etc
%define bump 0
# release bumptag
%define bumptag .taw
# % define bumptag % {nil}
# ...the release bumptag is used to convey information about who built the
# package (or other extra information) and is really only useful during early
# spins of the RPMs. For example, ".taw" is a reference to the original
# packager, Todd Warner (his initials).
# For actual releases, you may want to NIL the value above
%define _release %{bump}%{bumptag}

# We don't want a debuginfo package
%define debug_package %{nil}

%define _name riot-web
Name: riot-web
Version: 0.9.5
Release: 1.%{_release}%{?dist}
Summary: Riot - Front-end client for the decentralized, secure, messaging and data-transport protocol, Matrix.org

%define namev %{name}-%{version}
%define namevr %{namev}-%{release}
%define archivebasename %{namev}
%define sourcetree %{namev}
%define riotdefaultinstalltree /opt/Riot

License: Apache-2.0

Group: Applications/Internet
URL: http://riot.im/
# upstream
#Source0: https://github.com/vector-im/riot-web
Source0: %{archivebasename}.tar.gz
Source1: %{archivebasename}-extras.tar.gz
# patch for RPM builds - not really needed, but here for possible completeness
Patch0: %{archivebasename}-rpm.patch

BuildRoot:	%(mktemp -ud %{_tmppath}/%{namevr}-XXXXXX)
BuildRequires: npm git desktop-file-utils

%description
Riot is a front-end client implementing the decentralized, secure, messaging and
data-transport protocol, Matrix.org.

Riot is more than a messaging app. Riot is a shared workspace for the web. Riot
is a place to connect with teams. Riot is a place to to collaborate, to work, to
discuss your current projects.

Riot removes the barriers between apps, allowing you to connect teams and
functionality like never before.

Riot is free. Riot is secure.


%prep
# riot upstream stuff
%setup -q -n %{sourcetree}
# extra stuff
%setup -q -T -D -b 1 -n %{sourcetree}
# patches to make an RPM by default though we don't use it. (a completist I am)
#%patch0 -p1


%build
npm install
npm run build
# builds linux-friendly stuff (we use this) and a default tarball, rpm, or deb (not used)
%define linuxunpacked electron/dist/linux-unpacked
%ifarch x86_64 amd64
%define linuxunpacked electron/dist/linux-unpacked
node_modules/.bin/build -l tar.gz --x64
%else
%define linuxunpacked electron/dist/linux-ia32-unpacked
node_modules/.bin/build -l tar.gz --ia32
%endif


%install
rm -rf %{buildroot}
mkdir %{buildroot}
mkdir -p %{buildroot}%{riotdefaultinstalltree}
cp -a %{linuxunpacked}/* %{buildroot}%{riotdefaultinstalltree}
#install -D -m755 -p electron/dist/linux-unpacked/riot-web %{buildroot}%{_bindir}/riot-web
# a little ugly - the symbolic link creation requires this since it is not "installed"
mkdir -p %{buildroot}%{_bindir}
ln -s %{riotdefaultinstalltree}/riot-web %{buildroot}%{_bindir}/riot-web
install -D -m644 -p extras/riot-web.desktop %{buildroot}%{_datadir}/applications/riot-web.desktop
install -D -m644 -p extras/riot-web1.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/riot-web.png
install -D -m644 -p extras/riot-web2.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/riot-web.png
desktop-file-validate %{buildroot}%{_datadir}/applications/riot-web.desktop
install -D -m755 -p %{buildroot}%{riotdefaultinstalltree}/libffmpeg.so %{buildroot}%{_libdir}/libffmpeg.so
install -D -m755 -p %{buildroot}%{riotdefaultinstalltree}/libnode.so %{buildroot}%{_libdir}/libnode.so


%files
%defattr(-,root,root,-)
%{riotdefaultinstalltree}
%{_datadir}/*
%{_bindir}/*
%{_libdir}/libffmpeg.so
%{_libdir}/libnode.so
#%{_docsdir}/*
#%{_mandir}/*
%license LICENSE


%post
umask 007
/sbin/ldconfig > /dev/null 2>&1


%postun
umask 007
/sbin/ldconfig > /dev/null 2>&1


%clean
rm -rf %{build}
rm -rf %{buildroot}


%changelog
* Sun Jan 01 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.0.taw
- Initial build. Everything still ends up in /opt/Riot (messy) but... meh.
