 // C++ (and CasADi)
#include <casadi/casadi.hpp>
using namespace std;

// source : https://github.com/casadi/casadi/blob/master/docs/examples/cplusplus/nlp_codegen.cpp

void usage_cplusplus(){
  cout << "---" << endl;
  cout << "Usage from CasADi C++:" << endl;
  cout << endl;

  // Create a new NLP solver instance from the compiled code
  casadi::Function solver = casadi::nlpsol("solver", "ipopt", "../../lib/libSolver.so");

  // Use like any other CasADi solver instantiation
  // Bounds and initial guess
  std::map<std::string, casadi::DM> arg, res;
  arg["lbx"] = -casadi::DM::inf();
  arg["ubx"] =  casadi::DM::inf();
  arg["lbg"] =  0;
  arg["ubg"] =  casadi::DM::inf();
  arg["x0"] = 0;
  arg["p"] = 10;

  // Solve the NLP
  res = solver(arg);

  // Print solution
  cout << "-----" << endl;
  cout << "objective at solution = " << res.at("f") << endl;
  cout << "primal solution = " << res.at("x") << endl;
  cout << "dual solution (x) = " << res.at("lam_x") << endl;
  cout << "dual solution (g) = " << res.at("lam_g") << endl;

}

int main(){

  // Usage from C++
  usage_cplusplus();

  return 0;
}
