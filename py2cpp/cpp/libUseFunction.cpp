 // C++ (and CasADi)
#include <casadi/casadi.hpp>
using namespace std;


void usage_cplusplus(){
  cout << "---" << endl;
  cout << "Usage from CasADi C++:" << endl;
  cout << endl;

  // Use CasADi's "external" to load the compiled function
  casadi::Function f = casadi::external("f", "../../lib/libExampleFun.so");

  // Use like any other CasADi function

  // example values 1st ex
  vector<double> x = {1, 2, 3, 4};
  vector<casadi::DM> arg = {reshape(casadi::DM(x), 4, 1), 3};

  // example values 2nd ex
  // vector<DM> arg = {DM(0), 3};

  vector<casadi::DM> res = f(arg);

  cout << "result (0): " << res << endl;

}

int main(){

  // Usage from C++
  usage_cplusplus();

  return 0;
}
