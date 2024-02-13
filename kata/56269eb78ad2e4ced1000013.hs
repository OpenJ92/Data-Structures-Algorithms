module Perfect (findNextSquare) where

import Control.Monad

perfect_square :: Integer -> Maybe Integer
perfect_square n = let sq = floor $ sqrt $ (fromIntegral n::Double) in 
  case sq * sq == n of
    True  -> Just sq
    False -> Nothing

findNextSquare :: Integer -> Integer
findNextSquare n = case perfect_square n of 
  Just sq -> (sq + 1) ^ 2
  Nothing -> -1
