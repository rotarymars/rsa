#!/bin/bash
clang++ -O3 -I. -std=gnu++2b ./generate_primenumber.cpp
unzip primes.zip
for ((i = 0; ; i++)); do
  ./a.out
done
