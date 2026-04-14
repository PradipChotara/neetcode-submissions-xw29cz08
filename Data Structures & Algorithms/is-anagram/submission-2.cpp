class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())
        {
            return false;
        }
        std::unordered_map<char,int> map;
        for(char c : s)
        {
            auto it = map.find(c);
            if(it == map.end())
            {
                map.insert({c,1});
            }
            else
            {
                it->second++;
            }
        }
        for(char c : t)
        {
            auto it = map.find(c);
            if(it == map.end())
            {
                return false;
            }
            else
            {
                it->second--;
            }
        }
        for(auto it=map.begin() ; it!=map.end() ; it++)
        {
            if(it->second != 0)
            {
                return false;
            }
        }
        return true;
    }
};
