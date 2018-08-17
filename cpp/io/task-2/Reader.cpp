#include "Reader.h"
#include <fstream>
#include <string>
#include <iostream>

using namespace std;
Reader::Reader()
{
    //ctor
}

string Reader::ReadFile(char* filename){
    string line;
    ifstream myfile (filename);
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
        //cout << line << '\n';
            return line;
        }
        myfile.close();
    }
    else cout << "Unable to open file";
  }



