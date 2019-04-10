from sklearn.externals import joblib
trs = joblib.load('trs.pkl')
x=[[0,1,0,0,0,1]]
c=trs.predict(x)
print(c)