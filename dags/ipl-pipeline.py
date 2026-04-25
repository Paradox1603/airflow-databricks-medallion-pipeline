from airflow import DAG
from datetime import datetime
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="ipl_databricks_trigger",
    start_date=datetime(2026,4,18),
    schedule=None,
    catchup=False
) as dag:
    
    start=EmptyOperator(task_id="start")

    bronze_ball_by_ball=DatabricksRunNowOperator(
        task_id="bronze_ball_by_ball",
        databricks_conn_id="databricks_default",
        job_id=499517591558382
    )

    bronze_match=DatabricksRunNowOperator(
        task_id="bronze_match",
        databricks_conn_id="databricks_default",
        job_id=161200589571520
    )

    bronze_player_match=DatabricksRunNowOperator(
        task_id="bronze_player_match",
        databricks_conn_id="databricks_default",
        job_id=493385794554370
    )

    bronze_player=DatabricksRunNowOperator(
        task_id="bronze_player",
        databricks_conn_id="databricks_default",
        job_id=618700655659821
    )

    bronze_team=DatabricksRunNowOperator(
        task_id="bronze_team",
        databricks_conn_id="databricks_default",
        job_id=391439797767374
    )

    validate_bronze_layer=DatabricksRunNowOperator(
        task_id="validate_bronze_layer",
        databricks_conn_id="databricks_default",
        job_id=473362326081844
    )

    silver_transform=DatabricksRunNowOperator(
        task_id="silver_transform",
        databricks_conn_id="databricks_default",
        job_id=646961473990781
    )

    validate_silver_layer=DatabricksRunNowOperator(
        task_id="validate_silver_layer",
        databricks_conn_id="databricks_default",
        job_id=39498861804119
    )

    gold_batsmen_perf=DatabricksRunNowOperator(
        task_id="gold_batsmen_perf",
        job_id=35923279158137,
        databricks_conn_id="databricks_default"
    )

    gold_bowler_perf=DatabricksRunNowOperator(
        task_id="gold_bowler_perf",
        job_id=766512556141271,
        databricks_conn_id="databricks_default"
    )

    gold_match_summary=DatabricksRunNowOperator(
        task_id="gold_match_summary",
        job_id=539286427072276,
        databricks_conn_id="databricks_default"
    )

    gold_top_batsman_season=DatabricksRunNowOperator(
        task_id="gold_top_batsman_season",
        job_id=129191866101583,
        databricks_conn_id="databricks_default"
    )

    gold_powerplay_bowlers=DatabricksRunNowOperator(
        task_id="gold_powerplay_bowlers",
        job_id=306734883245342,
        databricks_conn_id="databricks_default"
    )

    gold_toss_impact=DatabricksRunNowOperator(
        task_id="gold_toss_impact",
        job_id=288575267173198,
        databricks_conn_id="databricks_default"
    )

    end=EmptyOperator(task_id="end")


    start >> [bronze_ball_by_ball,bronze_match,bronze_player_match,bronze_player,bronze_team] >> validate_bronze_layer >> silver_transform >> validate_silver_layer >> [gold_batsmen_perf,gold_bowler_perf,gold_match_summary,gold_top_batsman_season,gold_powerplay_bowlers,gold_toss_impact] >> end