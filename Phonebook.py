#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{	char choice;
	int phone[10];
	int s[3];
		
	printf("Phonebook - Input your command(h for help)");
	scanf("%c",&choice);
	//while()
	switch(choice){
		case 'h':	printf("\ni - insert a phone number\nd - delete a phone number\nm - modify a phone number\ns - search\nx - exit program");
					break;
		case 'i':	printf("\nEnter a phone number to be inserted :");
					scanf("%d",&phone);
					break;
		case 'd':	printf("\nThe List is :");
					break;
		case 'm': 	printf("The List is :");
					break;
		case 's':	printf("Enter 3 digits to search:");
					scanf("%d %d %d",&s[0],&s[1],s[2]);
					break;
		case 'x':	break;
							
	}
}
