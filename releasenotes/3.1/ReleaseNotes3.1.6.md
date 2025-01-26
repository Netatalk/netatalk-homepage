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

# Netatalk 3.1.6

<div id="body">

<div class="paragraph">

The Netatalk development team is proud to announce latest release of the
Netatalk 3.1 release series. Users are encouraged to update their
servers to the 3.1 release series which is the stable and supported
version for production systems.

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

<http://netatalk.sourceforge.net/3.1/htmldocs/configuration.html>

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

### Changes in 3.1.6

<div class="ulist">

- FIX: Spotlight: fix for long running queries

- UPD: afpd: distribute SIGHUP from parent afpd to children and force
  reload shares

- FIX: netatalk: refresh Zeroconf registration when receiving SIGHUP

- NEW: configure option "--with-init-style=debian-systemd" for Debian 8
  jessieand later. "--with-init-style=debian" is renamed
  "--with-init-style=debian-sysv".

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

- The Netatalk Development Team, August 2014

</div>

</div>

<div class="footer">

[<img src="https://www.w3.org/Icons/valid-xhtml10" width="88" height="31"
alt="Valid XHTML 1.0 Strict" />](https://validator.w3.org/check?uri=referer)
[<img src="https://jigsaw.w3.org/css-validator/images/vcss"
style="border:0;width:88px;height:31px" alt="Valid CSS!" />](https://jigsaw.w3.org/css-validator/check?uri=referer)

</div>
