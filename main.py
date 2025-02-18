import ltc_reader
from pathlib import Path

def main(wav_file_path: Path) -> None:
    with wav_file_path.open("rb") as f:
        raw_data = f.read()

    ltc_reader.decode_ltc(raw_data)

if __name__ == "__main__":
    main(Path("./data/01-241205_1405.wav"))
