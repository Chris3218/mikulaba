import streamlit as st
import base64


# Funktion zum Abspielen von Audio
def play_audio(audio_file, loop=False):
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
        b64 = base64.b64encode(audio_bytes).decode()
        loop_attr = "loop" if loop else ""
        audio_html = f"""
        <audio autoplay {loop_attr}>
            <source src="data:audio/wav;base64,{b64}" type="audio/wav">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)


# Sidebar for configurable colors
bg_color = "#2C3E50"
btn_bg_color = "#BDC3C7"
btn_text_color = "#23303D"
btn_hover_color = "#AAB7B8"

# Custom CSS for dynamic color application
st.markdown(
    f"""
    <style>
    body, .stApp {{
        background-color: {bg_color}; /* Background color from the sidebar */
    }}
    .row {{
        display: flex;
        flex-direction: column; /* Buttons in einer Spalte anordnen */
        justify-content: center; /* Buttons zentrieren */
        align-items: center; /* Buttons horizontal zentrieren */
        gap: 5mm; /* Abstand zwischen den Buttons */
    }}
    .stButton {{
        display: flex;
        justify-content: center;
        width: 100% !important; /* Ensure button fills container width */
    }}
    .stButton button {{
        width: 344px;
        height: 20mm;
        font-size: 46px;
        border-radius: 6px;
        background: {btn_bg_color}; /* Button background from the sidebar */
        color: {btn_text_color}; /* Button text color from the sidebar */
        box-shadow: inset 1px 1px 1px #101010, inset -1px -1px 2px #292929;
        transition: all 0.15s ease-in-out;
    }}
    .stButton button:hover {{
        background: {btn_hover_color}; /* Button hover color from the sidebar */
        color: white;
        transform: scale(1.05);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    "<h1 style='text-align: center; color: white;'>🔊 The Laber Machine</h1>",
    unsafe_allow_html=True,
)

# Exact centering of the buttons
st.markdown("<div class='button-container'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Anta"):
        play_audio("audio/wanta.wav", loop=True)
with col2:
    if st.button("Dumm"):
        play_audio("audio/how.wav", loop=True)

col3, col4 = st.columns(2)
with col3:
    if st.button("Wanta"):
        play_audio("audio/herr_zafi.wav", loop=True)
with col4:
    if st.button("What"):
        play_audio("audio/what_labersch.wav", loop=True)

st.markdown("</div>", unsafe_allow_html=True)
