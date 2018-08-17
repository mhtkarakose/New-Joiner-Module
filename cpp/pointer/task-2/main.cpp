#include <cstring>
#include <stdio.h>
#include <iostream>
#define TEST_TRUE(x) printf("Test '%s' %s\n", #x, (x) ? "passed" : "failed!")
using namespace std;

template <class T>
class unique_int_ptr
{
    public:
        unique_int_ptr(int * data)
        {val = data;}
        int * get();
    protected:
    private:
        int * val;
        int * val2;
};

template <class T>
int * unique_int_ptr<T>::get()
{
    //cout << unique_int_ptr::val; // FOR TEST
    return unique_int_ptr::val;
}

int main()
{
    int* data = new int(55);	// allocate raw pointer
    // create a managed pointer and let it manage data
	unique_int_ptr <int *> data_ptr(data);

    //cout << data << endl;  // FOR TEST

	// Make sure that both pointers show the same value
	TEST_TRUE(*data == *(data_ptr.get()));

	// Both ways
	cout << *(data_ptr.get()) << endl;
	*(data_ptr.get()) = 99;
	cout << *(data_ptr.get()) << endl;
	TEST_TRUE(*data == *(data_ptr.get()));
	cout << *(data_ptr.get()) << endl;
	cout << *data << endl;


    return 0;
}
