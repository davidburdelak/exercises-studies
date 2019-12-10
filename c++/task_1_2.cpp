#include <cstdlib>
#include <iostream>
#include <ctime>
#include <time.h>
#include<conio.h>
#include<dos.h>
#include <windows.h>
using namespace std;

void baner()
{ 
	cout <<" ===============================================================\n"
         <<"|              Program generuje liczby z przedzialu             |\n"
         <<"|                      ktory okreslisz                          |\n"
         <<"|---------------------------------------------------------------|\n"
         <<"|             WWSSE (C) 2019  Dawid Burdelak                    |\n"
         <<" ===============================================================\n\n";
}

int main(int argc, char *argv[])  
{     
	char znak;
	baner();
	int n;
	int min,max;
	int i=1;

	do 
	{
    	cout << "Wprowadz liczbe:"<<endl;
    	cin >> n;
    	cout << "Wprowadz liczbe minimalna:";
    	cin >> min;
		cout << "               maksymalna:";
		cin >> max;
		cout << "\n\n\n";
		// u¿y³em kolory bardziej kontrastowe, poniewa¿ niektórzy mog¹ mieæ ma³o wyraŸn¹ konsolê
		system("color 2f");
		system("color 0e");
		
		for (int i = 0; i<21; i++)
	{
		system("cls");
		cout << "Czekaj, trwa generowanie liczb..."<<i*5<<"%"<<endl;
		for (int z = 0; z<i;z++)
               cout << (char)219;
		for (int y = 0; y < 20 - i; y++)
		{
			cout << (char)177;
		}
		Sleep(250);
	}
	
		cout << endl << endl;

    	for (; i<=n;i++)
    		cout<<min+rand()%((max-min)+1)<<endl; 
	
		cout << " Czy chcesz kontynuowac? [T/N] ";
		cin >> znak;
		cout <<endl;
	}
    while (znak=='T' || znak=='t');         
    system("PAUSE");
    return EXIT_SUCCESS;
}


