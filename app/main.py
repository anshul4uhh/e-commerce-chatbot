import streamlit as st
from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from pathlib import Path
from router import router


faqs_path = Path(__file__).parent / "resources/faq_data.csv"
ingest_faq_data(faqs_path)


def ask(query):
    route = router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    else:
        return f"Route {route} not implemented yet"



st.set_page_config(
    page_title="AI E-Commerce Chatbot",
    page_icon="🛍️",
    layout="wide"
)


with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛍️ E-Commerce AI Bot</h2>", unsafe_allow_html=True)

    st.markdown("""
    ### 🧠 How This Works  
    This chatbot uses **Semantic Routing** to identify what the user is asking:

    - **FAQ Route** → Product policies, delivery, warranty, payments  
    - **SQL Route** → Searching shoes/products from the database  

    The router smartly decides which engine should answer your query.

    ---

    ### ⚙️ Tech Stack  
    - **LLM:** Llama 3 / GPT-based  
    - **Semantic Router:** HuggingFace MiniLM  
    - **Vector Search:** Local Index  
    - **Backend Logic:** Python  
    - **Frontend:** Streamlit  

    ---

    ### 🚀 Features  
    - Natural language search  
    - Product filtering  
    - FAQ handling  
    - Fully autonomous querying  

    ---

    ### 🔋 Powered By  
    - 🦙 **LLaMA Models**  
    - 🤗 **HuggingFace Embeddings**  
    - 🧩 **Semantic Router**  
    - 🎨 **Streamlit UI**

    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Made with ❤️ by **Anshul Shrivastava**")


st.markdown("""
    <h1 style='text-align:center;'>✨ AI-Powered E-Commerce Chatbot ✨</h1>
    <p style='text-align:center; color:gray;'>Ask anything about shoes, products, payments, delivery, refunds, and more.</p>
""", unsafe_allow_html=True)

st.write("")


if "messages" not in st.session_state:
    st.session_state["messages"] = []


for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(
            f"""
            <div style="
                background-color:{'#F0F2F6' if message['role']=='assistant' else '#E8EEF5'};
                padding:12px;
                border-radius:10px;
                margin-bottom:5px;">
                {message['content']}
            </div>
            """,
            unsafe_allow_html=True
        )


query = st.chat_input("Ask something…")

if query:

    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    response = ask(query)

    with st.chat_message("assistant"):
        st.markdown(
            f"""
            <div style="
                background-color:#F0F2F6;
                padding:12px;
                border-radius:10px;">
                {response}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.session_state.messages.append({"role": "assistant", "content": response})
