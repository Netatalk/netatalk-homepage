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

# Netatalk 2.1.6

<div id="body">

<div class="paragraph">

The Netatalk development team is proud to announce version 2.1.6 of the
Netatalk File Sharing suite. This is the last update to the old stable
2.1 release series. All users are encouraged to upgrade their systems to
2.1.6.

</div>

<div class="paragraph">

Netatalk is a freely-available Open Source AFP fileserver. It also
provides a kernel level implementation of the AppleTalk Protocol Suite.
A \*NIX/\*BSD system running Netatalk is capable of serving many
Macintosh clients simultaneously as an AppleShare file server (AFP),
AppleTalk router, \*NIX/\*BSD print server, and for accessing AppleTalk
printers via Printer Access Protocol (PAP). Included are a number of
minor printing and debugging utilities.

</div>

<div class="paragraph">

The suite contains:

</div>

<div class="ulist">

- afpd - a file server that implements the Apple Filing Protocol,
  allowing clients running MacOS to access Unix file servers

- atalkd - an implementation of the AppleTalk protocol

- papd - a print server that enables Macintosh computers to access
  printers connected to Unix servers

- megatron - a tool to convert files in Macintosh specific formats like
  BinHex, AppleSingle, or MacBinary into files readable by Unix
  computers

- various supporting programs and utilities

</div>

</div>

### License

<div class="paragraph">

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPL). The full license text is available
at:

</div>

<div class="literalblock">

<div class="content monospaced">

    http://www.gnu.org/licenses/gpl.html

</div>

</div>

### Changes in 2.1.6

<div class="ulist">

- FIX: afpd: Fix for LDAP user cache corruption

- FIX: afpd: Fix for not shown ACLs for when filesyem uid or gid
  couldn’t be resolved because (eg deleted users/groups)

- FIX: afpd: generate mersenne primes for DHX2 UAM once at startup, not
  for every login, backport from 2.2.0

- FIX: gentoo: cannot set \$CNID_CONFIG

- FIX: ubuntu: servername was empty

- FIX: Solaris: configure script failed to enable DDP module

- FIX: AppleDouble buffer overrun by extremely long filename

- UPD: afpd: return version info with machine type in DSIGetStatus

- UPD: dbd: use on-disk temporary rebuild db instead of in-memory db

- UPD: suse: initscript update

</div>

### Supported Platforms

<div class="paragraph">

As of Netatalk 2.2 the following operating systems are supported:

</div>

<div class="ulist">

- FreeBSD

- Linux

- OpenBSD

- NetBSD

- \[Open\]Solaris

- Tru64 (TCP only)

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

- The Netatalk Development Team, September 2011

</div>

</div>

<div class="footer">

[<img src="https://www.w3.org/Icons/valid-xhtml10" width="88" height="31"
alt="Valid XHTML 1.0 Strict" />](https://validator.w3.org/check?uri=referer)
[<img src="https://jigsaw.w3.org/css-validator/images/vcss"
style="border:0;width:88px;height:31px" alt="Valid CSS!" />](https://jigsaw.w3.org/css-validator/check?uri=referer)

</div>
