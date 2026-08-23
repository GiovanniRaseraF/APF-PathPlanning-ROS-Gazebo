#include "sjtu_drone_autopilot/field.hpp"
#include <cuda_runtime.h>
#include <iostream>

// Un kernel CUDA molto semplice: eleva al quadrato ogni elemento
__global__ void square_kernel(const float* d_in, float* d_out, int size) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < size) {
        d_out[idx] = d_in[idx] * d_in[idx];
    }
}

void run_cuda_kernel() {
    std::cout << "Will run the cuda kernel" << std::endl;
}
