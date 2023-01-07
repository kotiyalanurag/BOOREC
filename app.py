import numpy as np
import pickle
import streamlit as st

with open('popular_books.pkl', 'rb') as popular_books:
    popular_book = pickle.load(popular_books)

with open('book_matrice.pkl', 'rb') as book_matrice:
    book_matrix = pickle.load(book_matrice)

with open('book_ratings.pkl', 'rb') as book_ratings:
    book_rating = pickle.load(book_ratings)

with open('similarity_scores.pkl', 'rb') as similarity_scores:
    similarity_score = pickle.load(similarity_scores)

header = st.container()
popular = st.container()
recommendation = st.container()

with header:
    st.markdown("<h1 style='text-align: center; color: teal;'>BOOREC</h1>", unsafe_allow_html=True)
    st.write('''
    Are you someone that likes to read a book but can't make up your mind as to what
    you should read next. Look no further! BOOREC will help you decide your next book.
    ''')

st.sidebar.header('What would you like to do with BOOREC?')
n = st.sidebar.number_input("Choose 'n' to see the most popular 'n' books ", 2, 10, 3)

n_popular_books = popular_book.head(n)
n_popular_books_title = n_popular_books['Book-Title'].tolist()

with popular:
    st.markdown("<h3 style='text-align: center; color: teal;'>Most Popular Books Right Now!</h3>", unsafe_allow_html=True)
    #st.write(str(n) + ' most popular books right now')

    for title in n_popular_books_title:
        st.markdown("- " + title)

book_title = popular_book['Book-Title'].tolist()

user_choice = st.sidebar.selectbox('Choose a book that you like', book_title)
st.sidebar.write('You chose the book - ' + str(user_choice))

def recommend_books(book_rating, book_name):
    
    if book_rating['Book-Title'].str.contains(book_name).any() == False:
        return -1
    
    index = np.where(book_matrix.index == book_name)[0][0]
    similar_books = list(enumerate(similarity_score[index]))
    similar_books = sorted(similar_books, key = lambda x:x[1], reverse = True)[1:6]
    
    recommended_books = []
    for i in similar_books:
        
        data = book_rating[book_rating['Book-Title'] == book_matrix.index[i[0]]]
        recommended_books.extend(list(data.drop_duplicates('Book-Title')['Book-Title'].values))
        
    return recommended_books



with recommendation:    
    title = user_choice
    book_recommend = recommend_books(book_rating, title)

    if book_recommend == -1:
        st.markdown("<h3 style='text-align: center; color: teal;'>Here are some recommendations for you!</h3>", unsafe_allow_html=True)
        st.write('Sorry, no recommendations were found for your favourite book. Please try choosing another book.')
    else:
        st.markdown("<h3 style='text-align: center; color: teal;'>Here are some recommendations for you!</h3>", unsafe_allow_html=True)
        for book in book_recommend:
            st.markdown("- " + book)           