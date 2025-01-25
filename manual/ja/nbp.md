# 名前

nbplkup, nbprgstr, nbpunrgstr — NBP データベースにアクセスするツール群

# 説明

`nbprgstr` registers <nbpname\> with `atalkd(8)`, at the given
<port\>. `nbpunrgstr` informs *atalkd* that <nbpname\> is no longer to
be advertised.

`nbplkup` displays up to <maxresponses\> (default 1000) entities
registered on the AppleTalk internet. *<nbpname\>* is parsed by
`nbp_name(3)`. An \`*=*' for the *object* or *type* matches anything,
and an \`*\**' for *zone* means the local zone. The default values are
taken from the *NBPLKUP* environment variable, parsed as an <nbpname\>.

# 環境変数

NBPLKUP

> nbplkup のデフォルトの nbpname

ATALK_MAC_CHARSET

> Appletalk ネットワーク上のクライアントが使用するコードページ

ATALK_UNIX_CHARSET

> このシェルで拡張文字を表示するために使用するコードページ。

# 例

ローカル ゾーンでタイプ *LaserWriter* のすべてのデバイスを検索する。

    example% nbplkup :LaserWriter
                   Petoskey:LaserWriter        7942.129:218
                 Gloucester:LaserWriter        8200.188:186
                     Rahway:LaserWriter        7942.2:138
                 517 Center:LaserWriter        7942.2:132
                      ionia:LaserWriter        7942.2:136
         Evil DEC from Hell:LaserWriter        7942.2:130
                  Hamtramck:LaserWriter        7942.2:134
             Iron Mountain :LaserWriter        7942.128:250
    example%

# 参照

`nbp_name(3)`, `atalkd(8)`.

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
