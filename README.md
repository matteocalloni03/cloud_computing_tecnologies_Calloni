# A Cloud-Native Serverless Architecture Deployed on AWS 

**Author:** [Matteo Calloni] -[Matricola 77021A]

## Overview
This repository contains the final project for the **Cloud Computing Technologies** course. 
The project demonstrates the implementation of a 100% serverless, event-driven, and decoupled architecture on Amazon Web Services (AWS), designed to handle massive IoT telemetry workloads.

The architecture was specifically engineered to address advanced cloud concepts:
*   **Total Service Decoupling** via Message Brokers.
*   **Controlled Rapid Elasticity** (Rate limiting to protect downstream databases).
*   **Application-Level Fault Tolerance** (Dead Letter Queues).
*   **Strict Security** via the Least Privilege principle.

## Architecture Flow
`Local Script` ➡️ `Amazon S3` ➡️ `Amazon SQS (Buffer)` ➡️ `AWS Lambda (Compute)` ➡️ `Amazon DynamoDB`
*With a secondary routing from SQS to an `SQS DLQ` for corrupted payload isolation.*

## Key Features Implemented
1. **Queue-Based Load Leveling:** Instead of invoking Lambda directly, S3 notifications are buffered in an SQS queue. This absorbs sudden traffic spikes.
2. **Maximum Concurrency Limit:** The Lambda Event Source Mapping is strictly limited to 5 concurrent executions. This prevents DynamoDB throttling and guarantees predictable costs.
3. **Fault Tolerance (DLQ):** Intentionally corrupted files injected during the stress test are caught and isolated into a Dead Letter Queue after 2 failed processing attempts, ensuring zero data loss and uninterrupted pipeline execution.
4. **Custom IAM Policies:** AWS Managed Policies were avoided. Strict inline JSON policies were created to lock down resource access via exact ARNs.

## Repository Structure
*   `/src/stress_test.py`: The local multithreaded Python script used to simulate a massive IoT load spike (injecting both valid and corrupted JSON files).
*   `/src/lambda_function.py`: The stateless compute logic that validates data and acts as a router.
*   `/infrastructure/iam_least_privilege_policy.json`: The specific IAM security rules applied to the compute layer.
*   `Report & Presentation`: PDF documentation containing architectural choices and live test screenshots (CloudWatch metrics, SQS DLQ status, DynamoDB records).

## Technologies Used
*   **Compute:** AWS Lambda (Python 3.12)
*   **Storage & DB:** Amazon S3, Amazon DynamoDB
*   **Integration:** Amazon SQS
*   **Observability:** Amazon CloudWatch
*   **SDK:** `boto3`
