#ifndef WRITER_H
#define WRITER_H
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

class Writer
{
    public:
        Writer();
        void WriteFile(string value, char* filename);
    protected:
    private:
};

#endif // WRITER_H
