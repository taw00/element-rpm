# changelog
* Thu Jul 23 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-3.taw
* Thu Jul 23 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-2.4.testing.taw
  - reducing the PNG icon set to 64, 128, 256, and 512

* Wed Jul 22 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-2.3.testing.taw
  - adding back the png icons: the spec does not require both png and svg  
    icons, but certain external desktop components expect PNGs. Plus the  
    appstream spec states that PNGs are preferred. gnome-software goes one  
    step further and will only work with PNGs.
  - a bit more explicit about what this rpm owns on the file system

* Tue Jul 21 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-2.2.testing.taw
  - spec adherance refinement:
    - icons: element.png (and .svg) --> io.element.Element.png (and .svg)
    - icons: only installing the .svg images (pngs are redundant)
    - .appdata.xml --> .metainfo.xml
  - /usr/share/element --> /usr/share/io.element.Element
  - element.wrapper.sh --> io.element.Element.wrapper.sh
  - the libdir configuration stuff is not needed. Removed.
  - call appid what it is, appid (instead of tld\_vendor\_product\_id)
  - metainfo.xml file was missing the launchable tag and corrected screenshot urls

* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-2.1.testing.taw
  - github repo: taw00/riot-rpm --> taw00/element-rpm

* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-2.taw
* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-1.1.testing.taw
  - riot.im moved to element.io, not element.im

* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-1.taw
* Sat Jul 18 2020 Todd Warner <t0dd_at_protonmail.com> 1.7.1-0.1.testing.taw
  - 1.7.1
  - App name change. From Riot to Element (as of 1.7.0).

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
    with the OS. See also, https://github.com/taw00/element-rpm/issues/34

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

* Mon Jun 01 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.2-2.taw
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
  - 1.6.0
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

* Thu Apr 16 2020 Todd Warner <t0dd_at_protonmail.com> 1.6.0-0.1.rc.2.taw
  - 1.6.0
  - new buildrequires: sqlcipher-devel

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
* Fri Jan 24 2020 Todd Warner <t0dd_at_protonmail.com> 1.5.8-0.1.rc2.taw
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
  - 1.2.4 -- node\_modules/.bin/electron-builder has to be symlinked to  
    node_modules/.bin/build for RHEL and SUSE

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
  - Attempt at RHEL8-beta ... failed for now.

* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-2.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.3.testing.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.2.testing.taw
* Wed Mar 27 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.1.testing.taw
  - OpenSUSE Tumbleweed builds once again. Turns out, you need to include  
    ca certs in the base install. I am unsure which ones, so... I  
    installed a pile of them. Addresses github pull request #20  
    <https://github.com/taw00/element-rpm/pull/20>

* Sun Mar 24 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-1.taw
* Sun Mar 24 2019 Todd Warner <t0dd_at_protonmail.com> 1.0.5-0.1.testing.taw
  - 1.0.5

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
  - XDG\_CURRENT\_DESKTOP=Unity and not UNITY apparently. So fragile.

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
    <https://github.com/taw00/element-rpm/issues/16>  
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

* Thu Nov 15 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.5-1.taw
* Thu Nov 15 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.5-0.1.testing.taw
  - v0.17.5
  - specfile: reduced some of the complexity

* Mon Nov 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-2.taw
* Mon Nov 12 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-1.1.testing.taw
  - /usr/share/applications/riot.desktop file Exec line updated to work
    better with KDA Plasma desktops. Something to do with an electron bug
    or somesuch.
  - Now it reads: `Exec=env XDG_CURRENT_DESKTOP=Unity /usr/bin/riot`
    instead of `Exec=/usr/bin/riot`
  - Credit to @luminoso:chat.naoestusou.eu

* Sun Nov 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-1..taw
* Sun Nov 11 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.3-0.1.testing.taw
  - v0.17.3

* Wed Oct 24 2018 Todd Warner <t0dd_at_protonmail.com> 0.17.2-1.taw
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
  - v0.16.3

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

* Sat May 26 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.4-2.taw
* Sat May 26 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.4-1.3.testing.taw
* Sat May 26 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.4-1.2.testing.taw
* Sat May 26 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.4-1.1.testing.taw
  - Recieving HTTP 429 errors. This is due to rate-limiting on the nodejs  
    registry servers for anyone pulling down npm's via non-ssl calls. Which,  
    we have to do for OpenSuse builds. So... I added more refinded OS distro  
    querying logic.
  - A pile of sleeps added to slow things down for opensuse builds. Probably  
    does nothing.
  - TODO: include all deps so that no over-the-wire calls are necessary

* Fri May 25 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.4-1.taw
  - v0.15.4

* Fri May 25 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.4-0.1.testing.taw
  - v0.15.4 testing

* Fri May 25 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.3-2.taw
  - Updated v15.3 builds that are more OpenSuse compatible

* Thu May 24 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.3-1.1.testing.taw
  - Reverted the hardcoded Requires (broke Suse builds)
  - Trying to make this OpenSuse compatible (Suse builds don't like https for  
    some reason):  
    ```
npm ERR! code UNABLE_TO_GET_ISSUER_CERT_LOCALLY
npm ERR! errno UNABLE_TO_GET_ISSUER_CERT_LOCALLY
npm ERR! request to https://registry.npmjs.org/minimist failed, reason: unable to get local issuer certificate
    ```

* Wed May 23 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.3-1.taw
  - v0.15.3

* Wed May 23 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.3-0.1.testing.taw
  - v0.15.3 testing
  - minor spec file cleanup
  - locking down supported architectures w/ ExclusiveArch

* Thu May 17 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.2-1.taw
  - v0.15.2

* Thu May 17 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.2-0.1.testing.taw
  - v0.15.2 testing

* Sat May 12 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.0-0.1.rc.3.taw
  - v0.15.0-rc.3
  - Added back the required libffmpeg.so library - my experiment failed. :(

* Sat May 12 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.0-0.1.rc.2.taw
  - fixed dependency issue

* Fri May 11 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.15.0-0.1.rc.2.taw
  - v0.15.0 release candidate
  - attempted to yank libffmpeg.so from the package. FAILED (added back later)
  - had to manually construct the Requires because can't exclude from AutoReq
  - map proper lib (or lib64) path to the /etc/ld.so.conf.d/riot.conf file
  - spec file: mkdir without -p can be problematic on repeat builds.

* Sat May 5 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-2.taw
  - Update after testing

* Sat May 5 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-1.1.testing.taw
  - Tweaked the .desktop and .appdata.xml files a bit (more conforming)
  - Apparrently, `name_at_example.com` is more "standard" for email formatting.

* Thu May 3 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-1.taw
  - release 14.2

* Thu May 3 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-0.2.rc.final.taw
  - 14.2-rc.final

* Fri Apr 27 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-0.1.rc.3.taw
  - 14.2-rc.3

* Thu Apr 12 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.1-1.taw
  - GA build for 14.1

* Thu Apr 12 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.1-0.1.testing.taw
  - Release: 740b221 (git) v0.14.1
  - Cleaned up %%files a bit (too broad of inclusion)
  - https://github.com/vector-im/riot-web/releases/tag/v0.14.1

* Thu Apr 12 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.0-0.2.testing.taw
  - Added an 'npm cache clean --force' (and more) to hopefully address cache  
    integrity issues (sha1 integrity checks, namely). Very ugly.
  - Refactored the nvrea bits yet again.
  - Fixed /usr/lib versus /usr/lib64
  - rpmlint and Packaging Guidelines compliance fixes:
    - Removed "Vender:" and "Packager:" - that's why we have changelogs.
    - Source0 has a github URL and there is additional instruction above
    - Obsolotes done right.
    - Moved all the application code to /usr/share/riot (opt is frowned upon)
    - Removed %%clean and removed the buildroot cleanup in %%install section
    - Made the Summary: compliant (shorter, no ending period, no name repeat
  - Restructured the contrib tarball.

* Wed Apr 11 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.0-1.taw
  - Release: eaeb495 - 0.14.0
  - Changelog: https://github.com/vector-im/riot-web/releases/tag/v0.14.0
  - Changes specific to these builds...
  - name-version-release more closely matches industry guidelines:  
    https://fedoraproject.org/wiki/Packaging:Versioning
  - A lot of spec file cleanup.

* Tue Apr 10 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.13.5-3.taw
  - Added an 'npm cache clean --force' to hopefully about cache integrity  
    issues (sha1 integrity checks, namely)

* Mon Apr 9 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.0-0.1.rc.6.taw
  - Release - 7445456 - 0.14-0 RC6
  - name-version-release more closely matches industry guidelines:  
    https://fedoraproject.org/wiki/Packaging:Versioning
  - A lot of spec file cleanup.
  - Nuked .build\_ids in order to avoid conflicts.

* Sun Feb 11 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.13.5-1.taw
  - Adjusted location of libffmpeg and libnode in order to avoid conflicts.

* Fri Feb 09 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.13.5-0.taw
  - Updated upstream source that fixes a security issue with external URL  
    management.
  - https://github.com/vector-im/riot-web/releases/tag/v0.13.5

* Sat Jan 06 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.13.4-0.taw
  - Updated upstream source that fixes one of the default configuration files.
  - https://github.com/vector-im/riot-web/releases/tag/v0.13.4

* Wed Dec 06 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.13.3-1.taw
  - Updated upstream source.
  - https://github.com/vector-im/riot-web/releases/tag/v0.13.3
  - Bumped to -1.taw to fix this changelog date which was incorrectly labeled.

* Fri Nov 17 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.13.0-1.taw
  - Fedora 27 does not install 7zip-bin-linux when you perform "npm install",  
    so we specifically add it.

* Fri Nov 17 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.13.0-0.taw
  - Updated upstream source.

* Tue Oct 24 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.12.7-0.taw
  - Updated upstream source.

* Mon Sep 25 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.12.6-0.taw
  - Updated upstream source.
  - Updated build tree structure.

* Tue Apr 25 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.9-0.taw
  - Updated upstream source.

* Sun Apr 16 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.8-0.taw
  - Updated upstream source.

* Sun Feb 05 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.7-1.0.taw
  - Updated upstream source.

* Sat Jan 21 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.6-1.2.taw
  - Tweaks

* Mon Jan 16 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.6-1.1.taw
  - Small restructuring

* Mon Jan 16 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.6-1.0.taw
  - 0.9.6

* Mon Jan 09 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.5-1.5.taw
  - improved icons a bit

* Wed Jan 04 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.5-1.4.taw
  - Package renamed riot instead of riot-web -- cuz, it's not a webapp. :)

* Tue Jan 03 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.5-1.3.taw
  - Fixing icons
  - Moving towards calling the package riot, versus riot-web, which
  - makes little sense. Undecided.

* Tue Jan 03 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.5-1.2.taw
  - Fixing icons

* Sun Jan 01 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.5-1.1.taw
  - Minor tweaks.

* Sun Jan 01 2017 Todd Warner `<t0dd_at_protonmail.com>` 0.9.5-1.0.taw
  - Initial build. Everything still ends up in /opt/Riot (messy) but... meh.

