class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        if(moves.count("L") == moves.count("R")):
            return moves.count("_")
        else:
            return abs(moves.count("L")-moves.count("R"))+moves.count("_")