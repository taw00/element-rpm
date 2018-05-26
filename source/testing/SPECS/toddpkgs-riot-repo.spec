Name:		toddpkgs-riot-repo
Version:	1.0
Release:	3.2.testing%{?dist}.taw0
Summary:	Repository configuration to enable management of Riot packages

Group:		System Environment/Base
License:	MIT
URL:		https://github.com/taw00/riot-rpm
Source0:	https://raw.githubusercontent.com/taw00/riot-rpm/master/testing/source/SOURCES/toddpkgs-riot-repo-1.0.tar.gz
BuildArch:	noarch
#BuildRequires:  tree

# CentOS/RHEL/EPEL can't do "Suggests:"
%if 0%{?fedora:1}
Suggests:	distribution-gpg-keys-copr
%endif


%description
Todd (aka, taw, taw00, t0dd in various communities) packages applications for
Fedora Linux and RHEL/CentOS/EPEL. This package deploys the repository
configuration file necessary to enable on-going management of the Riot
messaging client RPM package for Fedora Linux and CentOS/RHEL/EPEL.

Install this, then...

* For fedora:
  sudo dnf install riot -y --refresh

* For CentOS or RHEL:
  sudo yum clean expire-cache
  sudo yum install riot -y

* For OpenSuse Leap
  sudo zypper refresh
  sudo zypper modifyrepo -er "riot-stable-leap"
  sudo zypper install riot

* For OpenSuse Tumbleweed
  sudo zypper refresh
  sudo zypper modifyrepo -er "riot-stable-tumbleweed"
  sudo zypper install riot

You can edit /etc/yum.repos.d/riot.repo (as root) and 'enable=1' or '0'
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

%if 0%{?fedora:1}
  install -D -m644 riot-fedora.repo %{buildroot}%{_sysconfdir}/yum.repos.d/riot.repo
%endif
%if 0%{?rhel:1}
  install -D -m644 riot-epel.repo %{buildroot}%{_sysconfdir}/yum.repos.d/riot.repo
%endif
%if 0%{?suse_version:1}
  install -D -m644 keybase-toddwarner_riot-opensuse.repo %{buildroot}%{_sysconfdir}/zypp/repos.d/riot.repo
%endif


%files
%attr(644, root,root) %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-todd-694673ED-public
%license LICENSE

%if 0%{?fedora:1}
%config(noreplace) %attr(644, root,root) %{_sysconfdir}/yum.repos.d/riot.repo
%endif

%if 0%{?rhel:1}
%config(noreplace) %attr(644, root,root) %{_sysconfdir}/yum.repos.d/riot.repo
%endif

%if 0%{?suse_version:1}
%config(noreplace) %attr(644, root,root) %{_sysconfdir}/zypp/repos.d/riot.repo
%endif


%changelog
* Sat May 26 2018 Todd Warner <t0dd_at_protonmail.com> 1.0-3.2.testing.taw
  - OpenSuse uses /etc/zypp and not /etc/yum... apparently. :/
  - Need a license for this package. Punted, like everyone else, and chose MIT

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

