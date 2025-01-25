# 名前

afp.conf - Netatalk の設定ファイル

# 概要

`afp.conf`は**Netatalk** AFPファイルサーバの設定ファイルである。

全てのAFP固有の設定とAFPボリュームの定義がこのファイルを通して行われる。

# ファイルの書式

ファイルはセクションとパラメータから構成される。セクションはブラケット\[各括弧\]で囲まれたセクション名に始まり、次のセクションが始まるまで続く。セクションには次のような書式のパラメータが含まれている:

        name = value

このファイルは行を基本とする。それぞれの行は改行文字で終端し、コメント、セクション名、パラメータのうちどれかを表す。

セクション名とパラメータ名は大文字と小文字の区別がある。

パラメータに最初に現れる等号だけは重要な意味を持つ。最初の等号の前後にある空白は破棄される。セクション名とパラメータ名の前、後、途中にある空白は意味を持たない。パラメータ値の前後の空白は破棄される。パラメータ値の途中の空白はそのま維持される。

セミコロン(“;”)やハッシュ文字(“\#”)で始まるいかなる行も、空白だけの行と同様に無視される。

“`\`”で終わるいかなる行も、通例のUNIX方式で次の行に続くことを意味する。

パラメータにおいて等号の後ろに続く値は、文字列(引用符は必要ない)または真偽値である。真偽値はyes/no、1/0、true/falseで表現する。大文字と小文字の区別は真偽値では意味を持たないが、文字列では保存される。「file
perm」のようないくつかの項目は数値を表す。

「`include =
path`」というパラメータは、設定ファイルの中にもう一つの設定ファイルを組み込むことを可能にする。そのファイルはまるでその場所に書き込まれたように、そっくりそのまま組み込まれる。入れ子になった組み込みはサポートされない。

# セクションの説明

設定ファイル中のそれぞれのセクション(\[Global\]セクション以外)は共有リソース(“volume”として知られる)を記述する。セクション名はボリュームの名前であり、セクション内のパラメータはボリューム属性とオプションを定義する。

\[Global\]と\[Homes\]という二つの特殊なセクションがあるが、これについては下の方の*特殊なセクション*で説明する。以下の解説は通常のセクションに適用される。

一つのボリュームは、アクセスを許可するディレクトリ設定と、そのサービスにおいてユーザに与えるアクセス権設定で成り立つ。ボリュームに対して`path`オプションを使って共有ディレクトリを指定しなければならない。

`path`オプションのないボリュームセクションは、他のボリュームセクションから`vol
preset`オプション経由で呼び出され、ボリュームのデフォルト値を決める*ボリュームプリセット*と見なされる。プリセット*と*ボリュームセクションの両方で指定されたオプションについては、ボリュームオプション設定がプリセットオプションを完全に上書きする。

サーバが許可したアクセス権は、ホストシステムの特定のUNIXユーザまたはゲストユーザのアクセス権でマスクされる。サーバはホストシステムの許可以上の許可をしない。

以下のセクションの例は、一つのAFPボリュームを定義している。ユーザはパス`/foo/bar`への完全なアクセス権を持つ。
`baz`という共有名でアクセスできる:

     [baz]
        path = /foo/bar

# 特殊なセクション

## \[Global\]セクション

このセクションのパラメータはサーバ全体に適用される。以下で(G)の印がついているパラメータはこのセクションで設定しなければならない。

## \[Homes\]セクション

このセクションはUNIXサーバ側のユーザのホームディレクトリを共有できるようにする。オプションの`path`パラメータを指定すると、ユーザのホームディレクトリ全体ではなく、サブディレクトリ`path`が共有される。`basedir
regex`オプションを定義する必要がある。これはホームディレクトリの親ディレクトリにマッチする正規表現である。(H)の印がついているパラメータはこのボリュームセクション用である。オプションパラメータ`home
name`はAFPボリューム名を変更するのに使うものであり、デフォルトは*$u's home*である。下の「変数置換」の項を見よ。

以下の例でこれを解説する。全てのユーザのホームディレクトリは`/home`の下にある:

     [Homes]
          path = afp-data
          basedir regex = /home

ユーザ*john*について、`/home/john/afp-data`というパスがAFPホームボリュームになる。

`basedir
regex`ががシンボリックリンクを含む場合、正規化した絶対パスを設定してください。`/home`が`/usr/home`にリンクしているとき:

     [Homes]
          basedir regex = /usr/home

# パラメータ

パラメータはセクション固有の属性を定義する。

いくつかのパラメータは\[Global\]セクションに固有のものである(たとえば*log
type*)。それ以外は全てボリュームセクションのみに許される。(*G*)はパラメータが\[Global\]セクション固有であることを示す。(*V*)はボリューム固有のセクションで指定できることを示す。

# 変数置換

ボリューム名で変数を使うことができる。パスでの変数の利用は$uに限られる。

1.  不明な変数を指定した場合、それは変換されない。

2.  既知の変数を指定したが変数が値を持たない場合、それは無視される。

置換に使われる変数は以下のとおり:

$b

> ベース名

$c

> クライアントのIPアドレス

$d

> サーバ上のボリュームパス名

$f

> フルネーム (passwdファイルのGECOSフィールドの内容)

$g

> グループ名

$h

> ホスト名

$i

> クライアントのIPアドレス。ポート番号なし

$s

> サーバ名 (ホスト名になることができる)

$u

> ユーザ名 (ゲストの場合、ゲストとして動作しているユーザ名)

$v

> ボリューム名

$$

> ドル記号($)を表示する

# グローバルパラメータの説明

## 認証オプション

ad domain = `DOMAIN` `(G)`

> 認証時にユーザ名に@DOMAINを追加する。Active
Directory環境で有用。さもなくば、完全な文字列user@domainで参加するユーザを要求するだろう。

admin auth user = `user` `(G)`

> 例えば"`admin auth user = root`"を指定すると、通常ユーザのログインが失敗したときにafpdは必ず指定した`admin auth user`として認証を試みる。これが成功した場合、元の接続ユーザとして通常のセッションが確立される。言い換えると、あなたが`admin auth user`のパスワードを知っている場合、如何なる他のユーザとしてでも認証できる。

admin group = <group\> `(G)`

> 信頼できるグループのユーザがログインしたときスーパユーザとして見えるようにする。このオプションはデフォルトで無効である。

force user = <USER\> `(G)`

> このサーバに接続する全ユーザへ、デフォルトユーザとして割り当てるUNIXユーザ名を指定する。これは共有ファイルに役立つ。間違ってセキュリティ問題を引き起こすような使い方が可能なので、それにも注意して利用すべきである。

force group = <GROUP\> `(G)`

> このサーバに接続する全ユーザへ、デフォルトプライマリグループとして割り当てるUNIXグループ名を指定する。

k5 keytab = <path\> `(G)`; k5 service = <service\> `(G)`; k5 realm = <realm\> `(G)`

> サーバがKerberos 5認証UAMをサポートする場合、これらが必要である。

nt domain = `DOMAIN` `(G)`; nt separator = `SEPARATOR` `(G)`

> 例えばwinbind認証で利用し、有効かつ動作中のUAM認証を通して、ログイン時のユーザ名の前に両方の文字列を付けたもので認証を試みる。

save password = <BOOLEAN\> (default: *yes*) `(G)`

> パスワードをローカルに保存するクライアントの機能を有効または無効にする。

set password = <BOOLEAN\> (default: *no*) `(G)`

> chooserや「サーバへ接続」のダイアログを通してパスワードの変更をするクライアントの機能を有効または無効にする。

uam list = <uam list\> `(G)`

> スペースまたはカンマで区切られたUAMの一覧。(デフォルトは「uams_dhx.so
uams_dhx2.so」)

最も一般的に使われるUAMは以下の通り:

uams_guest.so

> ゲストログインを許可する

uams_clrtxt.so

> (uams_pam.soまたはuams_passwd.so)
暗号化なしで転送されたパスワードによるログインを許可する。(時代遅れ)

uams_randnum.so

> 認証のための乱数および双方向乱数交換を許可する
(パスワードを含んだファイル、つまりafppasswdファイルか"`passwd file`"で指定したファイルのどちらかが必要)。詳細は
`afppasswd(1)`を見よ。(時代遅れ)

uams_dhx.so

> (uams_dhx_pam.soまたはuams_dhx_passwd.so)
認証のためのDiffie-Hellman交換(DHX)を許可する。

uams_dhx2.so

> (uams_dhx2_pam.soまたはuams_dhx2_passwd.so)
認証のためのDiffie-Hellman交換2(DHX2)を許可する。

uam_gss.so

> 認証のためのKerberos Vを許可する。(オプション)

uam path = <path\> `(G)`

> このサーバのためのUAMのデフォルトパスを設定する。

## 文字セットオプション

OS XでAppleはAFP3プロトコルを導入した。大きな変更の一つは、AFP3は分解済UTF-8
(UTF8-MAC)としてエンコードされたUnicode名を用いることである。以前のAFP及びOSバージョンはMacRomanやMacCentralEuropeといった文字セットを用いた。

AFP3と古いクライアントに同時に応対できるように、`afpd`はUTF-8とMac文字セットの間の変換ができる必要がある。OS
Xですら部分的にMac文字セットに依存している。AFP3以前のクライアントが使うコードページを`afpd`が検出する方法はないので、あなたは`mac
charset`オプションを使ってそれを指定しなけらばならない。デフォルトはMacRomanであり、多くの西欧ユーザにとって良いであろう。

`afpd`はUNIXオペレーティングシステムとも相互に作用する必要があるので、UTF8-MAC/Mac文字セットからUNIX文字セットへ変換できる必要がある。デフォルトで`afpd`は*UTF8*を用いる。`unix
charset`オプションを使ってUNIX文字セットを設定できる。`afpd`のための設定ファイルで拡張文字セットを使う場合、端末が`unix
charset`に一致することを確認してください。

mac charset = `CHARSET` `(G)/(V)`

> Macクライアントの文字セット、例えば*MAC_ROMAN*を指定する。これは文字列やファイル名をOS9やClassic環境のクライアントコードページに変換するために用いられる。すなわち認証やAFPメッセージ(SIGUSR2
messaging)である。これはボリュームの`mac charset`のデフォルトにもなる。デフォルトは*MAC_ROMAN*。

unix charset = `CHARSET` `(G)`

> サーバのunix文字セット、例えば*ISO-8859-15*や*EUC-JP*を指定する。これは文字列をシステムロケールとの間で変換するのに使われる。すなわち認証やサーバメッセージやボリューム名である。LOCALEが設定された場合、システムロケールが使われる。デフォルトはUTF8。

vol charset = `CHARSET` `(G)/(V)`

> ボリュームのファイルシステムのエンコーディングを指定する。デフォルトでは`unix charset`と同じである。

> **注記**

> デフォルトのUTF-8エンコーディングを使うことをを強く推奨する。

## パスワードオプション

passwd file = `path` `(G)`

> このサーバの乱数UAMパスワードファイルのパスを設定する。

passwd minlen = `number` `(G)`

> UAMが最小パスワード長をサポートする場合、それを設定する。

## ネットワークオプション

advertise ssh = <BOOLEAN\> (default: *no*) `(G)`

> 古いMac OS
Xクライアント(10.3.3から10.4)にSSHでトンネルしたAFP接続を魔法のように自動的に確立させる。このオプションを設定した場合、クライアントのFPGetSrvrInfo要求へのサーバの返答は追加エントリを含む。これはクライアントの設定と`sshd(8)`が正しく設定されて動作するサーバ上で実行中であるかに依存する。

> **注記**

> SSHを介した全体を暗号化するAFP接続はサーバの負荷を著しく増加させるので、このオプションの設定は推奨しない。一方、バージョン10.3.4より前のMacOS
Xにおけるこの機能のAppleクライアント側の実装はセキュリティ欠陥があった。

afp interfaces = <name \[name ...\]\> `(G)`

> サーバがリッスンするネットワークインターフェースを指定する。デフォルトではシステムの最初のIPアドレスを宣伝するが、入ってくる如何なる要求もリッスンする。

> **注記**

> `afp listen` オプションと同時に使用しないでください。

afp listen = <ip address\[:port\] \[ip address\[:port\] ...\]\> `(G)`

> サーバが宣伝**および**リッスンするIPアドレスを指定する。デフォルトではシステムの最初のIPアドレスを宣伝するが、入ってくる如何なる要求もリッスンする。ネットワークアドレスはIPv4のドット付き10進数フォーマットやIPv6の16進数フォーマットのどちらでも指定してよい。

IPv6 address + portの組み合わせは角かっこを使ったフォーマット\[IPv6\]:portのURLを使わなければならない。

> **注記**

> `afp interfaces` オプションと同時に使用しないでください。

afp port = <port number\> `(G)`

> 異なるTCPポートをAFPに使わせる。デフォルトは548である。`afp listen`オプションで何も指定しなかった場合も適用されたデフォルトポートを設定する。

appletalk = <BOOLEAN\> (default: *no*) `(G)`

> AFP-over-Appletalk
のサポートを有効にする。このオプションを使用するには、オペレーティング
システムが AppleTalk ネットワーク
プロトコルをサポートしている必要がある。

cnid listen = <ip address\[:port\] \[ip address\[:port\] ...\]\> `(G)`

> CNIDサーバがリッスンするIPアドレスを指定する。デフォルトは**localhost:4700**である。

ddp address = <ddp address\> `(G)`

> サーバーの DDP アドレスを指定する。デフォルトでは、アドレス (0.0)
が自動的に割り当てられる。これは、複数のインターフェイスで AppleTalk
を実行している場合にのみ役立つ。

ddp zone = <ddp zone\> `(G)`

> サーバーを登録する AppleTalk
ゾーンを指定する。デフォルトでは、システムによって最後に構成されたインターフェースのデフォルト
ゾーンにサーバーが登録される。

disconnect time = <number\> `(G)`

> ドロップする前に、切断されたAFPセッションを`number`時間維持する。デフォルトは24時間である。

dsireadbuf = <number\> `(G)`

> DSI/TCP先読みバッファのサイズを決定する係数。デフォルトは12である。これにDSI
server quantum
(デフォルトは1MiB)をかけるとバッファサイズになる。この値を増やすと速いローカルネットワークでのボリュームからボリュームへのコピーのスループットが増えるかもしれない。
*注記*:
このバッファはafpdの子プロセス毎に割り当てられるので、大きな値を指定すると大量のメモリが食われる
(バッファサイズ \* クライアント数)。

fqdn = <name\[:port\]\> `(G)`

> Specifies a fully-qualified domain name, with an optional port. This is
discarded if the server cannot resolve it. This option is not honored by
AppleShare clients <= 3.8.3. This option is disabled by default. Use
with caution as this will involve a second name resolution step on the
client side. Also note that afpd will advertise this name:port
combination but not automatically listen to it.

hostname = <name\> `(G)`

> 宣伝用のIPアドレスを決定するため、ホスト名の呼出結果の代わりにこれを用いる。従って、このホスト名から宣伝用IPアドレスが解決されるようになる。これはリスニングには使われないし、`afp listen`によっても上書きされてしまう。

max connections = <number\> `(G)`

> 同時にサーバに接続できるクライアントの最大数を設定する(デフォルトは200)。

server quantum = <number\> `(G)`

> これはDSI server quantumを指定する。デフォルト値は0x100000
(1MiB)である。最大値は0xFFFFFFFFFであり最小値は32000である。範囲外の値を指定した場合、デフォルト値が設定される。自分が何をしようとしているか確信がない限り、この値を変更しないでください。

sleep time = <number\> `(G)`

> スリープモードにおいてクライアントを切断する前に、スリープ中のAFPセッションを`number`時間維持する。デフォルトは10時間である。

tcprcvbuf = <number\> `(G)`

> setsockopt()を使ってTCP受信バッファの設定を試みる。しばしばOSはこの値を設定しようとするアプリケーションの資格を制限する。

tcpsndbuf = <number\> `(G)`

> setsockopt()を使ってTCP送信バッファの設定を試みる。しばしばOSはこの値を設定しようとするアプリケーションの資格を制限する。

recvfile = <BOOLEAN\> (default: *no*) `(G)`

> データ受信のためにLinuxのsplice()を使うかどうか。

splice size = <number\> (default: *64k*) `(G)`

> spliceする最大バイト数。

use sendfile = <BOOLEAN\> (default: *yes*) `(G)`

> クライアントにファイルデータを送るためにsendfileシステムコールを使うかどうか。

zeroconf = <BOOLEAN\> (default: *yes*) `(G)`

> AvahiまたはmDNSResponder込みでコンパイル済の場合、自動的なZeroconfサービス登録を使うかどうか。

## 雑多なオプション

afp read locks = <BOOLEAN\> (default: *no*) `(G)`

> FPReadコールにおいてバイト領域リードロックを適用するかどうか。AFPの仕様はこれを義務付けるが、実際のところこれはUNIXの動作に合致しないし、パフォーマンスを抑え込む。

afpstats = <BOOLEAN\> (default: *no*) `(G)`

> dbusを介してAFPランタイム統計 (接続ユーザ、開いてるボリューム)
を提供するかどうか。

basedir regex = <regex\> `(H)`

> ユーザホームの親ディレクトリにマッチする正規表現。`basedir regex`がシンボリックリンクを含む場合、正規化した絶対パスを設定しなければならない。簡単なケースだとこれは単に一つのパスである。つまり`basedir regex = /home`である。

chmod request = <preserve (default) | ignore | simple\> `(G)/(V)`

> ACLに対応する高度なパーミッション制御。

- `ignore` -
  UNIXのchmod()要求を完全に無視する。新規作成を上書きして親ディレクトリのACL継承に完全コントロールさせるためにこのオプションを使う。

- `preserve` - 名前付きユーザとグループのためのZFS ACEやPOSIX ACLグループマスクを維持する

- `simple` - いかなる追加の手順も踏まず、単に要求通りにchmod()する

close vol = <BOOLEAN\> (default: *no*) `(G)`

> ボリュームが設定から削除され、その設定が再読み込みされたとき、クライアントが既に開いているボリュームを可能な限り閉じるかどうか。

cnid mysql host = <MySQL server address\> `(G)`

> mysql CNIDバックエンド利用時のMySQLサーバの名前またはアドレス。

cnid mysql user = <MySQL user\> `(G)`

> MySQLサーバ認証のためのユーザ名。

cnid mysql pw = <password\> `(G)`

> MySQLサーバのためのパスワード。

cnid mysql db = <database name\> `(G)`

> 指定ユーザが完全アクセス権を持つための存続しているデータベースの名前。

cnid server = <ipaddress\[:port\]\> `(G)/(V)`

> cnid_metadサーバのIPアドレスとポート番号を指定する。CNID
dbdバックエンドのために必要。デフォルトはlocalhost:4700。ネットワークアドレスはIPv4のドット分割10進数フォーマットでもよいし、IPv6の16進数フォーマットでもよい。

dbus daemon = `path` `(G)`

> Spotlight機能が使用するdbus-daemon実行ファイルのパスを設定する。
コンパイル時のデフォルト値が実行環境と一致しない場合に使用する。

dircachesize = <number\> `(G)`

> ディレクトリキャッシュにおける最大エントリ数。キャッシュはディレクトリとファイルを格納する。これはディレクトリのフルパスと、ディレクトリ一覧を大幅にスピードアップするCNIDをキャッシュするために使われる。

デフォルトサイズは8192、最大サイズは131072。与えられた値は最も近い2の累乗に丸められる。それぞれのエントリは約100バイトを消費し、これは大きな値とは言えないが、それぞれの接続ユーザ毎のafpd子プロセスがキャッシュを持つことを念頭に置いてください。

extmap file = `path` `(G)`

> ファイル拡張子とタイプ/クリエータのマッピングを定義するファイルのパスを設定する。

force xattr with sticky bit = <BOOLEAN\> (default: *no*) `(G/V)`

> ディレクトリへの書き込み権限があったとしても、スティッキービット設定を使ってメタデータ(拡張属性)を書き込むことに失敗するかもしれない。なぜなら、スティッキービットが設定されている場合、所有者だけが拡張属性への書き込みを許されるからである。

このオプションを有効にするとNetatalkはroot権限でメタデータ(拡張属性)を書き込む。

guest account = <name\> `(G)`

> ゲストが利用するユーザ名を指定する (デフォルトは nobody である)。
本ユーザ名はシステム上の有効なユーザーである必要がある。

home name = <name\> `(H)`

> AFPユーザのホームのボリューム名。デフォルトは*$u's home*である。
ボリューム名の文字列に"*$u*"は必須である。

ignored attributes = <all | nowrite | nodelete | norename\> `(G)/(V)`

> サーバが無視すべきファイルとディレクトリの属性を設定する。`all`はオプション全部という意味である。

OS Xにおいて、Finderがファイル/ディレクトリのロックを設定する場合、またはターミナルでBSD
uchgフラグを設定する場合、3つの属性が全て使われる。従って、Finderロック/BSD uchgフラグを無視する目的で*ignored
attributes = all*の設定を追加してください。

legacy icon = <icon\> `(G)`

> Classic Mac OS の Finder に表示される共有ボリューム アイコンを設定する。
参考に、ある Classic Mac OS
バージョンでは、このアイコン設定が無視される。
有効なアイコン名の例は以下になる。

- `daemon`

- `globe`

- `sdcard`

login message = <message\> `(G)/(V)`

> クライアントがサーバにログオンしたときに表示されるメッセージを設定する。メッセージは`unix charset`で書く。拡張文字が使える。

mimic model = <model\> `(G)`

> クライアント上に表示されるアイコンモデルを指定する。デフォルトではクライアント
Mac
に任せること。netatalkがZeroconfをサポートしなければならないことに注意してください。例:

- `Laptop`

- `RackMount`

- `Tower`

macOSは認識しているモデルコードは
`/System/Library/CoreServices/CoreTypes.bundle/Contents/Info.plist`
を参照すれば確認できる。(macOS 14 Sonoma の場合)

signature = <STRING\> `(G)`

> サーバシグネチャを指定する。最大長は16文字である。このオプションは障害隔離などを提供するクラスタ環境において有用である。デフォルトでは、afpdは自動的にシグネチャを(乱数を元に)生成し、それを`afp_signature.conf`に保存する。asip-status(1)も見よ。

solaris share reservations = <BOOLEAN\> (default: *yes*) `(G)`

> Solarisの共有予約を利用する。Solaris
CIFSサーバもこれを利用するので、ロックを統一したマルチプロトコルサーバを形成する。

sparql results limit = <NUMBER\> (default: *UNLIMITED*) `(G)`

> SPARQLクエリを介した Tracker もしくは LocalSearch
からのクエリ結果の数に制限を課す。

spotlight = <BOOLEAN\> (default: *no*) `(G)/(V)`

> Spotlight検索を有効にするかどうか。注記:
一度グローバルオプションで有効にすると、有効でないボリュームは全く検索できない。*dbus
daemon*オプションも見よ。

spotlight attributes = <COMMA SEPARATED STRING\> (default: *EMPTY*) `(G)`

> Spotlight検索で使うことを許された属性のリスト。デフォルトでは全ての属性を検索できるが、文字列を渡せば属性をその文字列の要素に制限できる。
例:

    spotlight attributes = *,kMDItemTextContent

spotlight expr = <BOOLEAN\> (default: *yes*) `(G)`

> 検索において論理式の使用を認めるかどうか。

veto message = <BOOLEAN\> (default: *no*) `(G)`

> 禁止ファイルに関するオプションのAFPメッセージを送る。クライアントが禁止名を持つファイルやディレクトリにアクセスを試みたとき、名前とディレクトリを示したAFPメッセージを送る。

vol dbpath = <path\> `(G)/(V)`

> データベース情報をpathに格納するように設定する。ボリュームが読み込み専用だったとしても、書き込み可能な場所を設定しなければならない。

vol dbnest = <BOOLEAN\> (default: *no*) `(G)`

> このオプションをtrueに設定するとNetatalk
2の動作に立ち返る。つまり、それぞれの共有のボリュームルートの下にある.AppleDBというフォルダにCNIDデータベースを格納する。

volnamelen = <number\> `(G)`

> Mac OS
XのためのUTF8-MACボリューム名の最大長。ハングルはこれに特に敏感なので注意してください。

    73: Mac OS X 10.1の制限
    80: Mac OS X 10.4/10.5の制限 (デフォルト)
    255: 最近のMac OS Xの制限

Mac OS 9以前はこれに影響されない。なぜならMac文字セットのボリューム名は常に27バイト制限がある。

vol preset = <name\> `(G)/(V)`

> (\[Global\]セクションで設定したときは)
全ボリューム、(ボリュームセクションで設定したときは)そのボリュームのオプション初期設定となるセクションの`name`を使う。

zeroconf name = <name\> `(G)`

> 登録サービスをユニークに表した、人間が読めるnameを設定する。このzeroconf
nameは最大長63オクテット（バイト）のUTF-8で宣伝される。netatalkがZeroconfをサポートしなければならないことに注意してください。

## ログのオプション

log file = <logfile\> `(G)`

> ログを`logfile`に出力する。指定しない場合、Netatalkはsyslogデーモン機能にログを出力する。

log level = <type:level \[type:level ...\]\> `(G)`; log level =
<type:level,\[type:level, ...\]\> `(G)`

> 与えられた`log level`までのログレベルのメッセージを出力するように設定する。

デフォルトではafpdは`default:note`に相当する設定でsyslogに出力する。

ログタイプ: default, afpdaemon, logger, uamsdaemon

ログレベル: severe, error, warn, note, info, debug, debug6, debug7, debug8,
debug9, maxdebug

> **注記**

> ログタイプとログレベルはどちらも大文字小文字を区別しない。

log microseconds = <BOOLEAN\> (default: *yes*) `(G)`

> タイムスタンプをマイクロ秒単位の精度でログに記録する。無効にすると、タイムスタンプは秒単位のみを記録する。`log file`
オプションと組み合わせて使用​​した場合にのみ有効になる。

## ファイルシステム変更イベント (FCE)

Netatalk には素敵なファイルシステム変更イベント機構が含まれている。ここで、afpd
プロセスは、なにがしかのファイルシステムイベントについて、関心を寄せているリスナーに、UDP ネットワークデータグラムで通知する。

以下の FCE イベントが定義されている:

- ファイル変更 (`fmod`)

- ファイル削除 (`fdel`)

- ディレクトリ削除 (`ddel`)

- ファイル作成 (`fcre`)

- ディレクトリ作成 (`dcre`)

- ファイル移動または名前変更 (`fmov`)

- ディレクトリ移動または名前変更 (`dmov`)

- ログイン (`login`)

- ログアウト (`logout`)

fce listener = <host\[:port\]\> `(G)`

> FCE イベントを指定された `host`
に送ることができるようにする。もし指定されていなければデフォルトの
`port` は 12250
である。複数のリスナーを指定するにはそれぞれのリスナーに対するオプションを一度に指定することである。

fce version = <1|2\> `(G)`

> FCE プロトコルのヴァージョンで、デフォルトでは 1
である。fmov、dmov、login あるいは logout イベントのためにはバージョン 2
が必要である。

fce events = <fmod,fdel,ddel,fcre,dcre,fmov,dmov,login,logout\> `(G)`

> どの FCE イベントがアクティブかを指定する。デフォルトでは
`fmod,fdel,ddel,fcre,dcre` である。

fce coalesce = <all|delete|create\> `(G)`

> FCE イベントを結合する。

fce holdfmod = <seconds\> `(G)`

> これは、もしクライアントによって FCE ファイル変更イベント (fmod)
を送信する前に同じファイルに対する別の変更が同時に行われる場合、常に待機する遅延時間を秒単位で決定する。例えば、フォトショップでファイルを保存することでそのファイル自体の複数のイベントを引き起こす。なぜなら、アプリケーションはその“保存する”たびにファイルを複数回、開き、変更しそして閉じるからである。デフォルトでは
60 秒である。

fce sendwait = <milliseconds\> `(G)`

> 各 FCE イベントの発行間の遅延をミリ秒単位で定義する。
非常に多くのファイルを一度に作成または削除するときに、FCE
イベントの損失が発生する場合は、これを使用して問題を防げる。
このような操作によって引き起こされる大量のイベントにより、UDP バッファ
オーバーフローが発生し、その後パケット損失が発生する可能性がある。 0
から 999 までの値は設定可能。デフォルト: 0 ミリ秒。

fce ignore names = <NAME\[/NAME2/...\]\> `(G)`

> FCE
イベントを生成すべきでないファイル名をスラッシュで区切ったリスト。デフォルトでは
.DS_Store。

fce ignore directories = <NAME\[,NAME2,...\]\> `(G)`

> FCE
イベントが生成されないディレクトリのカンマ区切りのリスト。デフォルトは無し。

fce notify script = <PATH\> `(G)`

> 各々の FCE
イベントに対して実行されるスクリプト。スクリプト例については、Netatalk
のソースの contrib/shell_utils/fce_ev_script.sh を参照のこと。

## デバッグパラメータ

これらのオプションはデバッグのみに有用である。

tickleval = <number\> `(G)`

> tickleタイムアウトの間隔を(秒単位で)設定する。デフォルトは30。

timeout = <number\> `(G)`

> 接続がタイムアウトする前に送るtickleの数を指定する。デフォルトは4なので、2分後に接続がタイムアウトする。

client polling = <BOOLEAN\> (default: *no*) `(G)`

> このオプションを有効にすると、afpdはserver
notificationの機能があることを宣伝しない。これは、接続中のクライアントが開いているサーバのウインドウの変更を検出するために10秒毎にポーリングするのを目的としている。*注記*:
同時接続クライアント数とネットワークスピード次第でネットワークの負荷が相当に高くなる!

現在のNetatalkはserver
notificationを正確にサポートしており、接続中のクライアントは他のクライアントが内容を変更したときにフォルダ内の一覧を更新できるので、もはやこのオプションは使わないでください。

## ACL処理のためのオプション

デフォルトでは、認証済ユーザの有効な権限は記載済UARights権限構造にだけマップされる。UNIXモードではない。この挙動は設定オプション`map
acls`で調整できる:

map acls = `none|rights|mode` `(G)`

> none

> ACLのマッピングをしない

rights

> 有効な権限がUARights構造にマップされる。これがデフォルトである。

mode

> ACLはファイルシステムオブジェクトのUNIXモードにもマップされる。

もしクライアント上で ACL を表示できるようにしたければ、 クライアントもサーバーも認証ドメイン（ディレクトリサービス、例えば、LDAP、Open
Directory、Active Directory）の一部としてセットアップしなければならない。その理由は、OS X の ACL は単に uid
ないしは gid と結合しているのではなく、UUID と結合しているからである。それ故、Netatalk は、OS X の UUID と紐付けした
UNIX uid と gid に結合したサーバー側の ACL を返せるように、ファイルシステム全ての uid と gid を UUID
と紐付けできるようにしなければならない。

Netatalk は LDAP 検索を用いてディレクトリサーバーを検索をすることができる。ディレクトリサーバーが既にユーザーとグループの UUID
属性を提供している（Active Directory、Open
Directory）か、ディレクトリサーバー（例えばOpenLDAP）の未使用の属性を再使用（あるいは新しい属性を追加）するか、のいずれかである。

Netatalk では以下の LDAP オプションが設定されなければならない:

ldap auth method = `none|simple|sasl` `(G)`

> 認証方式: `none | simple | sasl`

none

> 匿名 LDAP 認証

simple

> 簡易 LDAP 認証

sasl

> SASL. まだサポートされていない!

ldap auth dn = `dn` `(G)`

> 簡易認証でのユーザーの識別名。

ldap auth pw = `password` `(G)`

> 簡易認証でのパスワード。

ldap uri = `ldap://somehost:1234/` `(G)`

> 接続先のLDAP サーバーのURI。選択可能の URI スキームは ldap、ldapi 又は
ldaps である。TCP、ICP 又は TLS プロトコルに当たる。実際のサポートは
LDAP ライブラリ次第。本オプションは LDAP に UUID
の問い合わせをできるようにするために、明示的な ACL
サポートを必要とする時のみ必要。

設定の構文的なチェックのために `afpldaptest(1)` を使うこともできる。

ldap userbase = `base dn` `(G)`

> LDAP 内のユーザーコンテナの DN。

ldap userscope = `scope` `(G)`

> ユーザー検索での検索スコープ: `base | one | sub`

ldap groupbase = `base dn` `(G)`

> LDAP 内のグループコンテナの DN。

ldap groupscope = `scope` `(G)`

> グループ検索での検索スコープ: `base | one | sub`

ldap uuid attr = `dn` `(G)`

> UUID のある LDAP 属性の名前。

注記: これはユーザーでもグループでも双方で用いられる。

ldap name attr = `dn` `(G)`

> ユーザーの短縮名のある LDAP 属性の名前。

ldap group attr = `dn` `(G)`

> グループの短縮名のある LDAP 属性の名前。

ldap uuid string = `STRING` `(G)`

> ディレクトリでの UUID 文字列のフォーマット。'x' と
'-'を続けたもので、それぞれの 'x' は 0-9a-f の値を示し、'-'
はそれぞれ区切り文字である。

デフォルト: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

ldap uuid encoding = `string | ms-guid (デフォルト: string)` `(G)`

> LDAP 属性の UUID のフォーマットは Active Directory からの obhectGUID
バイナリーフィールドの使用を許す。もし未指定のままだと string
がデフォルトとなる。これはほとんどの LDAP ストアによって ASCII UUID
を通して渡される。もし ms-guid
が設定されると、サーバーと相互に動作する時 Active Directory
内にあるオブジェクトの objectGUID 属性で用いられる内部 UUID
表記とバイナリー形式が相互に変換される。

オプション `ldap user filter` 及び `ldap group filter` も参照のこと。

string

> UUID は文字列。例えば OpenDirectory とで使用する。

ms-guid

> Active Directory からの objectGUID バイナリー。

ldap user filter = `STRING (デフォルト: 未使用)` `(G)`

> ユーザーオブジェクトにマッチする任意の LDAP
フィルター。これは、ユーザーとグループが同じディレクトリのサブツリーに保存されている
Active Directory 環境で必要。

Active Directory での推奨設定: `objectClass=user`

ldap group filter = `STRING (デフォルト: 未使用)` `(G)`

> グループオブジェクトにマッチする任意の LDAP
フィルター。これは、ユーザーとグループが同じディレクトリのサブツリーに保存されている
Active Directory 環境で必要。

Active Directory での推奨設定: `objectClass=group`

# ボリュームパラメータの説明

## パラメータ

セクション名ボリューム名を定義する。同じ名前の二つのボリュームというのは無いであろう。ボリューム名が文字 ':'
を含むことはできない。ボリューム名がとても長ければマングルされる。Mac キャラクターセットのボリューム名は27 文字までに制限される。UTF8-MAC
ボリューム名は volnamelen パラメータで制限される。

path = <PATH\> `(V)`

> パス名は完全修飾パス名でなければならない。

appledouble = <ea|v2\> `(V)`

> メタデータファイルのフォーマットを指定する。これは Mac
のリソースフォークの保存にも用いられる。初期のバージョンでは AppleDouble
v2 が用いられ、新しいデフォルトのフォーマットは **ea** である。

vol size limit = <size in MiB\> `(V)`

> Time Machine に有用：報告されるボリュームサイズを制限する。故に Time
Machine
がバックアップのために実ディスク領域全体を使うことを防止する。例えば
"vol size limit = 1000" は報告されるディスク領域を 1 GB
に制限する。

> **重要**

> これは Time Machine sparsebundle
イメージの中身を考慮した概算である。それ故このオプションを使用した時、このボリュームを他のコンテンツを保管するのに使用
“してはならない”。なぜなら勘定に入っていないからである。計算は:
sparsebundle の Info.plist XML
ファイルからバンドサイズを読む、バンドファイルの数を数えて
バンド／ディレクトリ
を読む、そしてお互いの乗算をする。ことによって行われる。

valid users = <user @group\> `(V)`

> この許可オプションは指定された共有にそのユーザーとグループのアクセスを許可する。ユーザーとグループはスペースかコンマで区切って指定する。グループは
@ プレフィックスで明示する。例:

    valid users = user @group

invalid users = <users/groups\> `(V)`

> この拒否オプションはその共有にアクセスを許可しないユーザーとグループを指定する。それ以外は
"valid users" オプションと同じフォーマットである。

hosts allow = <IP host address/IP netmask bits \[ ... \]\> `(V)`

> 列挙されたホストとネットワークのみが許可され、ほかの全ては拒否される。ネットワークアドレスは
IPv4
のドット区切りフォーマット、IPv6の16進数フォーマットのどちらでもよい。

例: hosts allow = 10.1.0.0/16 10.2.1.100 2001:0db8:1234::/48

hosts deny = <IP host address/IP netmask bits \[ ... \]\> `(V)`

> 列挙されたホストとネットのみが拒否され、ほかの全ては許可される。

例: hosts deny = 192.168.100/24 10.1.1.1 2001:db8::1428:57ab

cnid scheme = <backend\> `(V)`

> そのボリュームに使う CNID
バックエンドをセットする。デフォルトのバックエンドは
\[@DEFAULT_CNID_SCHEME@\] で、有効なバックエンドは
\[@compiled_backends@\] である。

> **注記**

> 「mysql」バックエンドでは、システム管理者が netatalk で使用するために
MySQL データベース インスタンスを構成する必要がある。

> **警告**

> `afpd` が持続性のある ID
データベースに重く依存しているので、このバックエンドをボリュームに使用するのは推奨*されていない*。エイリアスはおそらく機能しないだろうし、ファイル名のマングリングもサポートされていない。

ea = <none|auto|sys|ad|samba\> `(V)`

> 拡張属性をどのように保存するか指定する。`auto`
がデフォルトである。

auto

> （共有ディレクトリ自体に EA を設定することにより） `sys`
を試行して、フォールバックすると `ad`
になる。試行を実行するためにはボリュームが書き込み可能であることが必要である。"`read only = yes`"
ならば `auto` は `none`
で上書きされる。書き込み専用のボリュームには必要に応じて明確に
"`ea = sys|ad`" を使ってください。

sys

> ファイルシステムの拡張属性を使う。

samba

> ファイルシステムの拡張属性を使うが、Sambaのvfs_streams_xattrとの互換性の目的で、それぞれの拡張属性に値がゼロの1バイトを追加する。

ad

> *.AppleDouble* ディレクトリ内のファイルを使う。

none

> 拡張属性をサポートしない。

> **警告**

> **samba** オプションは、以前に **sys**
に設定されたボリュームでは使用しないでください。これにより、データが失われる可能性がある。

mac charset = <CHARSET\> `(V)`

> もしグローバル設定を適用する指定がなければ、そのボリュームに対しての Mac
クライアントのキャラクターセット、例えば *MAC_ROMAN*、*MAC_CYRILLIC*
等を指定する。この設定は Mac キャラクターセットが \[Global\]
セクションで全体的にセットしたキャラクターセットと異なるというボリュームを必要とする時のみ必須である。

casefold = `option` `(V)`

> ファイル名の大文字小文字を変更すべき場合、casefold
オプションが処理する。有効なオプションは:

`tolower` - 双方向で名前を小文字に変換する。

`toupper` - 双方向で名前を大文字に変換する。

`xlatelower` - クライアントでは小文字に見えて、サーバでは大文字に見える。

`xlateupper` - クライアントでは大文字に見えて、サーバでは小文字にみえる。

password = <password\> `(V)`

> このオプションはボリュームパスワードの設定を許可する。パスワードは最大で
8 文字の長さ（これを記入するときには ASCII を強く推奨）

file perm = <mode\> `(V)`; directory perm = <mode\> `(V)`

> クライアントが要求した権限との論理和(or)をとる。`file perm`
はファイルにのみ、`directory perm` はディレクトリにのみ用いる。
"`unix priv = no`" と共に用いてはならない。

## 例：共同作業グループ向けのボリューム

    file perm = 0660
    directory perm = 0770

umask = <mode\> `(V)`

> 権限のマスクを設定する。"`unix priv = no`" と共に用いてはならない。

preexec = <command\> `(V)`

> ボリュームがマウントされる時に実行されるコマンド

postexec = <command\> `(V)`

> ボリュームが閉じられる時に実行されるコマンド

rolist = `users/groups` `(V)`

> 信頼するユーザー及びグループの共有に対する読み込み専用アクセスを許可する。フォーマットは
allow オプションに準ずる。

rwlist = <users/groups\> `(V)`

> 信頼するユーザー及びグループの共有に対する読み込み／書き込みアクセスを許可する。フォーマットは
allow オプションに準ずる。

veto files = <vetoed names\> `(V)`

> '/' で区切られた
禁止名のどれかに一致するパスのファイルとディレクトリを隠す。禁止文字列は常に
'/' で終わらなければならない。例えば、"veto files = veto1/"、"veto files
= veto1/veto2/"。

## ボリュームオプション

ブーリアン型のボリュームオプション。

acls = <BOOLEAN\> (default: *yes*) `(V)`

> ボリュームが ACL をサポートしてるというフラグを立てるかどうか。もし ACL
サポートでコンパイルしていれば、これはデフォルトで yes。

case sensitive = <BOOLEAN\> (default: *yes*) `(V)`

> ボリュームが大文字小文字を区別したファイル名をサポートしてるというフラグを立てるかどうか。
もしファイルシステムが大文字小文字を区別しなければ no
を設定せよ。しかしながらこれは完全には確かめられていない。

> **注記**

> 実際には大文字小文字を区別しているにもかかわらず、netatalk 3.1.3
とそれ以前のものはクライアントに kCaseSensitive
フラグを通知しなかった。バージョン 3.1.4
からはデフォルトで正しく通知される。

cnid dev = <BOOLEAN\> (default: *yes*) `(V)`

> CNID バックエンド内でデバイス番号を使うかどうか。
例えばクラスターなどでリブートを経るとデバイス番号が固定ではない時有用。

convert appledouble = <BOOLEAN\> (default: *yes*) `(V)`

> クライアントからのファイルシステムへのアクセス時、`appledouble = v2`
から `appledouble = ea`
への自動的な変換を行うかどうか。これは概して有用であるがいくらかパフォーマンスが犠牲となる。ボリューム上で
`dbd` を実行しそれで変換をするのが推奨される。その後このオプションを no
に設定することもできる。

delete veto files = <BOOLEAN\> (default: *no*) `(V)`

> このオプションは Netatalk が一つあるいはそれ以上の veto
されたファイルあるいはディレクトリ（veto files
オプションを見よ）を削除しようとした時用いられる。もしこのオプションを
no に設定し（デフォルト）、そしてもしあるディレクトリが何か非 veto
ファイルないしはディレクトリを含んでいたら、ディレクトリの削除は失敗するであろう。これは通常あなたの望むところの動作である。

もしこのオプションが yes に設定されていたら、Netatalk は veto
化ディレクトリ・ディレクトリ内も含めあらゆるファイル、ディレクトリを再帰的に削除しようとするであろう。

follow symlinks = <BOOLEAN\> (default: *no*) `(V)`

> デフォルトの設定では偽なのでサーバー上でシンボリックリンクは辿られない。これは
OS X の AFP サーバーと同じ挙動である。オプションを真に設定すると afpd
がサーバー上でシンボリックリンクを辿るようにさせる。今のところ afpd は
"wide symlinks" を全く検査しないので、シンボリックリンクは AFP
ボリューム以外を指しているかもしれない。

> **注記**

> シンボリックリンクがファイルシステムの境界をまたいで張られている時、このオプションは巧妙に断ち切る。

invisible dots = <BOOLEAN\> (default: *no*) `(V)`

> ドットファイルを不可視にする。警告：このオプションを有効にすると、望まない副作用を
OS X アプリケーションに引き起こす。つまり、
先頭がドットではじまる一時ファイルにファイルをセーブし、それから一時ファイルを最終的なファイル名にリネームした時、
結果としてセーブしたファイルが見えなくなる。唯一このオプションが有用なのは、Mac
OS 9 でドットからはじまるファイルを見えなくさせるためである。Mac OS X
では、Finder
でもターミナルでもドットではじまるファイルはいずれにしても隠しファイルなので、完全に無駄である。

legacy volume size = <BOOLEAN\> (default: *no*) `(V)`

> レガシー クライアントのディスク サイズ レポートを 2GB
に制限する。これは、System 7.1 以前を実行し、新しい AppleShare
クライアントを使用している古い Macintosh で使用できる。

network ids = <BOOLEAN\> (default: *yes*) `(V)`

> サーバーがネットワーク id をサポートするかどうか。これを *no*
に設定すると結果としてクライアントは ACL AFP 機能を使わなくなる。

preexec close = <BOOLEAN\> (default: *no*) `(V)`

> preexec からの 0
以外のリターンコードで、クライアントがボリュームをマウントする／見ることを防ぐために当該ボリュームを即座に閉じる。

prodos = <BOOLEAN\> (default: *no*) `(V)`

> ProDOS サポートを有効にする。このオプションは、Apple II
をネットブートする予定のボリュームに対してのみ有効にする必要がある。ボリュームにブート
フラグを設定するだけでなく、表示されるボリュームの空き領域を 32MB
に制限する。

read only = <BOOLEAN\> (default: *no*) `(V)`

> その共有を全てのユーザーに対して読み込み専用と指定する。`ea = auto` は
`ea = none` で上書きされる。

search db = <BOOLEAN\> (default: *no*) `(V)`

> 低速な再帰的ファイルシステム検索の代わりに高速な CNID
データベースの名前検索を用いる。矛盾のない CNID
データベースを信頼する、すなわち Samba
やローカルのファイルシステムのアクセスが不正確さらには誤った結果を招く。"dbd"
CNID db のボリュームのみで動作する。

stat vol = <BOOLEAN\> (default: *yes*) `(V)`

> ボリュームリストを列挙するときにボリュームパスを stat
するかどうか。オートマウントや preexec
スクリプトで作成されたボリュームに有用である。

time machine = <BOOLEAN\> (default: *no*) `(V)`

> このボリュームの Time Machine サポートを有効にするかどうか。

unix priv = <BOOLEAN\> (default: *yes*) `(V)`

> AFP3 UNIX 権限を使うかどうか。これは OS X
クライアントに対しては設定すべきである。`file perm`、`directory perm`
及び `umask` も参照。

# 関連項目

`afpd(8)`, `afppasswd(5)`, `afp_signature.conf(5)`, `extmap.conf(5)`,
`cnid_metad(8)`

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
