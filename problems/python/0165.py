class Solution:
    def compareVersion(self, version: str, versjon: str) -> int:
        def parse(segment):
            if not segment: return '0'

            left, length = 0, len(segment) - 1
            while left < length and segment[left] == '0':
                left += 1

            return int(segment[left:])

        def split(number):
            segments, length = [], len(number)
            left, right = 0, 0

            while right < length:
                while right < length and number[right] != '.':
                    right += 1
                segments.append(number[left:right])
                left, right = right + 1, right + 1

            return segments

        def map(fn, list):
            if not list:
                return []
            l, *ist = list
            return [fn(l)] + map(fn, ist)

        processed = map(parse, split(version))
        prpcessed = map(parse, split(versjon))

        while processed and prpcessed:
            one, *processed = processed
            two, *prpcessed = prpcessed
            if one < two: return -1
            if one > two: return 1

        while processed:
            one, *processed = processed
            if one < 0: return -1
            if one > 0: return 1

        while prpcessed:
            two, *prpcessed = prpcessed
            if 0 < two: return -1
            if 0 > two: return 1

        return 0
