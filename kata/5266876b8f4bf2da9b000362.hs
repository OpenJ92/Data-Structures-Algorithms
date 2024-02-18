module Likes where

likes :: [String] -> String
likes []                      = "no one likes this"
likes (first:[])              = first ++ " likes this"
likes (first:second:[])       = first ++ " and " ++ second ++ " like this"
likes (first:second:third:[]) = first ++ ", " ++ second ++  " and " ++ third ++ " like this"
likes (first:second:string)   = first ++ ", " ++ second ++ " and " ++ show (length string) ++ " others like this"
