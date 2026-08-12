class Solution:
    
    def doOverlap(self, L1, R1, L2, R2):
      if(R1[0]< L2[0] or L1[0] > R2[0] or R1[1] > L2[1] or R2[1] > L1[1]  ):
          print("Rectangles does not overlap")
      else:
          print("Rectangle overlaps")
      
a = Solution()
a.doOverlap((0,10),(10,0),(5,5),(15,0))