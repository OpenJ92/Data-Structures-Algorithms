module DigitalRoot where

digits :: Integral a => a -> [a]
digits number
 | number > 9 = mod number 10 : digits (div number 10)
 | otherwise = pure number

digitalRoot :: Integral a => a -> a
digitalRoot number
 | next > 9 = digitalRoot next
 | otherwise = next
 where
   next = sum . digits $ number
