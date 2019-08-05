# changelog
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
    <https://github.com/taw00/riot-rpm/pull/20>

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
    <https://github.com/taw00/riot-rpm/issues/16>  
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

