module Codewars.G.Persistence where

digits :: Int -> [Int]
digits 0 = []
digits n = mod n 10 : digits (div n 10)

persistence :: Int -> Int
persistence = length . takeWhile (>=10) . iterate (product . digits)
