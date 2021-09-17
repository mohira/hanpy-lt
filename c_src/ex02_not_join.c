#include <stdio.h>
#include <pthread.h>
#include <zconf.h>

void task() {
    // 新しいスレッドで実行される関数
    sleep(1);
    printf("（っ'-')╮  Hello from spawned thread\n");
}

// エラー処理はしていない
int main() {
    pthread_t th_id;

    pthread_create(&th_id, NULL, (void *(*)(void *)) task, (int *) 0);


    printf("∠( ﾟдﾟ)／ Hello from Main Thread\n");
    printf("Main done\n");
}
