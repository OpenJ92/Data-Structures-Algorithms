module Codewars.Kata.Compare where

import Data.Map (insertWith, empty, Map)

insert' :: (Ord k, Num a) => k -> Map k a -> Map k a
insert' key = insertWith (+) key 1

make_counter :: (Ord a, Num a) => [a] -> Map a Int
make_counter [     ] = empty
make_counter numbers = foldl1 (.) (insert' <$> numbers) empty

comp :: [Integer] -> [Integer] -> Bool
comp as bs = counter == counter'
  where
    counter  = make_counter ((^2) <$> as)
    counter' = make_counter bs
