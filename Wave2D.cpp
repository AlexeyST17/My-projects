#include <fstream>
#include <vector>
#include <cmath>

#define PI 3.1415926535

using namespace std;

typedef vector<vector<double>> vector2d;
typedef vector<vector2d> vector3d;

class Wave2D {
private:
    double I1(double x, double y) {
        return 0;
    }
    double I2(double x, double y) {
        return sin(PI * x / L1) * sin(PI * y / L2);
    }
    double B1(double y, double t) {
        return 0;
    }
    double B2(double y, double t) {
        return 0;
    }
    double B3(double x, double t) {
        return 0;
    }
    double B4(double x, double t) {
        return 0;
    }
public:
    Wave2D(double t, double l1, double l2, double a)
        : T(t), L1(l1), L2(l2), A(a) {}

    vector3d getSol(int LP1, int LP2, double C) {
        double h1 = L1 / LP1;
        double h2 = L2 / LP2;

        int TP = A * T * sqrt(h1 * h1 + h2 * h2) / h1 / h2 / C;
        double t = T / TP;

        double C12 = pow(A * t / h1, 2);
        double C22 = pow(A * t / h2, 2);

        vector3d u(TP + 1, vector2d(LP1 + 1, vector<double>(LP2 + 1)));

        for (int i = 1; i < LP1; i++) {
            for (int j = 1; j < LP2; j++) {
                u[0][i][j] = I1(i * h1, j * h2);
            }
        }

        for (int i = 0; i <= TP; i++) {
            for (int j = 0; j <= LP2; j++) {
                u[i][0][j]   = B1(j * h2, i * t);
                u[i][LP1][j] = B2(j * h2, i * t);
            }
            for (int j = 0; j <= LP1; j++) {
                u[i][j][0]   = B3(j * h1, i * t);
                u[i][j][LP2] = B4(j * h1, i * t);
            }
        }

        for (int i = 1; i < LP1; i++) {
            for (int j = 1; j < LP2; j++) {
                u[1][i][j] = u[0][i][j]
                    + C12 * (u[0][i + 1][j] - 2 * u[0][i][j] + u[0][i - 1][j]) / 2.0
                    + C22 * (u[0][i][j + 1] - 2 * u[0][i][j] + u[0][i][j - 1]) / 2.0
                    + t * I2(i * h1, j * h2);
            }
        }

        for (int i = 2; i <= TP; i++) {
            for (int j = 1; j < LP1; j++) {
                for (int k = 1; k < LP2; k++) {
                    u[i][j][k] = 2 * u[i - 1][j][k]
                        - u[i - 2][j][k]
                        + C12 * (u[i - 1][j + 1][k] - 2 * u[i - 1][j][k] + u[i - 1][j - 1][k])
                        + C22 * (u[i - 1][j][k + 1] - 2 * u[i - 1][j][k] + u[i - 1][j][k - 1]);
                }
            }
        }

        return u;
    }

    double T;
    double L1;
    double L2;
    double A;
};

int main() {
    double  T = sqrt(2);
    double L1 = 1.0;
    double L2 = 1.0;
    double  A = 1.0;

    int  LP1 = 50;
    int  LP2 = 50;
    double C = 1.1;

    Wave2D wave2d(T, L1, L2, A);

    vector3d u = wave2d.getSol(LP1, LP2, C);

    ofstream file("data.txt");
    file.precision(15);

    for (int i = 0; i < u.size(); i++) {
        for (int j = 0; j < u[i].size(); j++) {
            for (int k = 0; k < u[i][j].size(); k++) {
                file.width(25);
                file << u[i][j][k];
            }
            file << endl;
        }
        file << endl;
    }

    return 0;
}