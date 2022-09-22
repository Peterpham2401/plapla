# Date: 2022-09-22

## Topic to query
Topic | max_offset
lc.payment.transaction.created | 1823444
lc.payment.debbit.completed | 10496
lc.payment.paymentRequest.AR.completed | 9127
lc.payment.paymentRequest.completed | 2020541
lc.payment.transaction.RD.created | 205
lc.payment.transaction.RT.created | 25894

Requirement
if transtraction.time have "+7:00"

## Sửa file mapping
* Nếu datetime không "+7:00" thì thêm vào
### các file ini
```
kafka_elasticsearch_bao_cao_quy_ci_lc_payment_transaction_rd_created.ini
kafka_elasticsearch_bao_cao_quy_ci_lc_payment_transaction_rt_created.ini
kafka_elasticsearch_bao_cao_quy_ordercode_ci_lc_payment_transaction_created.ini
kafka_elasticsearch_bao_cao_quy_ordercode_ci_lc_shipment_delivery_confirmed.ini
```
### các file python
* Find TransactionTime and modify line with
```python
if "+07:00" not in json_raw.gd("Transaction").g("TransactionTime") and json_raw.gd("Transaction").g("TransactionTime") != 'null' :
        doc["Transaction_TransactionTime"] = json_raw.gd("Transaction").g("TransactionTime") + '+07:00'
else:
    doc["Transaction_TransactionTime"] = json_raw.gd("Transaction").g("TransactionTime")
```
```
mapping_kafka_elasticsearch_bao_cao_quy_ci_lc_payment_transaction_rd_created.py -- done
mapping_kafka_elasticsearch_bao_cao_quy_ci_lc_payment_transaction_rt_created.py -- done
mapping_kafka_elasticsearch_bao_cao_quy_ordercode_ci_lc_payment_transaction_created.py --not have
mapping_kafka_elasticsearch_bao_cao_quy_ordercode_ci_lc_shipment_delivery_confirmed.py
```