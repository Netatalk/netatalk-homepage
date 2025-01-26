# netatalk-homepage
Netatalk html website.

The first layer of index pages are generated from local Markdown sources.

Release notes as well as wiki documentation pages are static html generated from markdown sources hosted on GitHub.

# New release procedure
- Create a news story at the top of `index.md`.
- Move an older news story to `archive.md`. Limit the number of news stories on `index.md` to about 4.
- Update the download and release note links in `templates/navbar.html`.
- Add link to release notes in `documentation.md`.
- Add the new netatalk release version to the "versions" list in `scripts/generate_releasenotes.py`
- Run the `run.sh` script, passing a GITHUB_TOKEN env variable with a valid GitHub API token.
- Validate the correctness and absence of spam in generated html sources in `public/`.
- Commit all above changes and push to remote git.
- The web host (currently: CloudFlare) will automatically build and publish the site via a webhook trigger.

# See also
- [Netatalk release process wiki](https://github.com/Netatalk/netatalk/wiki/Developer-Notes#user-content-Making_a_release)
