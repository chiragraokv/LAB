// Implement a program in cuda to perform parallel sparse matrix vector multiplication using 
// com pressed sparse row storage format. Represent the input sparse matrix in scr format in the host code.
#include <stdio.h>
#define N 4

__global__ void spmv(int *val, int *col, int *row, int *x, int *y) {
    int r = blockIdx.x * blockDim.x + threadIdx.x;
    if (r < N) {
        y[r] = 0;
        for (int j = row[r]; j < row[r+1]; j++)
            y[r] += val[j] * x[col[j]];
    }
}

int main() {
    printf("Chirag Rao KV\n240962180\n\n");
    // CSR representation on host
    int val[] = {1, 2, 3, 4, 5, 6};
    int col[] = {0, 2, 1, 3, 0, 2};
    int row[] = {0, 2, 3, 4, 6};
    int x[]   = {1, 2, 3, 4};
    int y[N], *dval, *dcol, *drow, *dx, *dy;

    cudaMalloc(&dval, 6*sizeof(int));
    cudaMalloc(&dcol, 6*sizeof(int));
    cudaMalloc(&drow, (N+1)*sizeof(int));
    cudaMalloc(&dx, N*sizeof(int));
    cudaMalloc(&dy, N*sizeof(int));

    cudaMemcpy(dval,val,6*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(dcol,col,6*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(drow,row,(N+1)*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(dx,x,N*sizeof(int),cudaMemcpyHostToDevice);

    spmv<<<1,N>>>(dval,dcol,drow,dx,dy);
    cudaMemcpy(y,dy,N*sizeof(int),cudaMemcpyDeviceToHost);

    for(int i=0;i<N;i++) printf("%d ",y[i]);
    printf("\n");
    cudaFree(dval); cudaFree(dcol); cudaFree(drow);
    cudaFree(dx); cudaFree(dy);
    return 0;
}
