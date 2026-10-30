
#include <stdio.h>
#include <cuda.h>

#define WIDTH 10
#define MASK_WIDTH 3
#define TILE 4

__global__ void conv(int *A, int *Mask, int *P, int width)
{
    __shared__ int tile[TILE + MASK_WIDTH - 1];

    int tid = threadIdx.x;
    int i = blockIdx.x * TILE + tid;

    int idx = blockIdx.x * TILE + tid - 1;

    if (tid < TILE + MASK_WIDTH - 1)
        tile[tid] = (idx >= 0 && idx < width) ? A[idx] : 0;

    __syncthreads();

    if (tid < TILE && i < width)
    {
        P[i] = 0;
        for (int j = 0; j < MASK_WIDTH; j++)
            P[i] += tile[tid + j] * Mask[j];
    }
}

int main()
{
    int A[WIDTH], Mask[MASK_WIDTH] = {1, 2, 1}, P[WIDTH];
    int *d_A, *d_Mask, *d_P;
    printf("Chirag Rao KV\n240962180\n\n");
    for (int i = 0; i < WIDTH; i++)
        A[i] = i + 1;

    cudaMalloc(&d_A, sizeof(A));
    cudaMalloc(&d_Mask, sizeof(Mask));
    cudaMalloc(&d_P, sizeof(P));

    cudaMemcpy(d_A, A, sizeof(A), cudaMemcpyHostToDevice);
    cudaMemcpy(d_Mask, Mask, sizeof(Mask), cudaMemcpyHostToDevice);

    conv<<<(WIDTH + TILE - 1) / TILE, TILE>>>(d_A, d_Mask, d_P, WIDTH);

    cudaMemcpy(P, d_P, sizeof(P), cudaMemcpyDeviceToHost);

    for (int i = 0; i < WIDTH; i++)
        printf("%d ", P[i]);

    cudaFree(d_A);
    cudaFree(d_Mask);
    cudaFree(d_P);
    printf("\n");
    return 0;
}
