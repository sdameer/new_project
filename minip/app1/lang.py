import langchain
import os
import sys
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
import pandas as pd
import json


llm = ChatGroq(
    model="llama-3.1-8b-instant",
# add yout api key here : 
    api_key="")  

messages = [
    ("system", "You are an expert customer reviewer assisstant "),
    ("human", """summarize : 
     {context} in 3 lines and give me the 
     sentiment (Postive/Negative/Neutral).
     output in json
     "transcript":"" , 
     "summary":"" , 
     "sentiment" :""
     Note : No preamble     
     """),
]

def main_func(context):
    """
        this function returns a json 
        {
            "transcript" : "",
            "summary" : "",
            "sentiment" : ""                        
        }
    """
    prompt_template = ChatPromptTemplate.from_messages(messages)
    dict_data = llm.invoke(prompt_template.invoke({"context": context})).content
    dict_data = json.loads(dict_data)  # type: ignore
    save_file(dict_data)
    # print(f"\n\n{dict_data}\n\n")
    return dict_data


def save_file(dict_data):
    """
        this function adds the data to the
        csv file if it exists if not 
        it will create one and add to it
    """
    
    # this will give me the current directory name : 
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # this will add the csv file into current directory :
    new_file = os.path.join(dir_path, "call_analysis.csv")

    # Check if file exists
    if not os.path.exists(new_file):
        df = pd.DataFrame(
            {
                "transcript": [dict_data['transcript']],
                "summary": [dict_data['summary']],
                "sentiment": [dict_data['sentiment']]
            }
        )
        df.to_csv(new_file, index=False)
        print('\n\nNO CSV available, creating new CSV.....\n\n')
    else:
        df = pd.read_csv(new_file)
        print('\n\nCSV available, updating CSV...\n\n')

        new_response = pd.DataFrame(
            {
                "transcript": [dict_data['transcript']],
                "summary": [dict_data['summary']],
                "sentiment": [dict_data['sentiment']]
            }
        )
        df = pd.concat([df, new_response], ignore_index=True)
        df.to_csv(new_file, index=False)