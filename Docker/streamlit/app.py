import os
import streamlit as st
from pyperclip import copy

def main():
    st.title('Spotify Downloader')
    uri = st.text_input('Enter Spotify URI:')
    if st.button('Search'):
        st.markdown('**Searching...**')
        search = f"spotdl {uri}" + \
            " --path-template 'Music/{artist}/{album}/{title}.{ext}'"
        copy(search)


        # os.system(search)
        # st.success('**Downloaded!**')


if __name__ == '__main__':
    main()
