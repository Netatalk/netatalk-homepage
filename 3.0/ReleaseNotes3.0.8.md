# Netatalk 3.0.8

The Netatalk development team is proud to announce version 3.0.8 of the
Netatalk File Sharing suite. This is the latest update to the 3.0
release series. All users are encouraged to upgrade their systems to
3.0.8.

Netatalk is a freely-available Open Source AFP fileserver. A \*NIX/\*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

The suite contains:

- netatalk - the main server service controller

- afpd - the AFP file server daemin

- cnid_metad - the CNID database multiplexing daemon

- cnid_dbd - the CNID database daemon serving CNIDs for AFP volumes

- various supporting programs and utilities

### Summary of major new features and enhancements in 3.0

- New ini style configuration file afp.conf which replaces all previous
  configuration files

- New default AppleDouble backend using filesystem Extended Attributes,
  conversion from AppleDouble v2 is done automatically on access

- New service controller process "netatalk" responsible for starting and
  restarting afpd and cnid_metad as necessary

- AppleTalk support has been removed

- Coherent cross-platform locking with Solaris CIFS server

Please make sure to read the upgrading section in the Netatalk online
manual before trying to upgrade your system to 3.0!


    http://netatalk.sourceforge.net/3.0/htmldocs/upgrade.html

### License

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPLv2). The full license text is
available at:


    http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


### Changes in 3.0.8

- FIX: dbd: remove orphaned .\_ AppleDouble files. Bug \#549.

- FIX: afpd: Fix a crash in of_closefork(). Bug \#551.

### Supported Platforms

As of Netatalk 3.0 the following operating systems are supported:

- FreeBSD

- Linux

- OpenBSD

- NetBSD

- Solaris and derivates

Netatalk may compile and run on other operating systems as well, but it
is not well-tested on those. We welcome patches and suggestions for
enhancing the portability of Netatalk as well as success and failure
stories. Please write to <netatalk-devel@lists.sourceforge.net>.

### Availability

Netatalk tar-balls can be found at:

<http://sourceforge.net/project/showfiles.html?group_id=8642>

Netatalk is also available via anonymous git. See the SourceForge
project site for anonymous git instructions.

### Contact

For more information about Netatalk, see its web page at:

<http://netatalk.sourceforge.net/>

The project is hosted at SourceForge. The SourceForge project page is
located at:

<http://sourceforge.net/projects/netatalk/>

The Netatalk development team can be reached via the mailing list
<netatalk-devel@lists.sourceforge.net>. For subscription information and
archives see Netatalk’s SourceForge project page.

<netatalk-admins@lists.sourceforge.net> is a mailing list for Netatalk
system administrators. For subscription information and archives see the
Netatalk web page.

### Acknowledgements

We would like to thank all contributors to the Netatalk project for
their commitment. Without the many suggestions, bug and problem reports,
patches, and reviews this project wouldn’t be where it is.

- The Netatalk Development Team, February 2014
