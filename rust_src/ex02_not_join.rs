use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        thread::sleep(Duration::from_millis(1000));
        println!("（っ'-')╮  Hello from spawned thread");
    });

    // 先にMainスレッドが終了してしまう!!!

    println!("∠( ﾟдﾟ)／ Hello from Main Thread");
    println!("Main done")
}