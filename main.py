from termcolor import colored
import argparse
from process import search_vec

def main():
    parser = argparse.ArgumentParser(description="search the vault")
    parser.add_argument("--query", type=str, help="query text for retrival")
    parser.add_argument("--k", type=int, default=5, help="k docs to retrive")
    parser.add_argument("--collection", type=str, help="chroma db collection")
    
    
    args = parser.parse_args()
    
    docs = search_vec(args.query, args.collection ,args.k)
    
    for doc in docs:
        print(f'Doc meta data : {colored(doc.metadata,"blue")}')
        print(f'Doc content : {colored(doc.page_content,"green")}')
        
if __name__ == "__main__":
    main()
        
