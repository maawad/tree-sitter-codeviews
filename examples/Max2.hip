#include <thrust/device_vector.h>

__global__ void vector_add(int* a, int* b) {
  int thread_id = threadIdx.x + blockIdx.x * blockDim.x;
  int a_value = a[thread_id];
  int b_value = b[thread_id];

  b[thread_id] = a_value + b_value;
}

// void main() {
//   thrust::device_vector<int> a(512, 1);
//   thrust::device_vector<int> b(512, 1);

//   vector_add<<<1, 512>>>(a.data().get(), b.data().get());

//   hipDeviceSynchronize();
// }