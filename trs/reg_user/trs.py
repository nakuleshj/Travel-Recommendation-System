from sklearn.externals import joblib
def recommend(age,occ,acc,interest,mot,dos):
    trs = joblib.load('trs.pkl')
    x=[[age,occ,acc,interest,mot,dos]]
    c=trs.predict(x)
    #print(c)
    return c