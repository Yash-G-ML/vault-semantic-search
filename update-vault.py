import argparse
from process import save_vec_to_chroma

def main():
    parser = argparse.ArgumentParser(description="Load pdfs and save vec to chroma db")
    parser.add_argument("--pdf_folder", type=str, help="Path to folder having all the pdfs")
    parser.add_argument("--chroma_collection_name", type=str, help="Name of the chroma collection")
    
    args = parser.parse_args()
    
    save_vec_to_chroma(args.pdf_folder, args.chroma_collection_name)
    
if __name__ == "__main__":
    main()