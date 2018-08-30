# riot.spec
# vim:tw=0:ts=2:sw=2:et:
#
# Riot - Riot is a decentralized, secure messaging client for collaborative
#        group communication.
#
# https://github/taw00/riot-rpm
# https://copr.fedorainfracloud.org/coprs/taw/Riot/
#
# https://riot.im/
# https://vector.im
# https://github.com/vector-im/riot-web

# ---

# Package (RPM) name-version-release.
# <name>-<vermajor.<verminor>-<pkgrel>[.<extraver>][.<snapinfo>].DIST[.<minorbump>]
# https://fedoraproject.org/wiki/Packaging:Versioning
# https://fedoraproject.org/wiki/Package_Versioning_Examples

Name: riot
%define _legacy_name riot-web
Summary: A decentralized, secure messaging client for collaborative group communication

%define targetIsProduction 1
%define includeMinorbump 1

# ie. if the dev team includes things like rc.3 in the filename
%define archiveQualifier rc.2
%define includeArchiveQualifier 0

# VERSION
# eg. 0.16.0
%define vermajor 0.16
%define verminor 2
Version: %{vermajor}.%{verminor}

# RELEASE
# If production - "targetIsProduction 1"
# eg. 1 (and no other qualifiers)
%define pkgrel_prod 1

# If pre-production - "targetIsProduction 0"
# eg. 0.2.testing -- pkgrel_preprod should always equal pkgrel_prod-1
%define pkgrel_preprod 0
%define extraver_preprod 1
%define snapinfo testing
%if %{includeArchiveQualifier}
  %define snapinfo %{archiveQualifier}
%endif

# if includeMinorbump
%define minorbump taw0

# Building the release string (don't edit this)...

# release numbers
%undefine _relbuilder_pt1
%if %{targetIsProduction}
  %define _pkgrel %{pkgrel_prod}
  %define _relbuilder_pt1 %{pkgrel_prod}
%else
  %define _pkgrel %{pkgrel_preprod}
  %define _extraver %{extraver_preprod}
  %define _relbuilder_pt1 %{_pkgrel}.%{_extraver}
%endif

# snapinfo and repackage (pre-built) indicator
%undefine _relbuilder_pt2
%if %{targetIsProduction}
  %undefine snapinfo
%endif
%if 0%{?sourceIsPrebuilt:1}
  %if ! %{sourceIsPrebuilt}
    %undefine snapinfo_rp
  %endif
%else
  %undefine snapinfo_rp
%endif
%if 0%{?snapinfo_rp:1}
  %if 0%{?snapinfo:1}
    %define _relbuilder_pt2 %{snapinfo}.%{snapinfo_rp}
  %else
    %define _relbuilder_pt2 %{snapinfo_rp}
  %endif
%else
  %if 0%{?snapinfo:1}
    %define _relbuilder_pt2 %{snapinfo}
  %endif
%endif

# put it all together
# pt1 will always be defined. pt2 and minorbump may not be
%define _release %{_relbuilder_pt1}
%if ! %{includeMinorbump}
  %undefine minorbump
%endif
%if 0%{?_relbuilder_pt2:1}
  %if 0%{?minorbump:1}
    %define _release %{_relbuilder_pt1}.%{_relbuilder_pt2}%{?dist}.%{minorbump}
  %else
    %define _release %{_relbuilder_pt1}.%{_relbuilder_pt2}%{?dist}
  %endif
%else
  %if 0%{?minorbump:1}
    %define _release %{_relbuilder_pt1}%{?dist}.%{minorbump}
  %else
    %define _release %{_relbuilder_pt1}%{?dist}
  %endif
%endif

Release: %{_release}
# ----------- end of release building section


Provides: riot-web = 0.9.6
Obsoletes: riot-web < 0.9.6
# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing
# Apache Software License 2.0
License: ASL 2.0
URL: https://riot.im/
# Note, for example, this will not build on ppc64le
ExclusiveArch: x86_64 i686 i586 i386

# how are debug info and build_ids managed (I only halfway understand this):
# https://github.com/rpm-software-management/rpm/blob/master/macros.in
%define debug_package %{nil}
%define _unique_build_ids 1
%define _build_id_links alldebug

# https://fedoraproject.org/wiki/Changes/Harden_All_Packages
# https://fedoraproject.org/wiki/Packaging:Guidelines#PIE
%define _hardened_build 1

# https://fedoraproject.org/wiki/Packaging:SourceURL
# * Sources as part of source RPM can be found at
#   https://github.com/taw00/riot-rpm
# * Source0 tarball can be snagged from https://github.com/vector-im/riot-web
%define _source0 %{_legacy_name}-%{version}
%if %{includeArchiveQualifier}
  %define _source0 %{_legacy_name}-%{version}-%{archiveQualifier}
%endif
#Source0: %%{_source0}.tar.gz
#Source0: https://github.com/PROJECT_NAME/%%{name}/releases/download/v%%{version}/%%{name}-%%{version}.tar.gz
#Source0: https://github.com/vector-im/%%{_legacy_name}/archive/v%%{version}/%%{_source0}.tar.gz
%if %{targetIsProduction}
Source0: https://github.com/taw00/riot-rpm/blob/master/source/SOURCES/%{_source0}.tar.gz
Source1: https://github.com/taw00/riot-rpm/blob/master/source/SOURCES/%{name}-%{vermajor}-contrib.tar.gz
%else
Source0: https://github.com/taw00/riot-rpm/blob/master/source/testing/SOURCES/%{_source0}.tar.gz
Source1: https://github.com/taw00/riot-rpm/blob/master/source/testing/SOURCES/%{name}-%{vermajor}-contrib.tar.gz
%endif


# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto

BuildRequires: nodejs npm git tree
BuildRequires: desktop-file-utils
%if 0%{?suse_version:1}
BuildRequires: appstream-glib
#BuildRequires: libappstream-glib8 appstream-glib
%else
BuildRequires: libappstream-glib
%endif

#t0dd: Trying to remove dependence on libffmpeg.so (FOSS issues, I believe).
#      Thus far, I have been unsuccessful. Additionally, hardcoded "Requires"
#      breaks cross-distro builds. :(
#AutoReq: no
# constructed subset from results of autoreq from previous builds - we do all this so we can exclude individual libraries
#Requires: bash nodejs alsa-lib atk glibc cairo cups-libs dbus-libs expat fontconfig freetype libgcc GConf2 gtk2 gdk-pixbuf2 glib2 
#Requires: libX11 libXcomposite libX11-xcb libXcursor libXdamage libXext libXfixes libXi libXrandr libXrender libXScrnSaver libXtst
#Requires: nspr nss nss-util pango libstdc++ libxcb 
# Requirements desired, but not found...
# ld-linux-x86-64.so.2 libnode.so (we provide) rpmlib rtld
# This package currently provides libffmpeg.so
#Requires: libffmpeg.so


# Unarchived source tree structure (extracted in {_builddir})
#   srcroot               riot-0.16
#      \_srccodetree        \_riot-0.16.0 (or riot-0.16.0-rc.2 or riot-v0.16.0 or riot-v0.16.0-rc.2)
#      \_srccontribtree     \_riot-0.16-contrib
%define srcroot %{name}-%{vermajor}
%define srccodetree %{_source0}
%define srccontribtree %{name}-%{vermajor}-contrib
# /usr/share/riot
%define installtree %{_datadir}/%{name}


%description
Riot is a decentralized, secure messaging client for collaborative group
communication. Riot's core architecture is an implementation of the matrix
protocol.

Riot is more than a messaging app. Riot is a shared work-space for the web.
Riot is a place to connect with teams. Riot is a place to to collaborate, to
work, to discuss your current projects.

Riot removes the barriers between apps, allowing you to connect teams and
functionality like never before.

Riot is free. Riot is secure.


%prep
# Prep section starts us in directory {_builddir}
# Extract into {_builddir}/{srcroot}/
mkdir %{srcroot}
%setup -q -T -D -a 0 -n %{srcroot}
%setup -q -T -D -a 1 -n %{srcroot}

# Make sure the right library path is used...
echo "%{_libdir}/%{name}" > %{srccontribtree}/etc-ld.so.conf.d_%{name}.conf

# Swap out our package.json because we have SSL issues with https://matrix.org
#cp %{srccontribtree}/package.json %{srccodetree}/

# For debugging purposes...
cd .. ; tree -df -L 1 %{srcroot} ; cd -


%build
# Build section starts us in directory {_builddir}/{srcroot}

# Clearing npm's cache and package lock to eliminate SHA1 integrity issues.
#%%{warn: "taw build note: I keep running into this fatal error --'integrity checksum failed when using sha1'. Taking dramatic action -brute force- in an attempt to remedy it.' If someone can figure out what is causing this, I will buy them a beer."}
/usr/bin/npm cache clean --force
rm -rf ../.npm/_cacache
#rm -f %%{srccodetree}/package-lock.json

%if 0%{?suse_version:1}
# We trust where we are getting modules from and Suse builds require
# https-agnostism apparently (I don't know why) -t0dd
/usr/bin/npm config set strict-ssl false
/usr/bin/npm config set registry http://registry.npmjs.org/
#/usr/bin/npm config set registry http://matrix.org/packages/npm/
/usr/bin/npm config list
%endif

# -- BEGIN EXPERIMENTAL BUILD FROM GIT REPO --
# Note, if we actually did this normally, we'd put the fetch into either
# Source0 or the prep section.
%define _devel_branch_yn 0
%if %{?_devel_branch_yn}
  # For now we are nuking the code tree and checking it out with git :(
  rm -rf %{srccodetree}
  %define _tag v%{version}
  %if %{includeArchiveQualifier}
    %define _tag v%{version}-%{archiveQualifier}
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
%if 0%{?suse_version:1}
  /usr/bin/sleep 15
%endif
/usr/bin/npm install 7zip-bin-linux
%if 0%{?suse_version:1}
  /usr/bin/sleep 15
  npm_config_strict_ssl=false /usr/bin/npm --reg="http://registry.npmjs.org/" run build
%else
  /usr/bin/npm --reg="http://registry.npmjs.org/" run build
%endif


# builds linux-friendly stuff (we use this) and a default tarball, rpm, or
# deb (not used)
%define linuxunpacked electron_app/dist/linux-unpacked
%ifarch x86_64 amd64
  %define linuxunpacked electron_app/dist/linux-unpacked
  %if 0%{?suse_version:1}
    npm_config_strict_ssl=false ./node_modules/.bin/build -l tar.gz --x64
  %else
    ./node_modules/.bin/build -l tar.gz --x64
  %endif
%else
  %define linuxunpacked electron_app/dist/linux-ia32-unpacked
  %if 0%{?suse_version:1}
    npm_config_strict_ssl=false ./node_modules/.bin/build -l tar.gz --ia32
  %else
    ./node_modules/.bin/build -l tar.gz --ia32
  %endif
%endif


%install
# Install section starts us in directory {_builddir}/{srcroot}

# Cheatsheet for some built-in RPM macros:
# https://fedoraproject.org/wiki/Packaging:RPMMacros
#   _builddir = {_topdir}/BUILD
#   _buildrootdir = {_topdir}/BUILDROOT
#   buildroot = {_buildrootdir}/{name}-{version}-{release}.{_arch}
#   _datadir = /usr/share
#   _mandir = /usr/share/man
#   _sysconfdir = /etc
#   _libdir = /usr/lib or /usr/lib64 (depending on system)

# Create directories
install -d %{buildroot}%{_libdir}/%{name}
install -d -m755 -p %{buildroot}%{_bindir}
install -d %{buildroot}%{installtree}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
%define _metainfodir %{_datadir}/metainfo

cp -a %{srccodetree}/%{linuxunpacked}/* %{buildroot}%{installtree}

# a little ugly - symbolic link creation
ln -s %{installtree}/%{_legacy_name} %{buildroot}%{_bindir}/%{name}

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
install -D -m644 -p %{srccontribtree}/desktop/riot.appdata.xml %{buildroot}%{_metainfodir}/riot.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

# /usr/lib/riot or /usr/lib64/riot...
install -D -m755 -p %{buildroot}%{installtree}/libffmpeg.so %{buildroot}%{_libdir}/%{name}/libffmpeg.so
rm %{buildroot}%{installtree}/libffmpeg.so
install -D -m755 -p %{buildroot}%{installtree}/libnode.so %{buildroot}%{_libdir}/%{name}/libnode.so
rm %{buildroot}%{installtree}/libnode.so
install -D -m644 -p %{srccontribtree}/etc-ld.so.conf.d_riot.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/riot.conf


%files
%defattr(-,root,root,-)
%license %{srccodetree}/LICENSE
# We own /usr/share/riot and everything under it...
%{installtree}
%{_datadir}/icons/*
%{_datadir}/applications/riot.desktop
%{_metainfodir}/riot.appdata.xml
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
/usr/bin/update-desktop-database &> /dev/null || :


%postun
umask 007
/sbin/ldconfig > /dev/null 2>&1
/usr/bin/update-desktop-database &> /dev/null || :


%changelog
* Wed Aug 29 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.2-1.taw
* Wed Aug 29 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.2-0.1.testing.taw
  - v16.2

* Wed Aug 22 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.1-1.taw
* Wed Aug 22 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.1-0.1.testing.taw
  - v16.1

* Mon Jul 30 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.0-1.taw
* Mon Jul 30 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.0-0.1.testing.taw
  - v16.0

* Wed Jul 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-1.taw
* Wed Jul 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-0.1.testing.taw
  - v15.7

* Mon Jul 09 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-0.1.rc.2.taw
  - v15.7 RC2

* Sun Jul 01 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-0.1.rc.1.taw
  - v15.7 RC1

* Sun Jul 01 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.6-1.taw
* Sun Jul 01 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.6-0.2.testing.taw
  - v15.6

* Sat Jun 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.6-0.1.rc.2.taw
  - v15.6 RC2

* Sat Jun 16 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.5-1.taw
* Sat Jun 16 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.5-0.1.testing.taw
  - v15.5

* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.4-2.taw
* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.4-1.3.testing.taw
* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.4-1.2.testing.taw
* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.4-1.1.testing.taw
  - Recieving HTTP 429 errors. This is due to rate-limiting on the nodejs  
    registry servers for anyone pulling down npm's via non-ssl calls. Which,  
    we have to do for OpenSuse builds. So... I added more refinded OS distro  
    querying logic.
  - A pile of sleeps added to slow things down for opensuse builds. Probably  
    does nothing.
  - TODO: include all deps so that no over-the-wire calls are necessary

* Fri May 25 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.4-0.1.testing.taw
  - v15.4 testing

* Fri May 25 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.3-2.taw
  - Updated v15.3 builds that are more OpenSuse compatible

* Thu May 24 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.3-1.1.testing.taw
  - Reverted the hardcoded Requires (broke Suse builds)
  - Trying to make this OpenSuse compatible (Suse builds don't like https for  
    some reason):  
    ```
npm ERR! code UNABLE_TO_GET_ISSUER_CERT_LOCALLY
npm ERR! errno UNABLE_TO_GET_ISSUER_CERT_LOCALLY
npm ERR! request to https://registry.npmjs.org/minimist failed, reason: unable to get local issuer certificate
    ```

* Wed May 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.3-1.taw
  - v15.3

* Wed May 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.3-0.1.testing.taw
  - v15.3 testing
  - minor spec file cleanup
  - locking down supported architectures w/ ExclusiveArch

* Thu May 17 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.2-1.taw
  - v15.2

* Thu May 17 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.2-0.1.testing.taw
  - v15.2 testing

* Sat May 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.0-0.1.rc.3.taw
  - v15.0-rc.3
  - Added back the required libffmpeg.so library - my experiment failed. :(

* Sat May 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.0-0.1.rc.2.taw
  - fixed dependency issue

* Fri May 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.0-0.1.rc.2.taw
  - v15.0 release candidate
  - attempted to yank libffmpeg.so from the package. FAILED (added back later)
  - had to manually construct the Requires because can't exclude from AutoReq
  - map proper lib (or lib64) path to the /etc/ld.so.conf.d/riot.conf file
  - spec file: mkdir without -p can be problematic on repeat builds.

* Sat May 5 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.2-2.taw
  - Update

* Sat May 5 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.2-1.1.testing.taw
  - Tweaked the .desktop and .appdata.xml files a bit (more conforming)
  - Apparently, name_at_example.com is more "standard" for email formatting.

* Thu May 3 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.2-1.taw
  - Release 14.2

* Thu May 3 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.2-0.2.rc.final.taw
  - v14.2-rc.final

* Fri Apr 27 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.2-0.1.rc.3.taw
  - v14.2-rc.3

* Thu Apr 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.1-1.taw
  - GA build for 14.1

* Thu Apr 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.1-0.1.testing.taw
  - Release: 740b221 (git) v0.14.1
  - Cleaned up %%files a bit (too broad of inclusion)
  - https://github.com/vector-im/riot-web/releases/tag/v0.14.1

* Thu Apr 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.0-0.2.testing.taw
  - Added an 'npm cache clean --force' (and more) to hopefully address cache  
    integrity issues (sha1 integrity checks, namely). Very ugly.
  - Refactored the nvrea bits yet again.
  - Fixed /usr/lib versus /usr/lib64
  - rpmlint and Packaging Guidelines compliance fixes:
    - Removed "Vender:" and "Packager:" - that's why we have changelogs.
    - Source0 has a github URL and there is additional instruction above
    - Obsolotes done right.
    - Moved all the application code to /usr/share/riot (opt is frowned upon)
    - Removed %%clean and removed the buildroot cleanup in %%install section
    - Made the Summary: compliant (shorter, no ending period, no name repeat
  - Restructured the contrib tarball.

* Wed Apr 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.0-1.taw
  - Release: eaeb495 - 0.14.0
  - Changelog: https://github.com/vector-im/riot-web/releases/tag/v0.14.0
  - Changes specific to these builds...
  - name-version-release more closely matches industry guidelines:  
    https://fedoraproject.org/wiki/Packaging:Versioning
  - A lot of spec file cleanup.

* Tue Apr 10 2018 Todd Warner <t0dd_at_protonmail.com> 0.13.5-3.taw
  - Added an 'npm cache clean --force' to hopefully about cache integrity  
    issues (sha1 integrity checks, namely)

* Mon Apr 9 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.0-0.1.rc.6.taw
  - Release - 7445456 - 0.14-0 RC6
  - name-version-release more closely matches industry guidelines:  
    https://fedoraproject.org/wiki/Packaging:Versioning
  - A lot of spec file cleanup.
  - Nuked .build_ids in order to avoid conflicts.

* Sun Feb 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.13.5-1.taw
  - Adjusted location of libffmpeg and libnode in order to avoid conflicts.

* Fri Feb 09 2018 Todd Warner <t0dd_at_protonmail.com> 0.13.5-0.taw
  - Updated upstream source that fixes a security issue with external URL  
    management.
  - https://github.com/vector-im/riot-web/releases/tag/v0.13.5

* Sat Jan 06 2018 Todd Warner <t0dd_at_protonmail.com> 0.13.4-0.taw
  - Updated upstream source that fixes one of the default configuration files.
  - https://github.com/vector-im/riot-web/releases/tag/v0.13.4

* Wed Dec 06 2017 Todd Warner <t0dd_at_protonmail.com> 0.13.3-1.taw
  - Updated upstream source.
  - https://github.com/vector-im/riot-web/releases/tag/v0.13.3
  - Bumped to -1.taw to fix this changelog date which was incorrectly labeled.

* Fri Nov 17 2017 Todd Warner <t0dd_at_protonmail.com> 0.13.0-1.taw
  - Fedora 27 does not install 7zip-bin-linux when you perform "npm install",  
    so we specifically add it.

* Fri Nov 17 2017 Todd Warner <t0dd_at_protonmail.com> 0.13.0-0.taw
  - Updated upstream source.

* Tue Oct 24 2017 Todd Warner <t0dd_at_protonmail.com> 0.12.7-0.taw
  - Updated upstream source.

* Mon Sep 25 2017 Todd Warner <t0dd_at_protonmail.com> 0.12.6-0.taw
  - Updated upstream source.
  - Updated build tree structure.

* Tue Apr 25 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.9-0.taw
  - Updated upstream source.

* Sun Apr 16 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.8-0.taw
  - Updated upstream source.

* Sun Feb 05 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.7-1.0.taw
  - Updated upstream source.

* Sat Jan 21 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.6-1.2.taw
  - Tweaks

* Mon Jan 16 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.6-1.1.taw
  - Small restructuring

* Mon Jan 16 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.6-1.0.taw
  - v0.9.6

* Mon Jan 09 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.5-1.5.taw
  - improved icons a bit

* Wed Jan 04 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.5-1.4.taw
  - Package renamed riot instead of riot-web -- cuz, it's not a webapp. :)

* Tue Jan 03 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.5-1.3.taw
  - Fixing icons
  - Moving towards calling the package riot, versus riot-web, which
  - makes little sense. Undecided.

* Tue Jan 03 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.5-1.2.taw
  - Fixing icons

* Sun Jan 01 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.5-1.1.taw
  - Minor tweaks.

* Sun Jan 01 2017 Todd Warner <t0dd_at_protonmail.com> 0.9.5-1.0.taw
  - Initial build. Everything still ends up in /opt/Riot (messy) but... meh.

