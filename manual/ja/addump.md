# 名前

addump - AppleSingle/AppleDouble フォーマットのデータをダンプする

# 概要

`addump [-a] [ FILE | DIR ]`

`addump [-e] [ FILE | DIR ]`

`addump [-f] [FILE]`

`addump [-d] [FILE]`

`addump [ -h | -help | --help ]`

`addump [ -v | -version | --version ]`

# 説明

`addump`はAppleSingle/AppleDoubleフォーマットのデータをダンプするperlスクリプトである。

このスクリプトはメーラ、アーカイバ、Mac OS
X、Netatalkなどが生成する様々なAppleSingle/AppleDoubleデータをダンプできる。

With no <FILE\>|<DIR\>, or when <FILE\>|<DIR\> is '-', read standard
input.

# オプション

`-a` \[<FILE\>|<DIR\>\]

> This is the default. Dump AppleSingle/AppleDouble data for <FILE\> or
<DIR\> automatically. If FILE is not in AppleSingle/AppleDouble format,
look for extended attributes, <.AppleDouble/FILE\> and <.\_FILE\>. If
<DIR\>, look for extended attributes, <DIR/.AppleDouble/.Parent\> and
<.\_DIR\>.

`-e` <FILE\>|<DIR\>

> Dump extended attributes of <FILE\> or <DIR\>.

`-f` \[<FILE\>\]

> Dump <FILE\>. Assume FinderInfo to be FileInfo.

`-d` \[<FILE\>\]

> Dump <FILE\>. Assume FinderInfo to be DirInfo.

`-h, -help, --help`

> ヘルプを表示して終了する

`-v, -version, --version`

> バージョンを表示して終了する

# 注記

FinderInfoがFileInfoなのかDirInfoなのかを検出する方法がありません。デフォルトでは、addumpはそれがファイルなのかディレクトリなのか、親ディレクトリが.AppleDoubleか、ファイル名が.\_\*か、ファイル名が.Parentかなどを調査する。

もしオプション-eまたは-fまたは-dを設定した場合、FinderInfoを仮定し他のデータを探しません。

# 関連項目

`ad(1)`, `getfattr(1)`, `attr(1)`, `runat(1)`, `getextattr(8)`,
`lsextattr(8)`

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
