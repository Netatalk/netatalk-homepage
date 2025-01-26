# Netatalk 3.0.1

The Netatalk development team is proud to announce version 3.0.1 of the
Netatalk File Sharing suite. This is the latest update to the 3.0
release series. All users are encouraged to upgrade their systems to
3.0.1.

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

- New default AppleDouble backend using filesytem Extended Attributes,
  conversion from AppleDouble v2 is done automatically on access

- New service controller process "netatalk" responsible for starting and
  restarting afpd and cnid_metad as necessary

- AppleTalk support has been removed

- Coherent cross-platform locking with Solaris CIFS server

Please make sure to read the upgrading section in the Netatalk online
manual before trying to upgrade your system to 3.0!
<div class="literalblock">

<div class="content monospaced">

    http://netatalk.sourceforge.net/3.0/htmldocs/upgrade.html

### License

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPLv2). The full license text is
available at:
<div class="literalblock">

<div class="content monospaced">

    http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


### Changes in 3.0.1

- NEW: afpd: Optional "ldap uuid encoding = string \| ms-guid" parameter
  to afp.conf, allowing for usage of the binary objectGUID fields from
  Active Directory.

- FIX: afpd: Fix a Solaris 10 SPARC sendfilev bug

- FIX: afpd: Fix a crash on FreeBSD

- FIX: afpd: Fixes open file handle refcounting bug which was reported
  as being unable to play movies off a Netatalk AFP share. Bug ID
  3559783.

- FIX: afpd: Fix a possible data corruption when reading from and
  writing to the server simultaniously under load

- FIX: Fix possible alignment violations due to bad casts

- FIX: dbd: Fix logging

- FIX: apple_dump: Extended Attributes AppleDouble support for \*BSD

- FIX: handling of */* and *:* in volume name

- UPD: Install relevant includes necessary for building programs with
  installed headers and shared lib libatalk

- UPD: libevent configure args to pick up installed version. Removed
  configure arg --disable-libevent, added configure args
  --with-libevent-header\|lib.

- UPD: gentoo initscript: merge from portage netatalk.init,v 1.1

- REM: Remove --with-smbsharemodes configure option, it was an empty
  stub not yet implemented

### Changes in 3.0

- UPD: afpd: force read only mode if cnid scheme is last

- REM: afpd: removed global option "icon"

- FIX: CNID path for user homes

### Changes in 3.0 beta2

- UPD: Solaris and friends: Replace initscript with SMF manifest

- FIX: Solaris and friends: resource fork handling

### Changes in 3.0 beta1

- UPD: afpd: Performance tuning of read/write AFP operations. New option
  "afp read locks" (default: no) which disables that the server applies
  UNIX byte range locks to regions of files in AFP read and write calls.

- UPD: apple_dump: Extended Attributes AppleDouble support. (\*BSD is
  not supported yet)

### Changes in 3.0 alpha3

- NEW: afpd: Per volume "login message", NetAFP bug ID \#18

- NEW: afpd: Cross-platform locking (share modes) on Solaris and
  derivates with Solaris CIFS/SMB server. Uses new Solaris fcntl F_SHARE
  share reservation locking primitives. Enabled by default, set global
  "solaris share reservations" option to false to disable it.

- NEW: ad: ad set subcommand for changing Mac metadata on the server

- UPD: unix charset is UTF8 by default vol charset is same value as unix
  charset by default

- UPD: .AppleDesktop/ are stored in \$localstatedir/netatalk/CNID
  (default: /var/netatalk/CNID), databases found in AFP volumes are
  automatically moved

- FIX: afpd: Server info packet was malformed resulting in broken server
  names being displayed on clients

- FIX: afpd: Byte order detection. Fixes an error where Netatalk on
  OpenIndiana returned wrong volume size information.

### Changes in 3.0 alpha2

- UPD: afpd: Store *.* as is and */* as *:* on the server, don’t CAP
  hexencode as "2e" and "2f" respectively

- UPD: afdp: Automatic name conversion, renaming files and directories
  containing CAP sequences to their not enscaped forms

- UPD: afpd: Correct handling of user homes and users without homes

- UPD: afpd: Perform complete automatic adouble:v2 to adouble:ea
  conversion as root. Previously only unlinking the adouble:v2 file was
  done as root

- UPD: dbd: -C option removes CAP encoding

- UPD: Add graceful option to RedHat init script

- UPD: Add --disable-bundled-libevent configure options When set to yes,
  we rely on a properly installed version on libevent CPPFLAGS and
  LDFLAGS should be set properly to pick that up

- UPD: Run ldconfig on Linux at the end of make install

- FIX: afpd: ad cp on appledouble = ea volumes

- FIX: dbd: ignore .\_ appledouble files

- REM: Volumes options "use dots" and "hex encoding"

### Changes in 3.0 alpha1

- NEW: Central configuration file afp.conf which replaces all previous
  files

- NEW: netatalk: service controller starting and restarting afpd and
  cnid_metad as necessary

- NEW: afpd: Extended Attributes AppleDouble backend (default)

- UPD: CNID databases are stored in \$localstatedir/netatalk/CNID
  (default: /var/netatalk/CNID), databases found in AFP volumes are
  automatically moved

- UPD: Start scripts and service manifests have been changed to only
  start the new netatalk service controller process

- UPD: afpd: UNIX privileges and use dots enabled by default

- UPD: afpd: Support for arbitrary AFP volumes using variable expansion
  has been removed

- UPD: afpd: afp_voluuid.conf and afp_signature.conf location has been
  changed to \$localstatedir/netatalk/ (default: /var/netatalk/)

- UPD: afpd: default server messages dir changed to
  \$localstatedir/netatalk/msg/

- UPD: dbd: new option -C for conversion from AppleDouble v2 to ea

- REM: AppleTalk support has been removed

- REM: afpd: SLP and AFP proxy support have been removed

- REM: afpd: legacy file extension to type/creator mapping has been
  removed

- REM: afpd: AppleDouble backends v1, osx and sfm have been removed

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

- The Netatalk Development Team, September 2012
