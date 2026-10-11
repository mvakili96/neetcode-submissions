class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        w_start = 0
        w_end = len(matrix[0])
        h_start = 0
        h_end = len(matrix)
        out = []
        while h_start < h_end and w_start < w_end:
            for i in range(w_start,w_end):
                out.append(matrix[h_start][i])
            h_start += 1
            for i in range(h_start,h_end):
                out.append(matrix[i][w_end-1])
            w_end -= 1
            if h_start < h_end:
                for i in range(w_end-1,w_start-1,-1):
                    out.append(matrix[h_end-1][i])
            h_end -= 1
            if w_start < w_end:
                for i in range(h_end-1,h_start-1,-1):
                    out.append(matrix[i][w_start])
            w_start += 1
        return out



            


            




        