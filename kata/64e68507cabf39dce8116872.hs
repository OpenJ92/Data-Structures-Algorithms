-- module TargetSum (getNumbers) where
-- 
-- import Control.Applicative
-- import Control.Monad
-- 
-- difference :: Int -> Int -> Maybe Int
-- difference x y
--   | x >= y = Just $ x - y
--   | otherwise = Nothing
-- 
-- getNumbers :: [Int] -> Int -> Maybe [Int]
-- getNumbers _  0 = Just []
-- getNumbers [] _ = Nothing
-- getNumbers ns'@(n:ns) target
--   = ((:) <$> (Just n) <*> join (getNumbers ns' <$> (difference target n)))
--  <|> getNumbers ns target
-- 
--
module TargetSum (getNumbers) where

import Control.Applicative
import Control.Monad

difference :: Int -> Int -> Maybe Int
difference x y
  | x >= y = Just $ x - y
  | otherwise = Nothing

getNumbers :: [Int] -> Int -> Maybe [Int]
getNumbers _  0 = Just []
getNumbers [] _ = Nothing
getNumbers ns'@(n:ns) target
  = ((:) <$> (Just n) <*> (getNumbers ns' =<< difference target n))
 <|> getNumbers ns target

