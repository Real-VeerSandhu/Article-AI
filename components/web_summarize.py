# Query articles based on search term and summarize each fetched article

from matplotlib.pyplot import LinearLocator
import streamlit as st
import nltk
nltk.download('punkt')

from newspaper import Article

from urllib.request import Request, urlopen 
from bs4 import BeautifulSoup
import requests

def get_links(user_search): # Web scrape articles related to search query
    root = "https://www.google.com/"
    search_engine_string = 'search?q='
    search_engine_other_half = '&sxsrf=AOaemvIiKfd8dkMCkRXEhoZm3rjXFGMzCQ:1631931499445&source=lnms&tbm=nws&sa=X&ved=2ahUKEwikm8nKuofzAhUPElkFHVshBFUQ_AUoAnoECAEQBA&biw=1295&bih=697&dpr=2'
    link = root + search_engine_string + user_search + search_engine_other_half
    lst = []
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'lxml')
        for item in soup.find_all('div', attrs={'class':'kCrYT'}):
            try:
                try:
                    raw_link = (item.find('a', href=True)['href'])
                    link = (raw_link.split("/url?q=")[1]).split('&sa=U&')[0]
                    if not link in lst:
                        lst.append(link)
                    else:
                        pass
                except IndexError:
                    break
            except TypeError:
                pass
    return lst

def fetch_text_data(input_url): # Fetch article data
    article = Article(input_url) 

    article.download()
    article.parse()
    article.nlp()
    print('\nTitle\n', article.title)
    print('\nSUMMARY\n', article.summary)
    print('\nKEYWORDS\n', article.keywords)
    return article


def app():
    st.markdown('## Article Summary via Search')

    st.write('Search the web for articles and output summaries')

    search_item = str(st.text_input('Enter Search Term(s)'))
    search_item = search_item.replace(' ', '')
    
    if (st.button('Search') and search_item != ''):
        links = get_links(search_item)

        link1 = str(links[0])
        link2 = str(links[1])
        link3 = str(links[2])

        primary_links = links[:3]
        other_links = links[3:]

        for i in range(len(primary_links)):
            processed_article = fetch_text_data(primary_links[i])
            st.write(f'**Article #{i+1}**')
            st.write('`Title: `', processed_article.title)
            st.write('`URL: `', primary_links[i])
            st.write('`AI Generated Summary: `', processed_article.summary)

            print(f'Link #{i+1} Completed @ {primary_links[i]}')


        with st.empty():
            for i in range(1):
                st.caption('Evaluating...')
                processed_article1 = fetch_text_data(link1)
                processed_article2 = fetch_text_data(link2)
                processed_article3 = fetch_text_data(link3)
            st.caption('Done!')
        st.write('**Article #1**')
        st.write('`Title: `', processed_article1.title)
        st.write('`URL: `', link1)
        st.write('`AI Generated Summary: `', processed_article1.summary)
        st.markdown('---')
        st.write('**Article #2**')
        st.write('`Title: `', processed_article2.title)
        st.write('`URL: `', link2)
        st.write('`AI Generated Summary: `', processed_article2.summary)
        st.markdown('---')
        st.write('**Article #3**')
        st.write('`Title: `', processed_article3.title)
        st.write('`URL: `', link3)
        st.write('`AI Summary: `', processed_article3.summary)
        st.markdown('---')

        st.write('**Related Generated Articles**')
        for i in other_links:
            st.markdown(f'- {i}')