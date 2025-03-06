import streamlit as st
import openai

# Streamlit App Configuration
st.set_page_config(
    page_title="🛠️ AI Code Debugger & Optimizer",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar: Page Selector
with st.sidebar:
    st.header("📌 Select a Page")
    page = st.radio(
        "Navigate:",
        ["About the App", "AI Code Debugger & Optimizer"],
        index=1  # Default to "About the App"
    )

# About the App Page
if page == "About the App":

    st.markdown("""




#### 1️⃣ Name & Role  
**Agent Name:** **PyFixer** – Your AI-Powered Python Debugging & Optimization Assistant  
**Role:** PyFixer is designed to help Python developers identify bugs, optimize performance, and improve overall code quality. Whether you're a beginner struggling with syntax errors or an experienced coder looking to refine your scripts, PyFixer acts as a smart AI partner to streamline your debugging and optimization workflow.  

---

#### 2️⃣ Origin Story  
Every developer, at some point, faces the frustrating cycle of debugging and optimizing code. Typos, inefficiencies, and hard-to-trace errors slow down progress, making coding more time-consuming than it should be.  

The idea for **PyFixer** was born out of a need to **simplify** and **automate** this process. Imagine having an expert Python mentor available 24/7—one that not only **spots errors** but also suggests **clear, optimized solutions**. PyFixer was built with **GPT-4o** to provide **instant, AI-driven feedback**, allowing developers to focus on creativity rather than debugging struggles.  

With PyFixer, developers can **write better code, faster**—turning debugging from a headache into a seamless, intuitive experience.  

---

#### 3️⃣ How It Works  
Using PyFixer is effortless. Here’s how you can improve your Python code in three simple steps:  

1. **Paste Your Python Code** 📝  
   - Drop your Python script into the text box. No need to format or modify it—just paste it as it is.  

2. **Click "Analyze & Optimize"** 🔍  
   - PyFixer will instantly scan your code, identifying errors, inefficiencies, and areas for improvement.  

3. **Receive an Enhanced Version** 🚀  
   - The AI will provide a detailed analysis and suggest an optimized version of your code with explanations.  

This process not only fixes immediate issues but also helps you **learn and write better Python code** over time.  

---

#### 4️⃣ Key Features  
PyFixer is packed with features that make it an essential tool for any Python developer:  

✅ **Error Detection & Fixing** – Identifies syntax errors, logical mistakes, and common bugs.  
🚀 **Performance Optimization** – Suggests better ways to structure your code for efficiency.  
📊 **Code Quality Insights** – Enhances readability, following best practices and clean coding principles.  
🤖 **AI-Powered Debugging** – Uses GPT-4o’s advanced reasoning to provide intelligent recommendations.  
💡 **Easy-to-Use Interface** – A simple, no-setup-required tool accessible to all developers.  
📈 **Continuous Improvement** – The more you use PyFixer, the better your coding skills become!  

---

PyFixer is **more than just a debugging tool**—it’s your **AI-powered coding assistant**, making Python development **smarter, faster, and frustration-free**. 🚀🐍  


    """)

# AI Code Debugger & Optimizer Page
else:
    st.title("🛠️ AI Code Debugger & Optimizer")
    st.markdown("""
        <div style='background-color: #FF8C00; padding: 1rem; border-radius: 0.5rem; margin-bottom: 2rem; color: white;'>
        Paste your Python code below to analyze, debug, and optimize it for better performance.
        </div>
    """, unsafe_allow_html=True)

    # Sidebar: API Configuration
    with st.sidebar:
        st.header("🔑 API Configuration")
        openai_api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
        if not openai_api_key:
            st.warning("⚠️ Please enter your OpenAI API Key to proceed")
            st.stop()
        st.success("API Key accepted!")

    # Code Input
    st.header("🐍 Paste Your Python Code")
    user_code = st.text_area("Enter Python code here", height=250, help="Paste your Python script for debugging and optimization.")

    if st.button("🔍 Analyze & Optimize"):
        with st.spinner("Analyzing and optimizing your code..."):
            system_prompt = "You are an expert Python programmer. Analyze the given code for errors, inefficiencies, and optimizations. Provide a detailed report and an optimized version of the code."
            
            def call_gpt4o(api_key, system_prompt, user_code):
                """Calls GPT-4o API using OpenAI's client API."""
                client = openai.Client(api_key=api_key)
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_code},
                        ]
                    )
                    return response.choices[0].message.content
                except Exception as e:
                    return f"❌ Error: {e}"

            response = call_gpt4o(openai_api_key, system_prompt, user_code)
            
            st.subheader("📋 Analysis & Optimized Code")
            st.markdown(response)

    st.write("---")
    st.caption("🔹 Developed with Streamlit & GPT-4o for AI-powered debugging and optimization.")
