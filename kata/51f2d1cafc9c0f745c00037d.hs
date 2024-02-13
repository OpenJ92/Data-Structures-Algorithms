module StringsEndsWith (solution) where

solution :: String -> String -> Bool
solution str ing = foldl (&&) True $ zipWith (==) str' ing'
  where 
    str' = reverse str
    ing' = reverse ing
       
