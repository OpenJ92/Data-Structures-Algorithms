module Vowel where

import Data.Map as Map

vowels :: Map Int String
vowels = fromList [ (117, "u")
                  , (101, "e")
                  , (105, "i")
                  , ( 97, "a")
                  , (111, "o")
                  ]

convert :: Map Int String -> Int -> Either Int String
convert hash code = case Map.lookup code hash of
  (Just vowel) -> Right vowel
  Nothing      -> Left code

isVow :: [Int] -> [Either Int String]
isVow ns = convert vowels <$> ns
