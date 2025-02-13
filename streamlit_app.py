import streamlit as st
import random

# Function to load a random motivational quote from a file
def load_motivational_quote():
    with open("motivation.txt", "r") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()  # Return a random quote

# Function to display the chat page
def chat_page():
    # Display a random motivational quote
    motivational_quote = load_motivational_quote()
    st.title(f"**Joke of the day :** \n {motivational_quote}")
    
    # Input box for leaving name and message
    user_name = st.text_input("Your name:")
    user_message = st.text_input("Your message:")
    
    # Save message to file: chat.txt when user clicks button
    if st.button("Send"):
        if user_name and user_message:  # Ensure both fields are filled
            with open("chat.txt", "a") as file:  # Use append mode
                file.write(f"{user_name}: {user_message}\n")  # Write message to file
            st.success(" 👍 ")  # Feedback to the user
        else:
            st.error("Please enter both your name and message.")  # Error message

    # Display all contents of file as conversation based on the user_name
    st.subheader("Chat History:")
    try:
        with open("chat.txt", "r") as file:
            chat_history = file.read()
            chat_lines = chat_history.splitlines()  # Split chat history into lines
            chat_data = []  # Prepare data for the table

            for line in chat_lines:
                if line.strip():  # Ensure the line is not empty
                    user_name, user_message = line.split(": ", 1)  # Split into user name and message
                    chat_data.append({"User Name": user_name, "User Message": user_message})  # Append to chat data
            st.table(chat_data) 
    except FileNotFoundError:
        st.write("No chat history found.")  # Handle case where the file does not exist
    
# Function to display the About page
def about_page():
    st.title("About Me")
    st.write("Welcome to my about page!")
    st.write("Here you can find my favourite songs, food and other personal information.")
    st.write("Feel free to share links on the chatbot")
    
    # Display CV as a downloadable link
    st.subheader("Song of the moment")
    st.write("Just click play - make sure you got your ear pieces on 🤪")
    # st.markdown("[Download CV](path_to_your_cv.pdf)")  # Replace with the actual path to your CV

# Function to display the Gallery page
def gallery_page():
    st.title("Gallery")
    st.write("Lets share memes and shit!")
    # st.write("T")
    
    # Example images
    st.image("./image.png", caption="Why oyu taking time to get here??")  # Replace with actual image paths
    # st.image("image2.jpg", caption="Image 2 Description")  # Replace with actual image paths

# Main function to control the app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Chat", "About", "Gallery"])

    if page == "Chat":
        chat_page()
    elif page == "About":
        about_page()
    elif page == "Gallery":
        gallery_page()

# Run the app
if __name__ == "__main__":
    main()
