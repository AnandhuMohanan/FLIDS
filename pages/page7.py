from navigation import make_sidebar
import streamlit as st
import os

make_sidebar()

st.markdown("# Intrusion Detection")
def predict_attack(numeric_features, http_service_used, successfully_logged_in):
    # Define threshold values for numeric features
    threshold_values = {
        'connections_to_same_dest_host': 10,
        'diff_services_percentage': 0.05,
        'same_src_port_percentage': 0.25,
        'same_dest_port_percentage': 0.1,
        'last_flag': 0,
        's0_s1_s2_s3_percentage': 0.5
    }

    # Check conditions based on threshold values and input features
    if (numeric_features['connections_to_same_dest_host'] > threshold_values['connections_to_same_dest_host'] and
            numeric_features['diff_services_percentage'] > threshold_values['diff_services_percentage']):
        return 'DoS Attack'
    elif (numeric_features['same_src_port_percentage'] > threshold_values['same_src_port_percentage'] and
            numeric_features['same_dest_port_percentage'] > threshold_values['same_dest_port_percentage']):
        return 'Port Scanning'
    elif numeric_features['last_flag'] < threshold_values['last_flag']:
        return 'Malware Infection'
    elif (http_service_used == 'No' and successfully_logged_in == 0):
        return 'Brute Force Attack'
    else:
        return 'Normal'

def main():
    
    
    connections_to_same_dest_host = st.number_input("Number of connections to the same destination host in the past two seconds", min_value=0)
    diff_services_percentage = st.number_input("Percentage of connections to different services among the connections aggregated in dst_host_count", min_value=0.0)
    same_src_port_percentage = st.number_input("Percentage of connections to the same source port among the connections aggregated in dst_host_srv_count", min_value=0.0)
    same_dest_port_percentage = st.number_input("Percentage of connections to the same service among the connections aggregated in dst_host_count", min_value=0.0)
    last_flag = st.number_input("Last flag value", value=0)
    s0_s1_s2_s3_percentage = st.number_input("Percentage of connections that have activated flags (4) s0, s1, s2, or s3 among the connections aggregated in count", min_value=0.0)

    st.subheader("Enter Categorical Features:")
    http_service_used = st.radio("Was HTTP service used?", ('Yes', 'No'))
    successfully_logged_in = st.radio("Was login successful?", ('Yes', 'No'))

    # Convert categorical features to numeric values
    http_service_used = 1 if http_service_used == 'Yes' else 0
    successfully_logged_in = 1 if successfully_logged_in == 'Yes' else 0

    # Predict the type of attack when button is clicked
    if st.button("Predict"):
        # Predict the type of attack
        numeric_features = {
            'connections_to_same_dest_host': connections_to_same_dest_host,
            'diff_services_percentage': diff_services_percentage,
            'same_src_port_percentage': same_src_port_percentage,
            'same_dest_port_percentage': same_dest_port_percentage,
            'last_flag': last_flag,
            's0_s1_s2_s3_percentage': s0_s1_s2_s3_percentage
        }
        predicted_attack = predict_attack(numeric_features, http_service_used, successfully_logged_in)

        st.subheader("Intrusion Type:")
        st.write(predicted_attack, font_size=30)

if __name__ == "__main__":
    main()
