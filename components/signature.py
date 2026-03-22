import streamlit as st
from config import APP_AUTHOR, APP_ROLE, APP_INSTITUTION


def render() -> None:
    st.markdown(f"""
    <hr>
    <div style="text-align:center; font-size:0.82em; line-height:2; color:#666; padding-bottom:0.5rem;">
        <span style="color:#00BFFF; font-weight:600; font-size:1em;">🛠️ {APP_AUTHOR}</span><br>
        <span style="color:#888;">{APP_ROLE}</span><br>
        <span style="color:#555;">{APP_INSTITUTION}</span><br>
        <span style="font-size:0.95em; display:block; margin-top:2px;">
            <span style="color:#50fa7b;">Python</span> &bull;
            <span style="color:#ff79c6;">Streamlit</span> &bull;
            <span style="color:#f1fa8c;">Google Sheets</span> &bull;
            <span style="color:#8be9fd;">Pandas</span> &bull;
            <span style="color:#bd93f9;">Plotly</span>
        </span>
    </div>
    """, unsafe_allow_html=True)
