#include <iostream>
#include <fstream>
#include <boost/multiprecision/cpp_int.hpp>
#include <set>
// #define _DEBUG
using namespace std;
int main(){
  constexpr int N = 10000000;
  std::cout<<"reading"<<endl;
  set<boost::multiprecision::cpp_int>se;
  {
    fstream generatedprime("./GeneratedPrime.txt");
    boost::multiprecision::cpp_int temp;
    while (generatedprime >> temp) {
      se.insert(temp);
    }
  }
  std::cout<<"read done"<<endl;
  /*cerr<<"se.size(): "<<se.size()<<endl;*/
  /*cerr<<"---"<<endl;*/
  /*for(auto&i:se) {*/
  /*  cerr<<i<<endl;*/
  /*}*/
  /*cerr<<"---"<<endl;*/
  auto isprime = [&](boost::multiprecision::cpp_int x) {
    for(auto&i:se){
      if(x%i==0){
        return false;
      }
      if(i*i>=x){
        break;
      }
    }
    return true;
  };
  boost::multiprecision::cpp_int maxint = *prev(se.end(),1);
  /*cerr<<"maxint: "<<maxint<<endl;*/
  std::cout<<"calculating"<<endl;
  for(boost::multiprecision::cpp_int i=maxint; i<=maxint+N;i++){
    if(isprime(i)){
#ifdef _DEBUG
      cout<<i<<'\n';
#endif
      se.insert(i);
    }
  }
  std::cout<<"calculate done"<<endl;
  ofstream generatedprime2("./GeneratedPrime.txt");
  for(auto&i:se){
    generatedprime2<<i<<'\n';
  }
  return 0;
}
