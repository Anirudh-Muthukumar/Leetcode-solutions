def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ct = 0
        
        for num1 in arr1:
            res = 1
            for num2 in arr2:
                if abs(num1-num2)<=d:
                    res = 0
                    break
            ct += res
        
        return ct