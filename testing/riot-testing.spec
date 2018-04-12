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

# <name>-<version>-<release>
# ...version is (can be many decimals):
# <vermajor>.<verminor>
# ...where release is:
# <pkgrel>[.<extraver>][.<snapinfo>].DIST[.<minorbump>]
# ...all together now:
# <name>-<vermajor.<verminor>-<pkgrel>[.<extraver>][.<snapinfo>].DIST[.<minorbump>]
# https://fedoraproject.org/wiki/Packaging:Versioning
# https://fedoraproject.org/wiki/Package_Versioning_Examples

%define isGA 0
%define includeMinorbump 1
%define includeSnapinfo 1


Name: riot
%define _name_archive riot-web
%define _snapinfo_archive rc.6
%undefine _snapinfo_archive
Summary: Riot - Front-end messaging client for the decentralized, secure, messaging and data-transport protocol, Matrix
Obsoletes: %{_name_archive}
License: Apache-2.0
Group: Applications/Internet
URL: https://riot.im/

#
# Build the version string
#
%define _vermajor 0.14
%define _verminor 0
Version: %{_vermajor}.%{_verminor}

#
# Build the release string
#

# --- set "minorbump" value here!
%define _minorbump taw0repackaged

# --- set "rel" (GA) or "pkgrel.extraver.snapinfo" (not GA) values here!
# ...is this *not* a GA release?
%undefine __relextended
%define _pkgrel 1
%if ! %{isGA}
%define _pkgrel 0
%define _extraver 2
%define _snapinfo testing
# ...are we including snapinfo in this non-GA release?
%if %{includeSnapinfo}
%define __relextended %{_extraver}.%{_snapinfo}
%else
%define __relextended %{_extraver}
%endif
%endif

# ---------------- end of commonly edited elements -------------------------

# This finishes building the release string; do not edit
%define _release %{_pkgrel}%{?dist}
# ...Set the string format for GA releases.
%if %{isGA}
%if %{includeMinorbump}
%define _release %{_pkgrel}%{?dist}.%{_minorbump}
%endif
# ...Set the string format for pre-preduction releases.
%else
%define _release %{_pkgrel}.%{__relextended}%{?dist}
%if %{includeMinorbump}
%define _release %{_pkgrel}.%{__relextended}%{?dist}.%{_minorbump}
%endif
%endif

Release: %{_release}

# how are debug info and build_ids managed (I only halfway understand this):
# https://github.com/rpm-software-management/rpm/blob/master/macros.in
%define debug_package %{nil}
%define _unique_build_ids 1
%define _build_id_links alldebug

# https://fedoraproject.org/wiki/Changes/Harden_All_Packages
#%%define_hardened_build 0

%define _source0 %{_name_archive}-%{version}
%if 0%{?_snapinfo_archive:1}
%define _source0 %{_name_archive}-%{version}-%{_snapinfo_archive}
%endif
Source0: %{_source0}.tar.gz
Source1: %{name}-%{_vermajor}-contrib.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: nodejs npm git desktop-file-utils tree

# Unarchived source tree structure (extracted in .../BUILD)
#   srcroot               riot-0.14
#      \_srccodetree        \_riot-web-0.14.0-rc.6
#      \_srccontribtree     \_riot-0.14-contrib
%define srcroot %{name}-%{_vermajor}
%define srccodetree %{_source0}
%define srccontribtree %{name}-0.14-contrib
# /usr/share/riot
%define installtree %{_datadir}/%{name}


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
# Prep section starts us in directory .../<_builddir>
# Extract into .../<_builddir>/<srcroot>/
mkdir %{srcroot}
%setup -q -T -D -a 0 -n %{srcroot}
%setup -q -T -D -a 1 -n %{srcroot}

# Libraries ldconfig file
echo "%{_libdir}/%{name}" > %{srccontribtree}/etc-ld.so.conf.d_riot.conf

# For debugging purposes...
cd .. ; tree -df -L 1 %{srcroot} ; cd -




%build
# Build section starts us in directory .../<_builddir>/<srcroot>

# Clearing npm's cache and package lock to eliminate SHA1 integrity issues.
%{warning:"taw: Keep running into this fatal error --'integrity checksum failed when using sha1'. Taking brute force dramatic action to remedy it.'"}
/usr/bin/npm cache clean --force
rm -rf ../.npm/_cacache
rm -f %{srccodetree}/package-lock.json

# -- BEGIN EXPERIMENTAL BUILD FROM GIT REPO --
# Note, if we actually did this normally, we'd put the fetch into either
# Source0 or the prep section.
%define _devel_branch_yn 0
%if %{?_devel_branch_yn}
# For now we are nuking the code tree and checking it out with git :(
rm -rf %{srccodetree}
%define _tag v%{version}
%if 0%{?_snapinfo_archive:1}
%define _tag v%{version}-%{_snapinfo_archive}
%endif
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
# Install section starts us in directory .../<_builddir>/<srcroot>
rm -rf %{buildroot} ; mkdir %{buildroot}

# Create directories
install -d %{buildroot}%{_libdir}/%{name}
install -d -m755 -p %{buildroot}%{_bindir}
install -d %{buildroot}%{installtree}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d

cp -a %{srccodetree}/%{linuxunpacked}/* %{buildroot}%{installtree}

# a little ugly - symbolic link creation
ln -s %{installtree}/%{_name_archive} %{buildroot}%{_bindir}/%{name}

install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.24x24.png   %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.hicolor.svg         %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/riot.svg

install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.16x16.png   %{buildroot}%{_datadir}/icons/HighContrast/16x16/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.22x22.png   %{buildroot}%{_datadir}/icons/HighContrast/22x22/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.24x24.png   %{buildroot}%{_datadir}/icons/HighContrast/24x24/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.32x32.png   %{buildroot}%{_datadir}/icons/HighContrast/32x32/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.48x48.png   %{buildroot}%{_datadir}/icons/HighContrast/48x48/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.128x128.png %{buildroot}%{_datadir}/icons/HighContrast/128x128/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.256x256.png %{buildroot}%{_datadir}/icons/HighContrast/256x256/apps/riot.png
install -D -m644 -p %{srccontribtree}/desktop/riot.highcontrast.svg         %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/riot.svg

install -D -m644 -p %{srccontribtree}/desktop/riot.desktop %{buildroot}%{_datadir}/applications/riot.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/riot.desktop

install -D -m755 -p %{buildroot}%{installtree}/libffmpeg.so %{buildroot}%{_libdir}/%{name}/libffmpeg.so
install -D -m755 -p %{buildroot}%{installtree}/libnode.so %{buildroot}%{_libdir}/%{name}/libnode.so
install -D -m644 -p %{srccontribtree}/etc-ld.so.conf.d_riot.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/riot.conf


%files
%defattr(-,root,root,-)
%license %{srccodetree}/LICENSE
# We own /usr/share/riot and everything under it...
%{installtree}
%{_datadir}/*
%{_bindir}/*
%{_sysconfdir}/ld.so.conf.d/riot.conf
%dir %attr(755,root,root) %{_libdir}/%{name}
%{_libdir}/%{name}/libffmpeg.so
%{_libdir}/%{name}/libnode.so
#%%{_docsdir}/*
#%%{_mandir}/*


%post
umask 007
/sbin/ldconfig > /dev/null 2>&1


%postun
umask 007
/sbin/ldconfig > /dev/null 2>&1


%clean
# The clean section starts us in directory .../<_builddir>/<srcroot>/
# Only needed for EPEL now.
rm -rf %{buildroot}


%changelog
* Thu Apr 12 2018 Todd Warner <t0dd@protonmail.com> 0.14.0-0.2.testing.taw0
- Added an 'npm cache clean --force' (and more) to hopefully address cache
  integrity issues (sha1 integrity checks, namely). Took ugly ugly action.
- Refactored the nvrea bits yet again.
- Fixed /usr/lib versus /usr/lib64
- Moved all the application code to /usr/share/riot (opt is frowned upon)
- Restructured the contrib tarball
- 6650f1024f16dcdc289025b16ec4ee245c0c585ea00945e8dcd989196110f4cb  riot-0.14-contrib.tar.gz
-
* Mon Apr 9 2018 Todd Warner <t0dd@protonmail.com> 0.14.0-0.1.rc.6.taw0
- Release - 7445456 - 0.14-0 RC6
- name-version-release more closely matches industry guidelines:
  https://fedoraproject.org/wiki/Packaging:Versioning
- A lot of spec file cleanup.
- Nuked .build_ids in order to avoid conflicts.
- 1818053ca890b5dce85d4ca4c20c2945cba69c656820baa7fe01b49ed67b94e5  riot-web-0.14.0-rc.6.tar.gz
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
