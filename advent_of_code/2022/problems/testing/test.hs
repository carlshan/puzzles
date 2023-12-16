import qualified Data.Set as S

main = do
    let testing = "ABC"
    let testlist = ['a', 'b', 'c']
    let myset = S.fromList testing
    let myset2 = S.fromList testlist
    print testing
    print myset2