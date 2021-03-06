# Automatically generated by pb2py
from .. import protobuf as p


class EthereumSignTx(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('nonce', p.BytesType, 0),
        3: ('gas_price', p.BytesType, 0),
        4: ('gas_limit', p.BytesType, 0),
        5: ('to', p.BytesType, 0),
        6: ('value', p.BytesType, 0),
        7: ('data_initial_chunk', p.BytesType, 0),
        8: ('data_length', p.UVarintType, 0),
        9: ('chain_id', p.UVarintType, 0),
        10: ('tx_type', p.UVarintType, 0),
    }
    MESSAGE_WIRE_TYPE = 58
