 // C++ (and CasADi) from here on
#include <casadi/casadi.hpp>
using namespace casadi;
using namespace std;


void usage_cplusplus(){
  cout << "---" << endl;
  cout << "Usage from CasADi C++:" << endl;
  cout << endl;

  // Use CasADi's "external" to load the compiled function
  Function f = external("f", "/home/theo/software/tools/CasADi/test/test-scripts-code/python/code2.so");

  // Use like any other CasADi function
  vector<double> x = {1, 2, 3, 4};
  vector<DM> arg = {reshape(DM(x), 4, 1), 3};

  // vector<DM> arg = {DM(0), 3};

  vector<DM> res = f(arg);

  cout << "result (0): " << res << endl;

}

int main(){

  // Usage from C++
  usage_cplusplus();

  return 0;
}
