# riot-rpms
Riot (riot-web or riot.im/app) matrix.org messaging client built for Fedora Linux, CentOS/RHEL

Riot is a fantastic client for communicating using the Matrix.org protocol. But... it needed RPMs built for the Red Hat family of linux operating systems. So... here be it!

Included here are SRPMs and specfiles so you can rebuilt it if you like. But binaries have been built for these platforms:

* x86_64, i686 on Fedora 24, 25, 26
* x86_64 on CentOS 7 (which works for RHEL7 as well)

All *.src.rpm packages should be signed with my GPG key: <https://keybase.io/toddwarner/key.asc>

## I just want to install Riot!

It's easy to install and run Riot...

### For Fedora...
```
sudo dnf install -y dnf-plugins-core
sudo dnf copr enable taw/Riot
sudo dnf install -y riot-web
```

### For CentOS or RHEL...
```
sudo yum install -y yum-plugin-copr
sudo yum copr enable taw/Riot
sudo yum install -y riot-web
```

### To run Riot...

Search for and select "Riot" from your desktop or run `riot-web` from the commandline.

Note: Riot can also be run as SaaS at <https://riot.im/app>
