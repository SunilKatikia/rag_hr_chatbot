from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_policy_document(text, filename):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " "]
    )
    docs = splitter.create_documents([text], metadatas=[{"source": filename}])
    return [{"content": d.page_content, "filename": filename} for d in docs]
