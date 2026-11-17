"""Generate the original chapter 1 foley still used by the game."""

from array import array
from pathlib import Path
import math
import random
import wave


RATE = 44100
OUT = Path(__file__).resolve().parent.parent / "game/sfx"


def write(name, samples):
    peak = max(abs(value) for value in samples) or 1.0
    pcm = array("h", (int(28000 * value / peak) for value in samples))
    with wave.open(str(OUT / name), "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(RATE)
        stream.writeframes(pcm.tobytes())


def pulse(t, start, length):
    x = (t - start) / length
    return math.sin(math.pi * x) ** 2 if 0.0 < x < 1.0 else 0.0


def rummage():
    rng = random.Random(212)
    samples = []
    filtered = 0.0
    for index in range(int(RATE * 1.6)):
        t = index / RATE
        noise = rng.uniform(-1.0, 1.0)
        filtered = 0.88 * filtered + 0.12 * noise
        scrape = sum(pulse(t, start, length) for start, length in
                     ((0.07, 0.36), (0.49, 0.32), (0.90, 0.41)))
        thump = (pulse(t, 0.41, 0.09) + pulse(t, 1.23, 0.12))
        samples.append(0.55 * scrape * filtered + 0.3 * thump * math.sin(2 * math.pi * 78 * t))
    write("chapter1_rummage.wav", samples)


def memory_fall():
    rng = random.Random(626)
    samples = []
    filtered = 0.0
    for index in range(int(RATE * 1.0)):
        t = index / RATE
        noise = rng.uniform(-1.0, 1.0)
        filtered = 0.78 * filtered + 0.22 * noise
        envelope = math.sin(math.pi * t) ** 1.5
        samples.append(envelope * (0.8 * filtered + 0.2 * noise))
    write("chapter1_memory_fall.wav", samples)


def memory_underwater():
    rng = random.Random(731)
    duration = 13.0
    starts = [rng.uniform(0.05, duration - 0.4) for _ in range(65)]
    samples = []
    filtered = 0.0
    for index in range(int(RATE * duration)):
        t = index / RATE
        noise = rng.uniform(-1.0, 1.0)
        filtered = 0.985 * filtered + 0.015 * noise
        bubble = 0.0
        for start in starts:
            dt = t - start
            if 0.0 <= dt < 0.11:
                bubble += 0.18 * math.sin(2 * math.pi * (250 * dt - 750 * dt * dt)) * math.exp(-35 * dt)
        fade = min(1.0, t / 0.15, (duration - t) / 0.35)
        samples.append(max(0.0, fade) * (0.17 * filtered + bubble))
    write("chapter1_memory_underwater.wav", samples)


def memory_tv_off():
    rng = random.Random(833)
    samples = []
    for index in range(int(RATE * 0.42)):
        t = index / RATE
        noise = rng.uniform(-1.0, 1.0)
        tone = math.sin(2 * math.pi * (1600 * t - 1600 * t * t))
        samples.append(math.exp(-14 * t) * (0.55 * tone + 0.25 * noise))
    write("chapter1_memory_tv_off.wav", samples)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    rummage()
    memory_fall()
    memory_underwater()
    memory_tv_off()
