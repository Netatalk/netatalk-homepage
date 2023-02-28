<?php echo "<?xml version=\"1.0\" encoding=\"iso-8859-1\"?".">"; ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<meta name="description" content="Netatalk - Unix file and print services for Apple clients" />
<meta name="keywords" content="Netatalk, AFP, AFP Server, File Server, PAP, Print Server, Appletalk, Mac, OSX, OS X, OS9, OS 9" />
<meta name="language" content="EN" />
<meta name="publisher" content="netatalk.sourceforge.net" />
<meta name="robots" content="index,follow" />
<meta name="audience" content="all" />

<link rel="stylesheet" type="text/css" charset="iso-8859-1" href="css/site.css" />
<link rel="stylesheet" type="text/css" charset="iso-8859-1" href="css/printer.css" media="print" />
<link rel="alternate stylesheet" type="text/css" charset="iso-8859-1" href="css/printer.css" title="Printer" />
<link rel="copyright" title="GNU General Public License, version 2" href="https://www.gnu.org/licenses/old-licenses/gpl-2.0.html" />
<link rel="author" title="The Netatalk Development Team" href="http://netatalk.sf.net" />
<link rel="help" href="/3.1/htmldocs/" title="Documentation" />
<link rel="home" href="index.php" title="Netatalk Home" />
<link rel="home" href="http://www.sourceforge.net/projects/netatalk" title="Netatalk Sourceforge" />
<link rel="bookmark" href="/3.1/htmldocs/" title="Netatalk Documentation" />
<link rel="bookmark" href="https://github.com/Netatalk/netatalk/wiki" title="wiki" />
<link rel="bookmark" href="https://sourceforge.net/projects/netatalk/files/netatalk/" title="Downloads" />

<title><?php echo ( $title ? ("Netatalk - ".$title) : "Netatalk" ); ?></title>
</head>

<body>
<div id="header">
  <!-- header -->
  <div id="logo"></div>
  <div id="menlinks">
	<a href="/" title="Return to Netatalk home">[main]</a>
	<a href="https://github.com/Netatalk/netatalk/wiki" title="Netatalk Wiki">[wiki]</a> 
	<a href="/3.1/htmldocs" title="Netatalk Manual">[documentation]</a>
	<a href="https://sourceforge.net/projects/netatalk/files/netatalk/" title="Download Netatalk from Sourceforge">[downloads]</a> 
	<a href="/support.php" title="Support">[support]</a> 
	<a href="/links.php" title="Netatalk related links">[links]</a>
	<img src="/gfx/end.gif" alt="" width="125" height="7" />
  </div>
</div>

<div id="header-print">
  <h1>netatalk.sourceforge.net</h1>
</div>

<div class="search"> 
  <!-- search box -->
  <h2>search netatalk.sf.net</h2>
  <form method="get" action="https://www.google.com/search">
    <p> 
      <input type="text" name="q" size="10" maxlength="255" value="" title="enter search text" />
      <input type="hidden" name="sitesearch" value="netatalk.sourceforge.net" />
      <input type="submit" name="btnG" value="Go" title="search netatalk.sf.net" />
    </p>
  </form>
  <span class="italic">powered by Google</span>
</div>

<div id="navbars">
  <!-- the left navigation/search bar -->
  <div class="navbar"> 
    <h2>current releases</h2>
    <p><b>stable</b></p>
    <ul>
      <li><a title="download 3.1.14 bzip2 compressed" href="https://sourceforge.net/projects/netatalk/files/netatalk/3.1.14/netatalk-3.1.14.tar.bz2/download">&nbsp;3.1.14
        (bzip2)</a></li>
      <li><a title="download 3.1.14 gzip compressed" href="https://sourceforge.net/projects/netatalk/files/netatalk/3.1.14/netatalk-3.1.14.tar.gz/download">&nbsp;3.1.14
        (gzip)</a></li>
      <li><a title="view 3.1.14 Release Notes" href="https://github.com/Netatalk/netatalk/releases/tag/netatalk-3-1-14">&nbsp;Release Notes </a></li>
    </ul>
    <p><b>legacy (AppleTalk support)</b></p>
    <ul>
      <li><a title="download 2.2.8 bzip2 compressed" href="https://sourceforge.net/projects/netatalk/files/netatalk/2.2.8/netatalk-2.2.8.tar.bz2/download">&nbsp;2.2.8
        (bzip2)</a></li>
      <li><a title="download 2.2.8 gzip compressed" href="https://sourceforge.net/projects/netatalk/files/netatalk/2.2.8/netatalk-2.2.8.tar.gz/download">&nbsp;2.2.8
        (gzip)</a></li>
      <li><a title="view 2.2.8 Release Notes" href="https://github.com/Netatalk/netatalk/releases/tag/netatalk-2-2-8">&nbsp;Release Notes </a></li>
    </ul>
  </div>
  <div class="navbar">
    <h2>documentation</h2>
    <h3><b>3.1 documentation</b></h3>
      <p>
      <a href="/3.1/htmldocs/">&nbsp;Manual (HTML)</a><br />
      </p>
    <h3><b>2.2 documentation</b></h3>
      <p>
      <a href="/2.2/htmldocs/">&nbsp;Manual (HTML)</a><br />
      </p>
  </div>
  <div class="navbar">
    <h2>community</h2>
    <p>
       <h3><a title="Support" href="http://netatalk.sourceforge.net/support.php">Support</a></h3>
    </p>
    <p>
       <h3><a title="Wiki" href="https://github.com/Netatalk/netatalk/wiki">Wiki</a></h3>
    </p>
  </div>
  <div class="navbar">
    <h2>development</h2>
    <p>
       <h3><a title="Project Home (GitHub)" href="https://github.com/Netatalk/netatalk">Project Home (GitHub)</a></h3>
    </p>
    <p><a href="https://sonarcloud.io/summary/overall?id=Netatalk_netatalk">
      <img alt="Sonarcloud Scan Build Status" height=30
         src="https://sonarcloud.io/images/project_badges/sonarcloud-orange.svg"/>
    </a></p>
  </div>
</div> <!-- /the left navigation/search bar -->

