from txtai.embeddings import Embeddings
from txtai.pipeline import Extractor
from txtai.pipeline import Textractor
from pathlib import Path
from itertools import chain

DATA_PATH = Path("/home/amunoz/projects/txtai/data")
# Create and run pipeline
textract = Textractor(paragraphs=True)

# Create extractor instance
extractor = Extractor(embeddings, "distilbert-base-cased-distilled-squad")
     
data = list(chain.from_iterable(extracted))
embeddings = Embeddings({"content": True})
embeddings.index(data)

# Create and run pipeline
rag = RAG(embeddings, "google/flan-t5-base", template="""
  Answer the following question using the provided context.

  Question:
  {question}

  Context:
  {context}
""")

