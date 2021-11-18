// Интеграл.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include "pch.h"
#include <iostream>
#include<cmath>
#include<vector>
#include<ctime>
using namespace std;
double Func(double x) {
	double y;  //y=(x^2-1)
	y=sin(x);
	return y;
}
double IntegrationTra(double a,double b,int n) {
	double h = abs((a - b) / n);
	double res = 0;
	vector<double>x;
	if (a < b) {
		x.push_back(a);
		double tmp = x[0];
		while (tmp < b) {
			tmp += h;
			x.push_back(tmp);
		};
		res += (Func(a) + Func(b)) / 2;
		for (int i = 1; i < x.size() - 1; i++) {
			res += Func(x[i]);
		};
		res *= h;
	}
	else {
		x.push_back(b);
		double tmp = x[0];
		while (tmp < a) {
			tmp += h;
			x.push_back(tmp);
		};
		res += (Func(x[0]) + Func(x[x.size() - 1])) / 2;
		for (int i = 1; i < x.size() - 1; i++) {
			res += Func(x[i]);
		};
		res *= h;
	};
	return res;
};
double IntegrationRec(double a, double b,int n) {
	double h =abs((a-b)/n);
	double res = 0;
	vector<double>x;
	if (a < b) {
		x.push_back(a);
		double tmp = x[0];
		while (tmp <= b) {
			x.push_back(tmp);
			tmp += h;
		};
		for (int i = 0; i < x.size(); i++) {
			res += Func(x[i]);
		};
		res *= h;
	}
	else {
		x.push_back(b);
		double tmp = x[0];
		while (tmp <= a) {
			x.push_back(tmp);
			tmp += h;
		};
		for (int i = 0; i < x.size(); i++) {
			res += Func(x[i]);
		};
		res *= h;
	};

	return res;
}
double IntegrationSim(double a, double b, int n) {

	double h = abs((b-a) / n);
	double res = 0;
	vector<double>x;
	if (a < b) {
		x.push_back(a);
		double tmp = x[0];
		while (tmp < b) {
			tmp += h;
			x.push_back(tmp);
		};
		res += Func(a) + Func(b);
		double tmp1 = 0;
		for (int i = 1; 2 * i < x.size(); i++) {
			tmp1 += Func(x[2 * i - 1]);
		};
		double tmp2 = 0;
		for (int i = 2; 2 * i < x.size(); i++) {
			tmp2 += Func(x[2 * i - 2]);
		};
		res += 4 * tmp1 + 2 * tmp2;
		res *= h / 3;
	}
	else {
		x.push_back(b);
		double tmp = x[0];
		while (tmp < a) {
			tmp += h;
			x.push_back(tmp);
		};
		res += Func(a) + Func(b);
		double tmp1 = 0;
		for (int i = 1; 2 * i < x.size(); i++) {
			tmp1 += Func(x[2 * i - 1]);
		};
		double tmp2 = 0;
		for (int i = 2; 2 * i < x.size(); i++) {
			tmp2 += Func(x[2 * i - 2]);
		};
		res += 4 * tmp1 + 2 * tmp2;
		res *= h / 3;
	}
	return res;
}
double IntegrationM_C(double a, double b, double n) {
	double res = 0;
	if (a < b) {
		double step = 0.01;
		double xi = a;
		double fmin =0;
		double fmax=Func(a);
		while (xi < b) {
			xi += step;
			if (fmax < Func(xi)) {
				fmax = Func(xi);
			}
			else {
				if (fmin > Func(xi)) {
					fmin = Func(xi);
				}
			}
		}
		double S1 =(fmax-fmin)*(b - a);
		double *x = new double[n];
		double *y = new double[n];
		int count = 0;
		for (int i = 0; i < n; i++) {
			x[i]=( a + (b - a)*rand());
			y[i] =(rand()%(int)(fmax-fmin));
			if (y[i] < Func(x[i])) {
				count++;
			}
		};
		res = S1*count / n;
		delete []x;
		delete []y;
	}
	
	return res;
}
void Show_row(int i, double *R) {
	cout<<"R["<<i<<",i]=";
	for (size_t j = 0; j <= i; ++j) {
		cout<<R[j]<<" ";
	}
	cout << endl;
}
double IntegrationRomberg(double a, double b, int n, double eps) {
	double *R1 = new double[n];
	double *R2 = new double[n];	
	double *Rp = &R1[0], *Rc = &R2[0]; //Rp предыдущий, Rc текущий
	double h = (b - a); //шаг
	Rp[0] = (Func(a) + Func(b))*h*0.5; //первый шаг
	Show_row(0, Rp);
	//int count = 0;
	for (int i = 1; i < n; ++i) {
		h /= 2.;
		double c = 0;
		int ep = 1 << (i - 1); //2^(n-1)
		for (int j = 1; j <= ep; ++j) {
			c += Func(a + (2 * j - 1)*h);
		}
		Rc[0] = h * c + 0.5*Rp[0]; //R(i,0)

		for (int j = 1; j <= i; ++j) {
			double n_k = pow(4, j);
			Rc[j] = (n_k*Rc[j - 1] - Rp[j - 1]) / (n_k - 1); // R(i,j)
		}
		Show_row(i, Rc);
		if (i > 1 && abs(Rp[i - 1] - Rc[i]) < eps) {
			//std::cout << endl<< count << endl;
			//count++;
			//std::cout << endl << "Number of splits=" << count << endl;
			return Rc[i - 1];
			
		}

		double *rt = Rp;
		Rp = Rc;
		Rc = rt;
		//count++;

	};

	//std::cout << endl <<"Number of splits="<< count<<endl;
	return Rp[n - 1]; 
}
int main()
{ 
	double eps, a, b;
	int menu;
	cout <<"Choose method of integration\n1.Trapeze\n2.Rectangle\n3.Simpson\n4.Romberg\nNumber - ";
	cin >> menu;
	system("cls");
	cout << "Choose your limits of integration" << endl << "a=";
	cin >> a;
	cout << "\nb=";
	cin >> b;
	cout << "\nChoose your eps" << endl << "eps=";
	cin >> eps;
	cout << endl;
	switch (menu)
	{
	case 1: {
		int count = 0;
		int n = 2;
		while (abs(IntegrationTra(a, b, n) - IntegrationTra(a, b, 2* n)) > eps) {
			//cout << IntegrationTra(a, b, 2*n) << endl;
			cout.precision(16);
			cout << IntegrationSim(a, b, n) << endl;
			count++;
			n *=2;
		};
		if(b<a){
			double tmp = IntegrationTra(a, b, n)*(-1);
			cout << "Method of trapeze:\n\nI=" << tmp<< endl << endl << "Number of splits - " << n << endl;
			cout << count;
		}
		else {
			double tmp = IntegrationTra(a, b, n);
			cout << "Method of trapeze:\n\nI=" <<tmp << endl << endl << "Number of splits - " << n << endl;
			cout << count;
		};
		break;
	}
	case 2: {
		int count = 0;
		int n = 2;
		while (abs(IntegrationRec(a, b, n) - IntegrationRec(a, b, 2 * n)) > eps) {
			count++;
			n*=2;
		};
		if (b < a) {
			double tmp = IntegrationRec(a, b, n)*(-1);
			cout << "Method of Simpson:\n\nI=" << tmp << endl << endl << "Number of splits - " << n << endl;
			cout << count;
		}
		else {
			double tmp = IntegrationRec(a, b, n);
			cout << "Method of rectangle:\n\nI=" << tmp<< endl << endl << "Number of splits - " << n << endl;
			cout << count;
		};
		break;
	}
	case 3: {
		int count = 0;
		int n =2;
		while (abs(IntegrationSim(a, b, n) - IntegrationSim(a, b, 2 * n)) > eps) {
			count++;
			cout.precision(16);
			cout << IntegrationSim(a, b, n) << endl;
			n*=2;
		};
		if (b < a) {
			cout.precision(16);
			double tmp = IntegrationSim(a, b, n)*(-1);
			cout << "Method of Simpson:\n\nI=" << tmp << endl << endl << "Number of splits - " << n << endl;
			cout << count;
		}
		else {
			cout.precision(16);
			double tmp = IntegrationSim(a, b, n);
			cout << "Method of Simpson:\n\nI=" << tmp << endl << endl << "Number of splits - " << n << endl;
			cout << count;
		};
		break;
	}
	case 4: {
		//Romberg(a, b, 100, eps);
		//cout << endl;

		int count = 0;
		int n = 2;
		while (abs(IntegrationRomberg(a, b, n,eps) - IntegrationRomberg(a, b, 2 * n,eps)) > eps) {
			count++;
			
			//cout << IntegrationRomberg(a, b, n,eps) << endl;
			n *= 2;
		};
		system("cls");
		cout << endl << "I=" << IntegrationRomberg(a, b, n, eps)<<endl;
		//cout << "Number of splits=" << n << endl;
		//cout << count << endl;

	}
	default:
		break;
	}
	return 0;
}
