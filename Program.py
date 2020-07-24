# importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing data into DataFrame
df=pd.read_csv('preprocessed.csv')
print("The columns in DataFrame are: ",list(df),'\n')


#Question 1) Identify top 10 videos with highest ratings
tdf = df.sort_values(by='rating', ascending=0)
tdf = tdf.head(10)
print("The top 10 videos with highest ratings are stored in 'top10videosbyrating.csv'\n")
tdf.to_csv('top10videosbyrating.csv')


#Question 2) Identify top 5 categories with highest ratings
def categorisedData(s): # function to find average value of 's' for each category
    d={}
    for i in df['category'].unique():
        avg=0
        if i not in d.keys():
            tdf=df[df['category']==i]
            l = tdf[s]
            for j in l:
                avg +=j
            try:
                avg/=len(l)
            except ZeroDivisionError:
                avg=0
            d.update({i:avg})
    sorted_d=sorted(d.items(),key=lambda kv:kv[1],reverse=True)
    tdf = pd.DataFrame(sorted_d)
    return tdf
tdf=categorisedData('rating')
tdf.columns=['Category', 'Avg Rating (/5)']
print("Categories with their average ratings (out of 5) are\n")
print(tdf,'\n')
print("The Categories with their average ratings are stored in 'categoriesbyrating.csv' \n")
tdf.to_csv('categoriesbyrating.csv')


#Question 3)Most controversial video categories based on no. of comments by no. of views
l1=np.ma.array(df['comments-cnt'],mask=(df['comments-cnt']==0))
l2=np.ma.array(df['views-cnt'],mask=(df['views-cnt']==0))
l=l1/l2*1000
df['controversial-score']=l
tdf=categorisedData('controversial-score')
tdf.columns=['Category', 'Avg Controversial Score']
print("Categories with their average Controversial Scores are\n")
print(tdf,'\n')
print("The Categories with their average Controversial Scores are stored in 'categoriesbycontroscore.csv' \n")
tdf.to_csv('categoriesbycontroscore.csv')


#Question 4)calculate popularity of each video and rank them from best to worst
tl1=np.ma.array(df['views-cnt'],mask=(df['views-cnt']==0))
tl2=np.ma.array(df['time-from-upload'],mask=(df['time-from-upload']==0))
l1=tl1/tl2
tl1=np.ma.array(df['rating'],mask=(df['rating']==0))
tl2=np.ma.array(df['ratings-cnt'],mask=(df['ratings-cnt']==0))
l2=tl1*tl2
l3=np.ma.array(df['comments-cnt'],mask=(df['comments-cnt']==0))
l=(l1+l2+l3)/1000
df['POPULARITY']=l
df=df.sort_values(by='POPULARITY', ascending=0)
print("The data sorted with respect to popularity is stored in 'sortedbyypopularity.csv'\n")
df.to_csv('sortedbypopularity.csv')
print("The popularity was calculated by (no. of views/interval after publish + rating out of 5*no. of ratings + no. of comments) by 1000\n")


#Question 5) plot graph between related videos count and views count and print conclusion
def plotScatterPlot(sx, sy):
    l1=list(df[sx])
    l2=list(df[sy])
    x=[]
    for i in range(len(l1)):
        l=[]
        l.append(l1[i])
        l.append(l2[i])
        x.append(list(l))
    x=np.array(x)
    plt.scatter(x[:, 0], x[:, 1])
    plt.title("Relation between "+sx+" and "+sy)
    plt.xlabel(sx)
    plt.ylabel(sy)
    plt.show()
    
plotScatterPlot('related-vids-cnt', 'views-cnt')
print('The conclusion, after analysing the scatter plot between no. of related videos and no. of views, is that More the no. of related videos a video has, more could be its no. of views.\n')


# plotting graph btw length and no. of views 
plotScatterPlot('length', 'views-cnt')
print('The conclusion, after analysing the scatter plot between length of video and no. of views, is that Lesser the length of video, more could be the no. of views.\n')
