## Module 1
<details>
* Create a simple pipeline for automating work with a machine learning model.
  
* Different stages of the machine learning pipeline are described in different Python scripts, which are then connected into a unified sequence of actions using a Bash script.
  
* All files should be placed in the "lab1" subdirectory of the root directory.

Stages:

1. Create a Python script (data_creation.py) that generates various datasets describing a certain process (e.g., daily temperature changes). There should be several datasets, and some of them can include anomalies or noise. Some of the datasets should be saved in the "train" folder, and another part in the "test" folder. One way to complete this stage is by downloading a dataset from the network and splitting it into a test and training set. Please note that the file must be accessible, and the download methods should be available in Ubuntu or can be installed via pip in the pipeline.sh file.
2. Create a Python script (data_preprocessing.py) that performs data preprocessing, for example, using sklearn.preprocessing.StandardScaler. Transformations are applied to both the test and training datasets.
3. Create a Python script (model_preparation.py) that creates and trains a machine learning model on the constructed data from the "train" folder. You can use pickle to save the model to a file (see example).
4. Create a Python script (model_testing.py) to test the machine learning model on the constructed data from the "test" folder.
Write a Bash script (pipeline.sh) that sequentially runs all Python scripts. If necessary, make the script more complex. As a result of running the script, one line with the metric evaluation on your model is printed to the standard output, for example:
```shell
Model test accuracy is: 0.876
```
</details>

## Module 2
<details>
In the practical assignment for this module, you need to apply the knowledge you've gained about working with Docker (and Docker Compose). You need to use the knowledge you've acquired about creating microservices. In this task, you need to deploy a microservice in a Docker container. For example, it could be a machine learning model that accepts requests via an API and returns responses. Another option could be implementing an application based on Streamlit (https://github.com/korelin/streamlit_demo_app).

The results of this task should be placed in the lab3 subdirectory of your repository's root directory.

Here's what you need to do:

Prepare Python code for the model and microservice.

Create a Dockerfile.

Build a Docker image.

Run a Docker container and verify its operation.

Additional points will be awarded for:

Using Docker Compose.

Automating image building, linking the tag name to the build version (e.g., commit SHA, branch name).
Deployment (uploading) of the image to an artifact repository such as Docker Hub.

</details>
