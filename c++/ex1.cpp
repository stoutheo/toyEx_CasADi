// A simple program that links with CasADi
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include <casadi/casadi.hpp>
using namespace casadi;

#include <Eigen/Core>

#include <Eigen/Sparse>

int main()
{
  //////////////////////////
          // SX
  //////////////////////////
  SX x = SX::sym( "x" ) ;
  SX y = SX::sym( "y" , 5 ) ;
  SX Z = SX::sym( "Z" , 4 , 2 );

  SX f = pow( x , 2 ) + 10;
  f = sqrt(f);
  std::cout << " f : " << f << std::endl ;

  //////////////////////////
          // DM
  //////////////////////////
  // Right hand side
  DM C = DM (2,3);

  Eigen::MatrixXd m(2,3);
  m(0,0) = 3;
  m(1,0) = 2.5;
  m(0,1) = -1;
  m(1,1) = m(1,0) + m(0,1);
  std::cout << m << std::endl;

  Eigen::MatrixXd c(C.size1(),C.size2());
  c(0,0) = 3;
  std::cout << c << std::endl;

  Eigen::SparseMatrix<double> c_Sparse = c.sparseView();
  std::cout << c_Sparse << std::endl;


  //////////////////////////
          // MX
  //////////////////////////
  SX x_n = SX::sym("x_n", 2 , 2 );
  SX y_n = SX::sym("y_n");
  SX f_n = 3*x_n + y_n;

  std::cout << " f : " << f_n << std::endl ;


  return 0;
}
