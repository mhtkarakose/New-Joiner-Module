#ifndef READER_H
#define READER_H
#include <fstream>
#include <string>
#include <iostream>


using namespace std;
class Reader
{
    public:
        Reader();
        string ReadFile(char* filename);
    protected:
    private:
};

#endif // READER_H
