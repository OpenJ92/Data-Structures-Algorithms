module MultiplesOf3And5 where

solution :: Integer -> Integer
solution number = (sum . filter (\x -> mod x 3 == 0 || mod x 5 == 0)) [1..number']
  where number' = number - 1
