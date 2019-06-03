"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL
such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny
URL can be decoded to the original URL.
"""

import random
import string

class Codec:
    """
    Runtime: 20 ms, faster than 93.41% of Python.
    Memory Usage: 11.9 MB, less than 28.81% of Python.
    """
    def __init__(self):
        self.storage = dict()
        self.prefix = 'sh'
        self.baseUrl = 'http://tinyurl.com/'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        sh_URL = ''.join(
            random.choice(string.ascii_letters) for _ in range(len(str(hash(longUrl)))))
        self.storage[sh_URL] = longUrl
        return self.baseUrl + self.prefix + sh_URL


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        cleanedID = shortUrl[len(self.baseUrl)+len(self.prefix):]
        long_URL = self.storage[cleanedID]
        return long_URL


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == "__main__":
    c = Codec()
    assert c.decode(c.encode('https://leetcode.com/problems')) == 'https://leetcode.com/problems'
