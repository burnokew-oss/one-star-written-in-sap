"""One Star, Written in Sap — entry program (pure stdlib, deterministic).

Writes the one-line one-star review to /output/entry.txt.
The line is judged against the published judge brief: a one-line, under-280-
character one-star review written by a houseplant about its human owner —
the plant's own grievance at the centre, funny through a surprising turn, in
a plant's voice (water, light, soil, pots, repotting, being moved), a genuine
review with a clear complaint and a reason for the single star, fresh specific
detail, no stock lines about drama queens, dramatic wilting or being ignored.
"""

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"

# The plant's grievance: four years in the same pot, watered like an apology,
# moved weekly for "better light", and blamed for the sun when a leaf drops.
# The leaf-drop is the evidence, not the complaint — the complaint is being
# unnamed after four years of service.
ENTRY_TEXT = "One star. He waters me like he's apologising, moves me weekly for 'better light', then blames the sun when I drop a leaf. Four years in this pot, and to him I'm still just 'the green one'."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY_TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes, sha256 %s)" % (OUTPUT_PATH, len(data), hashlib.sha256(data).hexdigest()))


if __name__ == "__main__":
    main()
