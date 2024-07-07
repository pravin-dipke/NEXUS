import gradio as gr
import ollama

def format_history(msg: str, history: list[list[str, str]], system_prompt: str):
    if not system_prompt:
        system_prompt = "You are a helpful assistant."  
    chat_history = [{"role": "system", "content": system_prompt}]
    for query, response in history:
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})  
    chat_history.append({"role": "user", "content": msg})
    return chat_history

def generate_response(msg: str, history: list[list[str, str]], system_prompt: str, selected_llm: str):
    chat_history = format_history(msg, history, system_prompt)
    if selected_llm == "phi3":
        response = ollama.chat(model='phi3', stream=True, messages=chat_history)
    elif selected_llm == "llama3":
        response = ollama.chat(model='llama3', stream=True, messages=chat_history)
    elif selected_llm == "mistral":
        response = ollama.chat(model='mistral', stream=True, messages=chat_history) 
    elif selected_llm == "deepseek-coder:6.7b":
        response = ollama.chat(model='deepseek-coder:6.7b', stream=True, messages=chat_history)
    else:
        raise ValueError(f"Unsupported LLM: {selected_llm}")
    
    message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        message += token
        yield message

llm_options = ["phi3", "llama3", "deepseek-coder:6.7b", "mistral"] 

chatbot = gr.ChatInterface(
                generate_response,
                chatbot=gr.Chatbot(
                        avatar_images=["/Users/PravinDipke/Documents/Project/final-project/user-img.jpeg", "/Users/PravinDipke/Documents/Project/final-project/chatbot.png"],
                        height="64vh",
                        label="Start typing"
                    ),
                additional_inputs=[
                    gr.Textbox(
                        label="System Prompt",
                        placeholder="Enter your system prompt here"
                    ),
                    gr.Dropdown(choices=llm_options, label="Select LLM", value="llama3")
                ],
                title="NEXUS",
                description="Feel free to ask any question.",
                theme="soft",
                submit_btn="⬅ Send",
                retry_btn="🔄 Regenerate Response",
                undo_btn="↩ Delete Previous",
                clear_btn="🗑️ Clear Chat"
)

chatbot.launch()