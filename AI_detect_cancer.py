#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import optuna


# In[2]:


# Load dataset
data = load_breast_cancer()
X, y = data.data, data.target

print(X)

print(y)


# In[3]:


# Preprocessing: Splitting the dataset and scaling features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[4]:


def objective(trial):
    # Hyperparameters to be tuned
    hidden_layer_sizes = trial.suggest_categorical(
    'hidden_layer_sizes', [
        (50,), (100,), (150,), 
        (50, 50), (100, 50), (150, 100), 
        (100, 100, 100), (50, 100, 50), (30, 50, 30), 
        (200, 100), (100, 100, 100, 100), 
        (200, 150, 100), (100, 200, 100, 50), 
        (30, 30), (20, 20, 20), (30, 30, 30), (40, 40, 40), 
        (20, 20, 20, 20), (30, 30, 30, 30), 
        (25, 25, 25, 25, 25), (20, 20, 20, 20, 20, 20), 
        (15, 15, 15, 15, 15, 15, 15), (10, 10, 10, 10, 10, 10, 10, 10), 
        (5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    ]
    )


    activation = trial.suggest_categorical('activation', ['tanh', 'relu', 'logistic'])

    solver = trial.suggest_categorical('solver', ['sgd', 'adam'])

    alpha = trial.suggest_float('alpha', 1e-6, 1e-1, log=True)

    learning_rate_init = trial.suggest_float('learning_rate_init', 1e-6, 1e-1, log=True)

    batch_size = trial.suggest_categorical('batch_size', [8, 16, 32, 64, 128, 256, 512])

    learning_rate = trial.suggest_categorical('learning_rate', ['constant', 'invscaling', 'adaptive', 'scheduled'])

    max_iter = trial.suggest_categorical('max_iter', [100, 200, 400, 800, 1600, 3200])

    
    # Model definition
    model = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes,
                          activation=activation,
                          solver=solver,
                          alpha=alpha,
                          learning_rate_init=learning_rate_init,
                          max_iter=1000,  # Increased to ensure convergence
                          random_state=42)
    
    # Cross-validation with scaled data
    score = cross_val_score(model, X_train_scaled, y_train, n_jobs=-1, cv=5).mean()
    return score


# In[5]:


# Optuna optimization
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=200, show_progress_bar=True)


# In[6]:


# Results
print(f'Best parameters overall: {study.best_params}')
print(f'Best cross-validation score overall: {study.best_value}\n')

# After optimization, retrieve the best 5 trials
best_trials = sorted(study.trials, key=lambda trial: trial.value, reverse=True)[:5]

# Print detailed information for the top 5 trials
print("Top 5 Trials:")
for i, trial in enumerate(best_trials, 1):
    print(f"Rank: {i}")
    print(f"  Trial Number: {trial.number}")
    print(f"  Parameters: {trial.params}")
    print(f"  Cross-validation Score: {trial.value}\n")


# In[7]:


# Use the best parameters found by Optuna, which includes 'max_iter'
best_model = MLPClassifier(**study.best_params).fit(X_train_scaled, y_train)
test_score = best_model.score(X_test_scaled, y_test)
print('Test set score:', test_score)

