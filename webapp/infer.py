"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

"""

from model import GPT2PPL

# initialize the model
model = GPT2PPL()

sentence = "your text here"

model(sentence)
