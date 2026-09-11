#include <stdio.h>
#include <cuda_runtime.h>

__global__ void sort(int *a, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    for (int phase = 0; phase < n; phase++) {
        int j = 2 * i + (phase % 2);

        if (j + 1 < n && a[j] > a[j + 1]) {
            int t = a[j];
            a[j] = a[j + 1];
            a[j + 1] = t;
        }
        __syncthreads();
    }
}

int main() {
    int a[] = {5, 2, 8, 1, 4, 3};
    int n = 6, *d;
    printf("Chirag Rao KV\n240962180\n\n");
    cudaMalloc(&d, n * sizeof(int));
    cudaMemcpy(d, a, n * sizeof(int), cudaMemcpyHostToDevice);

    sort<<<1, n / 2 + 1>>>(d, n);

    cudaMemcpy(a, d, n * sizeof(int), cudaMemcpyDeviceToHost);

    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);

    cudaFree(d);
}