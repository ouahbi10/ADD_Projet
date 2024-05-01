import streamlit as st
import pandas as pd
from CAH.CAH import agglomerative_clustering,read_csv
from scipy.cluster.hierarchy import dendrogram as sci_dendrogram , linkage
from io import StringIO
from matplotlib import pyplot as plt

def draw_dendogram(df):
    # Assuming that your custom dendogram function returns a linkage matrix
    X=df.values
    linkage_matrix = linkage(X, method='ward')
    fig, ax = plt.subplots()  # Create a new figure and axes
    sci_dendrogram(linkage_matrix, ax=ax)  # Plot the dendrogram using scipy's dendrogram function
    st.pyplot(fig) 


st.title("Hierarchy Clustering")

uploaded_file = st.file_uploader("Upload Your Dataset:")

if uploaded_file is not None:
    # Convert binary file to text stream for CSV reading
    file_content = uploaded_file.getvalue().decode("utf-8")
    if not file_content.strip():  # Check if the file content is empty
        st.error("Uploaded file is empty. Please upload a valid CSV file with data.")
    else:
        toclustering = read_csv(uploaded_file)
        df = pd.read_csv(StringIO(file_content),encoding='unicode_escape')
        if df.empty:
            st.error("No valid data found to parse.")
        else:
            st.write(df)
            n_cluster = st.slider("Number Of Clusters :", min_value=1, max_value=10)
            if st.button('Process Data'):
                result = agglomerative_clustering(toclustering, n_cluster)
                for i,item in enumerate(result,1):
                    st.write(f"Cluster : {i} ")
                    for j,point in enumerate(item,1):
                        st.write(f"point {j} : {point[0]} | {point[1]}")
                draw_dendogram(df)
else:
    st.error("Please upload a file. (Only CSV Files)")



