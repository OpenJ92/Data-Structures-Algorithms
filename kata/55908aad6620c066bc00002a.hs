module Codewars.Kata.XO where

import Data.Char

-- | Returns true if the number of
-- Xs is equal to the number of Os
-- (case-insensitive)

check :: Integer -> Integer -> String -> Bool
check x o [] = x == o
check x o (current:tail) 
  | current == 'x' = check (x+1) o tail
  | current == 'o' = check x (o+1) tail
  | otherwise      = check x o tail

xo :: String -> Bool
xo str = check 0 0 $ toLower <$> str
