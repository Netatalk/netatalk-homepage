<div id="header">

<div id="logo">

</div>

<div id="menlinks">

[\[main\]](/ "Return to Netatalk home")
[\[wiki\]](/docs "Netatalk Wiki")
[\[documentation\]](/documentation.html "Netatalk Manual")
[\[downloads\]](/download.html "Download Netatalk")
[\[support\]](/support.html "Support")
[\[links\]](/links.html "Netatalk related links")
<img src="/gfx/end.gif" width="125" height="7" />

</div>

</div>

<div id="header-print">

# netatalk.io

</div>

<div class="search">

#### search netatalk.io

<span class="italic">powered by Google</span>

</div>

<div id="content">

# Netatalk 3.1-beta2

<div id="body">

<div class="paragraph">

The Netatalk development team is proud to announce the second beta
release of the next Netatalk version 3.1. This release is intended for
testing only.

</div>

<div class="paragraph">

Netatalk is a freely-available Open Source AFP fileserver. A \*NIX/\*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

</div>

<div class="paragraph">

The suite contains:

</div>

<div class="ulist">

- netatalk - the main server service controller

- afpd - the AFP file server daemin

- cnid_metad - the CNID database multiplexing daemon

- cnid_dbd - the CNID database daemon serving CNIDs for AFP volumes

- various supporting programs and utilities

</div>

</div>

### Summary of major new features and enhancements in 3.1

<div class="ulist">

- AFP Spotlight Support with Gnome Tracker:
  <https://projects.gnome.org/tracker/>

</div>

<div class="paragraph">

Please refer to the online manual for details about compiling Netatalk
with Spotlight support and how to configure:

</div>

<div class="paragraph">

<http://netatalk.sourceforge.net/3.1/htmldocs/installation.html#compiling-netatalk>

</div>

<div class="paragraph">

<http://netatalk.sourceforge.net/3.1/htmldocs/configuration.html#id2615270>

</div>

<div class="paragraph">

Please make sure to read the upgrading section in the Netatalk online
manual before trying to upgrade your system from version 2:

</div>

<div class="paragraph">

<http://netatalk.sourceforge.net/3.1/htmldocs/upgrade.html>

</div>

### License

<div class="paragraph">

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPLv2). The full license text is
available at:

</div>

<div class="paragraph">

<http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt>

</div>

### Changes in 3.1-beta2

<div class="ulist">

- FIX: Fix special Spotlight RPC function

</div>

### Changes in 3.1-beta1

<div class="ulist">

- REM: Remove support for Tracker versions \< 0.7

- UPD: Add support for additional Spotlight RPC calls

</div>

### Changes in 3.1-alpha1

<div class="ulist">

- NEW: AFP Spotlight support with Gnome Tracker

- NEW: New option "spotlight" (G/V)

- NEW: Configure option --with-tracker-pkgconfig-version

- NEW: Configure option --with-tracker-prefix

- NEW: If Spotlight is enabled, launch our own dbus instance

- NEW: New option "dbus daemon" (G)

- UPD: Add configure option --with-afpstats for overriding the result of
  autodetecting dbus-glib presence

</div>

### Changes in 3.0.6

<div class="ulist">

- FIX: charset conversion failed when copying from Mac OS 9. Bug \#523.

- UPD: Don’t force S_ISGID for directories on FreeBSD. Bug \#525.

- NEW: Add support for ZFS ACLs on FreeBSD with libsunacl. From FR#83.

- FIX: Active Directory LDAP queries for ACL support with new options
  "ldap user filter" and "ldap group filter". Bug \#526.

</div>

### Changes in 3.0.5

<div class="ulist">

- FIX: Fix a crash when using pam_winbind. Fixes bug \#516.

- NEW: New global/volume option "ignored attributes"

- FIX: "afp listen" option failed to take IPv6 addresses. Bug \#515.

- FIX: Fix a possible crash in set_groups. Bug \#518.

- NEW: Send optional AFP messages for vetoed files, new option "veto
  messages" can be used to enable sending messages. Then whenever a
  client tries to access any file or directory with a vetoed name, it
  will be sent an AFP message indicating the name and the directory.
  From FR \#81.

- NEW: New boolean volume option "delete veto files". If this option is
  set to yes, then Netatalk will attempt to recursively delete any
  vetoed files and directories. FR \#82.

- UPD: systemd unit dir is /usr/lib/systemd/system .

- FIX: Saving files from application like MS Word may result in the file
  loosing metadata like the Finder label. Bug \#521.

</div>

### Changes in 3.0.4

<div class="ulist">

- FIX: Opening files without metadata EA may result in an invalid
  metadata EA. Check for malformed metadata EAs and delete them. Fixes
  bug \#510.

- FIX: Fix an issue with filenames containing non-ASCII characters that
  lead to a failure setting the size of a files ressource fork. This
  affected application like Adobe Photoshop where saving files may fail.
  Fixes bug \#511.

- UPD: Enhance ACL mapping, change global ACL option *map acl* to take
  the following options: "none", "rights" (default), "mode". none = no
  mapping, this resembles the previous false/no setting rights = map
  ACLs to Finder UARights, this resembles the previous true/yes setting.
  This is the default. mode = map ACLs to Finder UARights and UNIX mode
  From FR \#73.

- FIX: Fix a possible crash in cname() where cname_mtouname calls
  dirlookup() where the curdir is freed because the dircache detected a
  dev/inode cache difference and evicted the object from the cache.
  Fixes bug \#498.

- FIX: Add missing include, fixes bug \#512.

- FIX: Change default FinderInfo for directories to be all 0, fixes bug
  514.

- NEW: New option "afp interfaces" which allows specifying where
  Netatalk listens for AFP connections by interface names. From FR \#79.

</div>

### Changes in 3.0.3

<div class="ulist">

- UPD: afpd: Increase default DSI server quantum to 1 MB

- UPD: bundled libevent2 is now static

- NEW: --with-lockfile=PATH configure option for specifying an
  alternative path for the netatalk lockfile.

- UPD: systemd service file use PIDFile and ExecReload. From FR \#70.

- UPD: RedHat sysvinit: rm graceful, reimplement reload, add condrestart

- FIX: Couldn’t create folders on FreeBSD 9.1 ZFS fileystems. Fixed bug
  \#491.

- FIX: Fix an issue with user homes when user home directory has not the
  same name as the username. Fixes bug \#497.

- UPD: Fix PAM config install, new default installation dir is
  \$sysconfdir/pam.d/. Add configure option --with-pam-confdir to
  specify alternative path.

- NEW: AFP stats about active session via dbus IPC. Client side python
  program <span class="monospaced">afpstats</span>. Requires dbus,
  dbus-glib any python-dbus. configure option --dbus-sysconf-dir for
  specifying dbus system security configuration files. New option
  *afpstats* (default: no) which determines whether to enable the
  feature or not.

- NEW: configure option --with-init-dir

- NEW: dtrace probes, cf include/atalk/afp_dtrace.d for available
  probes.

- UPD: Reload groups when reloading volumes. FR \#71.

- FIX: Attempt to read read-only .\_ rfork results in disconnect. Fixes
  bug \#502.

- FIX: File’s ressource fork can’t be read if metadata EA is missing.
  Fixes bug \#501.

- FIX: Conversion from adouble v2 to ea for directories. Fixes bug
  \#500.

- FIX: Error messages when mounting read-only filesystems. Fixes bug
  \#504.

- FIX: Permissions of .\_ AppleDouble ressource fork after conversion
  from v2 to ea. Fixes bug \#505.

- UPD: Use FreeBSD sendfile() capability to send protocol header. From
  FR \#75.

- UPD: Increase IO size when sendfile() is not used. From FR \#76.

- FIX: Can’t set Finder label on symlinked folder with "follow symlinks
  = yes". Fixes bug \#508.

- FIX: Setting POSIX ACLs on Linux Fixes bug \#506.

- FIX: "ad ls" segfault if requested object is not in an AFP volume.
  Fixes bug \#496.

</div>

### Changes in 3.0.2

<div class="ulist">

- NEW: afpd: Put file extension type/creator mapping back in which had
  been removed in 3.0.

- NEW: afpd: new option *ad domain*. From FR \#66.

- FIX: volumes and home share with symlinks in the path

- FIX: Copying packages to a Netatalk share could fail, bug \#469

- FIX: Reloading volumes from config file was broken. Fixes bug \#474.

- FIX: Fix \_device-info service type registered with dns-sd API

- FIX: Fix pathname bug for FCE modified event.

- FIX: Remove length limitation of options like "valid users". Fixes bug
  \#473.

- FIX: Dont copy our metadata EA in copyfile(). Fixes bug \#452.

- FIX: Fix an error where catalog search gave incomplete results. Fixes
  bug \#479.

- REM: Remove TimeMachine volume used size FCE event.

- UPD: Add quoting support to *\[in\]valid users* option. Fixes bug
  \#472.

- FIX: Install working PAM config on Solaris 11. Fixes bug \#481.

- FIX: Fix a race condition between dbd and the cnid_dbd daemon which
  could result in users being disconnected from volumes when dbd was
  scanning their volumes. Fixes bug \#477.

- FIX: Netatalk didn’t start when the last line of the config file
  afp.conf wasn’t terminated by a newline. Fixes bug \#476.

- NEW: Add a new volumes option *follow symlinks*. The default setting
  is false, symlinks are not followed on the server. This is the same
  behaviour as OS X’s AFP server. Setting the option to true causes afpd
  to follow symlinks on the server. symlinks may point outside of the
  AFP volume, currently afpd doesn’t do any checks for "wide symlinks".

- FIX: Automatic AppleDouble conversion to EAs failing for directories.
  Fixes bug \#486.

- FIX: dbd failed to convert appledouble files of symlinks. Fixes bug
  \#490.

</div>

### Changes in 3.0.1

<div class="ulist">

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

</div>

### Changes in 3.0

<div class="ulist">

- UPD: afpd: force read only mode if cnid scheme is last

- REM: afpd: removed global option "icon"

- FIX: CNID path for user homes

</div>

### Changes in 3.0 beta2

<div class="ulist">

- UPD: Solaris and friends: Replace initscript with SMF manifest

- FIX: Solaris and friends: resource fork handling

</div>

### Changes in 3.0 beta1

<div class="ulist">

- UPD: afpd: Performance tuning of read/write AFP operations. New option
  "afp read locks" (default: no) which disables that the server applies
  UNIX byte range locks to regions of files in AFP read and write calls.

- UPD: apple_dump: Extended Attributes AppleDouble support. (\*BSD is
  not supported yet)

</div>

### Changes in 3.0 alpha3

<div class="ulist">

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

</div>

### Changes in 3.0 alpha2

<div class="ulist">

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

</div>

### Changes in 3.0 alpha1

<div class="ulist">

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

</div>

### Supported Platforms

<div class="paragraph">

As of Netatalk 3.0 the following operating systems are supported:

</div>

<div class="ulist">

- FreeBSD

- Linux

- OpenBSD

- NetBSD

- Solaris and derivates

</div>

<div class="paragraph">

Netatalk may compile and run on other operating systems as well, but it
is not well-tested on those. We welcome patches and suggestions for
enhancing the portability of Netatalk as well as success and failure
stories. Please write to <netatalk-devel@lists.sourceforge.net>.

</div>

### Availability

<div class="paragraph">

Netatalk tar-balls can be found at:

</div>

<div class="paragraph">

<http://sourceforge.net/project/showfiles.html?group_id=8642>

</div>

<div class="paragraph">

Netatalk is also available via anonymous git. See the SourceForge
project site for anonymous git instructions.

</div>

### Contact

<div class="paragraph">

For more information about Netatalk, see its web page at:

</div>

<div class="paragraph">

<http://netatalk.sourceforge.net/>

</div>

<div class="paragraph">

The project is hosted at SourceForge. The SourceForge project page is
located at:

</div>

<div class="paragraph">

<http://sourceforge.net/projects/netatalk/>

</div>

<div class="paragraph">

The Netatalk development team can be reached via the mailing list
<netatalk-devel@lists.sourceforge.net>. For subscription information and
archives see Netatalk’s SourceForge project page.

</div>

<div class="paragraph">

<netatalk-admins@lists.sourceforge.net> is a mailing list for Netatalk
system administrators. For subscription information and archives see the
Netatalk web page.

</div>

### Acknowledgements

<div class="paragraph">

We would like to thank all contributors to the Netatalk project for
their commitment. Without the many suggestions, bug and problem reports,
patches, and reviews this project wouldn’t be where it is.

</div>

<div class="ulist">

- The Netatalk Development Team, September 2013

</div>

</div>

<div class="footer">

[<img src="https://www.w3.org/Icons/valid-xhtml10" width="88" height="31"
alt="Valid XHTML 1.0 Strict" />](https://validator.w3.org/check?uri=referer)
[<img src="https://jigsaw.w3.org/css-validator/images/vcss"
style="border:0;width:88px;height:31px" alt="Valid CSS!" />](https://jigsaw.w3.org/css-validator/check?uri=referer)

</div>
