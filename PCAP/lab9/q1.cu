// implement a program in cuda to add two matrixes for the following specifications
// a each row of resultant matrix to be computed by one thread
// b. each column of resultant matrix to be computed by one thread
// c. each element of resultant matrix to be computed by one thread
#include <stdio.h>
#define N 4

__global__ void addRow(int *A, int *B, int *C) {
    int r = threadIdx.x;
    for (int j = 0; j < N; j++)
        C[r*N+j] = A[r*N+j] + B[r*N+j];
}

__global__ void addCol(int *A, int *B, int *C) {
    int c = threadIdx.x;
    for (int i = 0; i < N; i++)
        C[i*N+c] = A[i*N+c] + B[i*N+c];
}

__global__ void addElement(int *A, int *B, int *C) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N*N) C[i] = A[i] + B[i];
}

int main() {
    printf("Chirag Rao KV\n240962180\n\n");
    int A[N*N], B[N*N], C[N*N];
    int *dA, *dB, *dC, size = N*N*sizeof(int);

    for (int i=0; i<N*N; i++) A[i]=B[i]=i;

    cudaMalloc(&dA,size); cudaMalloc(&dB,size); cudaMalloc(&dC,size);
    cudaMemcpy(dA,A,size,cudaMemcpyHostToDevice);
    cudaMemcpy(dB,B,size,cudaMemcpyHostToDevice);

    addRow<<<1,N>>>(dA,dB,dC);       // a. One thread per row
    // addCol<<<1,N>>>(dA,dB,dC);    // b. One thread per column
    // addElement<<<N, N>>>(dA,dB,dC); // c. One thread per element

    cudaMemcpy(C,dC,size,cudaMemcpyDeviceToHost);
    for(int i=0;i<N*N;i++) printf("%d ",C[i]);

    cudaFree(dA); cudaFree(dB); cudaFree(dC);
    printf("\n");
    return 0;
}