class Solution(object):
    def maximumLength(self, nums):
        count = 1
        mapp = {}

        # Frequency map
        for i in nums:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1

        # Special case for 1
        if 1 in mapp:
            count = max(count, mapp[1] if mapp[1] % 2 else mapp[1] - 1)

        # Iterate over unique numbers
        for i in mapp:
            if i == 1:
                continue

            c = 0
            n = i

            while n in mapp and mapp[n] >= 2:
                c += 2
                n = n * n

            # Center element
            if n in mapp:
                c += 1
            else:
                c -= 1

            count = max(count, c)

        return count