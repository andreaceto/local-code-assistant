import streamlit as st
from openai import OpenAI

# Set up the Streamlit App
st.title("👾💬 AI Code Assistant")
st.caption("Chat with locally hosted Yi-Coder-9B using the LM Studio 💯")

# Point to the local server setup using LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Placeholder for assistant's response
    response_container = st.chat_message("assistant")
    full_response = ""

    # Stream the response in chunks
    with response_container:
        # Use a Streamlit markdown placeholder to update content incrementally
        assistant_message = st.empty()
        
        # Function to simulate pinging effect by changing ball color between gray and white
        def show_typing_effect():
            assistant_message.markdown(full_response + ' ●')
        
        # Initiate the stream
        response = client.chat.completions.create(
            model="lmstudio-community/Yi-Coder-9B-Chat-GGUF",
            messages=st.session_state.messages,
            temperature=0.7,
            stream=True
        )

        # Process streamed chunks and append the latest token to the UI
        for chunk in response:
            chunk_text = getattr(chunk.choices[0].delta, 'content', '')
            if chunk_text:  # Ensure chunk_text is not None
                full_response += chunk_text  # Append the chunk to the full response
                show_typing_effect()  # Show typing effect at the end of the message
    
    # Clear the ping effect when the message is complete
    assistant_message.markdown(full_response)  # Update with the final response (without ping effect)
    
    # Add the complete assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
