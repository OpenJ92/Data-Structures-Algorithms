module Codewars.Kata.TenMinuteWalk where

is_non_empty :: [a] -> Maybe [a]
is_non_empty      [   ] = Nothing
is_non_empty list@(_:_) = Just list

take_exactly' :: Int -> [a] -> [Maybe a]
take_exactly' 0 [ ]    = [Nothing]
take_exactly' 0 (x:xs) = [Nothing]
take_exactly' n [ ]    = [Nothing]
take_exactly' n (x:xs) = Just x : take_exactly' (n-1) xs

take_exactly :: Int -> [a] -> Maybe [a]
take_exactly n = sequence . take_exactly' n

valid :: [Char] -> Bool
valid moves = travel == (0,0)
  where
    travel = foldl1 (.) (update_state <$> moves) (0,0)

update_state :: Char -> (Int, Int) -> (Int, Int)
update_state 'n' (x, y) = (x, y + 1)
update_state 'e' (x, y) = (x + 1, y)
update_state 's' (x, y) = (x, y - 1)
update_state 'w' (x, y) = (x - 1, y)

isValidWalk :: [Char] -> Bool
isValidWalk walk = case valid <$> take_exactly 10 walk of
                     Just bool -> bool
                     Nothing   -> False
