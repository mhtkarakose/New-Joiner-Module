#include <cstring>
#include <stdio.h>
#include <iostream>
#include <memory>
#define TEST_TRUE(x) printf("Test '%s' %s\n", #x, (x) ? "passed" : "failed!")
using namespace std;

struct SimpleData
{
	int first;
	char second;
};

template <class T>
class unique_int_ptr
{
    public:
        unique_int_ptr(SimpleData* data)
        {val = data;}
        int *  get();
    protected:
    private:
        SimpleData * val;
        SimpleData * val2;
};

template <class T>
int * unique_int_ptr<T>::get()
{
    //cout << unique_int_ptr::val; // FOR TEST
    return unique_int_ptr::val;
}

int main()
{
    SimpleData* data = new SimpleData;	// allocate raw pointer
	data->first = 55;
	data->second = 'C';

	// create a managed pointer and let it manage data
	unique_ptr<SimpleData>  data_ptr(data);

	// Make sure that both pointers show the same value
	TEST_TRUE(data->first == data_ptr->first);
	TEST_TRUE(data->second == data_ptr->second);

	// Both ways
	data_ptr->first = 99;
	data_ptr->second = 'D';
	TEST_TRUE(data->first == data_ptr->first);
	TEST_TRUE(data->second == data_ptr->second);

	unique_ptr<int> int_ptr(new int);
	*int_ptr = 199;

	// both allocations are released here

    return 0;
}

