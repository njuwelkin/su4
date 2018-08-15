AllPatterns = [
    {
        'name': "",
        'sample': """
            月落乌啼霜满天
            江枫渔火对愁眠
            姑苏城外寒山寺
            夜半钟声到客船
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
            t n v n
            """,
        'connection': [
            ((3, 1), (3, 3))
            ]
    }
]
