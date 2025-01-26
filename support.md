# Support

## Bug Reports

If you think you have found a bug in Netatalk, first see if the bug has
already been reported in the [Netatalk issue tracker at
GitHub](https://github.com/Netatalk/netatalk/issues).

If no similar bug has been reported yet, please create a new ticket and
provide as much context as possible, including Netatalk version, OS
version, contents of configuration files, and debug or backtrace logs.

Feature requests can also be filed via the same issue tracker.

## Technical Support

If you want to get help from the Netatalk developers or the community,
or simply want to share a cool idea, you can start a new topic at
[Netatalk Discussions](https://github.com/Netatalk/netatalk/discussions)
at GitHub. Please don't forget to be courteous and mindful of others.

## Mailing Lists

As an alternative to GitHub, you can join the [netatalk-admins mailing
list](https://sourceforge.net/p/netatalk/mailman/netatalk-admins/). New
release announcements are posted here as well.

## Security Advisories

The Netatalk Project takes cyber security very seriously. In this
section we publish security advisories when vulnerabilities have been
disclosed and fixed.

If you think you have found a new exploit in Netatalk, please file a
[new security vulnerability
report](https://github.com/Netatalk/netatalk/security/advisories/new)
via GitHub. This enables us to collaborate on a patch in private.

| CVE ID                                           | Subject                                   | Publish Date | Affected Versions                 | Fixed Versions       |
|--------------------------------------------------|-------------------------------------------|--------------|------------------------------------|----------------------|
| [CVE-2024-38441](/security/CVE-2024-38441.html) | Heap out-of-bounds write in directory.c  | 2024/06/28   | 3.2.0, 3.0.0 - 3.1.18, 2.0.0 - 2.4.0 | 3.2.1, 3.1.19, 2.4.1 |
| [CVE-2024-38440](/security/CVE-2024-38440.html) | Heap out-of-bounds write in uams_dhx_pam.c | 2024/06/28   | 3.2.0, 3.0.0 - 3.1.18, 1.5.0 - 2.4.0 | 3.2.1, 3.1.19, 2.4.1 |
| [CVE-2024-38439](/security/CVE-2024-38439.html) | Heap out-of-bounds write in uams_pam.c   | 2024/06/28   | 3.2.0, 3.0.0 - 3.1.18, 1.5.0 - 2.4.0 | 3.2.1, 3.1.19, 2.4.1 |
| [CVE-2023-42464](/security/CVE-2023-42464.html) | afpd daemon vulnerable to type confusion | 2023/09/17   | 3.1.0 - 3.1.16                    | 3.1.17               |
| [CVE-2022-45188](/security/CVE-2022-45188.html) | Arbitrary code execution in afp_getappl  | 2023/03/26   | 3.0.0 - 3.1.14, 1.5.0 - 2.2.8   | 3.1.15, 2.2.9      |
| [CVE-2022-43634](/security/CVE-2022-43634.html) | Arbitrary code execution in dsi_writeinit | 2023/02/06  | 3.0.0 - 3.1.14                    | 3.1.15               |
| [CVE-2022-23125](/security/CVE-2022-23125.html) | Arbitrary code execution in copyapplfile | 2022/03/21   | 3.0.0 - 3.1.12, - 2.2.6         | 3.1.13, 2.2.7      |
| [CVE-2022-23124](/security/CVE-2022-23124.html) | Information leak in get_finderinfo       | 2022/03/21   | 3.0.0 - 3.1.12                    | 3.1.13               |
| [CVE-2022-23123](/security/CVE-2022-23123.html) | Information leak in getdirparams         | 2022/03/21   | 3.0.0 - 3.1.12, 1.5.0 - 2.2.6   | 3.1.13, 2.2.7      |
| [CVE-2022-23122](/security/CVE-2022-23122.html) | Arbitrary code execution in setfilparams | 2022/03/21   | 3.0.0 - 3.1.12                    | 3.1.13               |
| [CVE-2022-23121](/security/CVE-2022-23121.html) | Arbitrary code execution in parse_entries | 2022/03/21  | 3.0.0 - 3.1.12, 1.5.0 - 2.2.6   | 3.1.13, 2.2.7      |
| [CVE-2022-22995](/security/CVE-2022-22995.html) | afpd daemon vulnerable to symlink redirection | 2023/10/05 | 3.1.0 - 3.1.17                    | 3.1.18               |
| [CVE-2022-0194](/security/CVE-2022-0194.html)   | Arbitrary code execution in ad_addcomment | 2022/03/21  | 3.0.0 - 3.1.12, 1.5.0 - 2.2.6   | 3.1.13, 2.2.7      |
| [CVE-2021-31439](/security/CVE-2021-31439.html) | Arbitrary code execution in dsi_stream_receive | 2022/03/21 | 3.0.0 - 3.1.12                    | 3.1.13               |
| [CVE-2018-1160](/security/CVE-2018-1160.html)   | Unauthenticated remote code execution    | 2018/12/13   | 3.0.0 - 3.1.11, 1.5.0 - 2.2.6   | 3.1.12, 2.2.7      |
| [CVE-2008-5718](/security/CVE-2008-5718.html)   | papd daemon vulnerable to remote command execution | 2009/11/10 | 2.0.0 - 2.0.4                    | 2.0.5                |
| [CAN-2004-0974](/security/CAN-2004-0974.html)   | etc2ps.sh vulnerable to symlink attack   | 2004/10/24   | 2.0.0, - 1.6.4                 | 2.0.1, 1.6.4a      |

### See Also

[Netatalk CVE advisory archives on
cve.mitre.org](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=netatalk)
