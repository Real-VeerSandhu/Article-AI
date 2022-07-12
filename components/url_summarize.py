# Summarize articles via url input

from tabnanny import check
import streamlit as st
import nltk
nltk.download('punkt')
from newspaper import Article

import re
from math import ceil

def check_link(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if 'https://www.' in url or 'http://www.':
        return re.match(regex, url) is not None
    elif re.match(regex, url) is not None:
        return True
    else:
        return False

def fetch_text_data(article):
    article.download()
    article.parse()
    article.nlp()
    # print('\nTitle\n', article.title)
    # print('\nSUMMARY\n', article.summary)
    # print('\nKEYWORDS\n', article.keywords)
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
    complex_val = st.slider('Length (%)', 1, 100)

    if check_link(url) == True:
        st.success('Link Valid')
        reader_article = Article(url)
    else:
        st.error('Invalid Link')
        st.caption('Make sure link starts with `https://www.`')

    if (st.button('Summarize') and url != '' and check_link(url) == True):
        with st.empty():
            for i in range(1):
                st.caption('Evaluating...')
                processed_article = fetch_text_data(reader_article)
                full_summary = change_complexity(processed_article.summary, ceil(complex_val/25)+1)
            st.caption('Done!')
        st.write('`Title: `', processed_article.title)
        st.write('`AI Generated Summary: `', full_summary)
        st.write('`Key Words: `', processed_article.keywords)
            

def read_history(value):
    return value