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
# https://github.com/vector-im/riot-desktop (1.6+)
# https://github.com/vector-im/riot-web (1.5 and earlier)

# ---

# Package (RPM) name-version-release.
# <name>-<vermajor.<verminor>-<pkgrel>[.<extraver>][.<snapinfo>].DIST[.<minorbump>]
# https://fedoraproject.org/wiki/Packaging:Versioning
# https://fedoraproject.org/wiki/Package_Versioning_Examples

Name: riot
%define _name_d %{name}-desktop
%define _name_w %{name}-web
%define tld_vendor_product_id im.riot.Riot
Summary: A decentralized, secure messaging client for collaborative group communication

%define targetIsProduction 1

# ie. if the dev team includes things like rc.3 in the filename
%define buildQualifier rc.6
%undefine buildQualifier

# VERSION
%define vermajor 1.6
%define verminor 8
Version: %{vermajor}.%{verminor}

# RELEASE
%define _pkgrel 1
%if ! %{targetIsProduction}
  %define _pkgrel 0.1
%endif

# MINORBUMP
%define minorbump taw

#
# Build the release string - don't edit this
#

%define snapinfo testing
# Let's replace the default snapinfo with the archive qualifier
%if 0%{?buildQualifier:1}
  %define snapinfo %buildQualifier
%endif
%if %{targetIsProduction}
  %undefine snapinfo
%endif

# pkgrel will always be defined, snapinfo and minorbump may not be
%define _release %{_pkgrel}
%if 0%{?snapinfo:1}
  %if 0%{?minorbump:1}
    %define _release %{_pkgrel}.%{snapinfo}%{?dist}.%{minorbump}
  %else
    %define _release %{_pkgrel}.%{snapinfo}%{?dist}
  %endif
%else
  %if 0%{?minorbump:1}
    %define _release %{_pkgrel}%{?dist}.%{minorbump}
  %else
    %define _release %{_pkgrel}%{?dist}
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
# ...flip-flop next two lines in order to disable (nil) or enable (1) debuginfo package build
%define debug_package 1
%define debug_package %{nil}
%define _unique_build_ids 1
%define _build_id_links alldebug

# https://fedoraproject.org/wiki/Changes/Harden_All_Packages
# https://fedoraproject.org/wiki/Packaging:Guidelines#PIE
%define _hardened_build 1

# https://fedoraproject.org/wiki/Packaging:SourceURL
# * Sources as part of source RPM can be found at
#   https://github.com/taw00/riot-rpm
# * Source0 tarball can be snagged from https://github.com/vector-im/riot-desktop
%define _version %{version}
%if 0%{?buildQualifier:1}
  %define _version %{version}-%{buildQualifier}
%endif
%define _source0 %{_name_d}-%{_version}
%define _source1 %{_name_w}-%{_version}

#Source0: https://github.com/PROJECT_NAME/%%{name}/releases/download/v%%{version}/%%{name}-%%{version}.tar.gz
Source0: https://github.com/vector-im/%{_name_d}/archive/v%{_version}/%{_source0}.tar.gz
Source1: https://github.com/vector-im/%{_name_w}/archive/v%{_version}/%{_source1}.tar.gz
Source2: https://github.com/taw00/riot-rpm/raw/master/SOURCES/%{name}-%{vermajor}-contrib.tar.gz

# This is used to declare whether we pull additional sources dependencies from the contrib tarball
%define useExtraSources 1

#t0dd: I add tree, vim-enhanced, and less for mock environment introspection
%if ! %{targetIsProduction}
BuildRequires: tree vim-enhanced less findutils mlocate dnf
%endif

#
#TODO: Need to reduce the build-time fetches from the internet via...
#      https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/
#      Reference: Using tarballs from the npm registry
#

%if 0%{?suse_version:1}
# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
#BuildRequires: libappstream-glib8 appstream-glib
BuildRequires: ca-certificates-cacert ca-certificates-mozilla ca-certificates
BuildRequires: desktop-file-utils
BuildRequires: appstream-glib /bin/sh
BuildRequires: nodejs10 npm10 nodejs10-devel nodejs-common
BuildRequires: python2 libsecret-devel
%if 0%{?sle_version}
# Leap
# provides libcrypto.so.1
BuildRequires: libopenssl1_0_0
%if 0%{?sle_version} == 150100
# Leap 15.1
%endif
%if 0%{?sle_version} == 150200
# Leap 15.2
%endif
%else
# Tumbleweed
# provides libcrypto.so.1
BuildRequires: libcrypt1
%endif
%endif

%if 0%{?rhel:1}
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libsecret-devel
%if 0%{?rhel} < 8
###NOLONGERSUPPORTED### This is super ugly
###NOLONGERSUPPORTED### EL7 is too far behind on many many packages. Therefore, you have to pull
###NOLONGERSUPPORTED### from other repos. In this case, nodejs and yarn.
###NOLONGERSUPPORTED### Include these repos into your mock or build environments...
###NOLONGERSUPPORTED###   https://rpm.nodesource.com/pub_10.x/el/7/$basearch
###NOLONGERSUPPORTED###   https://dl.yarnpkg.com/rpm/
###NOLONGERSUPPORTED### Note that this version of nodejs installs npm as well.
###NOLONGERSUPPORTED##BuildRequires: nodejs >= 2:10
###NOLONGERSUPPORTED##BuildRequires: yarn
###NOLONGERSUPPORTED##BuildRequires: python
###NOLONGERSUPPORTED##BuildRequires: libxcrypt -- NOPE, not available
%else
# EL8 is based on Fedora 28
BuildRequires: nodejs npm
BuildRequires: python3
# provides libcrypto.so.1
BuildRequires: libxcrypt
%endif
%endif

%if 0%{?fedora:1}
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: python
BuildRequires: libsecret-devel
%if 0%{?fedora} >= 29
BuildRequires: nodejs npm nodejs-yarn
# provides libcrypto.so.1
BuildRequires: libxcrypt-compat
%else
BuildRequires: nodejs npm
# provides libcrypto.so.1
BuildRequires: libxcrypt
%endif
%endif

# BuildRequires for all platforms . . .
BuildRequires: cargo gcc-c++ cmake rust
BuildRequires: curl

# Everyone but RHEL can do sqlcipher
# XXX THIS IS A PROBLEM XXX
%if 0%{?rhel:1}
%else
BuildRequires: sqlcipher-devel
Requires: sqlcipher
%endif

# Unarchived source tree structure (extracted in {_builddir})
#   sourceroot               riot-1.6
#      \_sourcetree_d            \_riot-desktop-1.6.0 (or riot-desktop-1.6.0-rc.3)
#      \_sourcetree_w            \_riot-web-1.6.0 (or riot-web-1.6.0-rc.3)
#      \_sourcetree_contrib      \_riot-1.6-contrib
%define sourceroot %{name}-%{vermajor}
%define sourcetree_d %{_source0}
%define sourcetree_w %{_source1}
%define sourcetree_contrib %{name}-%{vermajor}-contrib
# /usr/share/riot
%define installtree %{_datadir}/%{name}

# Riot should not be providing any libraries. Certainly not libffmpeg.
%global __provides_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*))$
%global __requires_exclude ^((libffmpeg[.]so.*)|(lib.*\\.so.*))$


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

# The prep section is the first place we can run shell commands. Therefore,
# these checks are here . .. Unsupported OS versions:
%if 0%{?rhel} && 0%{?rhel} < 8
  %{error: "======== EL version: %{rhel}: EL7-based platforms (CentOS7/RHEL7), and older, are not supportable build targets."}
%endif

%if 0%{?sle_version} && 0%{?sle_version} <= 150100
  #%%{error: "======== OpenSUSE version: %{sle_version}: Builds for OpenSUSE 15.1 (and older) can no longer be supported due to outdated or unavailable packages."}
%endif

%if 0%{?fedora} && 0%{?fedora} < 30
  echo "======== Fedora version: %{fedora}"
  %{error: "Builds for this version of Fedora can no longer be supported."}
%endif


# Extract into {_builddir}/{sourceroot}/
mkdir %{sourceroot}
%setup -q -T -D -a 0 -n %{sourceroot}
%setup -q -T -D -a 1 -n %{sourceroot}
%setup -q -T -D -a 2 -n %{sourceroot}

# Make sure the right library path is used...
echo "%{_libdir}/%{name}" > %{sourcetree_contrib}/etc-ld.so.conf.d_%{name}.conf

# For debugging purposes...
%if ! %{targetIsProduction}
  cd .. ; tree -df -L 1 %{sourceroot} ; cd -
%endif

# We ship with riot supplied olm tarball. Use it . . .
%if %{useExtraSources}
mkdir -p %{sourcetree_w}/depends/sources
mv %{sourcetree_contrib}/build/config.sample.json %{sourcetree_w}/
mv %{sourcetree_contrib}/build/*.tgz %{sourcetree_w}/depends/sources/
%endif


%build
# Build section starts us in directory {_builddir}/{sourceroot}

_pwd_d=$(pwd)/%{sourcetree_d}
_pwd_w=$(pwd)/%{sourcetree_w}

# Start in riot-web
cd ${_pwd_w}

#
# OPENSUSE
#
%if 0%{?suse_version:1}
  echo "======== OpenSUSE version: %{suse_version} %{sle_version}"
  echo "-------- Leap 15.1  will report as 1500 150100"
  echo "-------- Leap 15.2  will report as 1500 150200"
  echo "-------- Tumbleweed will report as 1550 undefined"
  npm install yarn
  #source ~/.bashrc
  #which yarn > /dev/null 2>&1
  #if [ "$?" -ne 0 ] ; then
    echo "\
# yarn alias inserted here by the Riot RPM specfile build script
# this can be removed after build is complete
alias yarn='${_pwd_w}/node_modules/.bin/yarn'" >> ~/.bashrc
    source ~/.bashrc
  #fi
  # Not needed as of 1.6.0?
  #yarn add electron-builder --dev
  #yarn add electron-packager --dev
%endif

#
# FEDORA
#
%if 0%{?fedora:1}
  echo "======== Fedora version: %{fedora}"
  %if 0%{?fedora} <= 29
    echo "Builds for Fedora 29 and older are no longer supported."
    exit 1
  %endif
  # Rules for Fedora 29+
  %if 0%{?fedora} >= 29
    #source ~/.bashrc
    #which yarn > /dev/null 2>&1
    #if [ "$?" -ne 0 ] ; then
      echo "\
# yarn alias inserted here by the Riot RPM specfile build script
# this can be removed after build is complete
# nodejs-yarn installs /usr/bin/yarnpkg for some reason (conflicts?). So, we
# simply alias it so that embedded scripts don't stumble over this anomaly
alias yarn='/usr/bin/yarnpkg'" >> ~/.bashrc
      source ~/.bashrc
    #fi
  # Rules for Fedora 28-
  %else
    npm install yarn
    #source ~/.bashrc
    #which yarn > /dev/null 2>&1
    #if [ "$?" -ne 0 ] ; then
      echo "\
# yarn alias inserted here by the Riot RPM specfile build script
# this can be removed after build is complete
alias yarn='${_pwd_w}/node_modules/.bin/yarn'" >> ~/.bashrc
      source ~/.bashrc
    #fi
    # Not needed as of Riot 1.6.0?
    #yarn add electron-builder --dev
    #yarn add electron-packager --dev
  %endif
%endif

#
# RHEL / CENTOS
#
%if 0%{?centos}
  echo "======== Centos version(s): %{centos} and %{centos_ver}"
%endif
%if 0%{?rhel:1}
  echo "======== EL version: %{rhel}"
  # I don't grok how to declare what python you are using so that scripting
  # tools know where to find it. So we do this hack.
  mkdir -p $HOME/.local/bin
  if [ ! -e "$HOME/.local/bin/python" ] ;  then
    ln -s /usr/bin/python3 $HOME/.local/bin/python
  fi
  %if 0%{?rhel} < 8
    # Note: If you did not add the two extra repos mentioned in the BuildRequires
    # section for EL7 into your build system, that build will fail.
  %else
    # EL8 is based on Fedora 28
    npm install yarn
    #source ~/.bashrc
    #which yarn > /dev/null 2>&1
    #if [ "$?" -ne 0 ] ; then
      echo "\
# yarn alias inserted here by the Riot RPM specfile build script
# this can be removed after build is complete
alias yarn='${_pwd_w}/node_modules/.bin/yarn'" >> ~/.bashrc
      source ~/.bashrc
    #fi
  %endif
  # EL all versions
  # Not needed as of 1.6.0?
  #yarn add electron-builder --dev
  #yarn add electron-packager --dev
%endif

#
# all distributions -- THE BUILD!
#
%define linuxunpacked_d dist/linux-unpacked
#%%define linuxunpacked_w_old electron_app/dist/linux-unpacked
#%%define linuxunpacked_w dist/linux-unpacked

### Build riot-web ###
cd ${_pwd_w}
yarn install 
yarn run build
# bug https://github.com/vector-im/riot-web/issues/9166 ... alerted by user "Aaron"
install -D -m644 -p config.sample.json webapp/config.json

# Used only if building a distributable riot-web
# and not a support build for riot-desktop
##ifarch x86_64 amd64
## ./node_modules/.bin/electron-builder -l tar.gz --x64
##else
## ./node_modules/.bin/electron-builder -l tar.gz --ia32
##endif
##install -D -m644 -p config.sample.json %%{linuxunpacked_w}/resources/webapp/config.json

### Build riot-desktop ###
cd ${_pwd_d}
yarn install 
yarn run build:native
# Pull webapp tree from riot-web, stage here, and place in archive
#cp -a ${_pwd_w}/webapp ./
./node_modules/.bin/asar pack ${_pwd_w}/webapp webapp.asar
#./node_modules/asar/bin/asar.js pack ${_pwd_w}/webapp webapp.asar
yarn run build


%install
# Install section starts us in directory {_builddir}/{sourceroot}

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

cp -a %{sourcetree_d}/%{linuxunpacked_d}/* %{buildroot}%{installtree}

# a little ugly - symbolic link creation
ln -s %{installtree}/%{_name_d} %{buildroot}%{_bindir}/%{name}

install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.16x16.png   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.22x22.png   %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.24x24.png   %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.32x32.png   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.48x48.png   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.hicolor.svg         %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/riot.svg

install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.16x16.png   %{buildroot}%{_datadir}/icons/HighContrast/16x16/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.22x22.png   %{buildroot}%{_datadir}/icons/HighContrast/22x22/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.24x24.png   %{buildroot}%{_datadir}/icons/HighContrast/24x24/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.32x32.png   %{buildroot}%{_datadir}/icons/HighContrast/32x32/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.48x48.png   %{buildroot}%{_datadir}/icons/HighContrast/48x48/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.128x128.png %{buildroot}%{_datadir}/icons/HighContrast/128x128/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.256x256.png %{buildroot}%{_datadir}/icons/HighContrast/256x256/apps/riot.png
install -D -m644 -p %{sourcetree_contrib}/desktop/riot.highcontrast.svg         %{buildroot}%{_datadir}/icons/HighContrast/scalable/apps/riot.svg

install -m755  %{sourcetree_contrib}/desktop/riot.wrapper.sh %{buildroot}%{_bindir}/
install -D -m644 -p %{sourcetree_contrib}/desktop/%{tld_vendor_product_id}.desktop %{buildroot}%{_datadir}/applications/%{tld_vendor_product_id}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{tld_vendor_product_id}.desktop
install -D -m644 -p %{sourcetree_contrib}/desktop/%{tld_vendor_product_id}.appdata.xml %{buildroot}%{_metainfodir}/%{tld_vendor_product_id}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

# /usr/lib/riot or /usr/lib64/riot...
## REMOVING FOR NOW. I DON'T THINK IT IS NEEDED AND IT HAS LEGAL ISSUES ##
##install -D -m755 -p %%{buildroot}%%{installtree}/libffmpeg.so %%{buildroot}%%{_libdir}/%%{name}/libffmpeg.so
##rm %%{buildroot}%%{installtree}/libffmpeg.so
install -D -m644 -p %{sourcetree_contrib}/etc-ld.so.conf.d_riot.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/riot.conf


%files
%defattr(-,root,root,-)
%license %{sourcetree_d}/LICENSE
# We own /usr/share/riot and everything under it...
%{installtree}
%{_datadir}/icons/*
%{_datadir}/applications/%{tld_vendor_product_id}.desktop
%{_metainfodir}/%{tld_vendor_product_id}.appdata.xml
%{_bindir}/*
%{_sysconfdir}/ld.so.conf.d/riot.conf
%dir %attr(755,root,root) %{_libdir}/%{name}
#%%{_libdir}/%%{name}/libffmpeg.so
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
* Sun Jul 05 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.8-1.taw
* Sun Jul 05 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.8-0.1.testing.taw
  - 1.6.8

* Mon Jun 29 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.7-1.taw
* Mon Jun 29 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.7-0.1.testing.taw
  - 1.6.7

* Thu Jun 25 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.6-1.1.testing.taw
  - fixed buildrequires for OpenSUSE Leap (libcrypto.so.1 is supplied by  
    libopenssl1_0_0 on Leap 15.1 and 15.2). Thank you, @DJViking.
  - Leap 15.1 and 15.2 still have issues due to a dated rust version that ships  
    with the OS. See also, https://github.com/taw00/riot-rpm/issues/34

* Tue Jun 23 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.6-1.taw
* Tue Jun 23 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.6-0.1.testing.taw
  - 1.6.6
  - riot.desktop and riot.appdata.xml now follow the freedesktop standard and  
    are named im.riot.Riot.desktop and im.riot.Riot.appdata.xml
  - libsecret-devel is a new BuildRequires

* Tue Jun 16 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.5-1.taw
* Tue Jun 16 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.5-0.1.testing.taw
  - 1.6.5
  - Fixes some regression and includes some minor upgrades.

* Mon Jun 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.4-1.taw
* Mon Jun 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.4-0.1.testing.taw
  - 1.6.4
  - Fixes a security issue, a regression, and a login bug.

* Mon Jun 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.2-1.1.testing.taw
  - The riot package provides too many things. Libraries in particular.  
    Removing that cruft.
  - Adjusting suse logic to allow for leap 15.2 builds.

* Fri May 22 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.2-1.taw
* Fri May 22 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.2-0.1.testing.taw
  - 1.6.2

* Tue May 19 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.1-1.taw
* Tue May 19 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.1-0.1.testing.taw
  - 1.6.1

* Tue May 05 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-1.taw
* Tue May 05 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.4.testing.taw
  - 1.6.0
  - riot on RHEL will not build. rustc is too dated and sqlcipher is missing.
  - riot on OpenSUSE 15.1 has similar issues.
  - RHEL and OpenSUSE 15.1 users: use the flatpak instead

* Fri May 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.3.rc.6.taw
  - 1.6.0 RC6

* Thu Apr 23 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.3.rc.4.taw
  - 1.6.0 RC4

* Sat Apr 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.3.rc.3.taw
* Sat Apr 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.2.rc.3.taw
* Fri Apr 17 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.1.rc.3.taw
* Thu Apr 16 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.1.rc.2.taw
  - 1.6.0 RC3
  - building from riot-web AND riot-desktop now. First web and then that  
    feeds into desktop.
  - new buildrequires: cargo python gcc-c++ cmake rust libxcrypt-compat  
    sqlcipher-devel
  - new requires: sqlcipher
  - Can't build for:
    - RHEL7: missing deps: libcrypt.so.1, sqlcipher, sqlcipher-devel
    - RHEL8: missing deps: sqlcipher, sqlcipher-devel and rustc is too old
             Note: if RHEL ever works: libxcrypt instead of libxcrypt-compat
    - OpenSUSE 15.1: missing deps: libcrypt.so.1
  - OpenSUSE Tumbleweed note: use libcrypt1 instead of libxcrypt-compat
  - Other note: contrib tarball now supplies a tweaked config.sample.json  
    because the upstream is missing a config option that enables Message  
    search even in encrypted environments.  
    The option: "feature_event_indexing": "enable"

* Thu Apr 16 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.15-2.taw
* Thu Apr 16 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.15-1.1.testing.taw
  - using the olm tarball distributed by the riot team  
    we provide it via the riot-*-contrib.tar.gz archive

* Wed Apr 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.15-1.taw
* Wed Apr 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.15-0.2.testing.taw
* Wed Apr 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.15-0.1.testing.taw
  - 1.5.15 - security fix
  - Updated riot.desktop to better match these changes:  
    https://github.com/flathub/im.riot.Riot/pull/93/files
  - curl added to BuildRequires (specifically OpenSUSE 15.1 needed it).

* Tue Mar 31 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.14-1.taw
* Tue Mar 31 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.14-0.1.testing.taw
  - 1.5.14

* Tue Mar 17 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.13-1.taw
* Fri Mar 13 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.13-0.1.rc.1.taw
  - 1.5.13

* Wed Mar 04 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.12-1.taw
* Wed Mar 04 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.12-0.1.testing.taw
  - 1.5.12

* Mon Mar 02 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.11-1.taw
* Mon Mar 02 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.11-0.1.testing.taw
  - 1.5.11

* Wed Feb 19 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.10-1.taw
* Wed Feb 19 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.10-0.1.testing.taw
  - 1.5.10

* Mon Feb 17 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.9-1.taw
* Sat Feb 15 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.9-0.1.rc.1.taw
  - 1.5.9
  - Source0 points at upstream now for rpmlint completeness

* Mon Jan 27 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.8-2.taw
* Mon Jan 27 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.8-1.1.testing.taw
  - spec file adjustment in order to build for opensuse 15.1

* Mon Jan 27 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.8-1.taw
* Mon Jan 27 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.8-0.1.testing.taw
* Fri Jan 24 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.8-0.1.rc.2.taw
  - 1.5.8

* Mon Jan 13 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.7-0.1.testing.taw
  - 1.5.7 -- not functional. Talked to the team and ... we'll wait to 1.5.8

* Mon Dec 9 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.6-1.taw
* Mon Dec 9 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.6-0.1.testing.taw
  - 1.5.6

* Wed Nov 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.5-1.taw
* Wed Nov 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.5-0.1.testing.taw
  - 1.5.5

* Tue Nov 26 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.4-1.taw
* Tue Nov 26 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.4-0.1.testing.taw
  - 1.5.4

* Wed Nov 06 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.3-1.taw
* Wed Nov 06 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.3-0.1.testing.taw
  - 1.5.3

* Fri Oct 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.0-1.taw
* Fri Oct 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.5.0-0.1.testing.taw
  - 1.5.0

* Fri Oct 04 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.2-1.taw
* Fri Oct 04 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.2-0.1.testing.taw
  - 1.4.2

* Tue Oct 01 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.1-1.taw
* Tue Oct 01 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.1-0.1.testing.taw
  - 1.4.1

* Sat Sep 28 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.0-2.taw
* Sat Sep 28 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.0-1.1.testing.taw
* Sat Sep 28 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.0-1.taw
* Sat Sep 28 2019 Todd Warner <t0dd_at_protonmail.com> 1.4.0-0.1.testing.taw
  - 1.4.0
  - all version need a symlink now (fedora 28 and below... maybe not?)
  - cleanup of specfile

* Thu Sep 19 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.6-1.taw
* Thu Sep 19 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.6-0.1.testing.taw
  - 1.3.6

* Wed Sep 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.5-1.taw
* Wed Sep 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.5-0.1.testing.taw
  - 1.3.5

* Thu Sep 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.4-1.taw
* Thu Sep 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.4-0.1.testing.taw
  - 1.3.4

* Fri Aug 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.3-1.taw
* Fri Aug 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.3-0.1.testing.taw
  - 1.3.3

* Thu Aug 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.2-1.taw
* Thu Aug 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.2-0.1.testing.taw
  - 1.3.2

* Mon Aug 05 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.1-1.taw
* Mon Aug 05 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.1-0.1.testing.taw
  - 1.3.1

* Thu Jul 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.0-1.taw
* Thu Jul 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.3.0-0.1.testing.taw
  - 1.3.0

* Tue Jul 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.4-3.taw
* Tue Jul 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.4-2.1.testing.taw
* Tue Jul 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.4-2.taw
* Tue Jul 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.4-1.1.testing.taw
  - 1.2.4 -- node_modules/.bin/electron-builder has to be symlinked to  
    node_modules/.bin/build for SUSE

* Fri Jul 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.4-1.taw
* Fri Jul 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.4-0.1.testing.taw
  - 1.2.4 -- SUSE and RHEL started to fail builds -- Fedora builds fine.

* Mon Jul 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.3-1.taw
* Mon Jul 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.3-0.1.testing.taw
  - 1.2.3

* Fri Jun 21 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.2-1.taw
* Fri Jun 21 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.2-0.1.testing.taw
  - 1.2.2

* Fri May 31 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.1-1.taw
* Fri May 31 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.1-0.1.testing.taw
  - 1.2.1

* Wed May 29 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.0-1.taw
* Wed May 29 2019 Todd Warner <t0dd_at_protonmail.com> 1.2.0-0.1.testing.taw
  - 1.2.0

* Sat May 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.2-1.taw
* Sat May 18 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.2-0.1.testing.taw
  - 1.1.2

* Tue May 14 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.1-1.taw
* Tue May 14 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.1-0.1.testing.taw
  - 1.1.1
  - minor tweak to contributed wrapper script

* Thu May 09 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.0-3.taw
* Thu May 09 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.0-2.1.testing.taw
* Thu May 09 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.0-2.taw
* Thu May 09 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.0-1.1.testing.taw
  - Updated desktop logo icons.
  - ...and then really fixed it for 2.1.testing and 3

* Tue May 07 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.0-1.taw
* Tue May 07 2019 Todd Warner <t0dd_at_protonmail.com> 1.1.0-0.1.testing.taw
  - 1.1.0

* Tue Apr 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.8-1.taw
* Tue Apr 16 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.8-0.1.testing.taw
  - 1.0.8
  - Note, riot-web source tarball (packaged inside the src.rpm) signed with  
    new GPG key found at https://github.com/vector-im/riot-web:  
    Primary key fingerprint: A878 CDF6 6CF4 A9B4 807C  EBE5 7469 2659 BDA3 D940  
         Subkey fingerprint: 5EA7 E0F7 0461 A3BC BEBE  4D5E F615 1806 0320 26F9

* Mon Apr 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.7-1.taw
* Mon Apr 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.7-0.1.testing.taw
  - 1.0.7

* Wed Apr 03 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.6-2.taw
* Wed Apr 03 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.6-1.1.testing.taw
  - yarn aliasing commented better in .bashrc  
    note, I can't determine a way to test yarn executable availability  
    without blowing up rpm builds with a $? > 0
  - testing on EL8-beta and Fedora 30

* Mon Apr 01 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.6-1.taw
* Mon Apr 01 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.6-0.1.testing.taw
  - 1.0.6
  - OpenSUSE 15.1 _and_ 15.0 now.
  - Attempt at EL8-beta ... failed for now.

* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-2.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.3.testing.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.2.testing.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.1.testing.taw
  - OpenSUSE Tumbleweed builds once again. Turns out, you need to include  
    ca certs in the base install. I am unsure which ones, so... I  
    installed a pile of them. Addresses github pull request #20  
    <https://github.com/taw00/riot-rpm/pull/20>

* Sun Mar 24 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.taw
* Sun Mar 24 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-0.1.testing.taw
  - 1.0.5
  - OpenSUSE Tumbleweed is failing to build once again. Yarn+SSL issues.

* Tue Mar 19 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.4-1.taw
* Tue Mar 19 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.4-0.1.testing.taw
  - 1.0.4
  - yarn replaces npm for js package management

* Fri Mar 15 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-4.taw
* Fri Mar 15 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-3.1.testing.taw
  - fixing https://github.com/vector-im/riot-web/issues/9166  
    no config.json file in the webapp directory... breaks certain indices

* Tue Mar 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-3.taw
* Tue Mar 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-2.1.testing.taw
  - Attempting to support EL7 builds by using nodesource repositories  
    this requires including their repository in your build environ...  
      https://rpm.nodesource.com/pub_8.x/el/7/$basearch  
    and a reasonably specific version of nodejs (which includes npm)  
    BuildRequires: nodejs = 2:8.15.1
  - Special thanks go out to Grant Stephenson for figuring this out.

* Tue Mar 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-2.taw
* Tue Mar 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-1.1.testing.taw
  - XDG_CURRENT_DESKTOP=Unity and not UNITY apparently. So fragile.

* Thu Mar 07 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-1.taw
* Thu Mar 07 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.3-0.1.testing.taw
  - 1.0.3

* Wed Mar 06 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.2-1.taw
* Wed Mar 06 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.2-0.1.testing.taw
  - 1.0.2

* Tue Feb 19 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.1-1.taw
* Tue Feb 19 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.1-0.1.testing.taw
  - v1.0.1
  - And OpenSuse (tumbleweed at least) builds work once again! :)

* Thu Feb 14 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.0-1.taw
* Thu Feb 14 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.0-0.1.testing.taw
* Fri Feb 08 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.0-0.1.rc.1.taw
  - v1.0.0

* Tue Jan 22 2019 Todd Warner <t0dd_at_protonmail.com> 0.17.9-1.taw
* Tue Jan 22 2019 Todd Warner <t0dd_at_protonmail.com> 0.17.9-0.1.testing.taw
  - v0.17.9

* Thu Dec 13 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.8-2.taw
* Thu Dec 13 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.8-1.1.testing.taw
  - wrapper script in order to enable riot to better deal with the  
    KDE+Electron issue (mentioned below). And discussed here...  
    <https://github.com/taw00/riot-rpm/issues/16>  
    Using a more generic approach to the problem since the prior solution  
    assumed all desktops needed to be fixed, which is not the case. This  
    may introduce other issues, but it is headed in the right direction.

* Mon Dec 10 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.8-1.taw
* Mon Dec 10 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.8-0.1.testing.taw
  - v0.17.8

* Fri Nov 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.7-1.taw
* Fri Nov 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.7-0.1.testing.taw
  - v0.17.7

* Wed Nov 21 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.6-1.taw
* Wed Nov 21 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.6-0.1.testing.taw
  - v0.17.6

* Thu Nov 15 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.5-0.1.testing.taw
  - v0.17.5
  - specfile: reduced some of the complexity

* Mon Nov 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-2.taw
* Mon Nov 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-1.1.testing.taw
  - /usr/share/applications/riot.desktop file Exec line updated to work  
    better with KDE Plasma desktops. Something to do with an electron bug 
    or somesuch.
  - Now it reads: `Exec=env XDG_CURRENT_DESKTOP=Unity /usr/bin/riot`  
    instead of `Exec=/usr/bin/riot`
  - Credit to @luminoso:chat.naoestusou.eu

* Sun Nov 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-1.taw
* Sun Nov 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-0.1.testing.taw
  - v0.17.3

* Wed Oct 24 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.2-1..taw
* Wed Oct 24 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.2-0.1.testing.taw
  - v0.17.2

* Tue Oct 16 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.0-1.taw
* Tue Oct 16 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.0-0.1.testing.taw
  - v0.17.0

* Mon Oct 15 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.6-1.taw
* Mon Oct 15 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.6-0.1.testing.taw
  - v0.16.6

* Sat Oct 06 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.5-1.taw
* Sat Oct 06 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.5-0.1.testing.taw
  - v0.16.5

* Wed Sep 19 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.4-1.taw
* Wed Sep 19 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.4-0.1.testing.taw
  - v0.16.4

* Mon Sep 03 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.3-1.taw
* Mon Sep 03 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.3-0.1.testing.taw
  - v16.3

* Wed Aug 29 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.2-1.taw
* Wed Aug 29 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.2-0.1.testing.taw
  - v0.16.2

* Wed Aug 22 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.1-1.taw
* Wed Aug 22 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.1-0.1.testing.taw
  - v0.16.1

* Mon Jul 30 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.0-1.taw
* Mon Jul 30 2018 Todd Warner <t0dd_at_protonmail.com> 0.16.0-0.1.testing.taw
  - v0.16.0

* Wed Jul 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-1.taw
* Wed Jul 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-0.1.testing.taw
  - v0.15.7

* Mon Jul 09 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-0.1.rc.2.taw
  - v0.15.7 RC2

* Sun Jul 01 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.7-0.1.rc.1.taw
  - v0.15.7 RC1

* Sun Jul 01 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.6-1.taw
* Sun Jul 01 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.6-0.2.testing.taw
  - v0.15.6

* Sat Jun 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.6-0.1.rc.2.taw
  - v0.15.6 RC2

* Sat Jun 16 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.5-1.taw
* Sat Jun 16 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.5-0.1.testing.taw
  - v0.15.5

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
  - v0.15.4 testing

* Fri May 25 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.3-2.taw
  - Updated v0.15.3 builds that are more OpenSuse compatible

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
  - v0.15.3

* Wed May 23 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.3-0.1.testing.taw
  - v0.15.3 testing
  - minor spec file cleanup
  - locking down supported architectures w/ ExclusiveArch

* Thu May 17 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.2-1.taw
  - v0.15.2

* Thu May 17 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.2-0.1.testing.taw
  - v0.15.2 testing

* Sat May 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.0-0.1.rc.3.taw
  - v0.15.0-rc.3
  - Added back the required libffmpeg.so library - my experiment failed. :(

* Sat May 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.0-0.1.rc.2.taw
  - fixed dependency issue

* Fri May 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.15.0-0.1.rc.2.taw
  - v0.15.0 release candidate
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
  - v0.14.2-rc.final

* Fri Apr 27 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.2-0.1.rc.3.taw
  - v0.14.2-rc.3

* Thu Apr 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.14.1-1.taw
  - GA build for 0.14.1

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
    - Obsoletes done right.
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

