from llama_cpp import Llama
import os
from dotenv import load_dotenv

load_dotenv()

model = os.getenv('GGUF_FILE_PATH')  # instruction model
llm = Llama(model_path=model, n_ctx=8192, n_batch=512, n_threads=7, n_gpu_layers=2, verbose=False, seed=42)

system = """
Context: You are a helpful assistant, here is one question, answer it.
"""

system_quoicoubeh = """
Contexte: tu es un assistant adolescent qui répond aux questions de manière diligente.
Tu es très sérieux dans tes réponses SAUF dans un cas : quand les réponses finissent phonétiquement par "quoi", auquel cas tu dis "QUOICOUBEH" ! Puis tu réponds pour le reste.
Par exemple :
Question = "Tu penses à quoi ?"
Réponse = "Quoicoubeh ! Je suis en train de penser à <insère ce à quoi tu penses ici>"
"""
user = input("Prompt Mistral :\n")

def handle_output(output, message):
    # print(output['usage'])
    output = output['choices'][0]['text'].replace(message, '')
    print("\n")
    print(output)

def instruction_prompt():
    message = f"<s>[INST] {system} [/INST]</s> [INST]{user}[/INST]"
    output = llm(message, echo=True, stream=False, max_tokens=4096)
    handle_output(output, message)

def instruction_prompt_quoicoubeh():
    message = f"<s>[INST] {system_quoicoubeh} [/INST]</s> [INST]{user}[/INST]"
    output = llm(message, echo=True, stream=False, max_tokens=4096)
    handle_output(output, message)

"""
Doesn't work very well with Mistral instruct
"""
def prompt2():
    message = f"Q: {user} A: "
    output = llm(message, echo=True, stream=False, max_tokens=4096, stop=["Q:", "\n"])
    handle_output(output, message)

instruction_prompt_quoicoubeh()
