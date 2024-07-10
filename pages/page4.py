from navigation import make_sidebar
import streamlit as st
from time import sleep

make_sidebar()

# Define the slow_text function
def slow_text(text, delay=1):
    st.text(text)
    sleep(delay)

# Display headings with bigger font size
st.markdown("# Performance Metrics", unsafe_allow_html=True)

# Display setup messages
slow_text(" ")
slow_text("Evaluating performance metrics...")
slow_text("Available metrics after 5 federated learning rounds are:")
slow_text("Binary Accuracy")
slow_text("Loss")
slow_text("Model Accuracy")

# Define the performance metrics
performance_metrics = {
    'LOSS': [(1, 0.203), (2, 0.167), (3, 0.160), (4, 0.153), (5, 0.149)],
    'BINARY ACCURACY': [(1, 0.918), (2, 0.932), (3, 0.933), (4, 0.935), (5, 0.935)],
    'MODEL ACCURACY': [(1, 0.810), (2, 0.703), (3, 0.768), (4, 0.839), (5, 0.816)]
}

# Function to display metrics
def display_metrics(metrics):
    for metric, values in metrics.items():
        st.write(f"'{metric}':")
        for round_num, value in values:
            st.write(f"  Round {round_num}: {value}")

# Button to generate output metrics
if st.button("Generate the output Metrics"):
    display_metrics(performance_metrics)
