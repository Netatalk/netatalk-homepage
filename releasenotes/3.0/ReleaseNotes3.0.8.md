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

# Netatalk 3.0.8

<div id="body">

<div class="paragraph">

The Netatalk development team is proud to announce version 3.0.8 of the
Netatalk File Sharing suite. This is the latest update to the 3.0
release series. All users are encouraged to upgrade their systems to
3.0.8.

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

### Summary of major new features and enhancements in 3.0

<div class="ulist">

- New ini style configuration file afp.conf which replaces all previous
  configuration files

- New default AppleDouble backend using filesystem Extended Attributes,
  conversion from AppleDouble v2 is done automatically on access

- New service controller process "netatalk" responsible for starting and
  restarting afpd and cnid_metad as necessary

- AppleTalk support has been removed

- Coherent cross-platform locking with Solaris CIFS server

</div>

<div class="paragraph">

Please make sure to read the upgrading section in the Netatalk online
manual before trying to upgrade your system to 3.0!

</div>

<div class="literalblock">

<div class="content monospaced">

    http://netatalk.sourceforge.net/3.0/htmldocs/upgrade.html

</div>

</div>

### License

<div class="paragraph">

Netatalk is a Free/Open Source Software project and is released under
the GNU General Public License (GPLv2). The full license text is
available at:

</div>

<div class="literalblock">

<div class="content monospaced">

    http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

</div>

</div>

### Changes in 3.0.8

<div class="ulist">

- FIX: dbd: remove orphaned .\_ AppleDouble files. Bug \#549.

- FIX: afpd: Fix a crash in of_closefork(). Bug \#551.

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

- The Netatalk Development Team, February 2014

</div>

</div>

<div class="footer">

[<img src="https://www.w3.org/Icons/valid-xhtml10" width="88" height="31"
alt="Valid XHTML 1.0 Strict" />](https://validator.w3.org/check?uri=referer)
[<img src="https://jigsaw.w3.org/css-validator/images/vcss"
style="border:0;width:88px;height:31px" alt="Valid CSS!" />](https://jigsaw.w3.org/css-validator/check?uri=referer)

</div>
