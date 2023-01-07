# BOOREC

Are you someone that loves to read books but is always confused about what you should be reading next. Well, look no further! BOOREC is a book recommendation 
system that is capable of displaying the top 'n' most popular books at the time - based on user input. And it can also make recommendations to 
a user based on the user input for future readings, based on similarity scores between different books and the favourite book of a user. 

![books](https://images.unsplash.com/photo-1618365908648-e71bd5716cba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80)

## Overview

The books are recommended on the basis of their similarity scores with the book that is taken as a user input in the beginning. The books with the highest
similarity scores to the user input, are then displayed on the screen.

## What does similarity score mean?

It is a numerical value that ranges between zero and one, which helps us to determine how much two given items are similar to one another on a scale of zero 
to one. This similarity score is simply a measure of similarity between text details of given two items. We can compute this score by calculating the
cosine-similarity between any two items.

## How does cosine-similarity work?

Cosine similarity is a metric used to measure how similar the items are irrespective of their size. Mathematically, it measures the cosine of the angle 
between two vectors projected in a multi-dimensional space. It is advantageous because even if the two similar items are far apart by the Euclidean distance 
(due to the size of the items), chances are they may still be oriented closer together. The smaller the angle is, higher the cosine similarity will be (since 
cosine function ranges from 1 to -1 between 0 to 180 degrees).

![cosine](https://www.oreilly.com/api/v2/epubs/9781788295758/files/assets/2b4a7a82-ad4c-4b2a-b808-e423a334de6f.png)

## How to get started?

Open the terminal on your mac and type 
```html
mkdir BOOREC
```
Then switch to the new directory using
```html
cd BOOREC
```
Now clone the repository on your local machine using
```html
git clone https://github.com/kotiyalanurag/BOOREC.git
```
You can just pip install the packages using terminal
```html
pip install 'package-name'
```
Or install them directly in the notebook by using
```html
! pip install 'package-name'
```
You can now have fun running the notebook and seeing the results for yourself.

To run the streamlit app use
```html
streamlit run app.py
```

Check out the streamlit app [here.](https://kotiyalanurag-boorec-app-il6jfq.streamlit.app/)
