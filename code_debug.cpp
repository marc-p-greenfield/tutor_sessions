#include <iostream>
#include <sstream>
#include <string>
#define BR cout << "\n\n";
using std::cin;
using std::cout;
using std::endl;
using std::stringstream;
using std::string;

class Rational
{
	private:
		int n, d;
		Rational(int a, bool b) : n(a), d(a) {};
	public:
		Rational() : n(0), d(1) {};
		Rational(int wholeNumber) : n(wholeNumber), d(1) {};
		Rational(int numberator, int denominator) : n(numberator), d(denominator){};

		bool operator==(const Rational& rhs);
		bool operator<=(const Rational& rhs);
		bool operator>=(const Rational& rhs);
		bool operator>(const Rational& rhs);
		bool operator<(const Rational& rhs);
		Rational operator+(const Rational& rhs) const;
		Rational operator*(const Rational& rhs) const;
		Rational operator-(const Rational& rhs) const;
		Rational operator/(const Rational& rhs) const;
		friend std::ostream& operator << (std::ostream &o, const Rational &r);
		friend std::istream& operator >> (std::istream &in, Rational &r);
};

int main()
{
	Rational r1,r2;
	cout << "Enter two rational numbers in the form n/d separated by a space: ";
	cin >> r1 >> r2;
	cout << "\nThe rational numbers are " << r1 << " and " << r2 << endl << endl;
	string equals = (r1 == r2) ? "true":"false";
	string lteq = (r1 <= r2) ? "true":"false";
	string gteq = (r1 >= r2) ? "true":"false";
	string lt = (r1 < r2) ? "true":"false";
	string gt = (r1 > r2) ? "true":"false";
	Rational times = r1 * r2;
	Rational div = r1 / r2;
	Rational plus = r1 + r2;
	Rational minus = r1 - r2;
	cout<<r1<<" equals " << r2 << " is "<< equals<<endl;
	cout<<r1<<" less than or equal to "<< r2 << " is " << lteq << endl;
	cout<<r1<<" greater than or equal to "<< r2 <<" is " << gteq << endl;
	cout<<r1<<" less than " << r2 << " is " << lt << endl;
	cout<<r1<<" greater than "<< r2 << " is " << gt << endl;
	cout<<r1<<" plus " << r2 << " is " << plus << endl;
	cout<<r1<<" times " << r2 << " is " << times << endl;
	cout<<r1<<" divided by " << r2 << " is " << div << endl;
	cout<<r1<<" minus " << r2 << " is " << minus << endl;

	return 0;
}

bool Rational::operator==(const Rational& rhs)
{
	if ((rhs.n == this->n)&&(rhs.d == this->d))
	return true;
	else
	return false;
}
bool Rational::operator<=(const Rational& rhs)
{
	if(*this == rhs)
	return true;
	if(*this < rhs)
	return true;

	return false;
}
bool Rational::operator>=(const Rational& rhs)
{
	if(*this == rhs)
	return true;
	if(*this > rhs)
	return true;

	return false;
}
bool Rational::operator<(const Rational& rhs)
{
	int tempL, tempR;
	if((this->d == rhs.d)&&(this->n<rhs.n))
	return true;

	tempL = this->n*rhs.d;
	tempR = this->d*rhs.n;
	return (tempL<tempR);
}
bool Rational::operator>(const Rational& rhs)
{
	int tempL, tempR;
	if((this->d == rhs.d)&&(this->n>rhs.n))
	return true;

	tempL = this->n*rhs.d;
	tempR = this->d*rhs.n;
	return (tempL > tempR);
}
Rational Rational::operator+(const Rational& rhs)const
{
	Rational out, temp1 = *this, temp2 = rhs;
	if(temp1.d != temp2.d)
	{
		temp1 = *this * Rational(rhs.d, true);
		temp2 = rhs * Rational(this->d, true);
	}
	out.d = temp1.d;
	out.n = temp1.n + temp2.n;

	return out;
}
Rational Rational::operator-(const Rational& rhs)const
{
	Rational out, temp1 = *this, temp2 = rhs;

	if (temp1.d != temp2.d)
	{
		temp1 = *this *Rational(rhs.d, true);
		temp2 = rhs * Rational(this ->d, true);
	}

	out.d = temp1.d;
	out.n = temp1.n-temp2.n;
	return out;
}
Rational Rational::operator*(const Rational& rhs)const
{
	Rational out;

	out.n = this->n * rhs.n;
	out.d = this->d* rhs.d;

	return out;
}
Rational Rational::operator/(const Rational& rhs)const
{
	Rational out;
	Rational tempR = *this;
	int tempN;

	tempN = tempR.n;
	tempR.n = tempR.d;
	tempR.d = tempN;
	out = tempR * rhs;

	return out;
}
std::ostream& operator<<(std::ostream&o, const Rational&r)
{
	o<<r.n<<"/"<<r.d;
	return o;
}
std::istream& operator>>(std::istream&in, Rational&r)
{
	string tempString;
	int tempInt1, tempInt2;
	stringstream ss;
	std::getline(in, tempString, '/');
	in>>tempInt2;
	ss<<tempString;
	ss>>tempInt1;

	r.n=tempInt1;
	r.d=tempInt2;

	return in;
}
