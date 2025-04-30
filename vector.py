from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd
import glob

# Loop through and consolidate multiple CSV files

# Get list of all CSV files
csv_files = glob.glob("*.csv")
if not csv_files:
    raise FileNotFoundError("No CSV files found in the current directory")

# Initialize an empty DataFrame
df = pd.DataFrame()

# Loop through each CSV file and concatenate to the main DataFrame
for file in csv_files:
    try:
        # Use error_bad_lines=False to skip problematic rows
        temp_df = pd.read_csv(file, on_bad_lines="skip")
        df = pd.concat([df, temp_df], ignore_index=True)
    except Exception as e:
        print(f"Warning: Issue with file {file}: {e}")

# Check if any data was loaded
if df.empty:
    raise ValueError("No data found in CSV files")


embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=str(row["term"]) + " " + str(row["question"]),
            metadata={"answer": row["answer"], "domain": row["domain"]},
            id=str(i),
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="security_plus_notes",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
