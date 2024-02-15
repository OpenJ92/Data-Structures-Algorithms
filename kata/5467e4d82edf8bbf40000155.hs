module DescendingOrder where

import Data.List (sort)

digits :: Integer -> [Integer]
digits 0 = []
digits n = mod n 10 : digits (div n 10)

descendingOrder :: Integer -> Integer
descendingOrder = sum . zipWith (*) (iterate (*10) (1)) . sort . digits
