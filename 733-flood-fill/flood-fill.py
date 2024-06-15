class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        def fill(image, sr, sc, color, original):
            row = len(image)
            col = len(image[0])
            if sr < 0 or sr >= row or sc >= col or sc < 0 or image[sr][sc] != original:
                return

            image[sr][sc] = color

            fill(image, sr+1, sc, color, original)
            fill(image, sr-1, sc, color, original)
            fill(image, sr, sc+1, color, original)
            fill(image, sr, sc-1, color, original)
            
        fill(image, sr, sc, color, image[sr][sc])
        return image