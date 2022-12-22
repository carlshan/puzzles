import System.IO
import Data.List
import Data.List.Split

{-
General Strategy:
1. Read in the file
2. Break the list up by whitespace, resulting in many lists
3. Make sure each element is an integer
4. Sum over all the sub-lists
5. Find the max of all sub-lists and return the max
-}

main = do
    let filename = "day1.data"
    day1data <- readFile filename
    let splitted = split (whenElt (== "")) (lines day1data)
    let nums = [map (\e -> read e :: Integer) x | x <- splitted, (\e -> e /= [""]) x]
    let totals = map sum nums

    -- Part 1
    print (maximum totals)

    -- Part 2
    print (sum (take 3 (reverse (sort totals))))