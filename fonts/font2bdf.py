#!/usr/bin/env python3
"""Convert the glyph tables in font.cpp into a BDF font.

font.cpp stores each glyph column-major: one byte per column, bit 0 is the
top row and bit 7 the bottom row (8 px tall). BDF wants row-major bitmaps,
so the columns are transposed here.
"""
import re
import sys
from pathlib import Path

GLYPH_HEIGHT = 8
# font::get() inserts this many blank columns between glyphs by default.
DEFAULT_SPACING = 1


def parse(src):
    arrays = {}
    for name, body in re.findall(
            r"std::vector<uint8_t>\s+(\w+)\s*=\s*\{(.*?)\};", src, re.S):
        values = re.findall(r"0b[01]+|0x[0-9a-fA-F]+|\d+", body)
        arrays[name] = [int(v, 0) for v in values]
    table = re.search(r"table\s*=\s*std::map<[^{]*\{(.*?)\n\};", src, re.S)
    mapping = re.findall(r"\{\s*'(.)'\s*,\s*(\w+)\s*\}", table.group(1))
    return [(ch, arrays[name]) for ch, name in mapping]


def to_rows(columns):
    rows = []
    for y in range(GLYPH_HEIGHT):
        rows.append([(col >> y) & 1 for col in columns])
    return rows


def main():
    src_path = Path(sys.argv[1] if len(sys.argv) > 1 else "font.cpp")
    out_path = Path(sys.argv[2] if len(sys.argv) > 2 else "font.bdf")
    glyphs = sorted(parse(src_path.read_text()), key=lambda g: ord(g[0]))
    max_w = max(len(cols) for _, cols in glyphs)

    out = [
        "STARTFONT 2.1",
        "FONT -clock32-max7219-medium-r-normal--8-80-75-75-p-50-iso10646-1",
        f"SIZE {GLYPH_HEIGHT} 75 75",
        f"FONTBOUNDINGBOX {max_w} {GLYPH_HEIGHT} 0 0",
        "STARTPROPERTIES 4",
        f"FONT_ASCENT {GLYPH_HEIGHT}",
        "FONT_DESCENT 0",
        f"DEFAULT_CHAR {ord('*')}",
        'FAMILY_NAME "clock32 MAX7219"',
        "ENDPROPERTIES",
        f"CHARS {len(glyphs)}",
    ]
    for ch, cols in glyphs:
        w = len(cols)
        name = f"uni{ord(ch):04X}"
        out += [
            f"STARTCHAR {name}",
            f"ENCODING {ord(ch)}",
            f"SWIDTH {(w + DEFAULT_SPACING) * 1000 // GLYPH_HEIGHT} 0",
            f"DWIDTH {w + DEFAULT_SPACING} 0",
            f"BBX {w} {GLYPH_HEIGHT} 0 0",
            "BITMAP",
        ]
        for row in to_rows(cols):
            byte = 0
            for x, bit in enumerate(row):
                byte |= bit << (7 - x)  # all glyphs are <= 8 px wide
            out.append(f"{byte:02X}")
        out.append("ENDCHAR")
    out.append("ENDFONT")
    out_path.write_text("\n".join(out) + "\n")

    for ch, cols in glyphs:
        print(f"'{ch}' ({len(cols)}x{GLYPH_HEIGHT})")
        for row in to_rows(cols):
            print("  " + "".join("#" if b else "." for b in row))


if __name__ == "__main__":
    main()
