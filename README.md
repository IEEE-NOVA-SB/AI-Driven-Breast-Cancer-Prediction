# AI-Driven-Breast-Cancer-Prediction

![Code review]()



## Project Description

### What your application does?

 
### Why you used the technologies you used?


    
### Some of the challenges you faced and features you hope to implement in the future?




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
