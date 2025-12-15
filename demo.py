
import pandas as pd
import re
import plotly.express as px
import streamlit as st
from collections import Counter

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="Resume Data Analytics Dashboard",
    layout="wide"
)

st.title(" Resume Dataset  Analytics Dashboard")

# -----------------------------------------
# LOAD DATA
# -----------------------------------------
df = pd.read_csv("Resume.csv")

# -----------------------------------------
# DATA CLEANING
# -----------------------------------------
df.drop_duplicates(inplace=True)
df['resume_length'] = df['Resume_str'].apply(len)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df['cleaned_resume'] = df['Resume_str'].apply(clean_text)

# -----------------------------------------
# CREATE TABS
# -----------------------------------------
categories = sorted(df['Category'].unique())
tabs = st.tabs(["=Ì All Resumes"] + categories)

# ==================================================
# TAB 1: ALL RESUMES
# ==================================================
with tabs[0]:

    st.subheader(" Overall Resume Analysis")

    # KPIs
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Resumes", df.shape[0])
    col2.metric("Total Categories", df['Category'].nunique())
    col3.metric("Avg Resume Length", int(df['resume_length'].mean()))

    # Category Distribution
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'count']

    fig1 = px.bar(
        category_counts,
        x='Category',
        y='count',
        title="Resume Count by Job Category"
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Resume Length Distribution
    fig2 = px.histogram(
        df,
        x='resume_length',
        nbins=30,
        title="Overall Resume Length Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Top Keywords
    words = " ".join(df['cleaned_resume']).split()
    top_words = Counter(words).most_common(10)
    top_words_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])

    fig3 = px.bar(
        top_words_df,
        x='Frequency',
        y='Word',
        orientation='h',
        title="Top 10 Resume Keywords (Overall)"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ==================================================
# DEPARTMENT-WISE TABS
# ==================================================
for i, category in enumerate(categories, start=1):

    with tabs[i]:

        st.subheader(f"=Ì Department: {category}")

        dept_df = df[df['Category'] == category]

        # KPIs
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Resumes", dept_df.shape[0])
        col2.metric("Avg Resume Length", int(dept_df['resume_length'].mean()))
        col3.metric("Max Resume Length", int(dept_df['resume_length'].max()))

        # Resume Length Distribution
        fig1 = px.histogram(
            dept_df,
            x='resume_length',
            nbins=25,
            title="Resume Length Distribution"
        )
        st.plotly_chart(fig1, use_container_width=True)

        # Top Keywords
        words = " ".join(dept_df['cleaned_resume']).split()
        top_words = Counter(words).most_common(10)
        top_words_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])

        fig2 = px.bar(
            top_words_df,
            x='Frequency',
            y='Word',
            orientation='h',
            title="Top 10 Resume Keywords"
        )
        st.plotly_chart(fig2, use_container_width=True)

        # Sample Resumes
        with st.expander("= View Sample Resumes"):
            st.write(dept_df[['Resume_str']].head(3))

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown("---")
st.markdown(" **Aditya Bhandari  Resume Analytics Dashboard | Veridia**")
