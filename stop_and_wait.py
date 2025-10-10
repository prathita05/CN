import random
import time

def stop_and_wait(total_frames=5, loss_prob=0.3, timeout=2):
    frame = 0
    while frame < total_frames:
        print(f"Sending Frame {frame}")
        time.sleep(1)

        # Simulate frame loss
        if random.random() < loss_prob:
            print(f"Frame {frame} lost, retransmitting...")
            time.sleep(timeout)
            continue

        # ACK received
        print(f"ACK {frame} received\n")
        frame += 1

if __name__ == "__main__":
    stop_and_wait(total_frames=6, loss_prob=0.4)
