#include <fstream>
#include <string>
#include <iostream>
#include "Reader.h"
#include "Writer.h"

using namespace std;

int main()
{
    string input; char* filename;
    cout << "The user enters text from keyboard: ";
    cin >> input;

    cout << "File writing " ;
    Writer _writer; filename = "output.txt";
    _writer.WriteFile(input, filename);
    cout << "- END"<< endl;

    cout << "File reading " << endl;
    Reader _reader;
    string FileVal =_reader.ReadFile(filename);
    cout << "The user entered = " << FileVal ;
    cout << " - END"<< endl;

    cout << "File copying... " << endl;
    filename = "output-copy.txt";
    _writer.WriteFile(FileVal,filename);
    string CopyFileVal = _reader.ReadFile(filename);
    cout << "The copyied file val = " << CopyFileVal ;
    cout << " - END"<< endl;

    return 0;
}
