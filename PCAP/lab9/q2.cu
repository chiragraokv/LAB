// Implement a program in cuda to multiply two matrices for the following specifications
// a. each row of resultant matrix to be computed by one thread
// b. each column of resultant matrix to be computed by one thread
// c. each element of resultant matrix to be computed by one thread


#include <stdio.h>
#define N 4

__global__ void rowMul(int *A, int *B, int *C) {
    int r = threadIdx.x;
    for (int j = 0; j < N; j++) {
        C[r*N+j] = 0;
        for (int k = 0; k < N; k++)
            C[r*N+j] += A[r*N+k] * B[k*N+j];
    }
}

__global__ void colMul(int *A, int *B, int *C) {
    int c = threadIdx.x;
    for (int i = 0; i < N; i++) {
        C[i*N+c] = 0;
        for (int k = 0; k < N; k++)
            C[i*N+c] += A[i*N+k] * B[k*N+c];
    }
}

__global__ void elemMul(int *A, int *B, int *C) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N*N) {
        int r = i/N, c = i%N;
        C[i] = 0;
        for (int k = 0; k < N; k++)
            C[i] += A[r*N+k] * B[k*N+c];
    }
}

int main() {
    int A[N*N], B[N*N], C[N*N], *dA, *dB, *dC;
    int size = N*N*sizeof(int);
    printf("Chirag Rao KV\n240962180\n\n");
    for (int i=0; i<N*N; i++) A[i]=B[i]=i+1;

    cudaMalloc(&dA,size); cudaMalloc(&dB,size); cudaMalloc(&dC,size);
    cudaMemcpy(dA,A,size,cudaMemcpyHostToDevice);
    cudaMemcpy(dB,B,size,cudaMemcpyHostToDevice);

    rowMul<<<1,N>>>(dA,dB,dC);       // a. One thread per row
    // colMul<<<1,N>>>(dA,dB,dC);    // b. One thread per column
    // elemMul<<<N,N>>>(dA,dB,dC);   // c. One thread per element

    cudaMemcpy(C,dC,size,cudaMemcpyDeviceToHost);
    for(int i=0; i<N*N; i++)
        printf("%d ",C[i]);
    printf("\n");
    cudaFree(dA); cudaFree(dB); cudaFree(dC);
    return 0;
}