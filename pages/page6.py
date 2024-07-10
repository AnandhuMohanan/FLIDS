from navigation import make_sidebar
import streamlit as st
import os

make_sidebar()

st.markdown("# Data Visualization")

# Display the plot image
st.image("plot.png")

# Display the text
st.markdown("""
### X-axis:
Represents the rounds of training. Each round corresponds to a specific iteration or epoch during the training process.

### Y-axis (left):
Represents the values of the metric we're interested in. In this case, we're plotting the binary accuracy, which measures the accuracy of the model's predictions on a binary classification task.

### Y-axis (right):
Represents the loss values. The loss function is a measure of how well the model's predictions match the actual target values. Lower loss values indicate better performance.
""")
