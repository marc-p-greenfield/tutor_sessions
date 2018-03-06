#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main ()
{
string name;
double propertyValue;
double taxrate;
double assessedValue;
double taxableValue;
double annualPropertyTax;
double quarterly;

cout << "Enter the actual value of the property: ";
cin>> propertyValue;
cout<< "Enter the taxerpayer's name : " ;
cin>> name;
cout << "Enter the tax rate for each $100 of the assessed value: ";
cin >> taxrate;

assessedValue=0.6*propertyValue;
taxableValue=assessedValue-5000;
annualPropertyTax=(taxableValue/100)*taxrate;
quarterly=annualPropertyTax/4;

cout<< "\n For taxpayer " << name << " The tax information is:";
cout<< fixed;
cout << setprecision (2);
cout << " \n Property Value:         $"<< right << setw(12) << propertyValue;
cout << " \n Assessed Value:         $"<< right << setw(12) << assessedValue;
cout << " \n Taxable Value:          $" << right << setw(12) << taxableValue;
cout << " \n Annual Property Tax:    $" << right << setw(12) << annualPropertyTax;
cout << " \n Quarterly Property Tax: $"<< right << setw (12) << quarterly;

return 0;

}
