import re

class TrieNode:
    def __init__(self):
        self.children = [None] * 100  # Trie nodes for printable ASCII characters
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord(' ')  # Convert character to index (space as offset)

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord

def main():
    # List of example phone numbers to test
    phone_numbers = [
        "212-456-7890", "(212)456-7890", "(212)-456-7890", "212.456.7890",
        "212 456 7890", "+12124567890", "+12124567890", "+1 212.456.7890",
        "+212-456-7890", "1-212-456-7890"
    ]

    # Extract non-numeric characters from phone numbers and store in a list
    non_numeric_chars = []
    for phone_number in phone_numbers:
        phone_number_with_hash = phone_number + "#"
        non_numeric_chars.append(re.sub(r'[0-9\s]', '', phone_number_with_hash))
    
    # Create a Trie and insert non-numeric characters as keys
    t = Trie()
    for key in non_numeric_chars:
        t.insert(key)

    output = ["Not Valid Phone Number", "Valid Phone Number"]

    # Phone number to be checked for validity
    phone_number_to_be_checked = "+21-46-7-8-"
    phone_number_with_hash = phone_number_to_be_checked + "#"
    search_key = re.sub(r'[0-9\s]', '', phone_number_with_hash)  

    # Search for the key and print the result
    print("{}".format(output[t.search(search_key)]))

if __name__ == '__main__':
    main()
