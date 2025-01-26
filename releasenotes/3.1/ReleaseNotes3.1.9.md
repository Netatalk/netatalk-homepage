# Netatalk 3.1.9

The Netatalk development team is proud to announce latest release of the
Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

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

### Changes in 3.1.9

- FIX: afpd: fix "admin group" option

- NEW: afpd: new options "force user" and "force group"

- FIX: listening on IPv6 wildcard address may fail if IPv6 is disabled,
  bug \#606

- NEW: LibreSSL support, FR \#98

- FIX: cannot build when acl is not defined, bug \#574

- UPD: configure option "--with-init-style=" for Gentoo. "gentoo" is
  renamed to "gentoo-openrc". "gentoo-openrc" is same as "openrc".
  "gentoo-systemd" is same as "systemd".

- NEW: configure option "--with-dbus-daemon=PATH" for Spotlight feature

- UPD: use "tracker daemon" command instead of "tracker-control" command
  if Gnome Tracker is the recent version.

- NEW: configure options "--enable-rpath" and "--disable-rpath" which
  can be used to force setting of RPATH (default on Solaris/NetBSD) or
  disable it.

- NEW: configure option "--with-tracker-install-prefix" allows setting
  an alternate install prefix for tracker when cross-compiling.

- UPD: asip-status.pl: IPv6 support

- UPD: asip-status.pl: show GSS-UAM SPNEGO blob

- FIX: afpd: don’t use network IDs without LDAP, bug \#621

- FIX: afpd: reading from file may fail, bug \#619

- NEW: AFP clients should not be able to copy or manipulate special
  extended attributes set by NFS and SMB servers on Solaris, issue \#36

- FIX: ad: ad cp may crash, bug \#622

- UPD: Update Unicode support to version 9.0.0

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

- The Netatalk Development Team, July 2016
