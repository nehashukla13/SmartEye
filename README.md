# SmartEye
Smarteye is an amazing method to determine whether a piece of text is written by large language models (like ChatGPT, GPT3, GPT2, BLOOM etc) or Human-authored.

# Installation

 1) Using main.py file
--> python -m venv env (create environment)
--> env\Scripts\activate (activate environment)
--> pip install -r requirements.txt (install requirements)

 2) using docker
--> sudo docker build build -t smart-eye-image .
--> sudo docker run -d -p 80:80 smart-eye-image 

example
Please enter your sentence: (Press Enter twice to start processing)
Hello World.
My name is neha.
(empty line)


Acknowledgement
This repository is built based on the hugging face https://huggingface.co/docs/transformers/perplexity
