#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#importing text file as dataframe using pandas
df = pd.read_csv("youtubedata.txt",sep='\t')


#storing all related video ids in a single column and resizing data frame
print(df.shape)
l=[]
for i in range(0,4100):
    l0=[df.ix[i,j] for j in range(10,29)]
    l.append(list(l0))
df=df.ix[0:4099,0:9]
df['REL_VID_ID']=l
print(df['REL_VID_ID'])


#renaming columns
print(list(df))
df.columns = ['VID_ID', 'UPLOADER', 'INT_AFT_EST(m)', 'CATEGORY', 'LENGTH(m)', 'NO_OF_VIEWS', 'RATINGS(/5)', 'NO_OF_RATS', 'NO_OF_COMS', 'REL_VID_ID']
print(list(df))


#Question 1) Identify top 10 videos with highest ratings
z1 = df.sort_values(by='RATINGS(/5)', ascending=0)
z2 = z1.head(10)
print("\nThe top 10 videos with highest ratings are stored in 'top10rats.txt'\n\n\n")
z2.to_csv('top10rats.csv')


#Question 2) Identify top 5 categories with highest ratings
d={}
for i in df['CATEGORY'].unique():
    avg_rat=0
    if i not in d.keys():
        y1=df[df['CATEGORY']==i]
        l1 = y1['RATINGS(/5)']
        for j in l1:
            avg_rat+=j
        try:
            avg_rat=avg_rat/len(l1)
        except ZeroDivisionError:
            avg_rat=0
        d.update({i:avg_rat})
sorted_d=sorted(d.items(),key=lambda kv:kv[1],reverse=True)
l21=[i[0] for i in sorted_d]
l22=[i[1] for i in sorted_d]
data = {'Category':l21,'Avg_Ratings':l22}
y2 = pd.DataFrame(data)
y3=y2.head()
#print("Top 5 categories with highest ratings are\n")
#print(y3)
print("The top 5 Categories with maximum ratings are stored in 'top5cats.csv'")
y3.to_csv('top5cats.csv')
print("\n\n\n")

        
#Question 3) Identify top 10 videos with maximum video time(i.e Length)
x1 = df.sort_values(by='LENGTH(m)', ascending=0)
x2 = x1.head(10)
print("The top 10 videos with maximum video length are stored in 'top10lens.csv'\n\n\n")
x2.to_csv('top10lens.csv')

'''
#Question 4)Most controversial video categories based on no. of comments by no. of views
di={}
for i in df['CATEGORY'].unique():
    avg_com_score=0
    if i not in di.keys():
        w1=df[df['CATEGORY']==i]
        l31=np.array(w1['NO_OF_COMS'])
        l32=np.array(w1['NO_OF_VIEWS'])
        l33=np.ma.array(l31,mask=(l31==0))
        l34=np.ma.array(l32,mask=(l32==0))
        l3=l33/l34
        l3=[i*1000 for i in l3]
        for n in l3:
            avg_com_score+=n
        try:
            avg_com_score/=len(l3)
        except ZeroDivisionError:
            avg_com_score=0
        di.update({i:avg_com_score})
sorted_d=sorted(di.items(),key=lambda kx:kx[1],reverse=True)
w2=pd.DataFrame(sorted_d)
w2.columns=['Category', 'Con_Score']
print("Categories arranged in the order of  controversiality are stored in 'topconcats.csv'")
w2.to_csv('topconcats.csv')
print("\n\n\n")
'''   
        
#Question 5)calculate popularity of each video and rank them from best to worst
l41=np.ma.array(df['NO_OF_VIEWS'],mask=(df['NO_OF_VIEWS']==0))
l42=np.ma.array(df['INT_AFT_EST(m)'],mask=(df['INT_AFT_EST(m)']==0))
l4=l41/l42
l51=np.ma.array(df['RATINGS(/5)'],mask=(df['RATINGS(/5)']==0))
l52=np.ma.array(df['NO_OF_RATS'],mask=(df['NO_OF_RATS']==0))
l5=l51/l52
l6=np.ma.array(df['NO_OF_COMS'],mask=(df['NO_OF_COMS']==0))
l7=l4+l5+l6
df['POPULARITY']=l7
v=df.sort_values(by='POPULARITY', ascending=0)
print("The data sorted with respect to popularity is stored in 'sortedwithpop.csv'")
v.to_csv('sortedwithpop.csv')
print("The popularity was calculated by no. of views/interval after publish + rating out of 5/no. of ratings + no. of comments\n\n")


#trying clustering and finding relation between length of video and no. of views.
y=list(df['LENGTH(m)'])
z=list(df['NO_OF_VIEWS'])
x=[]
for i in range(len(y)):
    w1=[]
    if y[i] != 'nan' and z[i] != 'nan':
        if y[i]<=np.finfo(np.float64).max and z[i]<=np.finfo(np.float64).max:
            w1.append(y[i])
            w1.append(z[i])
            x.append(list(w1))
x=np.array(x)
#plt.subplot(2,2,1)
#plt.scatter(x[:,0],x[:,1], label='True Position')
kmeans=KMeans(n_clusters=3)
kmeans.fit(x)
print("The cluster centers are as follows")
l91=kmeans.cluster_centers_
for i in l91:
    print(float(i[0]),float(i[1]))
plt.subplot(1,1,1)
plt.scatter(x[:, 0], x[:, 1], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.title("Relation between Length of video and no. of views")
plt.xlabel("Length in mins")
plt.ylabel("no. of Views")
plt.show()
print('\n\n')


#categories with highest popularity
di={}
for i in df['CATEGORY'].unique():
    avg_pop_score=0
    if i not in di.keys():
        w1=df[df['CATEGORY']==i]
        l3=np.array(w1['POPULARITY'])
        for n in l3:
            avg_pop_score+=n
        try:
            avg_com_score/=len(l3)
        except ZeroDivisionError:
            avg_pop_score=0
        di.update({i:avg_pop_score})
sorted_d=sorted(di.items(),key=lambda kx:kx[1],reverse=True)
w2=pd.DataFrame(sorted_d)
w2.columns=['Category', 'Pop_Score']
print("Categories arranged in the order of  popularity are stored in 'toppopcats.csv'")
w2.to_csv('toppopcats.csv')
print("\n\n\n")


#Identify top 10 videos with maximum no. of views
x1 = df.sort_values(by='NO_OF_VIEWS', ascending=0)
x2 = x1.head(10)
print("The top 10 videos with maximum no. of views are stored in 'top10views.csv'\n\n\n")
x2.to_csv('top10views.csv')


#Identify top 10 videos with maximum no. of comments
x1 = df.sort_values(by='NO_OF_COMS', ascending=0)
x2 = x1.head(10)
print("The top 10 videos with maximum no. of comments are stored in 'top10coms.csv'\n\n\n")
x2.to_csv('top10coms.csv')