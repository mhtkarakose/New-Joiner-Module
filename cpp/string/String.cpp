#include "String.h"
#include <cstring>
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

String::String()
{
    arr = "";
}

String::String(char const* abc)
{

    if(abc == NULL || abc == "" || abc == '\0')
    {
        arr = "";
    }else{
        arr = new char[11];
        int i=0;
        while(abc[i]){
            arr[i] = abc[i];
            i++;
        }
    }
}
int String::empty()
{
    if(arr == ""){ // empty_string
        return 1;
    }
    else if (arr == NULL){ // empty_string2=
        return 1;
    }else if (arr[0] == '\0'){ // empty_string3-4
        return 1;
    }else{
        return 0;
    }
}



int String::equals(String val){

    cout << val.getVal();
/*
    int i=0,j=0;
    while(arr[i]){
        if(arr[i] == buf[i]){
            i++;
        }else{
            j++;
            break;
        }
    }
    cout<< buf << endl;

    if(j == 0){
        return 1;
    }else{
        return 0;
    }*/
}
char getVal(){
    return String::arrr;
}

int String::equals(char* val){

    //cout << val << endl;
    //cout << arr << endl;

    int i=0,j=0;
    while(arr[i]){
        if(arr[i] == val[i]){
            i++;
        }else{
            j++;
            break;
        }
    }
    cout<< val << endl;

    if(j == 0){
        return 1;
    }else{
        return 0;
    }
}

int String::length(){

    int i = 0;
    while (arr[i])
    {
        i++;
    }

    return i;
}

char const* String::charArray(){
    int i=0;
    while(arr[i]){
        //cout << arr[i] << endl;
        i++;
    }
    return arr;
}

void String::setCharAt(int num, char val){

    arr[num] = val;
}

void String::clear(){
    //arr[0] = '\0';
    arr = "";
    cout << arr[1];
}

void String::append(char const* value){
/*
ANLAMADIM GECIO
    int i = 0;
    while (value[i])
    {
        i++;
    }
    int j = 0;
    while (arr[j])
    {
        j++;
    }
    int bufSize = i + j;
    char * buffer = new char[bufSize];

    int z;
    for(z = 0; z < i; z++){
        buffer[z] = arr[z];
    }

    for(z = 0; z < bufSize; z++){
        buffer[z] = value[z];
    }
*/
}













