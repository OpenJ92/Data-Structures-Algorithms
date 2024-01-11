class Robot:
    def __init__(self):
        self.position = (0,0)
        self.facing   = (0,1)

    def go(self):
        x, y = self.position
        dx, dy = self.facing
        self.position = (x+dx, y+dy)

    def rotate_left(self):
        match self.facing:
            case (0,1) : self.facing = (-1,0)
            case (-1,0): self.facing = (0,-1)
            case (0,-1): self.facing = (1,0)
            case (1,0) : self.facing = (0,1)

    def rotate_right(self):
        match self.facing:
            case (0,1) : self.facing = (1,0)
            case (1,0) : self.facing = (0,-1)
            case (0,-1): self.facing = (-1,0)
            case (-1,0): self.facing = (0,1)

    def apply_instruction(self, instruction):
        match instruction:
            case 'G':
                self.go()
            case 'L':
                self.rotate_left()
            case 'R':
                self.rotate_right()

    def apply_instructions(self, instructions):
        for instruction in instructions:
            self.apply_instruction(instruction)

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        robot = Robot()
        robot.apply_instructions(instructions)

        return (0,0) == robot.position or (0,1) != robot.facing
