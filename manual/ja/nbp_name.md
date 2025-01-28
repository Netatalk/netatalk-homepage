# 名前

nbp_name — NBP 名の解析

# 概要

    int nbp_name(name,
        obj,
        type,
        zone);
    char *name;
    char **obj;
    char **type;
    char **zone;

# 説明

**nbp_name()** は、ユーザーが指定した名前を、そのコンポーネント オブジェクト、タイプ、およびゾーンに解析する。 *obj*、*type*、*zone* は参照渡しされ、呼び出し元のデフォルト値を指す必要がある。**nbp_name()** は、解析された値へのポインタを変更する。 *name* は、*object:type@**zone* の形式である。ここで、*object*、 *:type、*、および *@**zone* はそれぞれ、*obj*、 *type*、*zone,* です。*type* の前には \`*:*' が、*zone* の前には \`*@*' がなければなりません。

# 例

The argument of **afpd(8)**'s **-n** option is parsed with
**nbp_name()**. The default value of *obj* is the first component of the
machine's hostname (as returned by **gethostbyname(3)**). The default value
of *type* is \**\\**AFPServer'', and of *zone* is \**\\**\*'', the default
zone. To cause *afpd* to register itself in some zone other than the
default, one would invoke it as

    afpd -n @some-other-zone

*obj* と *type* はデフォルト値を保持する。

# バグ

*obj*、*type*、および *zone*
は、呼び出しごとに上書きされる可能性のある静的領域へのポインタを返する。

# 著者

[CONTRIBUTORS](https://netatalk.io/contributors) を参照
