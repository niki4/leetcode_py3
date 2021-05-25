"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
decoded back to the original list of strings.

Implement the encode and decode methods.
You are not allowed to solve the problem using any serialize methods (such as eval).

Example 1:
    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]

    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2

    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
"""


class Codec:
    """
    Runtime: 64 ms, faster than 63.54% of Python3
    Memory Usage: 14.3 MB, less than 97.53% of Python3
    """

    def __init__(self):
        self.sep = "--->"

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return self.sep.join(strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(self.sep)


class Codec2:
    """
    Runtime: 68 ms, faster than 46.61% of Python3
    Memory Usage: 14.5 MB, less than 73.18% of Python3
    """

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # any non-ascii symbol, e.g. chr(257)='ā', may guarantee us we not messed up delimiter with data
        return "".join(f"{len(s)}{chr(257)}{s}" for s in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        strings = []
        curr_pos = 0
        while curr_pos < len(s):
            d_pos = s.find(chr(257), curr_pos)  # index of first delimiter occurrence starting from curr_pos
            s_offset = int(s[curr_pos:d_pos])  # length of the string
            curr_pos = d_pos + s_offset + 1
            strings.append(s[(d_pos + 1):curr_pos])
        return strings


if __name__ == '__main__':
    codecs = [Codec(), Codec2()]
    tc = (
        (["Hello", "World"]),
        ([""]),
    )
    for codec in codecs:
        for deserialized in tc:
            assert codec.decode(codec.encode(deserialized)) == deserialized
