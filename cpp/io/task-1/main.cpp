#include <iostream>

using namespace std;

class IReader{
    public:
         void getRead();

};

class Keyboard : IReader{
    public:
        void getRead(){
            cout << "Keyboard Read" << endl;
        }
};

class IO : IReader{
    public:
        void getRead(){
            cout << "IO Read" << endl;
        }
};

int main(void){

    Keyboard keyboard;
    IO io;

    keyboard.getRead();
    io.getRead();

    return 0;
}
