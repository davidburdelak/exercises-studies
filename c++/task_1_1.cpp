#include <iostream>
#include <time.h>
 
using namespace std;
void baner()
{ 
	cout <<" ===============================================================\n"
         <<"|      Program rozwiazuje uklady rownan z dwoma niewiadomymi    |\n"
         <<"|---------------------------------------------------------------|\n"
         <<"|             WWSSE (C) 2019  Dawid Burdelak                    |\n"
         <<" ===============================================================\n\n";
}

int main(int argc, char *argv[])  
{     
	char znak;
	double a1,a2,b1,b2,c1,c2,wyznacznik_x,wyznacznik_y,wyznacznik_glowny,x,y;
    baner();
	do 
	{
		cout<<"Podaj a1: ";
		cin>>a1;
		cout<<"Podaj b1: ";
		cin>>b1;
		cout<<"Podaj c1: ";
		cin>>c1;
		cout<<"Podaj a2: ";
		cin>>a2;
		cout<<"Podaj b2: ";
		cin>>b2;
		cout<<"Podaj c2: ";
		cin>>c2;

		wyznacznik_glowny = a1*b2 - b1*a2;
		wyznacznik_x = c1*b2 - b1*c2;
		wyznacznik_y = a1*c2 - c1*a2;
		
			if(wyznacznik_glowny!=0) 
			{
				cout<<"x = "<<wyznacznik_x/wyznacznik_glowny<<endl;
				cout<<"y = "<<wyznacznik_y/wyznacznik_glowny<<endl;
			} 
			else if(wyznacznik_x==0&&wyznacznik_y==0) 
			{
				cout<<"Uklad ma nieskonczenie wiele rozwiazan"<<endl;
			}
			else 
			{
				cout<<"Uklad jest sprzeczny"<<endl;
			}
    	
			cout << " Czy chcesz kontynuowac? [T/N] ";
			cin >> znak;
			out <<endl;
	}
    while (znak=='T' || znak=='t');         
    system("PAUSE");
}
