# app.py

import streamlit as st
import pandas as pd
from dna_utils import clean_sequence, get_base_counts, gc_content

st.set_page_config(page_title="BioMirror", layout="centered")
st.title("🧬 BioMirror – DNA Visualizer & Analyzer")

st.markdown("Upload a DNA sequence file (.fasta or .txt) to analyze base composition, GC content, and visualize sequence metrics.")

uploaded = st.file_uploader("Upload DNA File", type=["fasta", "txt"])

if uploaded:
    raw_text = uploaded.read().decode("utf-8")
    if raw_text.startswith(">"):
        raw_text = ''.join(raw_text.split('\n')[1:])  # skip FASTA header
    
    sequence = clean_sequence(raw_text)

    st.subheader("🔍 DNA Summary")
    st.code(sequence[:100] + "...", language="text")  # show preview

    counts = get_base_counts(sequence)
    gc = gc_content(sequence)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Length", f"{len(sequence)} bp")
        st.metric("GC Content", f"{gc}%")
    with col2:
        st.metric("A-T Ratio", f"{counts['A']}/{counts['T']}")
        st.metric("G-C Ratio", f"{counts['G']}/{counts['C']}")

    st.subheader("📊 Base Composition")
    df = pd.DataFrame.from_dict(counts, orient='index', columns=['Count'])
    st.bar_chart(df)

else:
    st.info("Awaiting file upload...")

st.markdown("---")
st.caption("Developed by Farica | GitHub: Farica24")
