class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_types = []
        for num_boxes, num_units in boxTypes:
            box_types.append((-num_units, num_boxes))
        heapify(box_types)

        total_units = 0
        while truckSize >= 0 and box_types:
            units, boxes   = heappop(box_types)
            adjusted_boxes = min(truckSize, boxes)
            truckSize   -= adjusted_boxes
            total_units += adjusted_boxes*(-units)
        return total_units
