# Riot - Front-end client for the decentralized, secure, messaging and
#        data-transport protocol, Matrix.
#
# https://riot.im/
# https://github/taw00/riot-rpm
# https://copr.fedorainfracloud.org/coprs/taw/Riot/
#
# t0dd@protonmail.com


# Release bump is the base release number - i.e., we tend to "bump" this often.
# Recommend including the date for experimental builds
# for example 20160405.0, 20160405.1, 20160405.2, 20160406.0, etc
%define bump 1
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

Name: riot
Obsoletes: riot-web
Version: 0.13.5
Release: %{_release}%{?dist}
Packager: Todd Warner <t0dd@protonmail.com>
Summary: Riot - Front-end client for the decentralized, secure, messaging and data-transport protocol, Matrix.

%define _srcname riot-web
%define namev %{name}-%{version}
%define namevr %{namev}-%{release}
%define srcnamev %{_srcname}-%{version}
%define srcnamevr %{srcnamev}-%{release}
%define buildtree %{srcnamev}
%define archivebasename %{srcnamev}
%define contribarchivename %{name}-extras-desktop
%define riotdefaultinstalltree /opt/riot

License: Apache-2.0

Group: Applications/Internet
URL: http://riot.im/
# upstream
Source0: %{archivebasename}.tar.gz
Source1: %{contribarchivename}.tar.gz
# patch for RPM builds - not really needed, but here for possible completeness
#Patch0: % {archivebasename}-rpm.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{namevr}-XXXXXX)
BuildRequires: npm git desktop-file-utils

%description
Riot is a decentralized, secure messaging client for collaborative group
communication. Riot's core architecture is an implementation of the matrix
protocol.

Riot is more than a messaging app. Riot is a shared workspace for the web. Riot
is a place to connect with teams. Riot is a place to to collaborate, to work, to
discuss your current projects.

Riot removes the barriers between apps, allowing you to connect teams and
functionality like never before.

Riot is free. Riot is secure.


%prep
# riot upstream stuff
%setup -q -T -a 0 -c %{buildtree}
# extra stuff
#%setup -q -T -D -b 1 -n %{buildtree}
%setup -q -T -D -a 1
#%setup -q -T -D -b 1 -c %{buildtree}
# patches to make an RPM by default though we don't use it. (a completist I am)
#%patch0 -p1

# We leave with this structure...
# ~/rpmbuild/BUILD/riot-VERSION/riot-web-VERSION/
# ~/rpmbuild/BUILD/riot-VERSION/riot-extras-desktop/

%build
# building in riot-VERSION
# cd to riot-web-VERSION
cd %{buildtree}
/usr/bin/npm install 
/usr/bin/npm install 7zip-bin-linux
/usr/bin/npm run build
# builds linux-friendly stuff (we use this) and a default tarball, rpm, or deb (not used)
%define linuxunpacked electron_app/dist/linux-unpacked
%ifarch x86_64 amd64
%define linuxunpacked electron_app/dist/linux-unpacked
node_modules/.bin/build -l tar.gz --x64
%else
%define linuxunpacked electron_app/dist/linux-ia32-unpacked
node_modules/.bin/build -l tar.gz --ia32
%endif


%install
rm -rf %{buildroot}
mkdir %{buildroot}
install -d %{buildroot}%{riotdefaultinstalltree}
cp -a %{archivebasename}/%{linuxunpacked}/* %{buildroot}%{riotdefaultinstalltree}
#cp % {archivebasename}/LICENSE %{buildroot}%{_datadir}/licenses/LICENSE
#install -D -m755 -p electron_app/dist/linux-unpacked/riot-web %{buildroot}%{_bindir}/riot
# a little ugly - the symbolic link creation requires this since it is not "installed"
mkdir -p %{buildroot}%{_bindir}
ln -s %{riotdefaultinstalltree}/riot-web %{buildroot}%{_bindir}/riot
install -D -m644 -p %{contribarchivename}/extras/riot.desktop %{buildroot}%{_datadir}/applications/riot.desktop

install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.24x24.png   %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.hicolor.svg         %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/riot.svg

install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.16x16.png   %{buildroot}%{_datadir}/icons/HighContrast/16x16/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.22x22.png   %{buildroot}%{_datadir}/icons/HighContrast/22x22/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.24x24.png   %{buildroot}%{_datadir}/icons/HighContrast/24x24/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.32x32.png   %{buildroot}%{_datadir}/icons/HighContrast/32x32/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.48x48.png   %{buildroot}%{_datadir}/icons/HighContrast/48x48/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.128x128.png %{buildroot}%{_datadir}/icons/HighContrast/128x128/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.256x256.png %{buildroot}%{_datadir}/icons/HighContrast/256x256/apps/riot.png
install -D -m644 -p %{contribarchivename}/extras/riot.highcontrast.svg         %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/riot.svg

desktop-file-validate %{buildroot}%{_datadir}/applications/riot.desktop

install -d %{buildroot}/usr/lib/riot
install -d %{buildroot}/etc/ld.so.conf.d
install -D -m755 -p %{buildroot}%{riotdefaultinstalltree}/libffmpeg.so %{buildroot}/usr/lib/riot/libffmpeg.so
install -D -m755 -p %{buildroot}%{riotdefaultinstalltree}/libnode.so %{buildroot}/usr/lib/riot/libnode.so
install -D -m644 -p %{contribarchivename}/extras/etc-ld.so.conf.d-riot.conf %{buildroot}/etc/ld.so.conf.d/riot.conf
#install -D -m755 -p %{buildroot}%{riotdefaultinstalltree}/libffmpeg.so %{buildroot}%{_libdir}/libffmpeg.so
#install -D -m755 -p %{buildroot}%{riotdefaultinstalltree}/libnode.so %{buildroot}%{_libdir}/libnode.so


%files
%defattr(-,root,root,-)
%{riotdefaultinstalltree}
%{_datadir}/*
%{_bindir}/*
/etc/ld.so.conf.d/riot.conf
%dir %attr(755,root,root) /usr/lib/riot
/usr/lib/riot/libffmpeg.so
/usr/lib/riot/libnode.so
#%{_libdir}/libffmpeg.so
#%{_libdir}/libnode.so
#% {_docsdir}/*
#% {_mandir}/*
%license %{archivebasename}/LICENSE


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
* Sun Feb 11 2018 Todd Warner <t0dd@protonmail.com> 0.13.5-1.taw
- Adjusted location of libffmpeg and libnode in order to avoid conflicts.
-
* Fri Feb 09 2018 Todd Warner <t0dd@protonmail.com> 0.13.5-0.taw
- Updated upstream source that fixes a security issue with external URL management.
- https://github.com/vector-im/riot-web/releases/tag/v0.13.5
-
* Sat Jan 06 2018 Todd Warner <t0dd@protonmail.com> 0.13.4-0.taw
- Updated upstream source that fixes one of the default configuration files.
- https://github.com/vector-im/riot-web/releases/tag/v0.13.4
-
* Wed Dec 06 2017 Todd Warner <t0dd@protonmail.com> 0.13.3-1.taw
- Updated upstream source.
- https://github.com/vector-im/riot-web/releases/tag/v0.13.3
- Bumped to -1.taw to fix this changelog date which was incorrectly labeled.
-
* Fri Nov 17 2017 Todd Warner <t0dd@protonmail.com> 0.13.0-1.taw
- Fedora 27 does not install 7zip-bin-linux when you perform "npm install", so
- we specifically add it.
-
* Fri Nov 17 2017 Todd Warner <t0dd@protonmail.com> 0.13.0-0.taw
- Updated upstream source.
-
* Tue Oct 24 2017 Todd Warner <t0dd@protonmail.com> 0.12.7-0.taw
- Updated upstream source.
-
* Mon Sep 25 2017 Todd Warner <t0dd@protonmail.com> 0.12.6-0.taw
- Updated upstream source.
- Updated build tree structure.
-
* Tue Apr 25 2017 Todd Warner <t0dd@protonmail.com> 0.9.9-0.taw
- Updated upstream source.
-
* Sun Apr 16 2017 Todd Warner <t0dd@protonmail.com> 0.9.8-0.taw
- Updated upstream source.
-
* Sun Feb 05 2017 Todd Warner <t0dd@protonmail.com> 0.9.7-1.0.taw
- Updated upstream source.
-
* Sat Jan 21 2017 Todd Warner <t0dd@protonmail.com> 0.9.6-1.2.taw
- Tweaks
-
* Mon Jan 16 2017 Todd Warner <t0dd@protonmail.com> 0.9.6-1.1.taw
- Small restructuring
-
* Mon Jan 16 2017 Todd Warner <t0dd@protonmail.com> 0.9.6-1.0.taw
- 0.9.6
-
* Mon Jan 09 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.5.taw
- improved icons a bit
-
* Wed Jan 04 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.4.taw
- Package renamed riot instead of riot-web -- cuz, it's not a webapp. :)
-
* Tue Jan 03 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.3.taw
- Fixing icons
- Moving towards calling the package riot, versus riot-web, which
- makes little sense. Undecided.
-
* Tue Jan 03 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.2.taw
- Fixing icons
-
* Sun Jan 01 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.1.taw
- Minor tweaks.
-
* Sun Jan 01 2017 Todd Warner <t0dd@protonmail.com> 0.9.5-1.0.taw
- Initial build. Everything still ends up in /opt/Riot (messy) but... meh.
-
