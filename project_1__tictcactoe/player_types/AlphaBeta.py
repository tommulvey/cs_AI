class AlphaBeta:
    def __init__(self, char):
        self.char = char
        self.kind = "AlphaBeta"
        if self.char == 'X':
            self.opponent = 'O'
        else :
            self.opponent = 'X'


    '''
    if node is a leaf node :
        return value of the node
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each child node :
            value = minimax(node, depth+1, false, alpha, beta)
            bestVal = max( bestVal, value) 
            alpha = max( alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else :
        bestVal = +INFINITY 
        for each child node :
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min( bestVal, value) 
            beta = min( beta, bestVal)
            if beta <= alpha:
                break
        return bestVal
    '''


    def move(self, board):
        '''
        run alpha beta pruning on board passed, choose best path.
        '''
        return
    

        
