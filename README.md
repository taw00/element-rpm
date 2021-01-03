# Element: decentralized, encrypted chat & collaboration

_.&nbsp;.&nbsp;.&nbsp;packaged for Fedora and OpenSUSE_

> IMPORTANT!!!
> * If you encounter a problem that looks like this: `Curl error (6): Couldn't resolve host name for https://download.copr.fedoraproject.org/...` when you run dnf or zypper.
> * There is a solution: Follow the "Prep" step below for your distribution and you will be functional again.
> * Why does this happen: Because I screwed up and pushed out a repo configuration with the wrong URL. A deeply embarassing mistake.
> My apologies -todd

_**What is Element?**_ Decentralized, encrypted chat & collaboration powered by [matrix].

_**What is Matrix?**_ An open network for secure, decentralized communication.

In short, Element is an open-source, decentralized, end-to-end encrypted, team collaboration platform who's often compared to IRC, Rocket Chat, Mattermost, Slack, and Discord.

> Element was once branded Riot. The name changed as of version 1.7.0 (July, 2020).

More fully, Element is a desktop application implementing the client-side of the matrix protocol enabling decentralized, secure messaging for collaborative groups. This repository enables Element to be easily installed and maintained on the Fedora, Red Hat(IBM), and OpenSUSE family of Linux operating systems and tracks the source surrounding those builds. This GitHub repository maintains source RPM packages and spec files so you can rebuild Element if you are so inclined, though prebuilt binaries have been conveniently built for you. See below for how to install and run Element on your Linux desktop.

All `*.src.rpm` packages provided in this GitHub repository are signed with [my GPG key](https://keybase.io/toddwarner/key.asc)<br />All binary RPMs are signed with the [Fedora Project's](https://fedoraproject.org/) [COPR GPG signing key](https://download.copr.fedorainfracloud.org/results/taw/element/pubkey.gpg)

> Please note that packages also exist for Android, Apple products, and Microsoft Windows. Element for the web (Chromebook and anyone) is available here: <https://app.element.io/> — slick!

#### More about&nbsp;.&nbsp;.&nbsp;.

* Element: <https://element.io/> and the source repositories, [riot-desktop](https://github.com/vector-im/riot-desktop) and [riot-web](https://github.com/vector-im/riot-web)
* Matrix: <https://matrix.org/> and <https://en.wikipedia.org/wiki/Matrix_(communication_protocol)>
* A couple reviews from [some dude](http://www.1500wordmtu.com/2016/slack-no-more-why-you-should-use-riotim-and-matrixorg), [TechCrunch](https://techcrunch.com/2016/09/19/riot-wants-to-be-like-slack-but-with-the-flexibility-of-an-underlying-open-source-platform/), and the [Slant community](https://www.slant.co/options/12764/~matrix-review)<br />_Unsurprisingly, I personally think Element is superior to Slack and Rocket Chat._

# tl;dr&nbsp;.&nbsp;.&nbsp;.

## I just want to install Element!

It's easy to install, run, and maintain Element. Current builds are provided for these platforms (x86\_64 only)&nbsp;.&nbsp;.&nbsp;.  
_Note: I will stop building for any version of an OS that is itself no longer supported_

Successful builds:
* **CentOS:** versions 8 and Stream (as of Element 1.7.16)
* **Fedora:** versions 31+
* **OpenSUSE:** Tumbleweed and Leap 15.2 as of Element 1.7.1

Alternative builds:
* **Flatpak:** Leap 15.1 and EL8(RHEL/CentOS) folks can use the Element-team supplied Flatpak: <https://flathub.org/apps/details/im.riot.Riot> Ideally, we'd have native builds available for Leap 15.1 and RHEL/CentOS, alas. Using a Flatpak (or, for that matter, a Snap or an AppImage) is a brute-force solution, but it is a solution.

Unsuccessful and Struggling builds:
* **CentOS (and RHEL):**
  - A missing sqlcipher RPM is a major issue for CentOS builds. See also GitHub
    issues [#31](https://github.com/taw00/element-rpm/issues/31) and
[#33](https://github.com/taw00/element-rpm/issues/33). Until now (see next
bullet) one had to rely on the element flatpak for support. No longer! Or no
longer at least for now. :)
  - I was finally, as of 2021-01-03, able to work around it by building my own
    sqlcipher RPM for the CentOS repos. CentOS8 is essentially Fedora 28. I
rebuilt the sqlcipher RPM found
[here](https://rpms.remirepo.net/rpmphp/zoom.php?rpm=sqlcipher) (specifically
[here](https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/28/Everything/source/tree/Packages/s/sqlcipher-3.4.1-2.fc28.src.rpm)).
Please note that some of the links on that first page have changed. Read
[this](https://dl.fedoraproject.org/pub/fedora/linux/releases/28/README).
* **OpenSUSE:**
  - Leap 15.1: Riot 1.5 and older only. See also GitHub issue [#32](https://github.com/taw00/element-rpm/issues/32). Install "Flatpak" instead—see above—or upgrade to a newer OpenSUSE.

### [Fedora and CentOS]

**Prep&nbsp;.&nbsp;.&nbsp;.**
```bash
sudo dnf install -y dnf-plugins-core distribution-gpg-keys
sudo dnf copr enable taw/element
```

<!--
.&nbsp;.&nbsp;.&nbsp;alternative&nbsp;.&nbsp;.&nbsp;.
```bash
# Install GPG keys
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo rpm --import https://download.copr.fedorainfracloud.org/results/taw/element/pubkey.gpg
# Configure and enable the Element repository (fc31, fc32, etc ... doesn't matter)
sudo dnf install https://download.copr.fedorainfracloud.org/results/taw/element/fedora-32-x86_64/01571621-toddpkgs-element-repo/toddpkgs-element-repo-1.7-5.fc32.taw.noarch.rpm
```
-->

**Install&nbsp;.&nbsp;.&nbsp;.**
```bash
sudo dnf install -y element --refresh
```

### [OpenSUSE]

**Prep (Leap 15.2)&nbsp;.&nbsp;.&nbsp;.**
```bash
# Install GPG keys
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo rpm --import https://download.copr.fedorainfracloud.org/results/taw/element/pubkey.gpg
# Configure and enable the Element repository
sudo zypper install https://download.copr.fedorainfracloud.org/results/taw/element/opensuse-leap-15.2-x86_64/01571621-toddpkgs-element-repo/toddpkgs-element-repo-1.7-5.suse.lp152.taw.noarch.rpm
sudo zypper modifyrepo -er "element-stable"
sudo zypper refresh
```

**Prep (Tumbleweed)&nbsp;.&nbsp;.&nbsp;.**
```bash
# Install GPG keys
sudo rpm --import https://keybase.io/toddwarner/key.asc
sudo rpm --import https://download.copr.fedorainfracloud.org/results/taw/element/pubkey.gpg
# Configure and enable the Element repository
sudo zypper install https://download.copr.fedorainfracloud.org/results/taw/element/opensuse-tumbleweed-x86_64/01571621-toddpkgs-element-repo/toddpkgs-element-repo-1.7-5.suse.tw.taw.noarch.rpm
sudo zypper modifyrepo -er "element-stable"
sudo zypper refresh
```

**Install&nbsp;.&nbsp;.&nbsp;.**
```bash
sudo zypper install element
```

## I installed it, now I want to run Element!

Search for and select "Element" from your desktop environment. Done!

Note: If none of this made sense or you couldn't get it to work, Element can also be run as directly from your browser at <https://app.element.io/>

## I installed it, now I want to ensure I get future updates!

> Please Note
>
> If within your Element settings > Preferences, you have enabled _"Show tray
> icon and minimize window to it on close"_ when you exit Element, it minimizes
> and does not truly exit and upgrades will not be evident until the next
> reboot.
> 
> If you disable that setting, when you exit Element, it truly exits.

Once you have followed the repository and installation instructions above, you should be notified of any future updates enabling you to update the software automatically. And you can always force a check with&nbsp;.&nbsp;.&nbsp;.

```bash
# Fedora . . .
sudo dnf upgrade
```

```bash
# OpenSUSE . . .
sudo zypper update
```

I do this as a hobby, but I will try to be timely with my updates.

<!--
## I live on the edge! Do you have test packages available?

Yes!

1. Follow the steps described above to install the repository configure file.  
   _You will have to refresh it if you have done this before today._
2. Disable the stable repository and enable the testing repository...
```
# Fedora and RHEL/CentOS only
sudo dnf config-manager - - set-disabled element-stable
sudo dnf config-manager - - set-enabled riot-testing
sudo dnf list - - refresh |grep element
```
-->


# Disclaimer

I built these for my own use. I offer these builds for your own convenience (and have now for a long time). If it 'splodes your computer, I am sorry, but buyer beware. :) I am in no way affiliated with the originators of Element—[New Vector Ltd/Element](https://element.io/)—but I do thank them for their wonderful application and the community appreciates their welcoming approach to contributors like myself.

# Questions or comments&nbsp;.&nbsp;.&nbsp;.

Contact: **t0dd_at_protonmail.com** or find me at **@t0dd:matrix.org** after you have installed Element!

