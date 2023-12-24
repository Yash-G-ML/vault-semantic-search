# This file contains functions
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.storage import LocalFileStore
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import CacheBackedEmbeddings
from langchain.vectorstores import Chroma
import chromadb
from termcolor import colored
import os
from utils import *

def save_vec_to_chroma(filepath, collection):
    try:
        filepath = move_files(filepath,"vault")
        loader = PyPDFDirectoryLoader(filepath)
        text_splitter = CharacterTextSplitter(chunk_size=256, chunk_overlap=0)
        docs = loader.load_and_split(text_splitter=text_splitter)
        
        print(f"Total number of chunks : {colored(len(docs),'green')}")
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = Chroma.from_documents(docs, embedding_function,persist_directory=f"./{collection}")
        
    except Exception as e:
        print(colored(e,'red'))
        
        
def search_vec(query,collection,k=5):
    try:
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = Chroma(persist_directory=collection, 
                         embedding_function=embedding_function)
        
        # print(f"Connected to collection : {colored(db._collection,'yellow')}")

        docs = db.similarity_search(query,k)
        return docs
    except Exception as e:
        print(colored(e,'red')) 