// Implement a program in cuda to improve the performance of 1d parallel convolution using constant memory

#include <stdio.h>
#include <cuda.h>

#define N 10
#define M 3

__constant__ int mask[M];

__global__ void convolution(int *a, int *b)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < N)
    {
        b[i] = 0;
        for (int j = 0; j < M; j++)
        {
            int k = i + j - 1;
            if (k >= 0 && k < N)
                b[i] += a[k] * mask[j];
        }
    }
}

int main()
{
    printf("Chirag Rao KV\n240962180\n\n");
    int a[N], b[N], h_mask[M] = {1, 2, 1};
    int *d_a, *d_b;

    for (int i = 0; i < N; i++)
        a[i] = i + 1;

    cudaMalloc(&d_a, N * sizeof(int));
    cudaMalloc(&d_b, N * sizeof(int));

    cudaMemcpy(d_a, a, N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpyToSymbol(mask, h_mask, M * sizeof(int));

    convolution<<<1, 256>>>(d_a, d_b);

    cudaMemcpy(b, d_b, N * sizeof(int), cudaMemcpyDeviceToHost);

    for (int i = 0; i < N; i++)
        printf("%d ", b[i]);

    cudaFree(d_a);
    cudaFree(d_b);
    printf("\n");
    return 0;
}
