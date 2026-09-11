// impliment a program in cuda that performs convolutional operations 
// on one dimensional input array N of size width using a mask array M of size mask width to produce resultant one dimensional arry of p size
#include <stdio.h>
#include <cuda_runtime.h>

__global__ void conv(int *N, int *M, int *P, int w, int mw) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < w) {
        P[i] = 0;
        for (int j = 0; j < mw; j++) {
            int x = i + j - mw / 2;
            if (x >= 0 && x < w)
                P[i] += N[x] * M[j];
        }
    }
}

int main() {
    int N[] = {1,2,3,4,5}, M[] = {1,2,1}, P[5];
    int *a,*m,*p, w=5, mw=3;
    printf("Chirag Rao KV\n240962180\n\n");
    cudaMalloc(&a,w*sizeof(int));
    cudaMalloc(&m,mw*sizeof(int));
    cudaMalloc(&p,w*sizeof(int));

    cudaMemcpy(a,N,w*sizeof(int),cudaMemcpyHostToDevice);
    cudaMemcpy(m,M,mw*sizeof(int),cudaMemcpyHostToDevice);

    conv<<<1,256>>>(a,m,p,w,mw);
    cudaMemcpy(P,p,w*sizeof(int),cudaMemcpyDeviceToHost);

    for(int i=0;i<w;i++) printf("%d ",P[i]);
}
