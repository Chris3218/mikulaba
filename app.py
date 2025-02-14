import streamlit as st
from bson import ObjectId
import datetime

st.title("🔍 BSON ObjectId → Lesbares Datum")

# Eingabefeld für die ObjectId
object_id_input = st.text_input("Gib eine BSON ObjectId ein:")

if object_id_input:
    try:
        # ObjectId umwandeln
        obj_id = ObjectId(object_id_input)
        timestamp = obj_id.generation_time  # UTC-Zeit

        # Formatierte Ausgabe
        readable_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        st.success(f"📅 Erstellungszeit: **{readable_time} UTC**")

    except Exception as e:
        st.error("❌ Ungültige BSON ObjectId. Bitte gib eine gültige 24-stellige hexadezimale Zeichenkette ein.")
