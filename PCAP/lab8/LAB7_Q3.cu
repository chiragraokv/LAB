//Implement a CUDA program to compute the euclidian distance between two randomly initialized vectors a and b each of length n.
// keep the number of threads per block fixed at 256 and dynamically determine the number of blocks required to process all N elements
#include <stdio.h>
#include <cuda_runtime.h>
#include <math.h>
#include <time.h>

#define TPB 256

__global__ void distance(float *a, float *b, float *sum, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    

    if (i < n) {
        float d = a[i] - b[i];
        atomicAdd(sum, d * d);
    }
}

int main() {
    int n = 1000;
    float *a, *b, *sum, h_sum = 0;
    printf("Chirag Rao KV\n240962180\n\n");
    cudaMallocManaged(&a, n * sizeof(float));
    cudaMallocManaged(&b, n * sizeof(float));
    cudaMallocManaged(&sum, sizeof(float));
    srand(time(NULL));
    for (int i = 0; i < n; i++)
     {
        a[i] = (float)rand() / RAND_MAX;
        b[i] = (float)rand() / RAND_MAX;
    }

    *sum = 0;

    int blocks = (n + TPB - 1) / TPB;
    distance<<<blocks, TPB>>>(a, b, sum, n);
    cudaDeviceSynchronize();

    printf("Euclidean Distance = %f\n", sqrt(*sum));

    cudaFree(a);
    cudaFree(b);
    cudaFree(sum);
    return 0;
}
