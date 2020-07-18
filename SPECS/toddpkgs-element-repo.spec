Name:       toddpkgs-element-repo
Version:    1.7

%define targetIsProduction 1
%define _release 2
%if ! %{targetIsProduction}
  %define _release 1.1.testing
%endif
Release:   %{_release}%{?dist}.taw

# Name of package is no longer toddpkgs-riot-repo
Provides: toddpkgs-riot-repo = 1.7
Obsoletes: toddpkgs-riot-repo < 1.7

Summary:    Repository configuration to enable management of Element packages

Group:      System Environment/Base
License:    MIT
URL:        https://github.com/taw00/riot-rpm
Source0:    https://github.com/taw00/riot-rpm/raw/master/SOURCES/toddpkgs-element-repo-1.7.tar.gz
BuildArch:  noarch


%description
Todd (aka, taw, taw00, t0dd in various communities) packages applications for
Fedora Linux, RHEL/CentOS/EPEL, and OpenSUSE. This package deploys the
repository configuration file necessary to enable on-going management of the
Element messaging client RPM package.

Install this package, and then...

* For fedora:
  sudo dnf install element -y --refresh

* For CentOS or RHEL:
  sudo yum clean expire-cache
  sudo yum install element -y

* For OpenSuse Leap
  sudo zypper refresh
  sudo zypper modifyrepo -er "element-stable"
  sudo zypper install element

* For OpenSuse Tumbleweed
  sudo zypper refresh
  sudo zypper modifyrepo -er "element-stable"
  sudo zypper install element

You can edit /etc/yum.repos.d/element.repo (as root) and 'enable=1' or '0'
whether you want the stable or the testing repositories.

Notes about GPG keys:
* An RPM signing key is included. It is used to sign RPMs that I build by
  hand. Namely any *.src.rpm found in github.com/taw00/riot-rpm and (for now)
  all the binary OpenSuse packages
* RPMs from the copr repositories are signed by fedoraproject build system
  keys.


%prep
%setup -q
# For debugging purposes...
#cd .. ; tree -df -L 1  ; cd -


%build
# no-op


%install
# Builds generically. Will need a disto specific RPM though.
install -d %{buildroot}%{_sysconfdir}/yum.repos.d
install -d %{buildroot}%{_sysconfdir}/zypp/repos.d
install -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg

install -D -m644 todd-694673ED-public-2030-01-04.2016-11-07.asc %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-todd-694673ED-public

##
## Fedora
##
%if 0%{?fedora:1}
  install -D -m644 element-fedora.repo %{buildroot}%{_sysconfdir}/yum.repos.d/element.repo
%endif
##
## EL (Epel)
##
%if 0%{?rhel:1}
%if 0%{?rhel} < 8
  %{error: "Builds for versions of RHEL/CentOS < 8 can no longer be supported."}
%else
%if 0%{?rhel} < 9
  install -D -m644 element-el8.repo %{buildroot}%{_sysconfdir}/yum.repos.d/element.repo
%endif
%endif
%endif
##
## OpenSUSE
##
# https://en.opensuse.org/openSUSE:Packaging_for_Leap#RPM_Distro_Version_Macros
%if 0%{?is_opensuse:1}
%if 0%{?sle_version:1}
  # We're not checking for version of leap
  install -D -m644 element-suse-leap.repo %{buildroot}%{_sysconfdir}/zypp/repos.d/element.repo
%else
  install -D -m644 element-suse-tumbleweed.repo %{buildroot}%{_sysconfdir}/zypp/repos.d/element.repo
%endif
%endif


%files
%attr(644, root,root) %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-todd-694673ED-public
%license LICENSE

%if 0%{?fedora:1}
  %config(noreplace) %attr(644, root,root) %{_sysconfdir}/yum.repos.d/element.repo
%endif

%if 0%{?rhel:1}
  %config(noreplace) %attr(644, root,root) %{_sysconfdir}/yum.repos.d/element.repo
%endif

%if 0%{?suse_version:1}
  %config(noreplace) %attr(644, root,root) %{_sysconfdir}/zypp/repos.d/element.repo
%endif


%changelog
* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7-2.taw
* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7-1.1.testing.taw
* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7-1.taw
* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7-0.1.testing.taw
  - Riot is now Element
  - SUSE uses the COPR repos as well.
  - Repo moved from COPR taw/Riot to taw/element

* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0-8.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0-7.1.testing.taw
  - got leap and tumbleweed working! In COPR!

* Wed Mar 20 2019 Todd Warner <t0dd_at_protonmail.com> 1.0-7.taw
* Wed Mar 20 2019 Todd Warner <t0dd_at_protonmail.com> 1.0-6.1.testing.taw
  - Apparently, my EPEL URL was "too generic" and would fail for some people.  
    Made more explicit.

* Tue Mar 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.0-6.taw
* Tue Mar 12 2019 Todd Warner <t0dd_at_protonmail.com> 1.0-5.1.testing.taw
  - OpenSuse Tumbleweed now supported by COPR

* Mon Dec 17 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-5.taw
* Mon Dec 17 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-4.1.testing.taw
  - enabled_metadata needs to be set to 0 because COPR repos do not managed  
    appstream metadata correctly  
    <https://srvfail.com/packagekit-cant-find-file-in-var-cache-packagekit/>

* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-4.taw
* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-3.3.testing.taw
* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-3.2.testing.taw
  - OpenSuse uses /etc/zypp and not /etc/yum... apparently. :/
  - Need a license for this package. Punted, like everyone else, and chose MIT
  - Added type and autorefresh flags to repofile
  - Made leap specific SPEC file. This (primary spec) will work generically  
    though defaulting to opensuse tumbleweed.

* Fri May 25 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-3.1.testing.taw
  - Support for OpenSuse

* Sat May 12 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-3.taw
  - Update.

* Sat May 12 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-2.1.testing.taw
  - metadata for test repo expires immediately.
  - fixed error in test repo URL (for fedora)

* Sun May 6 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-2.taw
  - Update.

* Sun May 6 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-1.1.testing.taw
  - Made the rep info desplayed when updating less noisy. It annoyed me.

* Sun Apr 15 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-1.taw
  - Initial build

* Sun Apr 15 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-0.1.testing.taw
  - Initial test build

