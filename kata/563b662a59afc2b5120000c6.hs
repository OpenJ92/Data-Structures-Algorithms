module Codewars.G964.Arge where

update_population percent aug population  = population * (1 + percent) + aug

nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p = length $ takeWhile (<p') (iterate change p0')
  where
    p'   = fromIntegral p
    p0'  = fromIntegral p0
    aug' = fromIntegral aug
    percent' = percent / 100 
    change population = update_population percent' aug' population
