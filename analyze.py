from maketweettexts import TwitterJSONParser, twitter_entry
import pandas as pd

#input a json file name to read in tweets
filename = input("JOSN Filename : ")
print("Parsing data . . .")
json_stuff = TwitterJSONParser(filename+'.json')
all = json_stuff.tweets
print("Data retrieved")

#once data is retrieved, ask what section of the tweets we want to train
startindex = int(input("Give a starting index <int> : "))
numoftweets = int(input("Number of tweets you want to label <int> :"))

#begin labeling the tweets
print("Label each either as important or not")
pdindex = []
pdcolumns = ['rawtext, label']
t = []
l = []
data = {'rawtext': [], 'label': []}
for i in range(numoftweets):
    print('-')
    lab = 'a'
    while (lab != 'n' and lab != 'y'):
        print(all[startindex+i].get_raw_text())
        lab = str(input('y or n : '))
        if(lab != 'n' and lab != 'y'):
            print('Answer must be y or n, try again . . .')
    t.append(all[startindex+i].get_raw_text())
    l.append(lab)
    pdindex.append(startindex+i)

data['rawtext'] = t
data['label'] = l

#push the data into a dataframe then export as a csv file into local directory
df1 = pd.DataFrame(data, index=pdindex)
outputfilename = str(filename)+'-startindex'+str(startindex)+'-numtwts'+str(numoftweets)+'.csv'
df1.to_csv(outputfilename)
