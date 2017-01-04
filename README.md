# Riot is...<br />·	decentralized, secure messaging for collaborative groups<br />· a client developed upon the matrix protocol

## *Native builds for Fedora, CentOS, and Red Hat Enterprise Linux.*

Riot is a fantastic client for communicating using the Matrix communication protocol. But it needed RPMs built for the Red Hat family of linux operating systems. So... here they be!

_**What is Riot (and Matrix)?**_ In short, Riot is an open source, decentralized, end-to-end encrypted team collaboration platform who's often compared to IRC, Rocket Chat, Mattermost, Slack, etc.

Included directly here in this github repository are source RPM packages and specfiles so you can rebuild Riot if you are so inclined. But runnable binaries have also been built. See below for how to install and run Riot on your linux desktop. 

All \*.src.rpm packages here should be signed with [my GPG key](https://keybase.io/toddwarner/key.asc)<br />All binary RPMs are signed with the [Fedora Project's](https://fedoraproject.org/) [Copr GPG signing key](https://copr-be.cloud.fedoraproject.org/results/taw/Riot/pubkey.gpg)

#### More about...

* Riot: <https://riot.im/> and <https://github.com/vector-im/riot-web>
* Matrix: <https://matrix.org/> and <https://en.wikipedia.org/wiki/Matrix_(communication_protocol)>
* A couple reviews from [some dude](http://www.1500wordmtu.com/2016/slack-no-more-why-you-should-use-riotim-and-matrixorg), [TechCrunch](https://techcrunch.com/2016/09/19/riot-wants-to-be-like-slack-but-with-the-flexibility-of-an-underlying-open-source-platform/), and the [Slant community](https://www.slant.co/options/12764/~matrix-review)<br />_Unsurprisingly, I personally think Riot is superior to Slack and Rocket Chat._

## I just want to install Riot!

It's easy to install and run Riot, on these currently supported platforms...

* Fedora: versions 24, 25, 26 -- x86_64, i686
* CentOS (and RHEL): version 7 -- x86_64 only

### For Fedora...

```
sudo dnf install -y dnf-plugins-core
sudo dnf copr enable taw/Riot
sudo dnf install -y riot
```

### For CentOS or RHEL...

```
sudo yum install -y yum-plugin-copr
sudo yum copr enable taw/Riot
sudo yum install -y riot
```

**Optional set the metadata_expire value to something other than the default 2d (2 days):**<br />
_Note: It's the same setting whether Fedora, CentOS, or RHEL._

```
cat $(/etc/yum.repos.d/_copr_taw-Riot.repo) > temp.repo
echo "metadata_expire=1d" >> temp.repo
sudo mv -v temp.repo /etc/yum.repos.d/_copr_taw-Riot.repo
```

## I installed it, now I want to run Riot!

Search for and select "Riot" from your desktop or run `riot` from the commandline.

Note: Riot can also be run as SaaS at <https://riot.im/app>

## I installed it, now I want to ensure I get future updates!

Once you have followed the repository and installation instructions above, you should be notified of any future updates enabling you to update the software automatically. I do this as a hobby, but I will try to be timely with my updates.

## Disclaimer

I built these for my own use. I offer these builds for your own convenience. If it 'splodes your computer, I am sorry, but buyer beware. :) I am in no way affiliated with the orginators of Riot -- Vector Creations Ltd. (of Amdocs) -- but I do thank them for their contribution.

## Questions or comments...

Contact: **t0dd@protonmail.com** or find me at **@t0dd:matrix.org** after you installed Riot!
