import langchain
import os
from langchain.document_loaders import TextLoader

loader = TextLoader("text.txt",encoding = 'UTF-8')
document = loader.load()
os.environ["HUGGINGFACEHUB_APPI_TOKEN"] = 'BURAYA HUGGINFACE TOKENI GRIRIN'
#Preprocessing
import textwrap

def wrap_text_preserve_newlines(text, width=110):
    #split the input text into lines based on newline characters
    lines = text.split('\n')
    #Wrap each line individually
    wrapped_lines = [textwrap.fill(line,width=width) for line in lines]
    #Join the wrapped lines back tohether using newline characters
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

                    
                    
#Text Splitting
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size =1000,chunk_overlap = 0)   

from langchain.text_splitter import RecursiveCharacterTextSplitter


with open("text.txt",encoding='UTF-8') as f:
    state_of_the_union = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
document = text_splitter.split_text(state_of_the_union)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

docs = text_splitter.create_documents(document)

##Embedding
from langchain.embeddings import HuggingFaceBgeEmbeddings

embedding = HuggingFaceBgeEmbeddings()

from langchain.vectorstores import FAISS

db = FAISS.from_documents(docs,embedding)






from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub


llm = HuggingFaceHub(repo_id="google/flan-t5-xxl",model_kwargs = {"temperature":0.8,"max_lenght":128},huggingfacehub_api_token='BURAYAHUGGINGFACE TOKENIGIRILECEK')

chain = load_qa_chain(llm,chain_type="stuff")

queryText = "what is the OneAMZ?"
doc=db.similarity_search(queryText)

chain.run(input_documents = doc, question = queryText)