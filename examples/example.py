from __future__ import print_function
import os

import numpy as np
from sklearn.linear_model import LogisticRegression

from mlflow.sklearn import log_model
from mlflow import log_metric, log_param, log_artifacts,active_run
from random import random, randint

if __name__ == "__main__":
    print("Running example.py")

    log_param("my_param", randint(0, 100))
    
    log_metric("my_metric_name", random())
    
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
    with open("outputs/example.txt", "w") as f:
        f.write("Hello world!")

    log_artifacts("outputs")

    print("Train model")
    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression()
    lr.fit(X, y)
    score = lr.score(X, y)
    print("Score of LogisticRegression: %s" % score)
    log_metric("logistic_regression_score", score)
    log_model(lr, "model")
    print("Model saved in run %s" % active_run().info.run_uuid)

    print("Success")