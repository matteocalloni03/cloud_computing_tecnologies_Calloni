# A Cloud-Native Serverless Architecture Deployed on AWS ☁️

**University of Milan - Cloud Computing Technologies Course**  
**Author:** [Matteo Calloni] -[Matricola 77021A]

🎥 **[Watch the Video Demonstration](INSERISCI_QUI_IL_LINK_DI_YOUTUBE)** 🎥

## 📖 Project Overview
This repository contains the source code, configurations, and documentation for an event-driven serverless data processing pipeline deployed on Amazon Web Services (AWS).

The project practically demonstrates core cloud concepts, including:
*   **Cloudonomics:** Transitioning from CapEx to OpEx via a pure *pay-per-use* model (Zero cost when idle).
*   **Rapid Elasticity:** Automatic horizontal scaling via AWS Lambda to handle sudden traffic spikes.
*   **Security by Design:** Implementation of the *Least Privilege* principle using AWS IAM.
*   **NoOps / Serverless:** Complete decoupling of storage, compute, and database layers without provisioning virtual machines.

## 🏛️ Architecture
1. **Amazon S3 (Data Lake):** Receives incoming files and triggers an event (`s3:PutObject`).
2. **AWS Lambda (Compute):** A stateless function that processes file metadata asynchronously.
3. **Amazon DynamoDB (Persistence):** A managed NoSQL database to store the processed records.
4. **Amazon CloudWatch (Observability):** Monitors concurrent executions, invocations, and logs.

## 📂 Repository Structure
*   📄 `Report_Calloni_Matteo.pdf`: The complete academic report detailing the architecture, non-functional properties, and cloud metrics analysis.
*   🐍 `load_test.py`: A local Python script utilizing `ThreadPoolExecutor` (boto3) to simulate a massive concurrent workload (50 parallel uploads).
*   🐍 `lambda_function.py`: The Python code executed inside the AWS Lambda container.
*   🔐 `iam_policy.json`: The custom IAM Inline Policy applied to enforce the Least Privilege principle for the local client.

## 🚀 How to run the load test (Local Setup)
To reproduce the massive load simulation on your own AWS environment:
1. Ensure you have the AWS CLI installed and configured with appropriate credentials (`aws configure`).
2. Install the required Python AWS SDK: `pip install boto3`
3. Edit the `load_test.py` file to match your target S3 Bucket name.
4. Run the script: `python3 load_test.py`
5. Check S3, DynamoDB, and CloudWatch metrics to observe the automatic scaling.
