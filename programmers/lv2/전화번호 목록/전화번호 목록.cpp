#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    vector<int> intPhone_book;
    for(int i = 0; i < phone_book.size(); i++)
    {
        intPhone_book.push_back(stoi(phone_book[i]));
    }
    sort(intPhone_book.begin(), intPhone_book.end());
    vector<string> phn_bk;
    for(int i = 0; i < intPhone_book.size(); i++)
    {
        phn_bk.push_back(to_string(intPhone_book[i]));
    }

    for(int idx = 0; idx<phn_bk.size()-1 ; idx++)
    {
        for(int i = idx+1; i < phn_bk.size(); i++)
        {
            for(int j = 0; j < phn_bk[idx].length();)
            {
                if(phn_bk[idx][j] == phn_bk[i][j])
                {
                    //cout<<phn_bk[idx][j]<<" "<<phn_bk[i][j]<<endl;
                    j++;
                }
                else
                {
                    //cout<<phn_bk[idx][j]<<" "<<phn_bk[i][j]<<endl;;
                    break;
                }
                if(j == phn_bk[idx].length())
                {
                    //cout<<"접두"<<endl;
                    answer = false;
                }
            }
        }
    }
    return answer;
}