# importing packages
import pandas as pd


# importing Data into DataFrame
df=pd.read_csv("youtubedata.txt",sep='\t')


'''
            Data Preprocessing
'''

tdf=df[df.columns[9:]] # selecting related videos and all the unnamed columns
df=df[df.columns[0:9]] # removing related videos and all the unnamed columns

# renaming columns
df.columns=['id', 'uploader', 'time-from-upload', 'category', 'length', 'views-cnt', 'rating', 'ratings-cnt', 'comments-cnt']

# creating new column that contains count of related videos
l=[]
for row in tdf.iterrows():
    c=0
    for j in row[1]:
        if type(j)==float:
            break
        c+=1
    l.append(c)
df['related-vids-cnt']=l

# replacing NaN values by 0
df['views-cnt']=df['views-cnt'].fillna(0)
df['ratings-cnt']=df['ratings-cnt'].fillna(0)
df['comments-cnt']=df['comments-cnt'].fillna(0)

# converting column datatype to integer
df['views-cnt']=df['views-cnt'].astype('int')
df['ratings-cnt']=df['ratings-cnt'].astype('int')
df['comments-cnt']=df['comments-cnt'].astype('int')
df['related-vids-cnt']=df['related-vids-cnt'].astype('int')

# deleting rows with NaN values for category
df=df.dropna(subset=['category'])

'''   ***  END  ***   '''


# exporting preprocessed data to preprocessed.csv
df.to_csv('preprocessed.csv')


print("Data Preprocessed. Data stored in 'preprocessed.csv'")