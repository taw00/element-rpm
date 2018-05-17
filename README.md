# Riot

> _Native RPM package builds for Fedora, CentOS, and Red Hat Enterprise Linux_

Riot is a client implementing the matrix protocol enabling decentralized, secure messaging for collaborative groups. It's a great client, but it needed RPM packages built for the Red Hat family of linux operating systems. So... here they be!

_**What is Riot (and Matrix)?**_ In short, Riot is an open source, decentralized, end-to-end encrypted team collaboration platform who's often compared to IRC, Rocket Chat, Mattermost, Slack, etc.

Included directly here in this github repository are source RPM packages and specfiles so you can rebuild Riot if you are so inclined. But runnable binaries have also been built. See below for how to install and run Riot on your linux desktop.

All \*.src.rpm packages provided in this github repository should be signed with [my GPG key](https://keybase.io/toddwarner/key.asc)<br />All binary RPMs are signed with the [Fedora Project's](https://fedoraproject.org/) [Copr GPG signing key](https://copr-be.cloud.fedoraproject.org/results/taw/Riot/pubkey.gpg)

#### More about...

* Riot: <https://riot.im/> and <https://github.com/vector-im/riot-web>
* Matrix: <https://matrix.org/> and <https://en.wikipedia.org/wiki/Matrix_(communication_protocol)>
* A couple reviews from [some dude](http://www.1500wordmtu.com/2016/slack-no-more-why-you-should-use-riotim-and-matrixorg), [TechCrunch](https://techcrunch.com/2016/09/19/riot-wants-to-be-like-slack-but-with-the-flexibility-of-an-underlying-open-source-platform/), and the [Slant community](https://www.slant.co/options/12764/~matrix-review)<br />_Unsurprisingly, I personally think Riot is superior to Slack and Rocket Chat._

# tl;dr ...

## I just want to install Riot!

It's easy to install and run Riot. Currently built for these platforms...

* Fedora: versions 26, 27, 28 -- x86\_64, i686<br />
  NOTE: I will stop building for any version of an OS that is no longer supported
* CentOS (and RHEL): version 7 -- x86\_64 only
* The test repositories: I will usually try to build test packages for any OS that is in beta if I have time.

### For Fedora...

_Note that, by default, the 'riot-stable' repository will be enabled and 'riot-testing' will not._ 

**Prep...**
```bash
# Snag the repository configuration (should only need to do once)
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo dnf install -y https://raw.githubusercontent.com/taw00/riot-rpm/master/toddpkgs-riot-repo-1.0-3.fc28.taw0.noarch.rpm
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
sudo yum install -y https://raw.githubusercontent.com/taw00/riot-rpm/master/toddpkgs-riot-repo-1.0-3.el7.centos.taw0.noarch.rpm
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

I do this as a hobby, but I will try to be timely with my updates.

## I live on the edge! Do you have test packages available?

Yes! As of April 10, 2018, I started building test packages!

1. Follow the steps described able to install the repository configure file.  
   _You will have to refresh it if you have done this before today._
2. Edit that file &mdash;`riot-messaging-client.fedora.repo` or `riot-messaging-client.epel.repo`&mdash; and "enable=1" the riot-testing repository, and "enable=0" the riot-stable repository.


# Disclaimer

I built these for my own use. I offer these builds for your own convenience. If it 'splodes your computer, I am sorry, but buyer beware. :) I am in no way affiliated with the orginators of Riot -- Vector Creations Ltd. (of Amdocs) -- but I do thank them for their contribution.

# Questions or comments...

Contact: **t0dd_at_protonmail.com** or find me at **@t0dd:matrix.org** after you installed Riot!
