# Libraries for Data Processing and Visualization
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

####################################
# Title and Instructions
####################################
st.title(" Interactive Supervised Machine Learning!📈 ")

st.markdown("""
## About This Application:
In this interactive machine learning app, you will explore your dataset on a new level! You can upload any data set you'd like and experiement with different hyperparameters, and observe how these affect model training and performance. Decision Tree and K Nearest Neighbor classifiers will be taught and exploration is encouraged to learn more about your dataset!
            
            Instructions: 
    1. Upload any dataset in CSV format using the sidebar or use default titanic data.
    2. Select a target variable you would like to train on. 
    3. Choose a model (Decision Tree or K Nearest Neighbor).
    4. Adjust Hyperparameters. 
    5. Explore your model!
""")

st.info("Let's start to explore!")

##############################
# Dataset Selection:
##############################
st.sidebar.header("Step 1: Upload Dataset or Explore with Titanic Data!")

file = st.sidebar.file_uploader("Upload a CSV file 📂 ", type=["csv"])
if file:
    data = pd.read_csv(file)

else: 
    data = sns.load_dataset('titanic').dropna(subset=["age"])

################################
# Target Variable and Features
#################################
st.sidebar.header("Step 2. Select Target and Feature Variables")

target = st.sidebar.selectbox("Select a target variable:🎯 ", data.columns) 

features = st.sidebar.multiselect("Select Feature Variables:🚢 like adult_male & age", data.columns.drop(target))

X = data[features]
y = data[target]

##################################
# Choosing A Model and Test Size.
##################################
st.sidebar.header(" Step 3. Select A Model and Test Size ")
model = st.sidebar.selectbox("Select a model:", ["Decision Tree ", "K Nearest Neighbors"])
# test_size = st.sidebar.slider("Test Size", 0.1, 0.3, 0.2, 0.05)
test_size = st.sidebar.slider("Test Size (%):", 10, 30, 20)
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=test_size/100,
                                                    random_state=41)

###############################
# Hyperparamenters  
###############################
scaled = False
if model == "Decision Tree ":
    # Decision Tree Hyperparameters
    st.sidebar.header(" Step 4. Decision Tree Hyperparameters 🌿")
    max_depth = st.sidebar.slider("Max Depth", 1, 20, 5, 1)
    min_samples_leaf = st.sidebar.slider("Min Samples Leaf", 1, 10, 2, 1)
    min_samples_split = st.sidebar.slider("Min Samples Split", 2, 20, 4, 1)
    
    # Model
    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)

elif model == "K Nearest Neighbors":
    # K Nearest Neighbors Hyperparameters
    st.sidebar.header("Step 4. K Nearest Neighbors Hyperparameters🏡 ")
    n_neighbors = st.sidebar.slider("Number of Neighbors", 1, 19, 5, 2)

    # Model
    model = KNeighborsClassifier(n_neighbors=n_neighbors)

###################################
# Button to run all parameters
####################################
st.sidebar.header("Step 5. Train and Explore Your Model!")
if st.button("Train & Explore"):
    if not features:
        st.warning("***Using sidebar menu, select feature(s) before training.***")
        st.stop()
    data_selected = data[features + [target]].dropna()
    X = data_selected[features]
    X = pd.get_dummies(X, drop_first=True)

####################
# Dataset Preview
####################
st.write("## Data Preview 🔍")
st.markdown(""" Press ***"Train & Explore"*** button on top if preview is unavailable.""")
#with #st.expander("View your data subset"):
#st.subheader("Data Subset")
st.dataframe(data_selected.head(10))

################################
# Confusion Matrix
###############################

# Training the model
model.fit(X_train, y_train)

# Making predictions using data
y_pred = model.predict(X_test)

# Matrix
st.subheader("Model Confusion Matrix:😦 ")
st.markdown(""" A Confusion Matrix visualizes the accuracy of a model's performance by comparing actual and predicted values. 
 - **Top-left** = True Negatives (correctly predicted non-survival)
- **Top-right** = False Positives (falsely predicted survival)
- **Bottom-left** = False Negatives (falsely predicted non-survival)
- **Bottom-right** = True Positives (correctly predicted survival) """)

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot = True, cmap = 'Greens')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
st.pyplot(plt)

##############################
# Accuracy and Precision
###############################
# Performance Metrics
st.write("## Model Performance🎖️ ")

# Accuracy and Precision
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)


st.metric("Accuracy:", f"{accuracy:.4f}")
st.markdown(""" ***Accuracy*** is the percentage of correct classifications.""")
st.metric("Precision:", f"{precision:.4f}")
st.markdown(""" ***Precision*** is the percentage of a model's positive predictions.""")

#########################
# Classification Report
#########################

#show_classification(y_test, y_pred):
st.write("### Classification Report 📝")
    # Build and display the classification report.
st.text(classification_report(y_test, y_pred))

########################### 
# Notes of Encouragment!
###########################

st.info(" Continue to train and explore your data using different target variables and features using the sidebar menu! ")

st.info("Explore away!🚀 ")
