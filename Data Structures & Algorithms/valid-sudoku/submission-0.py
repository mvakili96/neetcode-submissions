class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_ = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    dict_[(i,j)] = board[i][j]
        
        for key_1 in dict_:
            for key_2 in dict_:
                if key_1 == key_2:
                    continue
                
                if dict_[key_1] == dict_[key_2]:
                    if key_1[0] == key_2[0] or key_1[1] == key_2[1] or (key_1[0]//3 == key_2[0]//3 and key_1[1]//3 == key_2[1]//3):
                        return False
        
        return True




        