#ifndef STRING_H
#define STRING_H


using namespace std;

class String
{
    public:
        String();
        //String(char* value);
        String(char const* value);
        int empty(void);
        int equals(char* value);
        int equals(String  value);
        int length();
        char const* charArray();
        void setCharAt(int num, char val);
        void clear();
        void append(char const* value);
        char getVal();
        static char arrr;
    protected:
    private:
        char * arr;

};





#endif // STRING_H
