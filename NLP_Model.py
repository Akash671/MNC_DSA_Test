# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:49:03 2024

@author: PCAT
"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud



import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords


data = pd.read_csv(r'C:\Akash\NLP\Amazon-Product-Reviews-Sentiment-Analysis-in-Python-Dataset.csv')
print(data.head())


data.dropna(inplace=True)



#1,2,3->negative(i.e 0)
data.loc[data['Sentiment']<=3,'Sentiment'] = 0

#4,5->positive(i.e 1)
data.loc[data['Sentiment']>3,'Sentiment'] = 1 

stp_words=stopwords.words('english')
def clean_review(review):
    if isinstance(review, str):  # Check if the review is a string
        cleanreview = " ".join(word for word in review.split() if word not in stp_words)
        return cleanreview
    else:
        return ""  # Or handle NaN values differently (e.g., return None, "missing")

data['Review'] = data['Review'].apply(clean_review)

data['Sentiment'].value_counts()


consolidated=' '.join(word for word in data['Review'][data['Sentiment']==0].astype(str))
wordCloud=WordCloud(width=1600,height=800,random_state=21,max_font_size=110)
plt.figure(figsize=(15,10))
plt.imshow(wordCloud.generate(consolidated),interpolation='bilinear')
plt.axis('off')
plt.show()



consolidated=' '.join(word for word in data['Review'][data['Sentiment']==1].astype(str))
wordCloud=WordCloud(width=1600,height=800,random_state=21,max_font_size=110)
plt.figure(figsize=(15,10))
plt.imshow(wordCloud.generate(consolidated),interpolation='bilinear')
plt.axis('off')
plt.show()

cv = TfidfVectorizer(max_features=2500)
X = cv.fit_transform(data['Review'] ).toarray()


from sklearn.model_selection import train_test_split
x_train ,x_test,y_train,y_test=train_test_split(X,data['Sentiment'],
                                                test_size=0.25 ,
                                                random_state=42)






from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model=LogisticRegression()

#Model fitting
model.fit(x_train,y_train)

#testing the model
pred=model.predict(x_test)

#model accuracy
print(accuracy_score(y_test,pred))

# This code is modified by Susobhan Akhuli



from sklearn import metrics
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm, 
                                            display_labels = [False, True])

cm_display.plot()
plt.show()

# This code is modified by Susobhan Akhuli
























