# Netatalk 3.1.1

The Netatalk development team is proud to announce the seconf release of
the Netatalk 3.1 release series. Early adopters are encouraged to update
production systems.

Netatalk is a freely-available Open Source AFP fileserver. A \*NIX/\*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

The suite contains:

- netatalk - the main server service controller

- afpd - the AFP file server daemin

- cnid_metad - the CNID database multiplexing daemon

- cnid_dbd - the CNID database daemon serving CNIDs for AFP volumes

- various supporting programs and utilities

### Summary of major new features and enhancements in 3.1

- AFP Spotlight Support with Gnome Tracker:
  <https://projects.gnome.org/tracker/>

Please refer to the online manual for details about compiling Netatalk
with Spotlight support and how to configure:

<http://netatalk.sourceforge.net/3.1/htmldocs/installation.html#compiling-netatalk>

<http://netatalk.sourceforge.net/3.1/htmldocs/configuration.html>

Please make sure to read the upgrading section in the Netatalk online
manual before trying to upgrade your system from version 2:

<http://netatalk.sourceforge.net/3.1/htmldocs/upgrade.html>

### License

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPLv2). The full license text is
available at:

<http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt>

### Changes in 3.1.1

- FIX: Add asprint() compatibility function for systems lacking it

- FIX: Fix ressource fork name conversion. Bug \#534.

- FIX: Fix a bug where only the first configured UAM was loaded. Bug
  \#537.

- UPD: Add support for AFP 3.4. From FR \#85.

- FIX: Registering with mDNS crashed. Bug \#540

- FIX: Saving from applications like Photoshop may fail, because
  removing the ressource fork AppleDouble file failed. Bug \#542.

- FIX: dbd: remove orphaned .\_ AppleDouble files. Bug \#549.

- NEW: afpd: Automatic conversion of .\_ AppleDouble files created by
  OS X. Bug \#550.

- FIX: afpd: Fix a crash in of_closefork(). Bug \#551.

- FIX: dbd: Don’t print message "Ignoring .*file" for every .* file. Bug
  \#552.

- FIX: afpd: Don’t flood log with failed sys_set_ea() messages.

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

- The Netatalk Development Team, March 2014
