// implement a program in cuda to perform matrix multiplication using 2d grid of 2d block

#include <stdio.h>
#include <cuda.h>

#define N 2

__global__ void multiply(int *A, int *B, int *C)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < N && col < N)
    {
        C[row * N + col] = 0;
        for (int k = 0; k < N; k++)
            C[row * N + col] += A[row * N + k] * B[k * N + col];
    }
}

int main()
{
    int A[N*N] = {1, 2, 3, 4};
    int B[N*N] = {5, 6, 7, 8};
    int C[N*N];
    printf("Chirag Rao KV\n240962180\n\n");
    int *d_A, *d_B, *d_C;

    cudaMalloc(&d_A, sizeof(A));
    cudaMalloc(&d_B, sizeof(B));
    cudaMalloc(&d_C, sizeof(C));

    cudaMemcpy(d_A, A, sizeof(A), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B, sizeof(B), cudaMemcpyHostToDevice);

    dim3 block(2, 2);
    dim3 grid(1, 1);

    multiply<<<grid, block>>>(d_A, d_B, d_C);

    cudaMemcpy(C, d_C, sizeof(C), cudaMemcpyDeviceToHost);

    for (int i = 0; i < N*N; i++)
    {
        printf("%d ", C[i]);
        if (i % N == N-1) printf("\n");
    }

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}
