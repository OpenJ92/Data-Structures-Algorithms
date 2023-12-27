class Solution:
    def compress(self, chars: List[str]) -> int:
        reader = 0
        writer = 0
        length = len(chars)

        while reader < length:
            group_length = 1
            while reader + group_length < length \
              and chars[reader+group_length] == chars[reader]:
                group_length += 1
            chars[writer] = chars[reader]

            writer += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[writer:writer+len(str_repr)] = list(str_repr)
                writer += len(str_repr)
            reader += group_length

        return write
