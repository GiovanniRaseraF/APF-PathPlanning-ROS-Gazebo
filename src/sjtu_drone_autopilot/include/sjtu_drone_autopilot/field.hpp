#ifndef FIELD_HPP_
#define FIELD_HPP_

#include <vector>
#include <string>

void run_cuda_kernel();

class Field {
public:
    Field();
    void generate();
    void query();
};

#endif // FIELD_HPP_