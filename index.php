<?php
 // main netatalk page
$title = "Networking Apple Macintosh through Open Source";
include_once "header.php";
?>

<div id="content"> 
  <h1>Welcome to the Netatalk Homepage!</h1>

  <p>Netatalk is a Free and Open Source Apple Filing Protocol (AFP) fileserver.
     A macOS, Linux, BSD, or Solaris system running Netatalk is capable of serving
     files to many macOS (Mac OS X), Classic Mac OS, and Apple II clients simultaneously.</p>

  <p>Since 1990, Netatalk has been providing fast and secure file sharing to Macs from
     *NIX-like hosts, providing seamless support for the unique demands
     of Macintosh networking, file systems, and operating system services.</p>

  <h2>Features</h2>
  <table summary="Netatalk feature comparison">
  <tr>
  <th>Feature</th>
  <th>Netatalk v3</th>
  <th>Netatalk v2</th>
  </tr>
  <tr>
  <td>Client Support</td>
  <td>Mac OS 7.5 ~ Mac OS 9, Mac OS X, macOS</td>
  <td>Apple II, Macintosh System 6 ~ Mac OS 9, Mac OS X, macOS</td>
  </tr>
  <tr>
  <td>AFP Protocol Versions</td>
  <td>2.2, 3.0, 3.1, 3.2, 3.3, 3.4</td>
  <td>1.1, 2.0, 2.1, 2.2, 3.0, 3.1, 3.2, 3.3</td>
  </tr>
  <tr>
  <td>AFP over TCP</td>
  <td>Yes</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>AFP over AppleTalk</td>
  <td>No</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>Macintosh Resource Forks</td>
  <td>Extended Attributes, AppleDouble v2</td>
  <td>AppleDouble v2, AppleDouble v1</td>
  </tr>
  <tr>
  <td><i>Bonjour</i> Service Discovery</td>
  <td>Zeroconf</td>
  <td>Zeroconf and SLP</td>
  </tr>
  <tr>
  <td><i>Time Machine</i> Backups</td>
  <td>Yes</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td><i>Spotlight</i> Indexed Search</td>
  <td>Yes</td>
  <td>No</td>
  </tr>
  <tr>
  <td>PAP Print Server</td>
  <td>No</td>
  <td>Yes, with CUPS support</td>
  </tr>
  <tr>
  <td><i>Timelord</i> Time Server</td>
  <td>No</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>Apple II Netboot Server</td>
  <td>No</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>Built-in AppleTalk Router</td>
  <td>No</td>
  <td>Yes</td>
  </tr>
  <tr>
  <td>Administrative GUI</td>
  <td>Webmin Module</td>
  <td>Webmin Module</td>
  </tr>
</table>

<hr />
  <h1>Latest News</h1>

  <small>8th of January 2024</small>
  <h2>Netatalk 3 Webmin Module 0.3 Released</h2>

  <p>Version 0.3 of the Netatalk 3 Webmin Module is now available.
  It introduces a range of minor improvements which makes usage of the module more convenient.</p>
  <p>For more information, see the
  <a href="https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk3-0.3">Release Notes</a>.
  </p>

<hr />
  <small>6th of January 2024</small>
  <h2>Netatalk 2 Webmin Module 1.1 Released</h2>

  <p>Version 1.1 of the Netatalk 2 Webmin Module is a companion to Netatalk 2.3.0.
  In addition, it includes a range of UX improvements and bugfixes.</p>
  <p>For more information, see the
  <a href="https://github.com/Netatalk/netatalk-webmin/releases/tag/netatalk2-1.1">Release Notes</a>.
  </p>

<hr />
  <small>28th of December 2023</small>
  <h2>Netatalk 2.3.0 is available</h2>
  <p>The Netatalk development team is proud to announce version 2.3.0 of
  the Netatalk File Sharing suite. This is the first stable release of the
  new 2.3 series. Early adopters are encouraged to upgrade their systems
  to 2.3.0.</p>
  <p>The theme for this release is security and code quality. Long-obsoleted
  features have been removed, bugs have been fixed, and documentation improved.</p>
  <p>For a summary of news and a detailed list of changes see the
  <a href="https://github.com/Netatalk/netatalk/releases/tag/netatalk-2-3-0">Release Notes</a>.</p>

<hr />
  <small>5th of October 2023</small>
  <h2>Netatalk 3.1.18 is available</h2>

  <p>The Netatalk development team is proud to announce the latest release
  of the Netatalk 3.1 release series. It includes a patch for security issue
  <a href="CVE-2022-22995.php">CVE-2022-22995</a>.
  All users of Netatalk 3.1 are encouraged to upgrade their systems to 3.1.18.</p>
  <p>For a summary of news and a detailed list of changes see the
  <a href="https://github.com/Netatalk/netatalk/releases/tag/netatalk-3-1-18">Release Notes</a>.</p>

<hr />
  <p>For a list of older releases, go to the <a href="archive.php">News Archive</a>.</p>

  <p>Netatalk is licensed under the <a href="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html">GNU
  General Public License 2.0</a>.</p>
  <p>If you are interested in contributing to the development process or just
  want to give Netatalk a try, please visit our
  <a href="https://github.com/Netatalk/netatalk">GitHub project page</a>.</p>

<hr />

</div>

<?php include_once "footer.php"; ?>
