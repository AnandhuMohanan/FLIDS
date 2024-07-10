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

# Function to get numerical inputs
def get_numeric_inputs():
    numeric_features = {}
    numeric_features['connections_to_same_dest_host'] = int(input("Enter number of connections to the same destination host in the past two seconds: "))
    numeric_features['diff_services_percentage'] = float(input("Enter the percentage of connections to different services among the connections aggregated in dst_host_count: "))
    numeric_features['same_src_port_percentage'] = float(input("Enter the percentage of connections to the same source port among the connections aggregated in dst_host_srv_count: "))
    numeric_features['same_dest_port_percentage'] = float(input("Enter the percentage of connections to the same service among the connections aggregated in dst_host_count: "))
    numeric_features['last_flag'] = int(input("Enter last flag value: "))
    numeric_features['s0_s1_s2_s3_percentage'] = float(input("Enter the percentage of connections that have activated flags (4) s0, s1, s2, or s3 among the connections aggregated in count: "))
    return numeric_features

# Function to get categorical inputs
def get_categorical_inputs():
    http_service_used = input("Was HTTP service used (Yes/No): ").capitalize()
    successfully_logged_in = int(input("Was login successful (1 for Yes, 0 for No): "))
    return http_service_used, successfully_logged_in

# Main function
def main():
    print("Enter numerical features:")
    numeric_features = get_numeric_inputs()
    print("\nEnter categorical features:")
    http_service_used, successfully_logged_in = get_categorical_inputs()

    # Predict the type of attack
    predicted_attack = predict_attack(numeric_features, http_service_used, successfully_logged_in)
    print("\nPredicted Attack Type:", predicted_attack)

if __name__ == "__main__":
    main()
