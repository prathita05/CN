import random

def go_back_n(total_frames=10, window_size=4, loss_prob=0.2):
    base = 0
    next_frame = 0
    
    while base < total_frames:
        # Send frames in window
        end = min(base + window_size, total_frames)
        print(f"Sending frames {list(range(next_frame, end))}")
        
        # Simulate random loss
        lost_frame = None
        for f in range(next_frame, end):
            if random.random() < loss_prob and lost_frame is None:
                lost_frame = f
                print(f"Frame {f} lost, retransmitting frames {list(range(f, end))}")
                break
        
        if lost_frame is not None:
            next_frame = lost_frame
        else:
            print(f"ACK {end - 1} received")
            base = end
            next_frame = base
            print(f"Window slides to {list(range(base, min(base + window_size, total_frames)))}\n")

if __name__ == "__main__":
    go_back_n(total_frames=12, window_size=4, loss_prob=0.3)
