import streamlit as st
import pandas as pd
from io import StringIO
from kmeans.Kmeans import k_means,assign_data
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def display_clusters(labeled):
    clusters = []
    for centroid, points in labeled.items():
        cluster = {'centroid': centroid, 'points': points}
        clusters.append(cluster)
    return clusters


def display_clusters_as_table(labeled):
    for centroid, points in labeled.items():
        st.write(f"**Centroid: ({', '.join(map(str, centroid))})**")
        df = pd.DataFrame(points, columns=['x', 'y'])  # Adjust columns based on your data dimensions
        st.table(df)


def KmeansDiagram(df, num_clusters):
    km = KMeans(n_clusters=num_clusters)
    y_predicted = km.fit_predict(df[['X', 'Y']])
    df['cluster'] = y_predicted

    fig, ax = plt.subplots()  # Create a figure and axis object
    df1 = df[df.cluster == 0]
    df2 = df[df.cluster == 1]
    df3 = df[df.cluster == 2]
    df4 = df[df.cluster == 3]
    df5 = df[df.cluster == 4]
    df6 = df[df.cluster == 5]
    df7 = df[df.cluster == 6]
    df8 = df[df.cluster == 7]
    df9 = df[df.cluster == 8]
    df10 = df[df.cluster == 9]

    ax.scatter(df1.X, df1['Y'], color="green")
    ax.scatter(df2.X, df2['Y'], color="blue")
    ax.scatter(df3.X, df3['Y'], color="red")
    ax.scatter(df4.X, df4['Y'], color="black")
    ax.scatter(df5.X, df5['Y'], color="yellow")
    ax.scatter(df6.X, df6['Y'], color="purple")
    ax.scatter(df7.X, df7['Y'], color="orange")
    ax.scatter(df8.X, df8['Y'], color="pink")
    ax.scatter(df9.X, df9['Y'], color="gray")
    ax.scatter(df10.X, df10['Y'], color="cyan")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

    st.pyplot(fig)  # Pass the figure object directly



st.title("K-means Clustering")

uploaded_file = st.file_uploader(label="Upload Your Dataset :")

if uploaded_file is not None:
    file_content = uploaded_file.getvalue().decode("utf-8")
    if not file_content.strip():
        st.error("Uploaded file is empty. Please upload a valid CSV file with data.")
    else:
        df = pd.read_csv(StringIO(file_content))
        if df.empty:
            st.error("No valid data found to parse.")
        else:
            st.write(df)
            # Ensure the maximum number of clusters does not exceed the number of rows
            max_clusters = min(len(df), 10)
            n_cluster = st.slider("Number Of Clusters :", min_value=1, max_value=max_clusters)

            if st.button('Process Data'):
                data_for_clustering = df.values.tolist()  # Convert DataFrame to list of lists
                result = k_means(data_for_clustering, n_cluster)
                
                labeled = assign_data(centroids=result, data=data_for_clustering)
                cluster_data = display_clusters(labeled)
                display_clusters_as_table(labeled)
                KmeansDiagram(df=df,num_clusters=n_cluster)
else:
    st.error("Please upload a file.(Only CSV Files)")
