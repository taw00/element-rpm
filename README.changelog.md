# changelog
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

