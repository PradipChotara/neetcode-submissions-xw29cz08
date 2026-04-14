class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length())
        {
            return false;
        }
        std::unordered_map<char,int> map ;
        for(char c : s)
        {
            if(map.count(c))
            {
                map[c] = map[c]+1;
            }
            else
            {
                map.insert({c,1});
            }
        }
        for(char c : t)
        {
            if(map.count(c)==0 || map[c]==0)
            {
                return false;
            }
            map[c] = map[c]-1;
        }
        return true;
    }
};
