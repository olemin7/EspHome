# font2bdf.py

Converts the glyph tables in `font.cpp` into a BDF font file.

## Usage

```sh
python3 font2bdf.py [input.cpp] [output.bdf]
```

Both arguments are optional. The defaults are `font.cpp` and `font.bdf` in the
current directory. Python 3 is the only requirement.

The script writes the BDF file and prints an ASCII preview of every glyph:

```
'1' (4x8)
  .##.
  .##.
  ###.
  .##.
  .##.
  .##.
  .##.
  ####
```

## Input format

The script looks for two things in the input file:

1. Glyph arrays, each declared as `std::vector<uint8_t> <name> = { ... };`.
   Values can be binary (`0b...`), hex (`0x..`) or decimal.
2. The character map, declared as `table = std::map<...>{ {'c', name}, ... };`.
   Only the glyphs listed in this map go into the BDF.

Each byte is one column of the glyph, left to right. Bit 0 is the top row and
bit 7 the bottom row. Glyphs can be up to 8 px wide.

## Adding a glyph

1. Add the array to `font.cpp`, for example `const std::vector<uint8_t> glif_minus = { 0x08, 0x08, 0x08 };`.
2. Add it to `table`, for example `{'-', glif_minus},`.
3. Run the script again and check the preview.

## Output

- Height is 8 px. Ascent is 8 and descent is 0.
- The advance width (`DWIDTH`) of each character is its width plus 1 px. This
  matches the one blank column that `font::get()` inserts between characters
  by default (`DEFAULT_SPACING` in the script).
- `DEFAULT_CHAR` is `*`, which is also what the firmware shows for unknown
  characters.

To check the result, run `bdftopcf -o /tmp/font.pcf font.bdf`, or open the
file in a BDF editor such as FontForge or gbdfed.
