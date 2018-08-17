#ifndef UNIQUE_INT_PTR_H
#define UNIQUE_INT_PTR_H

using namespace std;


class unique_int_ptr
{
    public:
        unique_int_ptr(int * data);
        int * get();
    protected:
    private:
        int * val;
        int * val2;
};

#endif // UNIQUE_INT_PTR_H
