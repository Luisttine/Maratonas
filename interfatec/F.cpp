#include <iostream>
#include <unordered_map>
using namespace std;
unordered_map<char, char> umap = {{'A','A'}, {'E','3'}, {'H','H'}, {'I','I'}, {'J','L'}, {'L','J'}, {'M','M'}, {'N','N'}, {'O','O'}, {'S','2'}, {'T','T'}, {'U','U'}, {'V','V'}, {'W','W'}, {'X','X'}, {'Y','Y'}, {'Z','5'}, {'1','1'}, {'2','S'}, {'3','E'}, {'5','z'}, {'8','8'}};

bool is_palindrome(string s){
    bool is_true = true;
    for(int i=0;i<(s.size()+1)/2;i++){
        is_true &= s[i] == s[s.size()-i-1];
    }
    return is_true;
}

bool is_mirror(string s){
    bool is_true = true;
    for(int i=0;i<(s.size()+1)/2;i++){
        is_true &= s[i] == s[s.size()-i-1];
    }
    return is_true;
}

int main(){
    string s;
    while(cin >> s){
        bool is_p = is_palindrome(s);
        bool is_m = is_mirror(s);
        if(is_p && is_m){
            cout << s << " -- is a mirrored palindrome." << endl;
        } 
        else if(is_p){
            cout << s << " -- is a regular palindrome." << endl;
        } 
        else if(is_m){
            cout << s << " -- is a mirrored string." << endl;
        } 
        else{
            cout << s << " -- is not a palindrome." << endl;
        } 
    }
}
