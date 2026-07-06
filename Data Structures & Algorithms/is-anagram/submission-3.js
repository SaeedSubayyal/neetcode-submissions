class Solution {

    isAnagram(s, t) {

        //base check
        if (s.length != t.length){
            return false;
        }

        let s_dict = {};
        let t_dict = {};

        for (const char of s){
            if (char in s_dict){
            s_dict[char] ++;
            }
            else {
             s_dict[char] = 1;
            }
        }
        
        for (const char of t){
            if (char in t_dict){
                t_dict[char]++;
            }
            else{
                t_dict[char] = 1; 
            }
        }

        for (const key in t_dict){
            if (s_dict[key] !== t_dict[key]){
                return false;
            }
        }
        return true;
    }
}
