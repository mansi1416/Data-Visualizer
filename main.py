import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # Important Library.

st.set_page_config(page_title="Data Visualizer Tool", layout="centered", page_icon="📊")
st.title("📊 Data Visualizer")

# Use st.file_uploader to upload files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display a preview of the data
    st.write("Preview of the data:")
    st.write(df.head(5))
    
    columns = df.columns.tolist()

    # Column layout
    col1, col2 = st.columns(2)
    with col1:
        st.write("Preview of the data:")
        st.write(df.head(5))
    
    with col2:
        # Select X and Y axis for plotting
        x_axis = st.selectbox("Select X axis", options=columns + ["None"], index=None)
        y_axis = st.selectbox("Select Y axis", options=columns + ["None"], index=None)
        
        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]
        selected_plot = st.selectbox("Select a plot type", options=plot_list, index=None)
        
        st.write(f"X-axis: {x_axis}")
        st.write(f"Y-axis: {y_axis}")
        st.write(f"Selected plot: {selected_plot}")
    
    if st.button(label="Generate A plot"):
        if selected_plot == "Line Plot" and x_axis != "None" and y_axis != "None":
            st.write("Generating Line Plot...")
            plt.figure(figsize=(10, 6))
            sns.lineplot(data=df, x=x_axis, y=y_axis)
            st.pyplot(plt)

        elif selected_plot == "Bar Chart" and x_axis != "None" and y_axis != "None":
            st.write("Generating Bar Chart...")
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x=x_axis, y=y_axis)
            st.pyplot(plt)

        elif selected_plot == "Scatter Plot" and x_axis != "None" and y_axis != "None":
            st.write("Generating Scatter Plot...")
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df, x=x_axis, y=y_axis)
            st.pyplot(plt)

        elif selected_plot == "Distribution Plot" and x_axis != "None":
            st.write("Generating Distribution Plot...")
            plt.figure(figsize=(10, 6))
            sns.histplot(df[x_axis], kde=True)
            st.pyplot(plt)

        elif selected_plot == "Count Plot" and x_axis != "None":
            st.write("Generating Count Plot...")
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=x_axis)
            st.pyplot(plt)
