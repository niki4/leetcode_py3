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


if __name__ == '__main__':
    codec = Codec()
    tc = (
        (["Hello", "World"], "Hello--->World"),
        ([""], ""),
    )
    for deserialized, serialized in tc:
        encoded_str = codec.encode(deserialized)
        assert encoded_str == serialized
        decoded_str = codec.decode(encoded_str)
        assert decoded_str == deserialized
