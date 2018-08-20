from __future__ import print_function

import os
import shutil
import sys
import random
import tempfile
import numpy as np
from sklearn.linear_model import LogisticRegression

from mlflow.store.rest_store import RestStore
from mlflow import log_metric, log_param, log_artifacts, get_artifact_uri, active_run,\
    get_tracking_uri,set_tracking_uri, log_artifact
from mlflow.sklearn import log_model

if __name__ == "__main__":
    print("Running {} with tracking URI {}".format(sys.argv[0], sys.argv[1]))
    set_tracking_uri(sys.argv[1])
    log_param("my_param", 5)
    log_metric("my_metric_name", 5)
    log_metric("my_metric_name", 1)
    log_metric("my_metric_name", 22)
    run = active_run()
    print("In run with UUID: %s" % run.info.run_uuid)
    tracking_uri = get_tracking_uri()
    if tracking_uri.startswith("http://"):
        store = RestStore({'hostname':tracking_uri})
        metric_obj = store.get_metric(run.info.run_uuid, "my_metric_name")
        metric_history = store.get_metric_history(run.info.run_uuid, "my_metric_name")
        param_obj = store.get_param(run.info.run_uuid, "my_param")
        print("Got metric %s, %s" % (metric_obj.key, metric_obj.value))
        print("Got param %s, %s" % (param_obj.key, param_obj.value))
        print("Got metric history %s" % metric_history)
    local_dir = tempfile.mkdtemp()
    message = "test artifact written during run %s within artifact URI %s\n" \
              % (active_run().info.run_uuid, get_artifact_uri())
    try:
        file_path = os.path.join(local_dir, "some_output_file.txt")
        with open(file_path, "w") as handle:
            handle.write(message)
        log_artifacts(local_dir, "some_subdir")
        log_artifact(file_path, "another_dir")
    finally:
        shutil.rmtree(local_dir)

    X = np.array([-2, -1, 0, 1, 2, 1]).reshape(-1, 1)
    y = np.array([0, 0, 1, 1, 1, 0])
    lr = LogisticRegression()
    lr.fit(X, y)
    score = lr.score(X, y)
    log_metric("logistic_regression_score", score)
    log_model(lr, "model")
    print("Model saved in run %s" % active_run().info.run_uuid)


