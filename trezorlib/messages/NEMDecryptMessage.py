# Automatically generated by pb2py
from .. import protobuf as p


class NEMDecryptMessage(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('network', p.UVarintType, 0),
        3: ('public_key', p.BytesType, 0),
        4: ('payload', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 75
