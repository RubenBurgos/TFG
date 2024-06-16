from validators.hashes import sha1, sha224, sha256, sha512, md5
from source_code.data.data import Data
from source_code.data.data_type import Data_Type


class Hash(Data):
    def __init__(self, data):
        super().__init__(data, Data_Type.HASH)

    def check_format(self, data):
        if sha1(data) or sha224(data) or sha256(data) or sha512(data) or md5(data):
            return True
        else:
            return False