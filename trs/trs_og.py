import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier  
from sklearn import metrics
from sklearn.externals import joblib
data=pd.read_csv('C:/Users/nakul/Downloads/trs-dataset01.csv')
#print (data.head(10))
y=data.rp
x=data.drop('rp',axis=1)
#print(x)
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,shuffle=False)
#print(x_train)
#print(x_train.shape)  #prints no. of rows,columns of training set
#print("\n Test data")
#print(x_test)
#print(x_test.shape)    #prints no. of rows,columns of testing set
#clf = DecisionTreeClassifier()  
#clf.fit(x_train, y_train)
#y_pred=clf.predict(x_test)
#print("Accuracy Score DT:\n")
#print(metrics.accuracy_score(y_test,y_pred))

#Gaussian classifier
gnb=GaussianNB()
gnb.fit(x_train, y_train)  #training the model
y_pred=gnb.predict(x_test)            #predicting the class for test data and expected is y_test
#joblib.dump(gnb, 'trs.pkl')
#print("Classification Report:\n")
#print(metrics.classification_report(y_test,y_pred))
#print("Confusion matrix:\n")
#print(metrics.confusion_matrix(y_test,y_pred))
print("Accuracy Score gnb:\n")
print(metrics.accuracy_score(y_test,y_pred))