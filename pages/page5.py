from navigation import make_sidebar
import streamlit as st
from time import sleep

make_sidebar()

st.markdown("# Logs and Reports")

# Define the slow_text function
def slow_text(text, delay=1):
    st.text(text)
    sleep(delay)

# Display setup messages
slow_text(" ")
slow_text("Available execution logs are of:\n")
slow_text("Please click one to view!")

def display_message(message):
    st.write(message)

# Creating buttons
button1 = st.button("SERVER LOG")
button2 = st.button("CLIENT 1 LOG")
button3 = st.button("CLIENT 2 LOG")
button4 = st.button("CLIENT 3 LOG")

# Checking if buttons are clicked
if button1:
    display_message(""" Starting Flower server, config: num_rounds=5, no round_timeout
        Flower ECE: gRPC server running (5 rounds), SSL is disabled
        [INIT]
        Requesting initial parameters from one random client
        Received initial parameters from one random client
        Evaluating initial global parameters
  
        [ROUND 1]
        configure_fit: strategy sampled 3 clients (out of 3)
        aggregate_fit: received 3 results and 0 failures
        configure_evaluate: strategy sampled 3 clients (out of 3)
        aggregate_evaluate: received 3 results and 0 failures
  
        [ROUND 2]
        configure_fit: strategy sampled 3 clients (out of 3)
        aggregate_fit: received 3 results and 0 failures
        configure_evaluate: strategy sampled 3 clients (out of 3)
        aggregate_evaluate: received 3 results and 0 failures
  
        [ROUND 3]
        configure_fit: strategy sampled 3 clients (out of 3)
        aggregate_fit: received 3 results and 0 failures
        configure_evaluate: strategy sampled 3 clients (out of 3)
        aggregate_evaluate: received 3 results and 0 failures
  
        [ROUND 4]
        configure_fit: strategy sampled 3 clients (out of 3)
        aggregate_fit: received 3 results and 0 failures
        configure_evaluate: strategy sampled 3 clients (out of 3)
        aggregate_evaluate: received 3 results and 0 failures
  
        [ROUND 5]
        configure_fit: strategy sampled 3 clients (out of 3)
        aggregate_fit: received 3 results and 0 failures
        configure_evaluate: strategy sampled 3 clients (out of 3)
        aggregate_evaluate: received 3 results and 0 failures
  
        [SUMMARY]
        
        History (loss, distributed):
           ('round 1: 1.0768674612045288'
            'round 2: 0.4758925139904022'
            'round 3: 0.4465745687484741'
            'round 4: 0.4131815731525421'
            'round 5: 0.45606303215026855')History (metrics, distributed, fit):
           {'binary_accuracy': [(1, 0.9177184303601583),
                                (2, 0.9312178293863932),
                                (3, 0.9336150685946146),
                                (4, 0.9348013202349345),
                                (5, 0.9353773395220438)],
            'loss': [(1, 0.20411745210488638),
                     (2, 0.17187572022279105),
                     (3, 0.1600524882475535),
                     (4, 0.15115996698538461),
                     (5, 0.14681994915008545)]}History (metrics, distributed, evaluate):
           {'accuracy': [(1, 0.7211169600486755),
                         (2, 0.7247607111930847),
                         (3, 0.7995675802230835),
                         (4, 0.7695185542106628),
                         (5, 0.7701622843742371)]}""")
if button2:
    display_message("""CLIENT 1 LOG:

[RUN 0, ROUND ]
Received: get_parameters message a0375279-f196-41d2-af93-04ca7093abf2
Sent reply

[RUN 0, ROUND ]
Received: train message 3387dc3f-0a13-4440-95ad-8a1b75ff0efc
2740/2740 ━━━━━━━━━━━━━━━━━━━━ 16s 4ms/step - binary_accuracy: 0.8761 - loss: 0.2896
Sent reply

[RUN 0, ROUND ]
Received: evaluate message f3684734-2cf1-4e43-9961-a8638cfc5933
2573/2573 ━━━━━━━━━━━━━━━━━━━━ 7s 3ms/step - binary_accuracy: 0.9362 - loss: 0.2633
Sent reply

[RUN 0, ROUND ]
Received: train message 07c3883e-5bde-4795-91bf-928f9d965eb8
2740/2740 ━━━━━━━━━━━━━━━━━━━━ 11s 4ms/step - binary_accuracy: 0.9312 - loss: 0.1768
Sent reply

[RUN 0, ROUND ]
Received: evaluate message 8d03936e-0353-4757-bdfc-632b6750d4bc
2573/2573 ━━━━━━━━━━━━━━━━━━━━ 7s 3ms/step - binary_accuracy: 0.9383 - loss: 0.2388
Sent reply

[RUN 0, ROUND ]
Received: train message 31401c23-fb4b-46ff-b0fc-77808e9ef0f3
2740/2740 ━━━━━━━━━━━━━━━━━━━━ 12s 4ms/step - binary_accuracy: 0.9256 - loss: 0.2049
Sent reply

[RUN 0, ROUND ]
Received: evaluate message 731ecf67-16fc-4e51-bf64-3d09133b1fd4
2573/2573 ━━━━━━━━━━━━━━━━━━━━ 7s 3ms/step - binary_accuracy: 0.9351 - loss: 0.2489
Sent reply""")
if button3:
    display_message("""CLIENT 2 LOG:
    [RUN 0, ROUND ]
Received: get_parameters message 01e5aaef-4ad3-47b5-84d5-3d80fe27c694
Sent reply

[RUN 0, ROUND ]
Received: train message c3fd49b1-d3c7-4bbd-a1eb-4393be468b70
2785/2785 ━━━━━━━━━━━━━━━━━━━━ 13s 5ms/step - binary_accuracy: 0.8777 - loss: 0.2896
Sent reply

[RUN 0, ROUND ]
Received: evaluate message 98117f8a-7e6b-4d79-84b7-8e7c0346070b
2785/2785 ━━━━━━━━━━━━━━━━━━━━ 8s 3ms/step - binary_accuracy: 0.9347 - loss: 0.2633
Sent reply

[RUN 0, ROUND ]
Received: train message 40d6ad2f-bc48-4cb3-b792-e68ebd9401cd
2785/2785 ━━━━━━━━━━━━━━━━━━━━ 13s 5ms/step - binary_accuracy: 0.9327 - loss: 0.1768
Sent reply

[RUN 0, ROUND ]
Received: evaluate message 44362895-42d3-4fa6-85c7-4cb1c5bde4c3
2785/2785 ━━━━━━━━━━━━━━━━━━━━ 8s 3ms/step - binary_accuracy: 0.9377 - loss: 0.2388
Sent reply

[RUN 0, ROUND ]
Received: train message 9f28739b-7993-49c1-b6fc-f193882f6181
2785/2785 ━━━━━━━━━━━━━━━━━━━━ 13s 5ms/step - binary_accuracy: 0.9274 - loss: 0.2049
Sent reply

[RUN 0, ROUND ]
Received: evaluate message 441ae514-8a6e-4f2f-a83b-d4d6b40c5d18
2785/2785 ━━━━━━━━━━━━━━━━━━━━ 8s 3ms/step - binary_accuracy: 0.9356 - loss: 0.2489
Sent reply

""")
if button4:
    display_message("""CLIENT 3 LOG:
    [RUN 0, ROUND ]
Received: get_parameters message 009bb50d-6822-4c31-8c7b-6f12ba56b88b
Sent reply

[RUN 0, ROUND ]
Received: train message 4c8719b8-77fd-4a4c-818d-5ef84ee21d4a
2696/2696 ━━━━━━━━━━━━━━━━━━━━ 13s 5ms/step - binary_accuracy: 0.8820 - loss: 0.2896
Sent reply

[RUN 0, ROUND ]
Received: evaluate message d9e3b72c-7b80-4055-9de2-f7cc268b7f47
2696/2696 ━━━━━━━━━━━━━━━━━━━━ 7s 3ms/step - binary_accuracy: 0.9352 - loss: 0.2633
Sent reply

[RUN 0, ROUND ]
Received: train message ebbbf95c-e183-43f4-8031-d5269bc2a9e1
2696/2696 ━━━━━━━━━━━━━━━━━━━━ 12s 5ms/step - binary_accuracy: 0.9320 - loss: 0.1768
Sent reply

[RUN 0, ROUND ]
Received: evaluate message 024b3e8a-bd6e-4d99-88fc-f0c3b4d75e95
2696/2696 ━━━━━━━━━━━━━━━━━━━━ 7s 3ms/step - binary_accuracy: 0.9378 - loss: 0.2388
Sent reply

[RUN 0, ROUND ]
Received: train message 57cfb170-e1ab-4ecb-aa4e-6e0c8d589ace
2696/2696 ━━━━━━━━━""")
