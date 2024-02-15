module CodeWars.SmallestInteger where

min' :: Int -> [Int] -> Int
min' number [] = number
min' number (x:xs) = min' (min number x) xs

findSmallestInteger :: [Int] -> Int
findSmallestInteger numbers = min' (head numbers) (tail numbers) 
