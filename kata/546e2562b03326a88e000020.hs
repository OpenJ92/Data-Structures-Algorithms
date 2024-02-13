module SquareDigit where
import Data.Char

squareDigit :: Int -> Int
squareDigit k = let (parity, number) = extract_parity k in
  case evaluate <$> valid number of
    Just n  -> parity * n
    Nothing -> k
  where
    evaluate = display . transform
    display    = read . concat . map show
    transform  = reverse . map (^2) . digits

digits :: Int -> [Int]
digits 0 = []
digits n = mod n 10 : digits (div n 10)

extract_parity :: Int -> (Int, Int)
extract_parity n
  | n < 0 = (-1, abs(n))
  | n >= 0 = (1, n)

valid :: Int -> Maybe Int
valid n
  | n <= 0    = Nothing
  | otherwise = Just n
