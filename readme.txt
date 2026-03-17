1.python 3.11.9 - To avoid issues with langchain
2.use model ollama phi3
Download and install https://ollama.com/download
and in Ollama UI select "phi3". This will download the right model
3.Additionally you can go to ~/helper/llmmethods.py and change this line
lm = ChatOllama(model="phi3") to select the model you want to use
                     

