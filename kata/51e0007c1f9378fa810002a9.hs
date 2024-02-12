module Kata.Deadfish (parse) where

parse :: String -> [Int]
parse string = init $ transform string [0]
  where
    transform = foldr (.) id . reverse . map operate

update_state_with :: (Int -> Int) -> [Int] -> [Int]
update_state_with endo xs = init xs ++ [endo (last xs)]

increment :: [Int] -> [Int]
increment = update_state_with (+1)

decrement :: [Int] -> [Int]
decrement = update_state_with (flip (-) 1)

square' :: [Int] -> [Int]
square' = update_state_with (flip (^) 2)

output :: [Int] -> [Int]
output xs@(x:_) = xs ++ pure (last xs)

operate :: Char -> [Int] -> [Int]
operate command = case command of
  'i' -> increment
  'd' -> decrement
  's' -> square'
  'o' -> output
  _ -> id


