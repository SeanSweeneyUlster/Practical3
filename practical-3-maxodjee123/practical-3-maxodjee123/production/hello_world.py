import os
import mlflow

def main():
    with mlflow.start_run():
        mlflow.log_param("hello_param", "world")
        mlflow.log_metric("hello_metric", 0.42)
        with open("helloworld.txt", "w") as f:
            f.write("hello world")
        mlflow.log_artifact("helloworld.txt")

if __name__ == "__main__":
    main()