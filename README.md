# vault-semantic-search

I have started this project to search the relative content 
from my collection of arXiv papers, which I call Vault

```bash
# Example installation commands
$ git clone https://github.com/Yash-G-ML/vault-semantic-search.git
$ cd vault-semantic-search
$ pip install -r requirements.txt
```
Now create a folder containing arXiv pdf files
run the command
```bash
$  python update-vault.py --pdf_folder <folder_path> --chroma_collection_name <collection_name>
```
Directory tree will be like:
- vault-semantic-search
  - pdf_folder_path
    - file1.pdf
    - file2.pdf
  - vault
    - file1.pdf
    - file2.pdf
  - chroma_collection
  - main.py
  - process.py
  - update-vault.py
  - utils.py
  - requirements.txt

pdf files will be moved to the vault folder,
to add new files to db place files in folder,
and run update-vault.py with existing db name 

Now for semantic search
run the command

```bash
$ python main.py --query "text to be searched" --k 2 --collection <collection_name>
```

