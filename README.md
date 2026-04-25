# Apache Airflow Orchestration for IPL Databricks ETL Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end **Apache Airflow orchestration framework** built to automate a Databricks-based IPL data pipeline using **PySpark** and **Medallion Architecture (Bronze → Silver → Gold)**.

The orchestration layer was containerized using Docker and designed to execute independent workloads in parallel, improving overall runtime and operational visibility.

This repository focuses on workflow orchestration. The transformation notebooks and medallion ETL logic are maintained separately in the companion repo: [ipl-databricks-etl-pipeline](https://github.com/Paradox1603/ipl-databricks-etl-pipeline).

---

## 🎯 Key Objectives

* Orchestrate Databricks ETL notebooks using Apache Airflow
* Implement parallel task execution for performance gains
* Manage task dependencies across Bronze, Silver, and Gold layers
* Monitor runs using Airflow UI
* Separate orchestration from transformation logic
* Compare notebook-based orchestration vs Airflow DAG orchestration

---

## 🏗️ Architecture

```text
Dockerized Apache Airflow
        ↓
Airflow DAG Scheduler
        ↓
Databricks Jobs / Notebooks
        ↓
PySpark Transformations
        ↓
Amazon S3 Storage
        ↓
Bronze → Silver → Gold Layers
```

---

## 🔄 DAG Workflow

```text
      start
        ↓

Parallel Bronze Layer:
- bronze_ball_by_ball
- bronze_match
- bronze_player_match
- bronze_player
- bronze_team

        ↓

validate_bronze_layer

        ↓

silver_transform

        ↓

validate_silver_layer

        ↓

Parallel Gold Layer:
- gold_batsmen_perf
- gold_bowler_perf
- gold_match_summary
- gold_top_batsman_season
- gold_powerplay_bowlers
- gold_toss_impact

        ↓
       end
```

---

## ⚡ Performance Improvement

| Orchestration Model        | Runtime   |
| -------------------------- | --------- |
| Databricks Runner Notebook | 8 Minutes |
| Airflow Parallel DAG       | 6 Minutes |

### ✅ Result

**25% reduction in runtime** by parallelizing independent tasks through Airflow.

---

## 🛠️ Tech Stack

* Apache Airflow
* Docker
* Databricks
* PySpark
* Amazon S3
* Python
* SQL

---

## 📂 Repository Structure

```text id="1im2ew"
ipl-airflow-orchestration/
│── dags/
│   └── ipl_pipeline.py
│── docker-compose.yml
│── .env.example
│── README.md
│── screenshots/
```

---

## ▶️ Local Setup Guide

### 1️⃣ Clone Repository

```bash id="6yr4la"
git clone <repo-url>
cd airflow-databricks-medallion-pipeline
```

### 2️⃣ Ensure Folder Structure

Place DAG files inside:

```text id="7bgqpd"
dags/
```

Keep `docker-compose.yml` in root folder.

---

### 3️⃣ Configure Environment

Create `.env` file:

```text id="0m2m0g"
AIRFLOW_UID=50000
```

(Add other configs if needed)

---

### 4️⃣ Start Airflow

Run from root folder (where `docker-compose.yml` exists):

```bash id="z4lsuk"
docker compose up -d
```

---

### 5️⃣ Open Airflow UI

```text id="sdfn4u"
http://localhost:8080
```

---

### 6️⃣ Configure Databricks Connection

Go to:

```text id="v1hcrq"
Admin → Connections
```

Create:

* Connection ID: `databricks_default`
* Type: Databricks
* Host: Databricks workspace URL
* Password: Personal Access Token

---

### 7️⃣ Trigger DAG

Run DAG:

```text id="cez7bw"
ipl_pipeline
```

from Airflow UI.

---

## 📊 Features Implemented

* Parallel Bronze & Gold layer execution
* Databricks job triggering from Airflow
* Dependency-based orchestration
* DAG monitoring through Airflow UI
* Dockerized local scheduler environment
* Runtime optimization benchmarking

---

## 💼 Business Value

This project simulates a real-world modern data platform where transformation workloads run in Databricks while orchestration is managed centrally through Airflow.

---

## 🔮 Future Enhancements

* Retry policies
* SLA alerts and email notifications
* CI/CD deployment pipeline
* Dynamic DAG generation
* Data quality checks with Great Expectations
* Environment-based configs (Dev / QA / Prod)

---

## 💼 Resume Value

This project demonstrates hands-on experience with:

* Workflow orchestration
* Parallel pipeline execution
* Cloud data platform integration
* Production scheduling concepts
* Performance optimization

---

## 👤 Author

Kevin V

---
