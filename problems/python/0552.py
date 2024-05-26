class Solution:
    def checkRecord(self, n: int) -> int:

        @cache
        def dynamic(record, absences, lates):
            if absences >= 2 or lates >= 3:
                return 0
            if record == 0:
                return 1

            present = dynamic(record-1, absences+0, lates*0)
            absent  = dynamic(record-1, absences+1, lates*0)
            late    = dynamic(record-1, absences+0, lates+1)

            return (present + absent + late) % (10**9 + 7)

        return dynamic(n, 0, 0)

class Solution:
    def checkRecord(self, n: int) -> int:
        ## dynamic[record][lates][absences]
        dynamic = [[[0 for _ in range(3)] for _ in range(4)] for _ in range(2)]

        for absences in range(2):
            for lates in range(3):
                dynamic[0][lates][absences] = 1

        read, write = 0, 1
        for record in range(1, n+1):
            read, write = (record - 1) % 2, record % 2

            for absences in range(2):
                for lates in range(3):
                    present = dynamic[read][lates*0][absences+0]
                    absent  = dynamic[read][lates*0][absences+1]
                    late    = dynamic[read][lates+1][absences+0]

                    dynamic[write][lates][absences] = \
                        (present + absent + late) % (10**9 + 7)


        return dynamic[(n%2)][0][0]

