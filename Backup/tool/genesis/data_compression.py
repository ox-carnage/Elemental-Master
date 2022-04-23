import struct
import sys

from romhacking.common import BitArray, RingBuffer, Compression, LZSS


class LZTECHNOSOFT(LZSS):
    """
        Class to manipulate LZTECHNOSOFT Compression

        Games where this compression is found:
            - [SMD] Elemental Master
    """

    def __init__(self, input_data):
        super(LZTECHNOSOFT, self).__init__(input_data)

    def decompress(self, offset=0, size=0):
        self.DATA.ENDIAN = '>'
        self._window = RingBuffer(0x1000, 0xFEE, 0x00)
        self._output = bytearray()
        self.DATA.set_offset(offset)
        _decoded = 0
        while (_decoded < size):
            control = self.DATA.read_8()
            _decoded+=1
            for readed_bits in range(8):
                bit = bool((control >> readed_bits) & 0x1)
                if bit:
                    _readed = self.DATA.read_8()
                    self.append(_readed)
                    _decoded+=1
                else:
                    _readed = self.DATA.read_16()
                    length = (_readed & 0xF) + 3
                    offset = ((_readed & 0xF0) << 4) | (_readed >> 8)
                    self.append_from_window(length, offset)
                    _decoded+=2
        return self._output

    def compress(self):
        self.DATA.ENDIAN = '>'
        self._window = RingBuffer(0x1000, 0xFEE, 0x00)
        self._buffer = bytearray()
        self._output = bytearray()
        self._encoded = self.DATA.SIZE
        self.LOOKAHEAD = 0b1111
        bitflag = []
        bitcount = 0
        while self._encoded > 0:
            current_offset = self.DATA.CURSOR
            if bitcount > 7:
                bitcount, bitflag = self.write_command_bit(bitcount, bitflag)
            match = self.find_matches()
            if match and match[1] >= 0x3:
                bitflag.append(0)
                (index, length) = match
                _readed = ((index << 8) & 0xFF00) | ((index >> 4) & 0xF0)
                _readed &= 0xFFF0
                _readed |= (length-3)
                self._buffer.append(_readed >> 8)
                self._buffer.append(_readed & 0xFF)
                for i in range(0, length):
                    self._window.append(self.DATA.read_8())
                self._encoded -= length
            else:
                bitflag.append(1)
                _readed = self.DATA.read_8()
                self._buffer.append(_readed)
                self._window.append(_readed)
                self._encoded -= 1
            bitcount += 1
        if bitcount > 0:
            bitcount, bitflag = self.write_command_bit(bitcount, bitflag)
        return self._output