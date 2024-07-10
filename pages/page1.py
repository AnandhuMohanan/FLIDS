from navigation import make_sidebar
import streamlit as st

make_sidebar()

# Model descriptions
model_descriptions = {
    "RNN": "Recurrent Neural Network (RNN) is a type of neural network that is specialized for sequence data. It is commonly used in network intrusion detection to analyze time-series data such as network traffic logs and detect anomalies or attacks.",
    "CNN": "Convolutional Neural Network (CNN) is a type of neural network that is commonly used for image recognition tasks. In the context of network intrusion detection, CNNs can be applied to analyze network packet headers or images of network traffic to identify patterns indicative of attacks.",
    "DNN": "Deep Neural Network (DNN) is a type of neural network that consists of multiple layers, often used for various tasks including classification and regression. In network intrusion detection, DNNs can be applied to analyze network traffic features extracted from packet payloads or other network data to classify normal and malicious activities."
}

# Main page content
st.title("Model Selection")
st.write("Please select one model from the following options:")
st.write("Note: Training procedures will be executed based upon the datasets provided.")


# Display model descriptions with radio button for selection
selected_model = st.radio("Select Model", ("RNN", "CNN", "DNN"))

# Display model description based on selected model
st.subheader(selected_model)
st.write(model_descriptions[selected_model])

# Save button
if st.button("Save", type="primary"):
    st.success("Model saved successfully!")
    st.write("Proceed to Data Input.")

else:
    st.error("Please select a model")
