import streamlit as st
import pandas as pd
import pickle
# import requests
st.markdown(f""" 
<style>
.stApp
{{
background-image:
url('https://64.media.tumblr.com/1a1daa90b7dccddba3abbeb6d3a2e179/60d55a5453fa3d0c-81/s2048x3072/704facf96ca4a40c7785357e52d040a5bdfe0c3c.jpg');
background-size:100%;
color:white;
font-size:15px;
background-color: rgb(93 17 17);
font-weight:bolder;
}}
#box
{{          height:250px;
            background-image:
            url('_img2.jpeg');
            color:white;
            background-size:100%;
            color:white;
}}
</style>
""",
            unsafe_allow_html=True)

similaritymatrix=pickle.load(open("similaritymatrix.pkl","rb"))
data=pickle.load(open("song_csv.pkl","rb"))
st.title("HarmoniSync - Personalized Song Recommendations")



def recomendation(song):
    song_ID=data[data["SongName"]==song].index[0]  # returns song ID  in dataframe 
    distance=similaritymatrix[song_ID]
    song_list=sorted(list(enumerate(distance)) ,reverse=True,key=lambda x:x[1])[1:6]
    song_name=[]
    artist_name=[]
    for A in song_list:
        # print("song Name:",data.iloc[A[0]].SongName,"Artsit name:", data.iloc[A[0]].ArtistName)
        song_name.append(data.iloc[A[0]].SongName)
        artist_name.append(data.iloc[A[0]].ArtistName)
    return song_name,artist_name
    


option = st.selectbox(
        "select song ",
        (data["SongName"]))
st.write('You selected:', option)
if st.button("Recommend"):

    song_name,Artist=recomendation(option)
    col1, col2, col3, col4  = st.columns(4)
    with col1:
        st. write('''<div id="box">
                  <h3>{0}</h3>
                  <br>
                  <h3>{1}</h3>
                  </div>'''
                  .format("\""+song_name[0]+"\"", Artist[0]),
                 unsafe_allow_html=True)
    with col2:  
        st. write('''<div id ="box">
                  <h3>{0}</h3>
                  <br>
                  <h3>{1}</h3>
                  </div>'''
                  .format("\""+song_name[1]+"\"", Artist[1]),
                 unsafe_allow_html=True)
    with col3:
        st. write('''<div id="box">
                  <h3>{0}</h3>
                  <br>
                  <h3>{1}</h3>
                  </div>'''
                  .format("\""+song_name[2]+"\"", Artist[2]),
                 unsafe_allow_html=True)
    with col4:
        st. write('''<div id="box">
                  <h3>{0}</h3>
                  <br>
                  <h3>{1}</h3>
                  </div>'''
                  .format("\""+song_name[3]+"\"", Artist[3]),
                 unsafe_allow_html=True)
        