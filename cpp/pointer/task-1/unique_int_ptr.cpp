#include "unique_int_ptr.h"
#include <cstring>
#include <stdio.h>
#include <iostream>

using namespace std;

unique_int_ptr::unique_int_ptr(int * data)
{
    //ctor
    val = data;
}

int * unique_int_ptr::get()
{
    //cout << unique_int_ptr::val; // FOR TEST
    return unique_int_ptr::val;
}
