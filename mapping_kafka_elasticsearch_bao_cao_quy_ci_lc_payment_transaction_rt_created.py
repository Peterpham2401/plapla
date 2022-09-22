import json
from .mapping_utils import *

def mapping_json(json_raw, index, kafka_topic_mark, kafka_partition, kafka_offset, kafka_receive_time, ecode_to_ename):
    doc = {}
    json_raw = MappingDict(json_raw)
    if json_raw.g("OrderCode") is not None:
        doc["OrderCode"] = json_raw.g("OrderCode")
    doc["Transaction_Id"] = json_raw.gd("Transaction").g("Id")
    doc["Transaction_TransactionTypeId"] = json_raw.gd("Transaction").g("TransactionTypeId")
    doc["Transaction_PaymentRequestId"] = json_raw.gd("Transaction").g("PaymentRequestId")
    doc["Transaction_Status"] = json_raw.gd("Transaction").g("Status")
    doc["Transaction_Amount"] = json_raw.gd("Transaction").g("Amount")
    doc["Transaction_ShopCode"] = json_raw.gd("Transaction").g("ShopCode")
    doc["Transaction_PaymentMethodId"] = json_raw.gd("Transaction").g("PaymentMethodId")
    doc["Transaction_TransactionTime"] = json_raw.gd("Transaction").g("TransactionTime")
    doc["Transaction_CreatedDate"] = json_raw.gd("Transaction").g("CreatedDate")
    doc["Transaction_CreatedBy"] = json_raw.gd("Transaction").g("CreatedBy")
    if doc["Transaction_CreatedBy"] not in ecode_to_ename:
        doc["Transaction_CreatedBy_Name"] = ""
    elif doc["Transaction_CreatedBy"] is not None:
        doc["Transaction_CreatedBy_Name"] = ecode_to_ename[doc["Transaction_CreatedBy"]]
    else:
        doc["Transaction_CreatedBy_Name"] = ""
    doc["Transfers"] = json_raw.g("Transfers")
    if doc['Transfers'] is not None and \
       len(doc['Transfers']) != 0:
        transfer = doc['Transfers']
        doc["Details"] = f"{transfer['AccountName']} - {transfer['AccountNum']} - {transfer['BankName']}, "
        doc["Details"] = doc["Details"][:-2]
        doc['HTTT'] = "Chuyển khoản"
    elif doc['Transfers'] is None:
        doc["Details"] = ""
        doc['HTTT'] = "Tiền mặt"
    # if doc["Transfers"] is not None:
    #     doc["Transfers"] = [doc["Transfers"]]
    # doc["documentType"] = "2_3"
    # doc["documentTypeName"] = "Chi tiền trả hàng"
    if doc["Transaction_TransactionTypeId"] == 3:
        doc["documentType"] = "2_3"
        doc["documentTypeName"] = "Chi tiền trả hàng"
    doc[kafka_topic_mark + "_KAFKA_PARTITION"] = kafka_partition
    doc[kafka_topic_mark + "_KAFKA_OFFSETS"] = kafka_offset
    doc[kafka_topic_mark + "_KAFKA_RECEIVE_TIME"] = kafka_receive_time
    doc["Transaction_Completed"] = True
    json_formatted = {
        "_op_type": 'update',
        "_index": index,
        "_id": doc["Transaction_Id"],
        "doc": doc,
        "doc_as_upsert": True
    }
    return json_formatted

