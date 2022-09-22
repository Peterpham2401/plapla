/opt/spark/bin/spark-submit \
     --name "Ingest prod_frt_pharmacy_ho_repl_item_dvt " \
     --class com.frt.spark.batch.IngestAsParquetsFromAvros \
     --master yarn \
     --deploy-mode cluster \
     --driver-memory 5g \
     --executor-memory 6g \
     --executor-cores 4 \
     hdfs://mycluster/user/hadoop/jobs/FrtSparkApp-0.0.1-SNAPSHOT-jar-with-dependencies.jar \
     "/user/hadoop/spark_job_info/last_success_info/prod_frt_pharmacy_ho_repl_item_dvt" \ -- path chứa lần chạy gần nhất
     "/user/hadoop/frt_databases/pos/FLC/prod_frt_pharmacy_ho_repl/item_dvt" \ -- path avro
     "/user/hadoop/parquet/tmp/item_dvt" "ID" \ -- path parquet
     "false" 

/user/hadoop/frt_databases/tùy xem là thuộc bên nào/FLC hoạc ICT/ tên DB/ tên bảng -- file avro
/user/hadoop/parquet/tùy xem là thuộc bên nào/FLC hoạc ICT/ tên DB/ tên bảng -- file parquet



/opt/spark/bin/spark-submit \
 --name "Remove Duplicate: Prod FRT Pharmacy HO REPL item_dvt" \
 --class com.frt.spark.batch.ParquetTablesRemoveDuplicatesTwoColumns \
 --master yarn \
 --deploy-mode cluster \
 --driver-memory 5g \
 --executor-memory 6g \
 --executor-cores 4 \
 hdfs://mycluster/user/hadoop/jobs/FrtSparkApp-0.0.1-SNAPSHOT-jar-with-dependencies.jar \
 "/user/hadoop/parquet/tmp/item_dvt" "ID"
 
 docentry và linenum


/opt/sqoop/script/sqoop_user_jobs/sqoop_create_daily_jobs.sh \
    get_daily2_f_order_stream_flc \
    user_beta \
    '/user/hadoop/frtsecret/user_beta_33.pwd' \
    '-1' \
    10.96.254.33 \
    1433 \
    TEST_ \
    'F_ORDER_STREAM_FLC' \
    ORDER_ID \
    ORDER_ID \
    '/user/hadoop/frt_databases/tmp/oms/f_order_stream_flc' 