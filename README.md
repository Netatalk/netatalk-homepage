# netatalk-homepage
Netatalk static website.

The first layer of index pages are written in PHP. The only PHP feature in use is the dynamic importing of headers and footers. No other dynamic content generation is happening.

Release notes as well as wiki documentation pages are static html generated from markdown sources hosted on GitHub. See the Python scripts in the wiki/ dir.

Manual pages are static html generated with xsltproc from [XSL sources](https://github.com/Netatalk/netatalk/tree/main/doc).

# New release procedure
- Create a news story at the top of `index.php`.
- Move an older news story to `archive.php`. Limit the number of news stories on `index.php` to about 4.
- Generate static release notes with the `wiki/release_notes.py` script.
- Update the current releases left rail in the `header.php` sources.
- Update `download.php` and `documentation.php` sources.
- As an admin, upload the updated sources to the web server with the `upload.sh` script.

# Wiki docs update procedure
- Run the `wiki/run.sh` script
- Validate in the git diff that the generated html pages in `docs/` don't contain any unwanted edits or spam.
- Commit the changes and upload to the web server

# See also
- [Netatalk release process wiki](https://github.com/Netatalk/netatalk/wiki/Developer-Notes#user-content-Making_a_release)
