class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        example: [5, 10, 5, 5, 20]

        
        """
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
                continue
            elif bill == 10:
                ten += 1
                if five > 0:
                    five -= 1
                    continue
                else:
                    return False

            # dont have enough money to return
            if five * 5 + ten * 10 < 15:
                return False
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif ten <= 0 and five >= 3:
                    five -= 3
                else:
                    return False
        
        return True





            


            



            
