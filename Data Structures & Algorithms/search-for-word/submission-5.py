class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board[0]) * len(board):
            return False
        def dfs(prev_pos,current_pos,i):
            if i == len(word):
                return True

            goal = word[i]
            displacements = [[-1,0],[1,0],[0,-1],[0,1]]
            for dsp in displacements:
                destination_tmp = [x + y for x, y in zip(current_pos, dsp)]
                destination_tmp[0] = min(destination_tmp[0],len(board)-1)
                destination_tmp[0] = max(destination_tmp[0],0)
                destination_tmp[1] = min(destination_tmp[1],len(board[0])-1)
                destination_tmp[1] = max(destination_tmp[1],0)

                if destination_tmp != current_pos and destination_tmp != prev_pos and board[destination_tmp[0]][destination_tmp[1]] == goal:
                    output = dfs(current_pos,destination_tmp,i+1)
                    if output:
                        return output
            
            return False

        starts = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    starts.append([i,j])

        for curr in starts:
            out = dfs([-1,-1],curr,1)
            if out:
                return out
        
        return False


        