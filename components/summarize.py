import streamlit as st
import nltk
nltk.download('punkt')
from newspaper import Article

from math import ceil

def fetch_text_data(article):
    article.download()
    article.parse()
    article.nlp()
    print('\nTitle\n', article.title)
    print('\nSUMMARY\n', article.summary)
    print('\nKEYWORDS\n', article.keywords)
    return article

def change_complexity(summary, range):
    sens = summary.split('.\n')
    full = []
    for i in sens[0:range]:
        full.append(i)
    final = ''
    for i in full:
        i = i + '.'
        final += i
    final = final.replace('.', '. ')
    return final[:-2]

def app():
    st.markdown('## Article Summary via URL')

    st.write('Summarize a specific article to a custom length')

    url = str(st.text_input('Enter an Article URL'))
    complex_val = st.slider('Length & Complexity (%)', 1, 100)
    reader_article = Article(url)
    
    if (st.button('Summarize') and url != ''):
        with st.empty():
            for i in range(1):
                st.caption('Evaluating...')
                processed_article = fetch_text_data(reader_article)
                full_summary = change_complexity(processed_article.summary, ceil(complex_val/25)+1)
            st.caption('Done!')
        st.write('`Title: `', processed_article.title)
        st.write('`AI Generated Summary: `', full_summary)
        st.write('`Key Words: `', processed_article.keywords)