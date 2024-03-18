from django.db import models
import datetime
from django.utils import timezone

# モデル記述後makemigrationsの前に、setting.pyのAPPSのとこに
# このアプリ（polls）.modelsのモジュール内にあることを知らせる


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # __str__ pythonからデータベース操作をする時に名前がわかるから書こう
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# on_delete=models.CASCADE:あるオブジェクト削除時関連づけられたオブジェクトも削除(他オプションSET_NULL, PROTECTなど)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text