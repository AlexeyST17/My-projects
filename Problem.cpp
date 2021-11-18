#include <iostream>
#include<cmath>
#include<vector>
#include<string>
#include<random>
#include<ctime>
#include "D:/gnuplot-cpp/gnuplot_i.hpp"
using namespace std;

void Graph(vector<double>P, vector<int>k);
long double Fuctorial(int k) {
	if (k < 0) {
		cout << "k<0" << endl;
		exit(1);
	};
	if (k == 0) {
		return 1;
	};
	return k * Fuctorial(k - 1);
}
void Molecules(double V0, double V, int N0) {
	srand(time(NULL));
	double p = V / V0;
	double q = 1 - p;
	vector<double>P;
	vector<int>count;
	count.resize(N0 + 1);
	P.resize(N0 + 1);
	for (int i = 0; i < N0; i++) {
		P[i] = (Fuctorial(N0) / (Fuctorial(i) * Fuctorial(N0 - i))) * pow(p, i) * pow(q, N0 - i);
		count[i] = i;
	};
	double sum = 0;
	//int c = 0;
	for (auto el : P) {
		//cout <<c<<": "<< el << endl;
		sum += el;
		//c++;
	}
	cout <<"sum binom = "<< sum << endl;
	count.shrink_to_fit();
	P.shrink_to_fit();
	Graph(P, count);
}
void Graph(vector<double>P, vector<int>k) {
	Gnuplot g1;
	g1.set_style("lines");
	g1.plot_xy(k, P, "ajkshkd");
	system("pause");

}
long double Coeff(int N, int m,double V,double V0){
	return ((N-m)*V)/((m+1)*(V0-V));
}
void Raspred(double V0, double V, int N0) {
	vector<double>P;
	double p = V / V0;
	vector<int>k;
	k.resize(N0 + 1);
	P.resize(N0 + 1);
	P[0] = pow((V0- V)/V0, N0);
	for (int i = 0; i < N0; i++) {
		P[i + 1] = P[i] * Coeff(N0,i,V,V0);
		k[i] = i;
	}
	double sum = 0;
	//int c = 0;
	for (auto el : P) {
		//cout <<c<<": "<< el << endl;
		sum += el;
		//c++;
	}
	cout <<"sum recul = "<< sum << endl;
	P.shrink_to_fit();
	k.shrink_to_fit();
	Graph(P, k);

}
int GenBin(int N, double p) {
	int ext = 0;
	for (int i = 1; i <= N; i++) {
		if (p - (double)rand() / RAND_MAX > 0)
			ext++;
	}
	return ext;
}
void Ensemble(double V0, double V, int m, int k) {
	srand(time(NULL));
	double p = V/V0;
	vector<double>pi;
	vector<int>count;
	count.resize(m + 1);
	pi.resize(k + 1);
	for (int i = 0; i < k; i++) {
		pi[i] = (GenBin(m, p));
	}
	for (int i = 0; i <= m; i++) {
		for (auto el : pi) {
			if (el == i) {
				count[i] += 1;
			}
		}
	}
	vector<int>mol;
	mol.resize(m + 1);
	for (int i = 0; i <= m; i++) {
		mol[i] = i;
	}
	Gnuplot g1;
	g1.set_style("points");
	g1.plot_xy(mol, count);
	system("pause");
}
int main()
{
	setlocale(LC_ALL, "ru");
	double V0;
	double V;
	int n,k;
	cout << "Начальный объем V0 = ";
	cin >> V0;
	cout << "Выделенный объем V = ";
	cin >> V;
	cout << "Количество молекул n = ";
	cin >> n;
	cout << "Количество испытаний k = ";
	cin >> k;
	//Molecules(V0, V, n);
	//Raspred(V0, V, n);
	Ensemble(V0, V, n, k);
	return 0;
}
