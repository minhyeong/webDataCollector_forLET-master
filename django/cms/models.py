from datetime import time
import datetime
from django.db import models

GENDER_CHOICES = (
    ("女性", '女性'),
    ("男性", '男性'),
)

BLOOD_CHOICES = (
    ("A", 'A'),
    ("B", 'B'),
    ("O", 'O'),
    ("AB", 'AB'),
    ("Other", 'その他'),
)

LIFE_STYLE_CHOICES = (
    ("和式", '和式'),
    ("洋式", '洋式'),
)

TIME_CHOICES = [
    (time(hour, 00, 00), "{0}時間".format(hour)) for hour in range(0, 24)
]

TASTE_CHOICES = (
    ("甘党", '甘党'),
    ("辛党", '辛党'),
    ("濃い味", '濃い味'),
    ("薄味", '薄味'),
)

SPORT_CHOICES = (
    ("サッカー", 'サッカー'),
    ("野球", '野球'),
    ("ゴルフ" , 'ゴルフ'),
    ("テニス" , 'テニス'),
    ("バスケットボール", 'バスケットボール'),
    ("陸上競技", '陸上競技'),
    ("バドミントン", 'バドミントン'),
    ("卓球", '卓球'),
    ("バレーボール", 'バレーボール'),
    ("その他", 'その他'),
)

MUSIC_CHOICES = (
    ("ロック", 'ロック'),
    ("歌謡曲", '歌謡曲'),
    ("クラシック", 'クラシック'),
    ("ジャズやブルース", 'ジャズやブルース'),
    ("フォーク", 'フォーク'),
    ("演歌・民謡", '演歌・民謡'),
    ("R&Bやソウル", 'R&Bやソウル'),
    ("ポップス", 'ポップス'),
    ("その他", 'その他'),
)

# Create your models here.
class QuestionList(models.Model):

    # name = models.CharField('名前', max_length=255)
    birth = models.DateField('生年月日',blank=False)
    gendar = models.CharField("性別", max_length=2, blank=False, choices=GENDER_CHOICES)
    blood = models.CharField('血液型', max_length=10 , blank=False , choices=BLOOD_CHOICES)
    # life_style = models.CharField('ライフスタイル',blank=True, max_length=10,choices=LIFE_STYLE_CHOICES)
    # sleep_time = models.TimeField('平均睡眠時間', default=time(6,00,00) ,choices=TIME_CHOICES)
    sleep_time_top = models.TimeField('最高睡眠時間',default=time(0,00,00))
    sleep_time_bottom = models.TimeField('最低睡眠時間',default=time(0,00,00))
    sport = models.CharField('好きなスポーツ',max_length=10, blank=False, choices=SPORT_CHOICES)
    music = models.CharField('好きな音楽のジャンル',max_length=10, blank=False, choices=MUSIC_CHOICES)
    taste = models.CharField('味覚のこだわり', max_length=5 , blank=False ,choices=TASTE_CHOICES)
    # tv_program = models.CharField('好きなTV番組',blank=True, max_length=255)
    # travel = models.CharField('思い出に残る旅行',blank=True, max_length=255)
    # event = models.CharField('思い出に残る出来事',blank=True, max_length=255)
    # weak = models.CharField('苦手なこと',blank=True, max_length=255)
    # help = models.CharField('手伝って欲しいこと',blank=True, max_length=255)
    # family = models.CharField('あなたにとって家族とは',blank=True, max_length=255)
    # friend = models.CharField('あなたにとって友人とは',blank=True , max_length=255)


    eat = models.IntegerField('1.口から食事ができる',default=50)
    move = models.IntegerField('2.自分で動くことができる',default=50)
    think = models.IntegerField('3.自分で考えることができる',default=50)
    breath = models.IntegerField('4.自分で呼吸ができる',default=50)
    fun = models.IntegerField('5.楽しみがある',default=50)
    no_pain = models.IntegerField('6.苦痛がない',default=50)

    rank1 = models.IntegerField('生命の質 1位', default=0)
    rank2 = models.IntegerField('生命の質 2位', default=0)
    rank3 = models.IntegerField('生命の質 3位', default=0)
    rank4 = models.IntegerField('生命の質 4位', default=0)
    rank5 = models.IntegerField('生命の質 5位', default=0)
    rank6 = models.IntegerField('生命の質 6位', default=0)


    tipi_j_01 = models.IntegerField('01.活発で外交的だと思う', default=4)
    tipi_j_02 = models.IntegerField('02.他人に不満をもち，もめごとを起こしやすいと思う', default=4)
    tipi_j_03 = models.IntegerField('03.しっかりしていて，自分に厳しいと思う', default=4)
    tipi_j_04 = models.IntegerField('04.心配性で，うろたえやすいと思う', default=4)
    tipi_j_05 = models.IntegerField('05.新しいことが好きで，変わった考えをもつと思う', default=4)
    tipi_j_06 = models.IntegerField('06.ひかえめで，おとなしいと思う', default=4)
    tipi_j_07 = models.IntegerField('07.人に気をつかう，やさしい人間だと思う', default=4)
    tipi_j_08 = models.IntegerField('08.だらしなく，うっかりしていると思う', default=4)
    tipi_j_09 = models.IntegerField('09.冷静で，気分が安定していると思う', default=4)
    tipi_j_10 = models.IntegerField('10.発想力に欠けた，平凡な人間だと思う', default=4)


    das_01 = models.IntegerField('01.死後の世界はあると思う', default=4)
    das_02 = models.IntegerField('02.世の中には「霊」や「たたり」があると思う', default=4)
    das_03 = models.IntegerField('03.死んでも魂は残ると思う', default=4)
    das_04 = models.IntegerField('04.人は死後、また生まれ変わると思う', default=4)
    das_05 = models.IntegerField('05.死ぬことがこわい', default=4)
    das_06 = models.IntegerField('06.自分が死ぬことを考えると、不安になる', default=4)
    das_07 = models.IntegerField('07.死は恐ろしいものだと思う', default=4)
    das_08 = models.IntegerField('08.私は死を非常に恐れている', default=4)
    das_09 = models.IntegerField('09.私は、死とはこの世の苦しみから解放されることだと思っている', default=4)
    das_10 = models.IntegerField('10.私は死をこの人生の重荷からの解放と思っている', default=4)
    das_11 = models.IntegerField('11.死は痛みと苦しみからの解放である', default=4)
    das_12 = models.IntegerField('12.死は魂の解放をもたらしてくれる', default=4)
    das_13 = models.IntegerField('13.私は死について考えることを避けている', default=4)
    das_14 = models.IntegerField('14.どんなことをしても死を考えることを避けたい', default=4)
    das_15 = models.IntegerField('15.私は、死についての考えが思い浮かんでくると、いつもそれをはねのけようとする', default=4)
    das_16 = models.IntegerField('16.死は恐ろしいのであまり考えないようにしている', default=4)
    das_17 = models.IntegerField('17.私は人生にはっきりとした使命と目的を見出している ', default=4)
    das_18 = models.IntegerField('18.私は人生の意義、目的、使命を見出す能力が十分にある ', default=4)
    das_19 = models.IntegerField('19.私の人生について考えると、今ここにこうして生きている理由がはっきりとしている', default=4)
    das_20 = models.IntegerField('20.未来は明るい', default=4)
    das_21 = models.IntegerField('21.「死とは何だろう」とよく考える ', default=4)
    das_22 = models.IntegerField('22.自分の死について考えることがよくある ', default=4)
    das_23 = models.IntegerField('23.身近な人の死をよく考える', default=4)
    das_24 = models.IntegerField('24.家族や友人と死についてよく話す', default=4)
    das_25 = models.IntegerField('25.人の寿命はあらかじめ「決められている」と思う ', default=4)
    das_26 = models.IntegerField('26.寿命は最初から決まっていると思う', default=4)
    das_27 = models.IntegerField('27.人の生死は目に見えないカ(運命・神など)によって決められている', default=4)


    yk = models.BooleanField('鎮痛薬・鎮静薬の使用',default=False)
    tje = models.BooleanField('中心静脈栄養',default=False)
    ke = models.BooleanField('胃ろうチューブからの栄養補給',default=False)
    syo = models.BooleanField('末梢点滴',default=False)
    zk = models.BooleanField('人工呼吸器',default=False)
    ks = models.BooleanField('鼻チューブからの栄養補給',default=False)
    zt = models.BooleanField('人工血液透析',default=False)
    sm = models.BooleanField('心肺蘇生',default=False)
    ot = models.BooleanField('その他の希望',default=False)

    def set_querys(self):

        return {
            "rank1":self.rank1,
            "rank2": self.rank2,
            "rank3": self.rank3,
            "rank4": self.rank4,
            "rank5": self.rank5,
            "rank6": self.rank6,

            "tipi_j_01":self.tipi_j_01,
            "tipi_j_02":self.tipi_j_02,
            "tipi_j_03":self.tipi_j_03,
            "tipi_j_04":self.tipi_j_04,
            "tipi_j_05":self.tipi_j_05,
            "tipi_j_06":self.tipi_j_06,
            "tipi_j_07":self.tipi_j_07,
            "tipi_j_08":self.tipi_j_08,
            "tipi_j_09":self.tipi_j_09,
            "tipi_j_10":self.tipi_j_10,

            "das_01": self.das_01,
            "das_02": self.das_02,
            "das_03": self.das_03,
            "das_04": self.das_04,
            "das_05": self.das_05,
            "das_06": self.das_06,
            "das_07": self.das_07,
            "das_08": self.das_08,
            "das_09": self.das_09,
            "das_10": self.das_10,
            "das_11": self.das_11,
            "das_12": self.das_12,
            "das_13": self.das_13,
            "das_14": self.das_14,
            "das_15": self.das_15,
            "das_16": self.das_16,
            "das_17": self.das_17,
            "das_18": self.das_18,
            "das_19": self.das_19,
            "das_20": self.das_20,
            "das_21": self.das_21,
            "das_22": self.das_22,
            "das_23": self.das_23,
            "das_24": self.das_24,
            "das_25": self.das_25,
            "das_26": self.das_26,
            "das_27": self.das_27,
        }

class Log(models.Model):
    user_id   = models.IntegerField("ユーザID", blank=False, default=0 )
    timestamp = models.BigIntegerField("タイムスタンプ" , default=0 )
    # operation = models.CharField("操作", blank=False, max_length=100 )
    # check_no  = models.IntegerField("チェックNo", blank=False, default=0 )
    # state_data = JSONField(default={})
    state_data = models.CharField("状態" , default="" , max_length=10000)
