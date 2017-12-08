# Riot

> _Native RPM package builds for Fedora, CentOS, and Red Hat Enterprise Linux_

Riot is a client implementing the matrix protocol enabling decentralized, secure messaging for collaborative groups. It's a great client, but it needed RPM packages built for the Red Hat family of linux operating systems. So... here they be!

_**What is Riot (and Matrix)?**_ In short, Riot is an open source, decentralized, end-to-end encrypted team collaboration platform who's often compared to IRC, Rocket Chat, Mattermost, Slack, etc.

Included directly here in this github repository are source RPM packages and specfiles so you can rebuild Riot if you are so inclined. But runnable binaries have also been built. See below for how to install and run Riot on your linux desktop.

All \*.src.rpm packages here should be signed with [my GPG key](https://keybase.io/toddwarner/key.asc)<br />All binary RPMs are signed with the [Fedora Project's](https://fedoraproject.org/) [Copr GPG signing key](https://copr-be.cloud.fedoraproject.org/results/taw/Riot/pubkey.gpg)

#### More about...

* Riot: <https://riot.im/> and <https://github.com/vector-im/riot-web>
* Matrix: <https://matrix.org/> and <https://en.wikipedia.org/wiki/Matrix_(communication_protocol)>
* A couple reviews from [some dude](http://www.1500wordmtu.com/2016/slack-no-more-why-you-should-use-riotim-and-matrixorg), [TechCrunch](https://techcrunch.com/2016/09/19/riot-wants-to-be-like-slack-but-with-the-flexibility-of-an-underlying-open-source-platform/), and the [Slant community](https://www.slant.co/options/12764/~matrix-review)<br />_Unsurprisingly, I personally think Riot is superior to Slack and Rocket Chat._

# tl;dr ...

## I just want to install Riot!

It's easy to install and run Riot, on these currently supported platforms...

* Fedora: versions 25, 26, 27 -- x86_64, i686<br />
  NOTE: Fedora 25 versions will become unsupported in 2018<br />
  NOTE2: **Having issues building Riot on Fedora 25, 26, and CentOS/RHEL.** Working on it! (2017-12-08)
* CentOS (and RHEL): version 7 -- x86_64 only

### For Fedora...

```
cd /etc/yum.repos.d/
sudo curl -O https://raw.githubusercontent.com/taw00/riot-rpm/master/riot-messaging-client.fedora.repo
sudo dnf install -y riot --refresh
```

...OR... if you prefer to use Fedora Project's Copr directly, follow the instructions found at this link: <https://copr.fedorainfracloud.org/coprs/taw/Riot/>


### For CentOS or RHEL...

```
cd /etc/yum.repos.d/
sudo curl -O https://raw.githubusercontent.com/taw00/riot-rpm/master/riot-messaging-client.epel.repo
sudo yum clean expire-cache
sudo yum install -y riot
```

...OR... if you prefer to use Copr (Fedora Project) directly, follow the instructions found at this link: <https://copr.fedorainfracloud.org/coprs/taw/Riot/>

<!--
**Optional set the metadata_expire value to something other than the default 2d (2 days):**<br />
_Note: It's the same setting whether Fedora, CentOS, or RHEL._

If you prefer to use Copr (Fedora Project) directly, do this...
```
cat $(/etc/yum.repos.d/_copr_taw-Riot.repo) > temp.repo
echo "metadata_expire=1d" >> temp.repo
sudo mv -v temp.repo /etc/yum.repos.d/_copr_taw-Riot.repo
```
-->

## I installed it, now I want to run Riot!

Search for and select "Riot" from your desktop or run `riot` from the commandline.

Note: If none of this made sense or you couldn't get it to work, Riot can also be run as SaaS from your browser at <https://riot.im/app>

## I installed it, now I want to ensure I get future updates!

Once you have followed the repository and installation instructions above, you should be notified of any future updates enabling you to update the software automatically. And you can always force a check with...

```
# Fedora...
sudo dnf upgrade
```
```
# CentOS or RHEL...
sudo yum update
```

I do this as a hobby, but I will try to be timely with my updates.

# Disclaimer

I built these for my own use. I offer these builds for your own convenience. If it 'splodes your computer, I am sorry, but buyer beware. :) I am in no way affiliated with the orginators of Riot -- Vector Creations Ltd. (of Amdocs) -- but I do thank them for their contribution.

# Questions or comments...

Contact: **t0dd@protonmail.com** or find me at **@t0dd:matrix.org** after you installed Riot!
