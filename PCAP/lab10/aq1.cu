// implement a program in cuda which displays a shopping mall item menu with price. The N number of friends are allowed to purchase as many items as possible they want. Calculate the total purchase done by N firends.

#include <stdio.h>
#include <cuda.h>

#define N 3
#define ITEMS 4

__global__ void purchase(int *qty, int *price, int *total)
{
    int i = threadIdx.x;

    if (i < N)
    {
        total[i] = 0;
        for (int j = 0; j < ITEMS; j++)
            total[i] += qty[i * ITEMS + j] * price[j];
    }
}

int main()
{
    printf("Chirag Rao KV\n240962180\n\n");
    int price[ITEMS] = {100, 200, 50, 300};
    int qty[N * ITEMS] = {
        2, 1, 3, 0,
        1, 2, 0, 1,
        3, 0, 2, 1
    };
    int total[N], *d_q, *d_p, *d_t;

    printf("Shopping Mall Menu:\n");
    printf("1. Bag = 100\n2. Shoes = 200\n");
    printf("3. Pen = 50\n4. Watch = 300\n");

    cudaMalloc(&d_q, sizeof(qty));
    cudaMalloc(&d_p, sizeof(price));
    cudaMalloc(&d_t, sizeof(total));

    cudaMemcpy(d_q, qty, sizeof(qty), cudaMemcpyHostToDevice);
    cudaMemcpy(d_p, price, sizeof(price), cudaMemcpyHostToDevice);

    purchase<<<1, N>>>(d_q, d_p, d_t);

    cudaMemcpy(total, d_t, sizeof(total), cudaMemcpyDeviceToHost);

    int grand = 0;
    for (int i = 0; i < N; i++)
    {
        printf("Friend %d total = %d\n", i + 1, total[i]);
        grand += total[i];
    }

    printf("Total purchase = %d\n", grand);

    cudaFree(d_q);
    cudaFree(d_p);
    cudaFree(d_t);

    return 0;
}
