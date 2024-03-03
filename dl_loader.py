from langchain.document_loaders import DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import chromadb
import os
import shutil
import chromadb
from langchain_community.vectorstores import Chroma


PATH = "data"
CHROMA_PATH = "chroma"
def load_documents():
    loader = DirectoryLoader(PATH , glob = "*.md")
    documents = loader.load()
    
    return documents

def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 500,
        length_function=len,
        add_start_index = True,
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)}  into {len(chunks)} chunks")
    print(documents.page_content)
    print(documents.metadata)
    return chunks

def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks ot {CHROMA_PATH}")


def load_documents():
    loader = DirectoryLoader(PATH, glob="*.md")
    documents = loader.load()
    return documents


embedding_function = OpenAIEmbeddings()
db = Chroma(persist_directory = CHROMA_PATH , embedding_function= embedding_function)


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


# results = db.similarity_search_with_relevance_scores(query_text , k=3)

# chroma_client = chromadb.Client()
if __name__ == "__main__":
    main()
