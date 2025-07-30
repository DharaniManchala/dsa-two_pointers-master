class Solution(object):
    def compress(self,chars):
        read=0
        write=0
        while read<len(chars):
            current_char=chars[read]
            count=0
            while read<len(chars) and chars[read]==current_char:
                read+=1
                count+=1
            chars[write]=current_char
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write
# Example usage
if __name__ == "__main__":
    solution = Solution()
    example_input = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    new_length = solution.compress(example_input)
    print(example_input[:new_length])  # Output: ['a', '2', 'b', '2', 'c', '3']
    print(new_length)  # Output: 6