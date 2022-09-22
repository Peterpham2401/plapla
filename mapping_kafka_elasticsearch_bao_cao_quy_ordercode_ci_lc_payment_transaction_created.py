import json
import sys
from .mapping_utils import *

def mapping_json(json_raw, index, kafka_topic_mark, kafka_partition, kafka_offset, kafka_receive_time, ecode_to_ename):
    doc = {}
    json_raw = MappingDict(json_raw)
    if json_raw.g("OrderCode") is not None:
        doc["OrderCode"] = json_raw.g("OrderCode")

    if json_raw.gd("Data").g("COD") is None:
        return None
    if json_raw.gd("Data").gd("COD").g("TransporterCode") != 6:
        return None
    doc["Transaction_PaymentRequestId"] = json_raw.gd("Data").gd("Transaction").g("PaymentRequestId")
    doc["Transaction_ShopCode"] = json_raw.gd("Data").gd("Transaction").g("ShopCode")
    doc["Transaction_CreatedDate"] = json_raw.gd("Data").gd("Transaction").g("CreatedDate")

    json_formatted = {
        "_op_type": 'update',
        "_index": index,
        "_id": doc["OrderCode"],
        "doc": doc,
        "doc_as_upsert": True
    }
    return json_formatted

