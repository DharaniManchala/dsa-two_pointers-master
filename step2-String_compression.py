class Solution(object):
    def compress(self, chars):
        """
        Compresses the character array in-place by replacing repeated characters
        with the character followed by its count.

        :param chars: List[str] - the input character array
        :return: int - the length of the compressed array

        Example:
            chars = ['a','a','b','b','c','c','c']
            compress(chars)
            # chars becomes ['a','2','b','2','c','3'], returns 6
        """
        read = 0
        write = 0

        while read < len(chars):
            current_char = chars[read]
            count = 0

            # Count how many times the current character repeats
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character
            chars[write] = current_char
            write += 1

            # Write the count (if more than 1)
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_input = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    new_length = solution.compress(example_input)
    print(example_input[:new_length])  # Output: ['a', '2', 'b', '2', 'c', '3']
    print(new_length)                  # Output: 6
