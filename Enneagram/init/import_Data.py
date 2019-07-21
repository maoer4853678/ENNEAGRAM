#coding=utf-8
import sys
sys.path.append("../")

from questionnaire.models import Choice,Question
import pandas as pd


df = pd.read_csv("data.csv")
for i in df.index:    
    print (i)
    q= Question(qid=df.loc[i,"ID"],qcontent= df.loc[i,"content"],qclass = df.loc[i,"class"])
    q.save()

print ("import Question completed")


for i in df.index:
    print (i)
    q = Question.objects.get(qid=i+1)
    c = Choice(question = q,ccontent='是',votes=0)
    c.save()
    c = Choice(question = q,ccontent='否',votes=0)
    c.save()
    
print ("import Choice completed")
    