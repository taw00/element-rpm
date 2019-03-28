# Riot Messaging Application for the Desktop

_Riot messaging client packaged (RPMs) for Fedora, CentOS, Red Hat Enterprise Linux, and OpenSuse_

Riot is a client implementing the matrix protocol enabling decentralized, secure messaging for collaborative groups. It's a great client, but it needed RPM packages built for the Red Hat family of linux operating systems. So... here they be!

_**What is Riot (and Matrix)?**_ In short, Riot is an open source, decentralized, end-to-end encrypted team collaboration platform who's often compared to IRC, Rocket Chat, Mattermost, Slack, etc.

This github repository maintains source RPM packages and specfiles so you can rebuild Riot if you are so inclined. From these source packages runnable binaries have been conveniently built for you. See below for how to install and run Riot on your linux desktop.

All \*.src.rpm packages provided in this github repository should be signed with [my GPG key](https://keybase.io/toddwarner/key.asc)<br />All binary RPMs are signed with the [Fedora Project's](https://fedoraproject.org/) [Copr GPG signing key](https://copr-be.cloud.fedoraproject.org/results/taw/Riot/pubkey.gpg)

#### More about...

* Riot: <https://riot.im/> and <https://github.com/vector-im/riot-web>
* Matrix: <https://matrix.org/> and <https://en.wikipedia.org/wiki/Matrix_(communication_protocol)>
* A couple reviews from [some dude](http://www.1500wordmtu.com/2016/slack-no-more-why-you-should-use-riotim-and-matrixorg), [TechCrunch](https://techcrunch.com/2016/09/19/riot-wants-to-be-like-slack-but-with-the-flexibility-of-an-underlying-open-source-platform/), and the [Slant community](https://www.slant.co/options/12764/~matrix-review)<br />_Unsurprisingly, I personally think Riot is superior to Slack and Rocket Chat._

# tl;dr ...

## I just want to install Riot!

It's easy to install and run Riot. Currently built for these platforms (x86\_64 only)...  
_Note: I will stop building for any version of an OS that is itself no longer supported_

* Fedora: versions 28, 29
* CentOS (and RHEL): version 7
* OpenSuse: Tumbleweed and Leap 15
* The test repositories: I will usually try to build test packages for any OS that is in beta if I have time.

### For Fedora...

_Note that, by default, the 'riot-stable' repository will be enabled and 'riot-testing' will not._ 

**Prep...**
```bash
# Snag the repository configuration (should only need to do once)
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo dnf install -y https://github.com/taw00/riot-rpm/raw/master/toddpkgs-riot-repo-fedora.rpm
```
**Install...**
```bash
# install Fedora's distribution GPG keys (should only need to do once)
sudo dnf install -y distribution-gpg-keys
# Install riot
sudo dnf install -y riot --refresh
```

_Note: If you installed the repository information by hand in the past, you may
have to clean up a file named `riot-messaging-client*.repo` in
`/etc/yum.repos.d/`_ 

### For CentOS or RHEL...

_Note that, by default, the 'riot-stable' repository will be enabled and 'riot-testing' will not._ 

**Prep...**
```bash
# Snag the repository configuration (should only need to do once)
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo yum install -y https://github.com/taw00/riot-rpm/raw/master/toddpkgs-riot-repo.epel.rpm
```
**Install...**
```bash
# install distribution GPG keys (should only need to do once)
sudo yum install -y distribution-gpg-keys
# Clean out the cache in case the change didn't get picked up
sudo yum clean expire-cache
# Install riot
sudo yum install -y riot
```

_Note: If you installed the repository information by hand in the past, you may
have to clean up a file named `riot-messaging-client*.repo` in
`/etc/yum.repos.d/`_ 

### For OpenSuse...

_Note that OpenSUSE support is still hit or miss._

**Prep (OpenSuse Leap)...**
```bash
# Snag the repository configuration (should only need to do once)
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo zypper install https://github.com/taw00/riot-rpm/raw/master/toddpkgs-riot-repo.suse.leap.rpm
sudo zypper modifyrepo -er "riot-stable-leap"
```

**Prep (OpenSuse Tumbleweed)...**
```bash
# Snag the repository configuration (should only need to do once)
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo zypper install https://github.com/taw00/riot-rpm/raw/master/toddpkgs-riot-repo.suse.tw.rpm
sudo zypper modifyrepo -er "riot-stable"
```

**Install...**
```bash
# Clean out the cache in case the change didn't get picked up
sudo zypper refresh
# Install riot
sudo zypper install riot
```

## I installed it, now I want to run Riot!

Search for and select "Riot" from your desktop or run `riot` from the commandline.

Note: If none of this made sense or you couldn't get it to work, Riot can also be run as SaaS from your browser at <https://riot.im/app>

## I installed it, now I want to ensure I get future updates!

Once you have followed the repository and installation instructions above, you should be notified of any future updates enabling you to update the software automatically. And you can always force a check with...

```bash
# Fedora...
sudo dnf upgrade
```
```bash
# CentOS or RHEL...
sudo yum update
```
```bash
# OpenSuse...
sudo zypper update
```

I do this as a hobby, but I will try to be timely with my updates.

## I live on the edge! Do you have test packages available?

Yes! As of April 10, 2018, I started building test packages (Fedora and Epel only).

1. Follow the steps described above to install the repository configure file.  
   _You will have to refresh it if you have done this before today._
2. Disable the stable repo and enable the testing repo...
```
# Fedora only
sudo dnf config-manager --set-disabled riot-stable
sudo dnf config-manager --set-enabled riot-testing
sudo dnf list --refresh |grep riot
```


# Disclaimer

I built these for my own use. I offer these builds for your own convenience. If it 'splodes your computer, I am sorry, but buyer beware. :) I am in no way affiliated with the orginators of Riot -- [New Vector](https://vector.im/) -- but I do thank them for their contribution.

# Questions or comments...

Contact: **t0dd_at_protonmail.com** or find me at **@t0dd:matrix.org** after you installed Riot!
