module MultiplesOf3And5 where

solution :: Integer -> Integer
solution = sum 
         . filter (\x -> mod x 3 == 0 || mod x 5 == 0)
         . flip take (iterate (+1) 1)
         . fromIntegral
         . subtract 1
