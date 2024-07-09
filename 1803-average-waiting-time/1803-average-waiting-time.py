class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish = customers[0][0] + customers[0][1]
        wait  = customers[0][1]
        for i in range(1, len(customers)):
            if finish > customers[i][0]:
                finish += customers[i][1]
                
            else:
                finish =  customers[i][0] + customers[i][1]
            wait += (finish - customers[i][0])
        return wait / len(customers)