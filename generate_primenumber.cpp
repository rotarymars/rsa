#include <iostream>
#include <fstream>
#include <boost/multiprecision/cpp_int.hpp>
#include <set>
#include <regex>  
#include <filesystem>
#ifndef __ROTARYMARS__RUD__
#define __ROTARYMARS__RUD__
template<class T>
T RUD(T a, T b) {
  return ((a + b - (T)1) / b);
}
#else
#endif
using namespace std;
int main(){
  constexpr int N = 10000000;
  std::cout<<"reading"<<endl;
  set<boost::multiprecision::cpp_int>se;
  {
    std::regex pattern("GeneratedPrime_[0-9]+.txt");
    try{
      for(const auto&entry:std::filesystem::directory_iterator("./")){
        if(entry.is_regular_file()){
          const auto&filename = entry.path().filename();
          if(std::regex_match(filename.string(),pattern)){
            std::cout<<filename<<'\n';
            std::ifstream generatedprime(entry.path());
            boost::multiprecision::cpp_int temp;
            while (generatedprime >> temp) {
              se.insert(temp);
            }
          }
        }
      }
    }
    catch(const std::filesystem::filesystem_error&e){
      std::cerr<<"Error: "<<e.what()<<'\n';
    }
  }
  std::cout<<"read done"<<endl;
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
  // 1000000 lines
  // ofstream generatedprime2("./GeneratedPrime.txt");
  // for(auto&i:se){
  //   generatedprime2<<i<<'\n';
  // }
  std::cout<<"writing"<<std::endl;
  int filecnt=0;
  std::vector<boost::multiprecision::cpp_int>temp;
  for(auto&i:se){
    temp.push_back(i);
    if(temp.size()==1000000){
      std::ofstream generatedprime("./GeneratedPrime_"+std::to_string(filecnt)+".txt");
      for(auto&j:temp){
        generatedprime<<j<<'\n';
      }
      temp.clear();
      filecnt++;
    }
  }
  if(!temp.empty()){
    std::ofstream generatedprime("./GeneratedPrime_"+std::to_string(filecnt)+".txt");
    for(auto&j:temp){
      generatedprime<<j<<'\n';
    }
  }
  std::cout<<"write done"<<endl;
  return 0;
}
