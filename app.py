import pinecone
from datasets import load_dataset

pinecone.init(
    api_key="16825179-e09f-4405-b454-53629d6ade00", environment="us-west4-gcp-free"
)

# load the dataset
celeb_faces = load_dataset("ashraq/tmdb-people-image", split="train")
celeb_faces

# examine data
celeb = celeb_faces[10]
celeb
