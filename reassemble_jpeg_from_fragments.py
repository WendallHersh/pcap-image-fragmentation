import re
import os

def extract_and_reassemble_jpeg_from_http_chunks(raw_file_path, output_path="reassembled_output.jpg"):
    with open(raw_file_path, "rb") as f:
        raw_data = f.read()

    # Regex to match HTTP Content-Range with payload (basic form)
    pattern = re.compile(
        rb'Content-Range:\s*bytes\s+(\d+)-(\d+)/(\d+).*?\r\n\r\n',
        re.DOTALL
    )

    fragments = {}
    for match in pattern.finditer(raw_data):
        start = int(match.group(1))
        end = int(match.group(2))
        total = int(match.group(3))

        body_start = match.end()
        body_end = body_start + (end - start + 1)
        body = raw_data[body_start:body_end]

        fragments[start] = body
        print(f"[+] Found chunk: bytes {start}-{end} (len={len(body)})")

    if not fragments:
        print("[-] No valid HTTP fragments with Content-Range found.")
        return

    # Reassemble in order
    reassembled = b''.join(fragments[k] for k in sorted(fragments.keys()))

    # Validate
    if len(reassembled) == total:
        with open(output_path, "wb") as out:
            out.write(reassembled)
        print(f"[✓] Reassembled full JPEG saved to: {output_path}")
    else:
        print(f"[!] Incomplete reassembly: expected {total}, got {len(reassembled)}")
        # Still write what we have
        with open("partial_" + output_path, "wb") as out:
            out.write(reassembled)
        print(f"[•] Partial JPEG saved to: partial_{output_path}")

# Example usage:
extract_and_reassemble_jpeg_from_http_chunks("Fragmentation.pcap", "reassembled_output.jpg")
