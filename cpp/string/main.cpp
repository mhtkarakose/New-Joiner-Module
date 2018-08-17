#include <cstring>
#include <stdio.h>
#include <iostream>
#include "String.h"

#define TEST_TRUE(x) printf("Test '%s' %s\n", #x, (x) ? "passed" : "failed!")

/**
 * IMPORTANT
 *
 * This file should not be modified to pass the tests.
 */

using namespace std;

int main()
{
// 1  PAST
    String empty_string;
    TEST_TRUE(empty_string.empty());

    String empty_string2(NULL);
    TEST_TRUE(empty_string2.empty());

    String empty_string3("");
    TEST_TRUE(empty_string3.empty());

    String empty_string4 = "";
    TEST_TRUE(empty_string4.empty());
// 2
    //TEST_TRUE(empty_string.equals(empty_string2));
   // TEST_TRUE(empty_string2.equals(empty_string3));
   // TEST_TRUE(empty_string3.equals(empty_string4));
// 3 PAST
    cout << "" << endl;
    char const* hello_world_str = "Hello World";
    String string1 = hello_world_str;
    TEST_TRUE(string1.length() == 11);
    TEST_TRUE(string1.equals("Hello World"));
// 4 PAST
    cout << "" << endl;
    char const* char_ptr = string1.charArray();
    TEST_TRUE(char_ptr != hello_world_str);
// 5
    cout << "" << endl;
    string1.setCharAt(0, 'h');
    TEST_TRUE(string1.equals("hello World"));
    TEST_TRUE(string1.charArray() != hello_world_str);
    TEST_TRUE(strcmp(hello_world_str, "Hello World") == 0);
// 6
    cout << "" << endl;
    string1.clear();
    TEST_TRUE(string1.empty());
// 7
    cout << "" << endl;
    String string2("Foo");
    TEST_TRUE(string2.length() == 3);
// 8
    cout << "" << endl;
    char const* bar = "_bar";
    string2.append(bar);
    TEST_TRUE(string2.equals("Foo_bar"));
// 9
    cout << "" << endl;
    String string3("Foo_");
    TEST_TRUE(string3.length() == 4);
// 10
    cout << "" << endl;
    string3.append("bar");
    TEST_TRUE(string3.equals("Foo_bar"));
// 11
    cout << "" << endl;
    String string4 = "Hello";
    String string5 = string4;
    TEST_TRUE(string4.equals(string5));
    TEST_TRUE(string4.charArray() != string5.charArray());
// 12
    cout << "" << endl;
    String string6("not");
    String string7("equal");
    TEST_TRUE(!string6.equals(string7));
    return 0;
}
