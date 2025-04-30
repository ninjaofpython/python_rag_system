from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about security+ 701 exam 

Here is a relevant term: {term}

Here is the question to answer: {question}

Here is the answer to the question: {answer}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    returned_terms = retriever.invoke(question)
    answer = ""
    result = chain.invoke(
        {"term": returned_terms, "question": question, "answer": answer}
    )
    print(result)
