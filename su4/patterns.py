AllPatterns = [
    {
        'name': "",
        'sample': """
            月落/乌啼/霜/满天
            江枫/渔火/对愁/眠
            姑苏/城外/寒山/寺
            夜半/钟声/到/客船
            """,
        'gelv': """
            11/00/0/*0|a
            00/0*/*0/0|a
            00/0*/00/1
            11/00/*/10|a
            """,
        'grammar': """
            n-vi n-vi n vi/ae
            n n df vi
            sn/n/an/nf sb a n
            t n v/pf n/sn/s
            """,
        'connection': [
            ((3, 1), (3, 3))
            ]
    },
    {
        'name': "",
        'sample': """
            水陌/轻寒
            社公/雨足/东风/慢
            定巢/新燕
            湿雨/穿花/转
            象尺/熏炉
            拂晓/停/针线
            愁蛾/浅
            飞红/零乱
            侧卧/珠帘/卷
            """,
        'gelv': """
            *1/00|a
            *0/*0/00/1|a
            *0/*1
            *1/00/1|a
            *1/*0
            *1/0/01|a
            **/1|a
            *0/*1
            *1/00/1|a
            """,
        'grammar': """
            sn ae
            n ae n ae
            af n
            a df vi
            n/s n
            t vt n
            n ae
            n ae
            v n ae
            """,
        'connection': [
            ((3, 1), (3, 3))
            ]
    },
    {
        'name': "水调歌头",
        'sample': """
            鸟影/度/疏木
            天势/入/平湖
            沧波/万顷
            轻风/落日/片帆/孤
            渡口/千章/云木
            苒苒/炊烟/一缕
            人在/翠微/居
            客里/更/愁绝
            回首/忆/吾庐
            """,
        'gelv': """
            **/*/*1|a
            *1/1/00|a
            *0/*1
            **/*1/10/0|a
            *1/*0/*1
            *1/*0/*1|a
            *1/10/0|a
            **/*/01
            *1/1/00|a
            """,
        'grammar': """
            n vt n
            n v sn
            n ml/ae
            n n n ae
            s af/ml n
            a n ae/ml
            n-p/n-pv s/sn v
            s/t df/aux ae
            df/dv vt n/sn
            """,
        'connection': [
            ((3, 1), (3, 3))
            ]
    },
]
