# Automatically generated by pb2py
from .. import protobuf as p


class EthereumMessageSignature(p.MessageType):
    FIELDS = {
        1: ('address', p.BytesType, 0),
        2: ('signature', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 66
