module Codewars.Kata.Bus where

number :: [(Int, Int)] -> Int
number [   ] = 0
number stops = foldl1 (.) (transfer <$> stops) 0

transfer :: (Int, Int) -> Int -> Int
transfer (on, off) total = total + on - off
