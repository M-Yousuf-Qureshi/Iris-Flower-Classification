import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Colab App", page_icon="🚀")

st.title("🚀 Custom My App")

# 1. Simple User Input
name = st.text_input("Enter your name:", "M.Yousaf")

if name:
    st.write(f"### Welcome, {name}!")

# 2. Data Table (Tunnels handle these well)
st.subheader("Sample Data Display")
df = pd.DataFrame({
    'Feature': ['Speed', 'Stability', 'Ease of Use'],
    'Score': [85, 70, 95]
})
st.table(df) # st.table is more stable than st.dataframe for weak tunnels

# 3. Simple Button Logic
if st.button("Click for a Surprise"):
    st.balloons()
    st.success("It works!")
st.title("Hello Streamlit!")
st.write("This is successfully running in Colab via LocalTunnel.")

st.title("My Interactive Data App")

# Add a slider
number = st.slider("Select a range", 0, 100, 50)
st.write(f"The current number is {number}")

# Add a simple chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)
