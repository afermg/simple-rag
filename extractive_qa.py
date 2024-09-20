from txtai.embeddings import Embeddings
from txtai.pipeline import Extractor, LLM, Textractor
from pathlib import Path
from itertools import chain

DATA_PATH = Path("/home/amunoz/projects/txtai/data")
# Create and run pipeline
textract = Textractor(paragraphs=True)

def stream(path):
  for f in path.rglob("*"):
    # Only accept documents
    if f.suffix in("docx", "xlsx", "pdf"):
      print(f"Indexing {fpath}")
      for paragraph in textractor(fpath):
        yield paragraph

embeddings = Embeddings(content=True)
embeddings.index(stream(DATA_PATH))

llm = LLM(
    # "ollama/llama3.1:70b"
          path="ollama/llama3.1:70b", api_base="http://localhost:11434")
