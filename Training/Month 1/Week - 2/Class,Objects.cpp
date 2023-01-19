#include <iostream>
using namespace std;
class Phone {
public:
	double cost;
	int slots;
};
int main() {
	Phone P1;
	Phone P2;

	P1.cost = 100.0;
	P1.slots = 2;

	P2.cost = 200.0;
	P2.slots = 2;
	cout << "Cost of Phone 1 : " << P1.cost << endl;
	cout << "Cost of Phone 2 : " << P2.cost << endl;

	cout << "Number of card slots for Phone 1 : " << P1.slots << endl;
	cout << "Number of card slots for Phone 2 : " << P2.slots << endl;

	return 0;
}