# 📝 Customer Call Analysis App

This project is a **Django + LangChain + Groq-based Python app** that analyzes customer call transcripts.  

It can:  
- Accept a transcript as input (via endpoint or UI).  
- Use **Groq API** + **LangChain** to:  
  - Summarize the conversation in 2–3 sentences.  
  - Extract sentiment (Positive / Neutral / Negative).  
- Display the transcript, summary, and sentiment.  
- Save results into a `.csv` file (`call_analysis.csv`) with columns:  
>>> ` Transcript | Summary | Sentiment `

---

## 🚀 Features
- Simple Python/Django app.  
- AI-powered summarization & sentiment detection using **Groq + LangChain**.  
- Automatically logs every result into a CSV file.  

---

## 🛠️ Tech Stack
- **Django** → Server framework  
- **LangChain** → LLM orchestration  
- **Groq API** → Model inference (LLaMA 3.1 8B Instant)  
- **Pandas** → CSV handling  

---

## 📂 Project Flow
1. Input a transcript.  
2. Groq API generates summary + sentiment.  
3. Results are shown and saved into `call_analysis.csv`.  
4. Next runs keep appending to the CSV.  

---

## ⚙️ How to Run
1. Clone the repo:  
 ```
 https://github.com/sdameer/new_project.git
 cd new_project
 cd minip
```

1. Install dependencies:
```
   pip install -r requirements.txt
```
2. Add your Groq API key inside the code:
```
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="your_api_key_here"
)
```
3 .Run the app:
```
python manage.py runserver
```
---

`main_func(context)` 

→ Takes a transcript, sends it to Groq, gets back JSON (transcript, summary, sentiment), saves it.

`save_file(dict_data)`

 → Checks if `call_analysis.csv` exists; creates it if not, otherwise appends new results.