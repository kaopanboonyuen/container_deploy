
import streamlit as st
import pandas as pd
import numpy as np
import pickle

from code import Packer, Container, Box


st.header(
    'KMUTNB (Master Thesis 2/2021)'
)

st.subheader(
    'Author: Fon'
)

# st.subheader(
#     'Guideline'
# )

# st.write(
#     """
#     In the bin packing problem, items of different volumes must be packed into a finite number of bins or containers each of a fixed given volume in a way that minimizes the number of bins used.
#     """
# )

st.subheader(
    'To use the application, please following below steps:'
)

st.write(
    """
    1. To input box conditions that needed to be calculated. \n
    2. See the results below.
    """
)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)


# Create sidebar
st.sidebar.header(
    'Input Box Condition'
)

GenderVar = st.sidebar.selectbox(
    'Sorting by Size', ['Yes','No']
)

width = st.sidebar.slider(
    'Size of Container (Width)',
    1, 10000, step = 1
)

height = st.sidebar.slider(
    'Size of Container (Height)',
    1, 10000, step = 1
)

depth = st.sidebar.slider(
    'Size of Container (Depth)',
    1, 10000, step = 1
)

max_weight = st.sidebar.slider(
    'Size of Container (Max Weight)',
    1, 10000, step = 1
)


st.sidebar.text_input(
            label = 'Please type your box1 information',
            value= 'e.g., 50g Box 1, 50, 50, 50, 50',
            key= 'question'
        )

# st.sidebar.text_input(
#             label = 'Please type your box2 information',
#             value= 'e.g., 100g Box 2, 100, 100, 100, 100',
#             key= 'question'
#         )

# st.sidebar.text_input(
#             label = 'Please type your box3 information',
#             value= 'e.g., 200g Box 3, 200, 200, 200, 200',
#             key= 'question'
#         )


#Step1
NewPacker = Packer()

#Step2 add Container        # name, width, height, depth, max_weight
NewPacker.add_bin(Container('Container1', 1000, 1000, 1000, 700.0))

#Step3 add Box
#                       # name, width, height, depth, weight
NewPacker.add_item(Box('50g [Box 1]', 50, 50, 50, 50)) 
NewPacker.add_item(Box('100g [Box 2]', 100, 100, 100, 100))
NewPacker.add_item(Box('200g [Box 3]', 200, 200, 200, 200))

NewPacker.add_item(Box('150g [Box 4]', 150, 150, 150, 150)) 
NewPacker.add_item(Box('300g [Box 5]', 300, 300, 300, 300))
NewPacker.add_item(Box('350g [Box 6]', 350, 350, 350, 350)) 



NewPacker.pack(sorting_by_size=True)

for b in NewPacker.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")

    st.write("FITTED ITEMS:")

    for item in b.items:
        print("====> ", item.string())
        st.write("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")

