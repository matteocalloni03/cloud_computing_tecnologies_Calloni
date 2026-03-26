# A Cloud-Native Serverless Architecture Deployed on AWS 

**Author:** [Matteo Calloni] -[Matricola 77021A]

🎥 **[Watch the Video Demonstration](INSERISCI_QUI_IL_LINK_DI_YOUTUBE)** 🎥

## 📂 Repository Structure
*   📄 `Report_Calloni_Matteo.pdf`: The complete academic report detailing the architecture, non-functional properties, and cloud metrics analysis.
*   🐍 `load_test.py`: A local Python script utilizing `ThreadPoolExecutor` (boto3) to simulate a massive concurrent workload (50 parallel uploads).
*   🐍 `lambda_function.py`: The Python code executed inside the AWS Lambda container.
*   🔐 `iam_policy.json`: The custom IAM Inline Policy applied to enforce the Least Privilege principle for the local client.

