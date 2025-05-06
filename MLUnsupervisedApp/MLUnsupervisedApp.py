###########################################################
# 
# Unsupervised Machine Learning Streamlit App
#
###########################################################

#---------------------------------------------------
# Libraries for Data Processing and Visualization
#---------------------------------------------------
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------
# Machine Learning Libraries
#-----------------------------------
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler

####################################
# Title and Instructions
####################################
st.set_page_config(layout="wide")  
st.title("🧠 Interactive Unsupervised Machine Learning App!")  # Add title to streamlit app.

# st.markdown creates text boxes that will appear in the app's dashboard. 
st.markdown("""  
## About This Application:
In this interactive machine learning app, you will explore your dataset in a cool new way using unsupervised learning models! Upload any data set you'd like and experiement with different hyperparameters. Observe how these affect model training and outcomes. This app includes Principal Component Analysis, KMeans Clustering, and Hierarchical Clustering!
            
            Instructions: 
    1. Upload any dataset in CSV format using the sidebar menu or use the Palmers Penguins dataset!
    2. Choose a model (KMeans Clustering, PCA, or Hierarchical Clustering).
    3. Adjust Hyperparameters. 
    4. Explore your model!
""") 

##############################
# Dataset Selection:
###############################
st.info("Let's start to explore!") # st.info creates a highlighted textbox

st.sidebar.header("Upload Dataset or Use Sample")  # Sidebar menu title
data_source = st.sidebar.radio("Choose Data Source", ["Upload your own", "Use Palmers Penguins Dataset"]) # Opens options for dataset upload. 

if data_source == "Upload your own":  # If user chooses to upload their own dataset.
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.warning("Please upload a CSV file.")
        st.stop()
else:  # If user does not upload dataset, they can choose to use Palmers Penguins dataset. 
    df = sns.load_dataset("penguins").dropna().drop(columns=["species"])

st.subheader("Preview of Dataset")  # Textbox that appears on app's main interface. Label for dataset preview.
st.dataframe(df.head(100))  # Preview allows users to scroll through first 100 rows in the dataset. 

##################################
# App Messages and Select Boxes
##################################
numeric_df = df.select_dtypes(include=np.number)  # Cleans dataset to only show numeric values. 
if numeric_df.empty:
    st.error("Dataset has no numeric columns.")  # Message that shows if dataset has no numeric values. 
    st.stop()

# Scaling
scaler = StandardScaler() # From sklearn. preprocessing import Standard Scaler library.
scaled_data = scaler.fit_transform(numeric_df) # Transforms each numeric column so that the mean is 0 and standard deviation is 1.
# Standardizing is necessary because models rely on normal distributions. Larger scales in data would skew results. 

st.sidebar.header("Choose Model & Hyperparameters")  # Label for box selection.
model_choice = st.sidebar.selectbox("Unsupervised Model", ["PCA", "KMeans", "Hierarchical Clustering"]) # Creates selectbox menu for the three Unsupervised models.

################################
# Principal Component Analysis
################################
if model_choice == "PCA":
    st.header("🟡 Principal Component Analysis")

    st.markdown("**PCA reduces the number of features in a dataset while preserving as much key information as possible. It transforms original features into a set of uncorrelated variables, called principal components.**")
    st.info("""
            - 1st component: Captures the most varience in the data.
             - 2nd component: Captures the next most, and etc.""")

    n_components = st.sidebar.slider("Number of Components", 2, min(10, scaled_data.shape[1]), 2) # Creates slider to pick number of components. 

    pca = PCA(n_components=n_components)  # Creates PCA models with number of components. 
    components = pca.fit_transform(scaled_data)  # fit_transforms learns components and projects original data. 
    explained_var = pca.explained_variance_ratio_ # fraction of total varience.

    if n_components >= 2: # Is user selects 2 or more compoents, first two are extracted and stored for plotting. 
        df["PCA1"], df["PCA2"] = components[:, 0], components[:, 1]
        st.subheader("📊 PCA - Scatter Plot (First 2 Components)")
        fig, ax = plt.subplots()
        sns.scatterplot(x=components[:, 0], y=components[:, 1])
        ax.set_xlabel("PCA 1") # label
        ax.set_ylabel("PCA 2") # label
        st.pyplot(fig) #Plotly to create interactive scatterplot.

    st.subheader("📌 PCA - Explained Variance") 
    st.bar_chart(explained_var) # Creates barchart for varience. 

###############################
# KMeans Clustering
###############################
elif model_choice == "KMeans":
    st.header("🔵 K-Means Clustering")
    st.info("**KMeans divides a dataset into K distinct clusters based on similarity. Clusters are made where points are nearest to eachother.**")

    k = st.sidebar.slider("Number of Clusters (k)", 2, 10, 3) # Creates slider for KMeans.

    kmeans = KMeans(n_clusters=k, random_state=42) # Initiates k clusters with KMeans model.
    labels = kmeans.fit_predict(scaled_data)
    df['KMeans Cluster'] = labels # Storing clusters into labels.

    silhouette = silhouette_score(scaled_data, labels) # Creates silhouette_score.
    st.header(f"**Silhouette Score:** {silhouette:.3f}") # Silhouette scores determine how well clusters are separated. 
    st.markdown(""" A silhouette score measures how well clusters are separated and how tightly points are grouped. Ranges from -1(bad) to 1(ideal).""")
    
    # PCA for visualization
    pca = PCA(2)
    comp = pca.fit_transform(scaled_data)
    df["PCA1"], df["PCA2"] = comp[:, 0], comp[:, 1]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 KMeans - Cluster Plot (PCA Projection)") # Creates interactive scatterplot.
        fig1, ax1 = plt.subplots()
        sns.scatterplot(data=df, x="PCA1", y="PCA2", hue="KMeans Cluster", palette="Set2", ax=ax1)
        st.pyplot(fig1)

    with col2:
        st.subheader("📉 KMeans - Elbow Plot")  # Creates elbow plot. Helpful for knowing optimal clusters.
        distortions = []
        for i in range(1, 11):  # Computes inertia for k values 1 to 10.
            km = KMeans(n_clusters=i, random_state=42)
            km.fit(scaled_data)
            distortions.append(km.inertia_)
        fig2, ax2 = plt.subplots()  # Plots inertia
        ax2.plot(range(1, 11), distortions, marker='o')
        ax2.set_xlabel("Number of clusters")
        ax2.set_ylabel("Inertia")
        ax2.set_title("Elbow Method")
        st.pyplot(fig2)

#################################
# Hierarchical Clustering
#################################
elif model_choice == "Hierarchical Clustering":
    st.header("🟣 Hierarchical Clustering")
    st.subheader("**Hierarchical Clustering groups data into a hierarchy of clusters. It can form a tree of nested clusters called dendrograms. In this model, we use agglomerative (bottom-up) clustering.**")

    n_clusters = st.sidebar.slider("Number of Clusters", 2, 10, 3) # Number of final groups. 

    # Dendrogram
    st.subheader("🌿 Dendrogram")
    link_matrix = linkage(scaled_data, method='ward') # Ises scipy.cluster.hierarchy.linkage to compute linkage matrix. Ward minimizes cluster varience.
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    dendrogram(link_matrix, truncate_mode="level", p=5, ax=ax3) # Generates hierarchical tree diagram.
    st.pyplot(fig3) # Displays on the app.

    # Clustering
    model = AgglomerativeClustering(n_clusters=n_clusters) # Creates hierarchical clustering model witht the number chosen in the hyperparamenters.
    labels = model.fit_predict(scaled_data) # label

    # PCA for 2D view
    pca = PCA(2)   # Applies PCA to reduce the dataset to 2 dimensions for plotting.
    comp = pca.fit_transform(scaled_data)
    df["PCA1"], df["PCA2"] = comp[:, 0], comp[:, 1]
    df["Cluster"] = labels

    st.subheader("🧬 Cluster Plot (PCA Projection)")
    fig4, ax4 = plt.subplots()
    sns.scatterplot(data=df, x="PCA1", y="PCA2", hue="Cluster", palette="Dark2", ax=ax4)
    st.pyplot(fig4)  # Interactive plot using plotly.
