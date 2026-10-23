// implement a program in cuda to read mxn matrix a and replace 1st row of this matrix 
// with the same elements 2nd row elements by square of each element and 3rd row elements by cube of each element and so on.
#include <stdio.h>
#define M 3
#define N 3

__global__ void transform(int *A) {
    int c = threadIdx.x;
    int r = blockIdx.x;
    if (r < M && c < N) {
        int x = A[r*N+c], p = 1;
        for (int i = 0; i < r+1; i++) p *= x;
        A[r*N+c] = p;
    }
}

int main() {
    printf("Chirag Rao KV\n240962180\n\n");
    int A[M][N], *dA;

    for (int i=0; i<M; i++)
        for (int j=0; j<N; j++)
            scanf("%d", &A[i][j]);

    cudaMalloc(&dA, sizeof(A));
    cudaMemcpy(dA, A, sizeof(A), cudaMemcpyHostToDevice);

    transform<<<M,N>>>(dA);

    cudaMemcpy(A, dA, sizeof(A), cudaMemcpyDeviceToHost);

    for (int i=0; i<M; i++) {
        for (int j=0; j<N; j++) printf("%d ", A[i][j]);
        printf("\n");
    }
    printf("\n");
    cudaFree(dA);
    return 0;
}
