// Implement a program in cuda to process a 1D array containing angles in radians to generate sine of 
// angles in the output array. Use appropriate function
#include <stdio.h>
#include <cuda_runtime.h>
#include <math.h>

__global__ void sine(float *a, float *b, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n)
        b[i] = sinf(a[i]);
}

int main() {
    int n = 5;
    float a[] = {0, 0.5, 1, 1.5, 3.14}, b[5];
    float *d_a, *d_b;
    printf("Chirag Rao KV\n240962180\n\n");
    cudaMalloc(&d_a, n * sizeof(float));
    cudaMalloc(&d_b, n * sizeof(float));

    cudaMemcpy(d_a, a, n * sizeof(float), cudaMemcpyHostToDevice);

    sine<<<(n + 255) / 256, 256>>>(d_a, d_b, n);

    cudaMemcpy(b, d_b, n * sizeof(float), cudaMemcpyDeviceToHost);

    for (int i = 0; i < n; i++)
        printf("%.2f ->%.2f\t",a[i], b[i]);
    printf("\n");

    cudaFree(d_a);
    cudaFree(d_b);
}
