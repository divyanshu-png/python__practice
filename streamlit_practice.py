import streamlit as st
import pandas as pd

# Title of the app
st.title("My First Streamlit App")

# Writing text is easy
st.write("Here is some data from a CSV file:")

# Displaying a dataframe (it will be interactive!)
df = pd.DataFrame({'Column A': [1, 2, 3], 'Column B': [10, 20, 30]})
st.dataframe(df)

#Chat input ke liye 
#jo bhi blur hua dikhrha hota in the message box is the placeholder
st.chat_input(placeholder="Type your message here", accept_file= True, file_type=None, width= "stretch")

# A simple slider
age = st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old.")

# A button
if st.button("Say Hello"):
    st.success("Hello there!")
else:
    st.info("Click the button above.")


# Sidebar
st.sidebar.header("User Panel")
theme = st.sidebar.selectbox("Choose a theme", ["Light", "Dark"])
st.sidebar.subheader("Practice in: ")
list_subject= st.sidebar.radio("Choose the subject: ", ['C++', 'Python', 'Java'])
# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.image("https://placekitten.com/200/200")

with col2:
    st.header("Column 2")
    st.write("Some descriptive text over here.")