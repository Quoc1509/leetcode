class Solution {
public:
    string intToRoman(int num) {
        int number[] = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        string sym[] = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        string result;
        int i = 12;
        while(num > 0)
        {
            int a = num / number[i];
            num %= number[i];
            while(a > 0)
            {
                result += sym[i];
                a--;
            }
            i--;
        }
        return result;
    }
};