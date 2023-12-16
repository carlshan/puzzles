import System.IO
import Data.List
import Data.List.Split


{-
Notes:
Rock: A, X (1 point)
Paper: B, Y (2 points)
Scissors: C, Z (3 points)

Strategy:
1. Convert A, B, C to 1, 2, 3
2. Convert X, Y, Z to 1, 2, 3
3. Subtract first column from the second.
    - If this result is exactly 1, then to the total score, add the second column + 6
    - If the result is exactly 0, then to the total score, add the second column + 3
    - Else add the second column
-}

map_to_ints :: String -> Integer
map_to_ints s | s == "A" || s == "X" = 0
              | s == "B" || s == "Y" = 1
              | s == "C" || s == "Z" = 2

-- Part 1
convert_to_points_part1 :: [Integer] -> Integer
convert_to_points_part1 l = snd + lose_draw_win where
    fst = head l
    snd = (head (tail l)) + 1
    diff = snd - fst
    lose_draw_win = (mod diff 3) * 3

-- Part 2
convert_to_points_part2 :: [Integer] -> Integer
convert_to_points_part2 l = points where
    fst = head l
    snd = (head (tail l))
    points = case snd of
        0 -> (mod (fst - 1) 3) + 1     -- Loss
        1 -> (fst + 1) + 3             -- Draw
        2 -> (mod (fst + 1) 3) + 1 + 6 -- Win


main = do
    let filename = "day2.data"
    daydata <- readFile filename
    let result = lines daydata -- i.e., ["A Z", "B X" ...]
    let split_results = map words result -- i.e. [["A", "Z"], ["B", "X"] ... ]
    let converted_to_nums = map (\l -> map map_to_ints l) split_results -- i.e. [[1, 3], [2, 1]]
    let points_part1 = map convert_to_points_part1 converted_to_nums
    print (sum points_part1)
    let points_part2 = map convert_to_points_part2 converted_to_nums
    print (sum points_part2)