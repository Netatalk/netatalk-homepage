# About Netatalk

[![Build Status](https://github.com/Netatalk/netatalk/actions/workflows/build.yml/badge.svg)](https://github.com/Netatalk/netatalk/actions/workflows/build.yml)
[![Container Status](https://github.com/Netatalk/netatalk/actions/workflows/containers.yml/badge.svg)](https://github.com/Netatalk/netatalk/actions/workflows/containers.yml)
[![Project releases](https://img.shields.io/github/release/Netatalk/netatalk)](https://github.com/Netatalk/netatalk/releases)
[![Downloads](https://img.shields.io/github/downloads/Netatalk/netatalk/total)](https://github.com/Netatalk/netatalk/releases)
[![Project contributors](https://img.shields.io/github/contributors/Netatalk/netatalk)](https://github.com/Netatalk/netatalk/graphs/contributors)
[![Monthly commits](https://img.shields.io/github/commit-activity/m/Netatalk/netatalk)](https://github.com/Netatalk/netatalk/graphs/commit-activity)
[![Packaging status](https://repology.org/badge/tiny-repos/netatalk.svg)](https://repology.org/project/netatalk/versions)
[![Lines of code](https://sonarcloud.io/api/project_badges/measure?project=Netatalk_netatalk&metric=ncloc)](https://sonarcloud.io/project/overview?id=Netatalk_netatalk)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=Netatalk_netatalk&metric=security_rating)](https://sonarcloud.io/project/overview?id=Netatalk_netatalk)
[![Reliability](https://sonarcloud.io/api/project_badges/measure?project=Netatalk_netatalk&metric=reliability_rating)](https://sonarcloud.io/project/overview?id=Netatalk_netatalk)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=Netatalk_netatalk&metric=sqale_rating)](https://sonarcloud.io/project/overview?id=Netatalk_netatalk)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=Netatalk_netatalk&metric=duplicated_lines_density)](https://sonarcloud.io/project/overview?id=Netatalk_netatalk)
[![License: GPL v2](https://img.shields.io/github/license/Netatalk/netatalk)](https://github.com/Netatalk/netatalk/blob/main/COPYING)

Netatalk is a Free and Open Source file server that implements the [Apple Filing Protocol](https://en.wikipedia.org/wiki/Apple_Filing_Protocol) (AFP) 3.4 over TCP/IP and AppleTalk.
AFP is the primary file sharing protocol used on Apple II, Classic Mac OS, and Mac OS X, as well as one of several supported protocols on macOS.
A *NIX/*BSD system running Netatalk provides high-speed AppleShare file sharing for Mac clients.

# Why Should I Use Netatalk?

If you have a local network macOS, Mac OS X, Classic Mac OS, or even Apple II computers,
running a Netatalk AppleShare server allows you to share, collaborate on, and back up files comfortably.
The latest macOS at the time of writing (macOS 15 Sequoia) ships with an AFP client,
so Netatalk can act as a seamless bridge between new and old Macs.

Compared to cross-platform file sharing protocols like NFS and FTP, Netatalk delivers a Mac-like user experience,
with seamless integration of Mac filesystem metadata (such as resource forks on Classic Mac OS) and modern macOS services such as Bonjour, Time Machine, and Spotlight.

Compared to [Samba](https://www.samba.org/), Netatalk has [demonstrably faster transfer speeds](https://github.com/Netatalk/netatalk/wiki/Benchmarks), as well as stronger backwards compatibility with OS X 10.8 Mountain Lion clients, and earlier.

# AppleTalk

Netatalk supports the [AppleTalk](https://en.wikipedia.org/wiki/AppleTalk) family of protocols, allowing it to provide AFP file sharing and other services with very old Macs or Apple II computers.

All versions of Netatalk except the 3.x release series can speak AppleTalk.

# Website

The Netatalk website [netatalk.io](https://netatalk.io) is where project updates and resources are published, including documentation, release notes, security advisories, links to related projects, and more.

# Community

Netatalk developers and users can be found in online communal spaces like [TinkerDifferent](https://tinkerdifferent.com/) or [68kmla](https://68kmla.org/).
You can head over there if you want to ask for help or share your Netatalk stories.

There is also an official [Netatalk Discussions](https://github.com/Netatalk/netatalk/discussions) board on GitHub which is the best place to ask for technical assistance.

Finally, the traditional place where Netatalk developers and users interact with each other are the [netatalk-admins](https://sourceforge.net/p/netatalk/mailman/netatalk-admins/) and [netatalk-devel](https://sourceforge.net/p/netatalk/mailman/netatalk-devel/) mailing lists.
While these lists aren't as active as they used to be, the archives are a veritable treasure trove of decades of Mac networking know-how.

# Installation

See [INSTALL.md](https://github.com/Netatalk/netatalk/blob/main/INSTALL.md)

# Docker

See [DOCKER.md](https://github.com/Netatalk/netatalk/blob/main/DOCKER.md)

# Webmin module

An administrative GUI frontend built on the Webmin 2.0 platform is distributed with Netatalk.

See the [Webmin README](https://github.com/Netatalk/netatalk/blob/main/contrib/webmin_module/README.md) for instructions how to install and get started with the module.

An [overview of the module's feature set](https://github.com/Netatalk/netatalk/wiki/Webmin-Module) can be found in the wiki.

# Contributions

Bug reports and feature requests should be filed as [GitHub issue tickets](https://github.com/Netatalk/netatalk/issues).

Before contributing code to the project, please read the [coding guidelines](https://github.com/Netatalk/netatalk/wiki/Developer-Notes) in the wiki on how to prepare a PR that is likely to be accepted by the maintainers.

PRs are automatically picked up by GitHub CI, which runs the builds, integration tests, as well as static analysis scan on SonarCloud (the latter only for PRs created by project members.)

# Security

We would love to hear from you if you think you found a security vulnerability in Netatalk.
Please file a [security issue ticket](https://github.com/Netatalk/netatalk/security/advisories/new) with us, and we will follow up with you as soon as possible.

# Documentation

To aid in your installation and configuration of Netatalk, a comprehensive [html manual](https://netatalk.io/stable/htmldocs/) is published online.

Additionally, each Netatalk program and configuration file also has a _troff_ man page which can be accessed on the command line, f.e. `man afpd`.

# Wiki

Collaborative articles can be found on the [Netatalk wiki](https://github.com/Netatalk/netatalk/wiki).
The [Netatalk website](https://netatalk.io/docs) also serves a static mirror of all wiki pages.

Editing is open to all registered GitHub users.
We are looking forward to your additions to existing material, or brand new articles on topics concerning Netatalk and Mac networking.

# We are Using GitHub Under Protest

This project is currently hosted on GitHub. This is not ideal; the GitHub platform itself is a proprietary system that is not Free and Open Souce Software (FOSS).
We are deeply concerned about using a proprietary system like GitHub to develop our FOSS project.
We have an [open ticket](https://gitlab.com/netatalk-team/netatalk/-/issues/1) for project members and volunteers to discuss how we can move away from GitHub in the long term.

The primary source of platform lock-in for this project, is the reliance on GitHub-hosted CI runners for cross-platform builds and tests.

If you are a contributor who prefer not using GitHub, please see the [Developer FAQ](https://netatalk.io/docs/Developer-FAQ) for how to submit patches without using GitHub directly.

Any use of this project's code by GitHub Copilot, past or present, is done without our permission.
We do not consent to GitHub's use of this project's code in Copilot.
