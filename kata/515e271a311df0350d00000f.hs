module SquareSum where

square :: Integer -> Integer
square x = x ^ 2

squareSum :: [Integer] -> Integer
squareSum = sum . map square
