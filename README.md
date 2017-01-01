# riot-rpms
Riot (riot-web or riot.im/app) matrix.org messaging client built for Fedora Linux, CentOS, and Red Hat Enterprise Linux

Riot is a fantastic client for communicating using the Matrix.org protocol. But it needed RPMs built for the Red Hat family of linux operating systems. So... here they be!

Included directly here are SRPMs and specfiles so you can rebuild Riot if you like. But binaries have been built for these platforms (see below on how to install and run Riot on your desktop). 

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

## I installed it, now I want to run Riot!

Search for and select "Riot" from your desktop or run `riot-web` from the commandline.

Note: Riot can also be run as SaaS at <https://riot.im/app>

## I installed it, now I want to ensure I get future updates!

Once you have followed the repository and installation instructions above, you should be notified of any future updates enabling you to update the software automatically. I do this as a hobby, but I will try to be timely with my updates.

## Questions or comments...

Contact: **t0dd@protonmail.com**
