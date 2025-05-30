import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="Esther Luo | Resume", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("Navigation")
nav = st.sidebar.radio("Go to", ("About Me", "Projects", "Contact Me"))

# --- ABOUT ME ---
if nav == "About Me":
    st.title("Esther Luo")
    st.subheader("Climate Finance | Impact Investing | Data-Driven Problem Solver")

    st.markdown("""
    I'm a finance professional with a background in investment banking and private equity,
    currently pivoting into climate finance and impact investing. With academic roots from
    **Wellesley College** in **Quantitative Economics** and **Computer Science**, I bring a
    rigorous analytical mindset and a passion for sustainable development.

    I've built forecasting tools with **Python**, **Streamlit**, **Prophet**, **SQL**, and
    am exploring scalable models to support ESG-aligned investments.
    """)

# --- PROJECTS ---
elif nav == "Projects":
    st.title("My Projects")

    tab1, tab2, tab3 = st.tabs([
        "📊 Emission Predict App",
        "🔄 Recyclable Project",
        "🧭 Sustainability Advisor KNN"
    ])

    with tab1:
        st.markdown("""
        A Streamlit application that predicts emissions based on various features using machine learning models.

        **Key Tools:** Streamlit, Scikit-learn, Pandas
        """)
        st.link_button("View GitHub Repo", "https://github.com/eluo0108/Emission_Predict_App")

    with tab2:
        st.markdown("""
        A project aimed at detecting recyclable materials using computer vision models and integrating them into a sustainability dashboard.

        **Key Tools:** Python, OpenCV, Streamlit
        """)
        st.link_button("View GitHub Repo", "https://github.com/eluo0108/Recyclable_Project")

    with tab3:
        st.markdown("""
        A K-Nearest Neighbors based advisor tool to suggest sustainable practices based on company characteristics.

        **Key Tools:** Python, Scikit-learn, Streamlit
        """)
        st.link_button("View GitHub Repo", "https://github.com/eluo0108/Sustainability_Advisor_KNN")

# --- CONTACT ME ---
elif nav == "Contact Me":
    st.title("Contact Me")
    st.markdown("""
    - 📧 Email: esther.luo@email.com
    - 🌐 LinkedIn: [linkedin.com/in/estherluo](https://linkedin.com/in/estherluo)
    - 📝 Blog: [move-with-power.substack.com](https://move-with-power.substack.com)
    """)

with st.form(key='contact_form'):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Message sent ✅")