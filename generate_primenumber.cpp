#include <iostream>
#include <string>
#include <fstream>
#include <boost/multiprecision/cpp_int.hpp>
#include <set>
using namespace std;
int main(){
  constexpr int N = 1000;
  set<boost::multiprecision::cpp_int>se;
  {
    fstream generatedprime("./GeneratedPrime.txt");
    boost::multiprecision::cpp_int temp;
    while (generatedprime >> temp) {
      se.insert(temp);
    }
  }
  cerr<<"se.size(): "<<se.size()<<endl;
  cerr<<"---"<<endl;
  for(auto&i:se) {
    cerr<<i<<endl;
  }
  cerr<<"---"<<endl;
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
  cerr<<"maxint: "<<maxint<<endl;
  for(boost::multiprecision::cpp_int i=maxint; i<=maxint+N;i++){
    if(isprime(i)){
      cout<<i<<'\n';
      se.insert(i);
    }
  }
  ofstream generatedprime2("./GeneratedPrime.txt");
  for(auto&i:se){
    generatedprime2<<i<<'\n';
  }
  return 0;
}
