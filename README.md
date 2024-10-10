## 👾💬 AI Code Assistant using Yi-Coder-9B
Inspired by [Shubham Saboo](https://github.com/Shubhamsaboo)'s [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

This project demonstrates how to build a ChatGPT-like code assistant using the [Yi-Coder-9B](https://huggingface.co/lmstudio-community/Yi-Coder-9B-Chat-GGUF) model running locally on your computer. The application is built using Python and Streamlit, providing a user-friendly interface for interacting with the language model. Best of all, it's 100% free and doesn't require an internet connection!

### Features
- Runs locally on your computer without the need for an internet connection and completely free to use.
- Utilizes the Yi-Coder-9B coding model from Yi, supporting a staggering 52 programming language, and featuring a max context length of 128k, making it great for ingesting large codebases
- Provides a chat-like interface for seamless interaction

### How to get Started?

1. Clone the GitHub repository

```bash
git clone https://github.com/andreaceto/local-code-assistant.git
```
2. Create a virtual environment and activate it:

```bash
python -m venv venv-name
venv-name/Scripts/activate  # On MacOS use `source venv-name/bin/activate`
```
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
4. Download and install the [LM Studio desktop app](https://lmstudio.ai/). Download the Yi-Coder-9B model from the 'Discover' tab. 

5. Expose the Yi-Coder-9B model as an OpenAI API by starting the server in LM Studio. Watch this [video walkthrough](https://x.com/Saboo_Shubham_/status/1783715814790549683).

6. Run the Streamlit App
```bash
streamlit run ai_code_assistant.py
```