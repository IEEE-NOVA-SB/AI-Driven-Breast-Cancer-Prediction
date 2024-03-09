# AI-Driven-Breast-Cancer-Prediction

![Code review](https://github.com/IEEE-NOVA-SB/AI-Driven-Breast-Cancer-Prediction/blob/main/doctors.png)



## Project Description

### What your application does?

The application leverages machine learning to accurately predict breast cancer based on diagnostic measurements. 

Utilizing the MLPClassifier from the scikit-learn library, it applies a multi-layer perceptron (a type of deep neural network) to classify instances into malignant or benign categories. 

The application preprocesses the data, scales features for better model performance, and utilizes a systematic approach to hyperparameter optimization to enhance the prediction accuracy.
 
### Why you used the technologies you used?

The technologies were chosen for their robustness, ease of use, and wide adoption in the machine learning community.

scikit-learn is a powerful library for machine learning that provides efficient tools for data mining and data analysis, including numerous algorithms for classification, regression, clustering, and dimensionality reduction.

It's highly compatible with Python's data manipulation tools and is complemented by libraries like Optuna for advanced hyperparameter optimization, enhancing the model's performance by fine-tuning its settings based on systematic trials and evaluations.

The use of MLPClassifier allows for complex model architectures that can capture intricate patterns in the dataset, and integrating Optuna further refines the model by selecting the optimal configuration of its hyperparameters, ensuring the best possible prediction accuracy.
    
### Some of the challenges you faced and features you hope to implement in the future?

One of the main challenges was finding the optimal architecture and hyperparameters for the MLPClassifier to maximize prediction accuracy. 

The model's performance heavily relies on the correct tuning of parameters such as the number of hidden layers, the size of these layers, and the learning rate. 

Another challenge was ensuring the model generalized well to unseen data, minimizing overfitting.


# Table of Contents
### [ How to Install and Run the Project ](#How_to_install)

### [ How to Use the Project ](#How_to_use)

### [ How to Contribute to the Project ](#how_to_contribute)

### [ Include Credits, Authors and acknowledgment for contributions ](#credits)


----



<a name="How_to_install">

# How to Install and Run the Project

### 1. Create a Virtual Environment (if not already created):
If you haven't already created a virtual environment for your project, you can do so using virtualenv or venv. Here's an example using venv:

```
python -m venv myenv
```


Replace ```myenv``` with the desired name for your virtual environment.

### 2. Activate the Virtual Environment:
On Windows, activate the virtual environment using:

```
myenv\Scripts\activate
```


On macOS and Linux, use:
```
source myenv/bin/activate
```
Replace ```myenv``` with the name of your virtual environment.


### 3. Install dependencies:
Once the virtual environment is activated, you can install Jupyter Notebook using pip:

```
pip install jupyter ipykernel optuna scikit-learn
```
This will install Jupyter Notebook within your virtual environment.

### 4. Verify Jupyter Installation:
To verify that Jupyter Notebook is installed in your virtual environment, you can run:


```
jupyter --version
```

This should display the version of Jupyter Notebook installed within your virtual environment.

### 5. Create a Jupyter Notebook Kernel for the Virtual Environment:
You need to create a Jupyter Notebook kernel that is associated with your virtual environment. This allows you to use the packages installed in your virtual environment within Jupyter Notebook.

#### a. First, activate your virtual environment (if it's not already activated).

#### b. Install the ipykernel package within the virtual environment:

```
pip install ipykernel
```
#### c. Now, you can create a Jupyter Notebook kernel for your virtual environment:


```
python -m ipykernel install --user --name=myenv --display-name="name"
```

Replace ```myenv``` with the name of your virtual environment and choose a suitable display name.

### 6. Start Jupyter Notebook:
Now, you can start Jupyter Notebook from within your virtual environment:

```
jupyter notebook
```
This will open a new Jupyter Notebook session in your web browser, and you should be able to select the "My Virtual Environment" kernel when creating a new notebook. This kernel will use the packages installed in your virtual environment.
</a>

<a name="How_to_use">


#### How to Use the Project

Run all jupyter notebooks cells
</a>


<a name="how_to_contribute">


#### How to Contribute to the Project

Make a pull request

</a>

<a name="credits">

#### Include Credits, Authors and acknowledgment for contributions

</a>

[Tiago Monteiro](https://www.linkedin.com/in/tiago-monteiro-)
