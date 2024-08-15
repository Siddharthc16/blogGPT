import streamlit as st
from helper import BlogGPTHelper

# Function to simulate blog generation (replace with actual content generation logic)
def generate_blog(topic, helper_content):
    # Placeholder for blog generation logic
    blog = f"""
    ### {topic}

    Based on the topic and helper content provided, here is your generated blog:

    {helper_content}

    (This is where the detailed blog content will be displayed, based on the topic and additional research.)
    """
    return blog

# Streamlit UI
st.title("Blog GPT")

st.write("Enter the topic and helper content below to generate a blog.")

# Input fields for topic and helper content
topic = st.text_input("Topic", placeholder="Enter the blog topic")
helper_content = st.text_area("Helper Content", placeholder="Enter helper content related to the topic")

# Button to generate blog
if st.button("Generate Content"):
    if topic and helper_content:
        helper = BlogGPTHelper()
        blog = helper.generate(topic, helper_content)
        st.write("### Generated Blog")
        st.markdown(blog)
    else:
        st.error("Please provide both a topic and helper content.")

