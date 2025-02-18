# LTC Reader

## A generic basic LTC decoder

LTC stands for Linear Timecode and is a signal used in media production to time synchronize multiple sources of audio and video involved in same production.

LTC is an analog audio signal and because of it can be easily transmitted among stations.

The faster your sound card driver is, the minor the jam interval is.

This script needs some improvements, but the main feature (read timecode) is working perfectly.

## Usage

Call the `decode_ltc` method, like so

```python
    import ltc_reader
    from pathlib import Path

    def main(wav_file_path: Path) -> None:
        with wav_file_path.open("rb") as f:
            raw_data = f.read()

        ltc_reader.decode_ltc(raw_data)

    if __name__ == "__main__":
        main(Path("a_file_with_LTC_signal.wav"))
```