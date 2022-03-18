#import streamlit as st
#st.set_page_config(page_title="Cyberbully Detection Demo Website", page_icon=":tada:", layout="wide")

#HEADER
#st.subheader("Trial for making website")
#st.title("title trial")
#st.write("writing trial")


import streamlit as st
import tensorflow as tf
#import pip
#import selenium
#from tensorflow import keras


st.set_page_config(page_title="Cyberbully Detection Demo Website", page_icon=":tada:", layout="wide")

#HEADER
st.subheader("Trial for making website")
st.title("title trial")
st.write("writing trial")

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
	st.title("Trial for making website")

title = st.text_input('Reply to', 'your txt')
st.write('You replied', title)



#!pip install tweet-preprocessor
#!pip install contractions

#!pip install gensim
model = keras.models.load_model('model.h5')

