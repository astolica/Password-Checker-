/*

Password Strength Checker 
Written by Alec Teran 
Will be updated as I learn more about C (pointers and whatnot)

*/

#include <stdlib.h>
#include <stdio.h>

#define MAX_LIMIT 128

int main(){
    
    printf("Enter your password: \n");
    char password[MAX_LIMIT];
    fgets(password, MAX_LIMIT, stdin);
    printf("Your password entered was %s Processing...\n", password);
    
}










