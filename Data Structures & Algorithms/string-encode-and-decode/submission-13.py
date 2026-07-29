class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for item in strs:
            item_length = str(len(item))
            encoder = item_length + "#" + str(item)
            encoded = encoded + encoder
        return(encoded)
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        return decoded

