# 名前

atalk — AppleTalk プロトコル ファミリ

# 概要

    #include <sys/types.h>
    #include <netatalk/at.h>

# 説明

AppleTalk プロトコル ファミリは、データグラム配信プロトコル (DDP)  の上位層にあり、AppleTalk
アドレス形式を使用するプロトコルのコレクションである。AppleTalk ファミリは、SOCK_STREAM (ADSP)、SOCK_DGRAM
(DDP)、SOCK_RDM (ATP)、および SOCK_SEQPACKET (ASP) を提供する。現在、DDP
のみがカーネルに実装されている。ATP と ASP は、ユーザー レベルのライブラリに実装されている。 ADSP も計画されている。

# アドレス指定

AppleTalk アドレスは 3 バイトの量で、ネットワーク バイト
オーダーで保存される。インクルード ファイル <*netatalk/at.h*\> は
AppleTalk アドレス形式を定義する。

AppleTalk プロトコル ファミリのソケットは、次のアドレス構造を使用する:

    struct sockaddr_at {
        short sat_family;
        unsigned char sat_port;
        struct at_addr sat_addr;
        char sat_zero[ 8 ];
    };

The port of a socket may be set with **bind(2)**. The node for *bind* must
always be *ATADDR_ANYNODE*: \**\\**this node.'' The net may be
*ATADDR_ANYNET* or *ATADDR_LATENET*. *ATADDR_ANYNET* corresponds to the
machine's \**\\**primary'' address (the first configured). *ATADDR_LATENET*
causes the address in outgoing packets to be determined when a packet is
sent, i.e. determined late. *ATADDR_LATENET* is equivalent to opening one
socket for each network interface. The port of a socket and either the
primary address or *ATADDR_LATENET* are returned with **getsockname(2)**.

# 関連項目

bind(2), getsockname(2), atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
