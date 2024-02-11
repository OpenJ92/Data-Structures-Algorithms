module Disemvowel where

vowel :: Char -> Bool
vowel char = elem char "aeiouAEIOU"

disemvowel :: String -> String
disemvowel = filter (not . vowel)
