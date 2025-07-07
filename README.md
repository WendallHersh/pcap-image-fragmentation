
# 🧩 HTTP Fragment Reassembler

This script is designed to extract and reassemble JPEG images from **fragmented HTTP responses**, particularly those using the `Content-Range` header to send data in chunks (e.g., via `Range` requests or partial transfers). It is especially useful for:

- Capture The Flag (CTF) challenges
- Forensic analysis of intercepted network traffic
- Rebuilding images hidden in fragmented packet captures or hex dumps

## 🔧 Features

- Parses raw files (e.g., `.pcap` or `.bin`) for HTTP payloads
- Detects and extracts `Content-Range` chunks
- Automatically orders fragments based on byte offsets
- Reassembles and outputs a valid `.jpg` file

## 📜 Example Use Case

Suppose you have a `.pcap` file or raw binary dump of HTTP traffic that includes fragmented JPEG responses:

```
Content-Range: bytes 82131-82802/82803
```

Each chunk contains a portion of the image. This tool will:

1. Locate each fragment
2. Parse the start/end bytes
3. Reassemble the full image in the correct order

## 🚀 Usage

```bash
python reassemble_jpeg_from_fragments.py Fragmentation.pcap
```

By default, it will create:

- ✅ `reassembled_output.jpg` — fully rebuilt if all fragments are found
- ⚠️ `partial_reassembled_output.jpg` — if fragments are missing, it still saves the combined output

## 🧪 Example Output

```
[+] Found chunk: bytes 0-1499 (len=1500)
[+] Found chunk: bytes 1500-2999 (len=1500)
[✓] Reassembled full JPEG saved to: reassembled_output.jpg
```

## 📂 Directory Structure

```
.
├── reassemble_jpeg_from_fragments.py
├── Fragmentation.pcap
├── reassembled_output.jpg
└── README.md
```

## 🛠️ Requirements

- Python 3.6+
- No external libraries required (uses `re`, `os`)

## 🔐 Disclaimer

This tool assumes that the HTTP payloads and headers are present in raw format (not deeply parsed). It's not a full PCAP protocol parser, but rather a targeted reassembly utility for known use cases like CTFs or forensic deep dives.

## 📜 License

MIT License – use it, modify it, break it, and win CTFs with it.
