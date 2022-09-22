import json
from .mapping_utils import *

def mapping_json(json_raw, index, kafka_topic_mark, kafka_partition, kafka_offset, kafka_receive_time, ecode_to_ename):
    doc = {}
    json_raw = MappingDict(json_raw)
    if json_raw.g("OrderCode") is not None:
        doc["OrderCode"] = json_raw.g("OrderCode")
    doc["COD_TransporterName"] = json_raw.g("CarrierName")
    doc["COD_waybillnumber"] = json_raw.g("DeliveryId")
    doc["Details"] = str(doc["COD_TransporterName"]) + " - " + str(doc["COD_waybillnumber"])
    doc[kafka_topic_mark + "_KAFKA_PARTITION"] = kafka_partition
    doc[kafka_topic_mark + "_KAFKA_OFFSETS"] = kafka_offset
    doc[kafka_topic_mark + "_KAFKA_RECEIVE_TIME"] = kafka_receive_time
    doc["Transaction_Completed"] = True
    json_formatted = {
        "_op_type": 'update',
        "_index": index,
        "_id": doc["OrderCode"],
        "doc": doc,
        "doc_as_upsert": True
    }
    return json_formatted
