# changelog
* Sat May 5 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-2.taw[n]
  - Update after testing

* Sat May 5 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-1.1.testing.taw[n]
  - Tweaked the .desktop and .appdata.xml files a bit (more conforming)
  - Apparrently, `name_at_example.com` is more "standard" for email formatting.

* Thu May 3 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-1.taw[n]
  - release 14.2

* Thu May 3 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-0.2.rc.final.taw[n]
  - 14.2-rc.final

* Fri Apr 27 2018 Todd Warner `<t0dd_at_protonmail.com>` 0.14.2-0.1.rc.3.taw[n]
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

* Wed Apr 11 2018 Todd Warner <t0dd@protonmail.com> 0.14.0-1.taw
  - Release: eaeb495 - 0.14.0
  - Changelog: https://github.com/vector-im/riot-web/releases/tag/v0.14.0
  - Changes specific to these builds...
  - name-version-release more closely matches industry guidelines:  
    https://fedoraproject.org/wiki/Packaging:Versioning
  - A lot of spec file cleanup.

* Tue Apr 10 2018 Todd Warner <t0dd@protonmail.com> 0.13.5-3.taw
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

