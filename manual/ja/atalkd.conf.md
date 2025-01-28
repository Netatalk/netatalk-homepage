# 名前

atalkd.conf — AppleTalk が使用するインターフェイスを構成するために atalkd が使用する構成ファイル

# 説明

*atalkd.conf* は、atalkd が Appletalk
インターフェイスとその動作を設定するために使用する設定ファイルである

先頭に *\#*
が付いていない行はすべて解釈される。各インターフェイスは、分割行をサポートせず、中断のない行で設定する必要がある。設定行の形式は次のとおり:

*interface* \[ `-seed` \] \[ `-phase` <number\> \] \[ `-net`
<net-range\> \] \[ `-addr` <address\> \] \[ `-zone` <zonename\> \]
...

最も単純なケースは、atalkd.conf がないか、有効な行はないかこの場合、atalkd はマシン上のローカル
インターフェースを自動検出し、atalkd.conf ファイルに書き込む。存在しない場合は作成する。

動作するネットワーク インターフェースを設定する。インターフェースは、Linux の場合は *eth0*、Solaris の場合は *le0* など

インターフェース以外のフィールドはすべてオプションであることに注意してください。ループバック インターフェースは自動的に構成される。`-seed`
が指定されている場合は、他のすべてのフィールドが存在する必要がある。また、ルーターがシード情報に同意しない場合、**atalkd**
は起動時に終了する。`-seed` が指定されていない場合は、他のすべての情報が自動構成中に上書きされる可能性がある。 `-phase`
オプションが指定されていない場合は、コマンドラインで指定されたデフォルトのフェーズが使用される (デフォルトは 2)。`-addr`
が指定されていて、`-net` が指定されていない場合は、net-range が 1 であると想定される。

The first -zone directive for each interface is the \**\\**default'' zone.
Under Phase 1, there is only one zone. Under Phase 2, all routers on the
network are configured with the default zone and must agree. **atalkd** maps
\**\\**\*'' to the default zone of the first interface. Note: The default
zone for a machine is determined by the configuration of the local routers;
to appear in a non-default zone, each service, e.g.  **afpd**, must
individually specify the desired zone. See also **nbp_name(3)**.

使用可能なオプションとその意味は次のとおり。

`-addr net.node`

このインターフェイスのネット番号とノード番号を指定できる。AppleTalk 番号形式 (例: `-addr 66.6`) で指定する。

`-dontroute`

> AppleTalk ルーティングを無効にする。これは、`-router` の逆。

`-net first[-last]`

> 使用可能なネットを、オプションで範囲として設定できる。

`-phase ( 1 | 2 )`

> このインターフェイスが使用する AppleTalk フェーズを指定する (フェーズ 1 またはフェーズ 2)。

`-router`

> 単一のインターフェイスで AppleTalk ルーターをシードする。逆の オプションは`-dontroute`。 `-seed`に似ているが、単一インターフェイス ルーティング。

`-seed`

> AppleTalk ルーターをシードする。これには、2 つ以上のインターフェイスを構成する必要がある。単一のネットワーク インターフェイスがある場合は、代わりに `-route` を使用する。これにより、不足しているすべての引数がネットワークから自動的に構成される。

`-zone zonename`

> このインターフェイスが表示される特定のゾーンを指定する (例: `-zone "Parking Lot"`)。スペースやその他の特殊文字を含むゾーンは、ダブルクォーテーションで囲む必要があることに注意してください。

# 例

Solaris 上の単一インターフェイスと自動検出パラメータ。

       le0

Linux でも同様。

       eth0

Below is an example configuration file from a Sun 4/40. The machine has two
interfaces, \**\\**le0'' and \**\\**le1''. The \**\\**le0'' interface is
configured automatically from other routers on the network. The machine is
the only router for the \**\\**le1'' interface.

       le0
       le1 -seed -net 9461-9471 -zone netatalk -zone Argus

# 関連項目

atalkd(8)

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
