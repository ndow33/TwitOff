import basilica
import os
from dotenv import load_dotenv

load_dotenv()

# Get my API key from the env file
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

# create a connection object that interfaces with basilica API using my API key
connection = basilica.Connection(BASILICA_API_KEY)



if __name__ == "__main__":
    
    print(type(connection))
    sentences = ["Hello world!", "How are you?"]
    # embed the strings above as a vector of numbers
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]