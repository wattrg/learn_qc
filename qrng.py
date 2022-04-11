from simulator import SimulatedQubit, SingleQubitSimulator
from interface import QuantumDevice

def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()

def main():
    qsim = SingleQubitSimulator()
    for idx_sample in range(10):
        random_sample = qrng(qsim)
        print(f"Our QRNG return {random_sample}")

if __name__ == "__main__":
    main()
