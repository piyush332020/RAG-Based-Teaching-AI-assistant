import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import joblib
import requests



def create_embeddings(text_list):
    r=requests.post("http://127.0.0.1:11434/api/embed",json={
        "model":"bge-m3",
        "input":text_list
    })
    embeddings=r.json()["embeddings"]
    return embeddings


def infrence(prompt,model):
    r=requests.post("http://127.0.0.1:11434/api/generate",json={
            "model":model,
            "prompt":prompt,
            "stream":False
        })
    response = r.json()
    print(response)
    return response
#load the dataframe
df=joblib.load('embeddings.joblib')


incoming_query=input("Ask a Question: ")
# here it crate the embdiing
question_embedding=create_embeddings([incoming_query])[0]
# df.to_json("records.json", orient="records", indent=4)
# print(question_embedding)
#Finding simalraity of question embedding with other embedding

#np.vstack used to flatten the array [[]] -> []
similarities=cosine_similarity(np.vstack(df['embedding'].values),[question_embedding]).flatten()
print(similarities)
#for getting highest value index use for top 3 index
max_indices=similarities.argsort()[::-1][0:5]
print(max_indices)
new_df=df.loc[max_indices]
print(new_df[['number','title','text']])


#prompt && model
prompt=f''' Here are vedio chunks containing vedio title,vedio number, start time in second,end time in second,the text at that time

{new_df[["title","number","start","end","text"]].to_json()}

---------------------------------------------------------
"{incoming_query}"
The user asked this question related to vedio chunks, you have to answer in human way(don't mention above format it just for you )where and how much content taught where (in which vedio and at what timestamp in minutes or hour format which is best suitable) and guide the user to go to that particular vedio
if user asks unrelated question ,tell him that you can only answer question related to the course
'''
model="deepseek-r1:14b"

with open("prompt.txt","w") as f:
    f.write(prompt)


response=infrence(prompt,model)["response"]
print(response)
with open("response.txt","w") as f:
    f.write(response)

for index,item in new_df.iterrows():
    print(index,item["title"],item["number"],item["text"],item["start"],item["end"])