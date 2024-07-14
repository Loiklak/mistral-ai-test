# Installation

## Virtual env
Make sure you have [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) installed.

```bash
virtualenv venv
```

## Activate virtual env

```bash
source venv/bin/activate
```

## Install requirements

### For MacOS
```bash
pip install -r requirements.txt
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python==0.2.27
```
When running on M1 Mac we must set the version to an older one because the newer versions do not properly use the GPU somehow and are thus very slow.
Cf [GitHub issue](https://github.com/abetlen/llama-cpp-python/issues/756#issuecomment-1946456235)

## Download a GGUF model

I'm currently using the Mistral-7B-Instruct-v0.1-GGUF model from TheBloke. You can download it from the following link:
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main

## Reference the model path
Copy paste the `.env.example` file and rename it to `.env`. Then, replace the `GGUF_FILE_PATH` variable with the path to the model you downloaded.

# Usage

```bash
python main.py
```
