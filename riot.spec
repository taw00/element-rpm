# Riot - Front-end client for the decentralized, secure, messaging and
#        data-transport protocol, Matrix.
#
# https://github/taw00/riot-rpm
# https://copr.fedorainfracloud.org/coprs/taw/Riot/
#
# https://riot.im/
# https://vector.im
# https://github.com/vector-im/riot-web
#
Packager: Todd Warner <t0dd@protonmail.com>
Vendor: New Vector

# How RPM names work!
#
# name-version-release
# ...version is (can be many decimals):
# <vermajor>.<verminor>
# ...where release is:
# <pkgrel>[.<extraver>][.<snapinfo>]{dist}[.<minorbump>] ...or, mine...
# <rel>[.<devrel>][.<devsnap>]{dist}[.<bump>]
# ...all together now:
# <name>-<vermajor.<verminor>-<rel>[.<devrel>][.<devsnap>]{dist}[.<bump>]
# For example:
# - testing:   riot-0.14.0-0.2.testing.fc27.taw0 [.src.rpm or x86_64.rpm]
# - producion: riot-0.14.0-1.fc27.taw0 [.src.rpm or x86_64.rpm]
#
# https://fedoraproject.org/wiki/Packaging:Versioning
# https://fedoraproject.org/wiki/Package_Versioning_Examples


Name: riot
%define _vermajor 0.14
%define _verminor 0
Version: %{_vermajor}.%{_verminor}

%define _rel 1
%define _devrel 0
# flip-flop if we are GA (undefine on bottom)
%define _devsnap rc.6
%undefine _devsnap
# flip-flop the undefine if we are GA (undefine on bottom)
%define __relextended %{_devrel}
%if 0%{?_devsnap:1}
%define __relextended %{_devrel}.%{_devsnap}
%endif
%undefine __relextended
# flip-flop next two lines if you don't want the minor bump
%undefine _bump
%define _bump taw0


# ---------------- end of commonly edited elements ----------------------------

# "Release" gets complicated-ish...

%define _release_part %{_rel}%{?dist}
%if 0%{?__relextended:1}
# extraver.snapinfo.[dist]...
%define _release_part %{_rel}.%{__relextended}%{?dist}
%endif

%define _release %{_release_part}
%if 0%{?_bump:1}
%define _release %{_release_part}.%{_bump}
%endif
Release: %{_release}

Summary: Riot - Front-end client for the decentralized, secure, messaging and data-transport protocol, Matrix.

# how are debug info and build_ids managed (I only halfway understand this):
# https://github.com/rpm-software-management/rpm/blob/master/macros.in
%define debug_package %{nil}
%define _unique_build_ids 1
%define _build_id_links alldebug

# https://fedoraproject.org/wiki/Changes/Harden_All_Packages
#%%define_hardened_build 0

%define srcarchive %{name}-web-%{version}
%define srccontribarchive %{name}-extras-desktop
%if 0%{?_devsnap:1}
%define srcarchive %{name}-web-%{version}-%{_devsnap}
%endif

# Unarchived source tree structure (extracted in .../BUILD)
#   srcroot               riot-0.14
#      \_srccodetree        \_riot-web-0.14.0
#      \_srccontribtree     \_riot-extras-desktop
%define srcroot %{name}-%{_vermajor}
%define srccodetree %{srcarchive}
%define srccontribtree %{srccontribarchive}
%define installtree /opt/riot

Obsoletes: riot-web
License: Apache-2.0
Group: Applications/Internet
URL: http://riot.im/
# upstream
Source0: %{srcarchive}.tar.gz
Source1: %{srccontribarchive}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: nodejs npm git desktop-file-utils

%description
Riot is a decentralized, secure messaging client for collaborative group
communication. Riot's core architecture is an implementation of the matrix
protocol.

Riot is more than a messaging app. Riot is a shared workspace for the web.
Riot is a place to connect with teams. Riot is a place to to collaborate, to
work, to discuss your current projects.

Riot removes the barriers between apps, allowing you to connect teams and
functionality like never before.

Riot is free. Riot is secure.


%prep
# Prep section starts us in directory .../BUILD
# process riot-web - Source0 - untars in:
#   .../BUILD/riot-0.14/riot-web-0.14.0-rc.4/
mkdir %{srcroot}
%setup -q -T -D -a 0 -n %{srcroot}
# extra stuff
%setup -q -T -D -a 1 -n %{srcroot}

# We leave with this structure...
# ~/rpmbuild/BUILD/riot-0.14/riot-web-0.14.0-rc.4/
# ~/rpmbuild/BUILD/riot-0.14/riot-extras-desktop/

%build
# This section starts us in directory .../BUILD/riot-0.14 (srcroot)

# Clearing npm's cache will hopefully elminate SHA1 integrity issues.
/usr/bin/npm cache clean --force

# -- BEGIN EXPERIMENTAL BUILD FROM GIT REPO --
%define _devel_branch_yn 0
%if %{?_devel_branch_yn}
# For now we are nuking the code tree and checking it out with git :(
rm -rf %{srccodetree}
%define _tag v%{version}-%{_devsnap}
/usr/bin/git clone https://github.com/vector-im/riot-web.git %{srccodetree}
cd %{srccodetree}
/usr/bin/git checkout tags/%{_tag}

./scripts/fetch-develop.deps.sh

cd matrix-js-sdk
/usr/bin/git pull
/usr/bin/npm install 
/usr/bin/npm run build
cd ..

cd matrix-react-sdk
/usr/bin/git pull
/usr/bin/npm install 
/usr/bin/npm run build
cd ..

if [ ! -e node_modules/matrix-js-sdk ]
then
  cd node_modules
  ln -s ../matrix-js-sdk .
  cd..
fi
if [ ! -e node_modules/matrix-react-sdk ]
  cd node_modules
  ln -s ../matrix-react-sdk .
  cd ..
fi

#mv matrix-js-sdk node_modules/
#mv matrix-react-sdk node_modules/
%else
cd %{srccodetree}
%endif
# -- END EXPERIMENTAL BUILD FROM GIT REPO --

/usr/bin/npm install 
/usr/bin/npm install 7zip-bin-linux
/usr/bin/npm run build

#/usr/bin/npm install electron
#/usr/bin/npm run electron

# builds linux-friendly stuff (we use this) and a default tarball, rpm, or
# deb (not used)
%define linuxunpacked electron_app/dist/linux-unpacked
%ifarch x86_64 amd64
%define linuxunpacked electron_app/dist/linux-unpacked
./node_modules/.bin/build -l tar.gz --x64
%else
%define linuxunpacked electron_app/dist/linux-ia32-unpacked
./node_modules/.bin/build -l tar.gz --ia32
%endif


%install
# This section starts us in directory .../BUILD/riot-0.14 (srcroot)
rm -rf %{buildroot} ; mkdir %{buildroot}

# Create directories
install -d %{buildroot}/usr/lib/riot
install -d -m755 -p %{buildroot}%{_bindir}
install -d %{buildroot}%{installtree}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d

cp -a %{srccodetree}/%{linuxunpacked}/* %{buildroot}%{installtree}

# a little ugly - symbolic link creation
ln -s %{installtree}/riot-web %{buildroot}%{_bindir}/riot

install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.24x24.png   %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.hicolor.svg         %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/riot.svg

install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.16x16.png   %{buildroot}%{_datadir}/icons/HighContrast/16x16/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.22x22.png   %{buildroot}%{_datadir}/icons/HighContrast/22x22/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.24x24.png   %{buildroot}%{_datadir}/icons/HighContrast/24x24/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.32x32.png   %{buildroot}%{_datadir}/icons/HighContrast/32x32/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.48x48.png   %{buildroot}%{_datadir}/icons/HighContrast/48x48/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.128x128.png %{buildroot}%{_datadir}/icons/HighContrast/128x128/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.256x256.png %{buildroot}%{_datadir}/icons/HighContrast/256x256/apps/riot.png
install -D -m644 -p %{srccontribtree}/extras/riot.highcontrast.svg         %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/riot.svg

install -D -m644 -p %{srccontribtree}/extras/riot.desktop %{buildroot}%{_datadir}/applications/riot.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/riot.desktop

install -D -m755 -p %{buildroot}%{installtree}/libffmpeg.so %{buildroot}/usr/lib/riot/libffmpeg.so
install -D -m755 -p %{buildroot}%{installtree}/libnode.so %{buildroot}/usr/lib/riot/libnode.so
install -D -m644 -p %{srccontribtree}/extras/etc-ld.so.conf.d-riot.conf %{buildroot}/etc/ld.so.conf.d/riot.conf
#install -D -m755 -p %%{buildroot}%{installtree}/libffmpeg.so %%{buildroot}%%{_libdir}/libffmpeg.so
#install -D -m755 -p %%{buildroot}%%{installtree}/libnode.so %%{buildroot}%%{_libdir}/libnode.so


%files
%defattr(-,root,root,-)
%license %{srccodetree}/LICENSE
# We own /opt/riot and everything under it...
%{installtree}
%{_datadir}/*
%{_bindir}/*
/etc/ld.so.conf.d/riot.conf
%dir %attr(755,root,root) /usr/lib/riot
/usr/lib/riot/libffmpeg.so
/usr/lib/riot/libnode.so
#%%{_libdir}/libffmpeg.so
#%%{_libdir}/libnode.so
#%%{_docsdir}/*
#%%{_mandir}/*


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
* Wed Apr 11 2018 Todd Warner <t0dd@protonmail.com> 0.14.0-1.taw0
- Release: eaeb495 - 0.14.0
- Changelog: https://github.com/vector-im/riot-web/releases/tag/v0.14.0
- Changes specific to these builds...
- name-version-release more closely matches industry guidelines:
  https://fedoraproject.org/wiki/Packaging:Versioning
- A lot of spec file cleanup.
- de16ceaeeea785d812d2e9e2d24581477f2727c812e9628576dc4647db0bae1d  riot-web-0.14.0.tar.gz
- d2de4f9b2018b04ffae532d68865154feaa017e0ca4a2bc871e64436ef401b70  riot-extras-desktop.tar.gz
-
* Tue Apr 10 2018 Todd Warner <t0dd@protonmail.com> 0.13.5-3.taw
- Added an 'npm cache clean --force' to hopefully about cache integrity issues
  (sha1 integrity checks, namely)
-
* Mon Apr 9 2018 Todd Warner <t0dd@protonmail.com> 0.13.5-2.taw
- Nuked .build_ids in order to avoid conflicts.
-
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
