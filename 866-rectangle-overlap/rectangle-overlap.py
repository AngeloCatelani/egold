class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Determine if two rectangles overlap.
      
        The rectangles are defined by their bottom-left and top-right corners:
        rec1 corresponds to (x1, y1, x2, y2)
        rec2 corresponds to (x3, y3, x4, y4)
      
        We return True if the rectangles overlap, False otherwise.
        """
      
        # Unpack coordinates for the first rectangle
        x1, y1, x2, y2 = rec1
      
        # Unpack coordinates for the second rectangle
        x3, y3, x4, y4 = rec2
      
        # Check for overlap:
        # There is no overlap if:
        # - The top edge of rec2 is below or on the bottom edge of rec1 (y3 >= y2)
        # - The bottom edge of rec2 is above or on the top edge of rec1 (y4 <= y1)
        # - The right edge of rec2 is to the left or on the left edge of rec1 (x3 >= x2)
        # - The left edge of rec2 is to the right or on the right edge of rec1 (x4 <= x1)
        # If none of these conditions are met, the rectangles overlap.
      
        return not (y3 >= y2 or y4 <= y1 or x3 >= x2 or x4 <= x1)