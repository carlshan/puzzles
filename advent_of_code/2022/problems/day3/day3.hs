import System.IO
import Data.List
import Data.List.Split
import qualified Data.Set as S


get_intersection t = do
    let (f, s) = t
    let common = S.intersection (S.fromList f) (S.fromList s)
    return common

{-
Split the string into halves

Part 1:
- For each element that consists of a tuple, turn both into sets
- Find the intersection of the two sets

-}

main = do
    let filename = "day3.test"
    daydata <- readFile filename
    let result = lines daydata
    let halves = map (\s -> splitAt (length s `div` 2) s) result
    let common = map (\s -> get_intersection s) halves
    print result