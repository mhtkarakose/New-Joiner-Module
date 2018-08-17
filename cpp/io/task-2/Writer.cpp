#include "Writer.h"
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

Writer::Writer()
{
    //ctor
}

void Writer::WriteFile(string value, char* filename)
{
char* name = filename;
    ofstream out(name);
    out << value;
    out.close();
}
