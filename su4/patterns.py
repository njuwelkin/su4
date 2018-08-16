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
        'name': "",
        'sample': """
            风雨/交加
            只得/在家
            问我/干嘛
            看书/玩咖
            """,
        'gelv': """
            01/00|a
            10/11|a
            11/*0
            10/00|a
            """,
        'grammar': """
            n ae
            aux/df vi
            v-n/w-r v/w
            v-n v-n
            """,
        'connection': [
            ((3, 1), (3, 3))
            ]
    },


]
