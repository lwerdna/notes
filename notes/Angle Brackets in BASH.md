tags: #Linux #Bash

```
<   passes the contents of a file to stdin
<<  "here document" passes multiple lines until a terminator to stdin
<<< "here string" passes a string to stdin
```

To experiment, use:

```python
#!/usr/bin/env python
import sys

result = ''
while True:
    char = sys.stdin.read(1)
    if not char:
        break
    result += char

print('repr:', repr(result))
print(' hex:', result.encode('utf-8').hex())
```

And input file:

```
$ echo -n 'AAAA' > a.txt # -n for no newline
$ cat a.txt | xxd -g 1   # -g 1 for 1-byte groups
00000000: 41 41 41 41                                      AAAA
```

It's clean when stdin comes from a file:

```
$ ./test.py < a.txt
repr: 'AAAA'
 hex: 41414141
```

Newlines creep in, as the terminator must be on a line by itself:

```
$ ./test.py << MYEND
> A
> AA
> AAA
> MYEND
repr: 'A\nAA\nAAA\n'
 hex: 410a41410a4141410a
```

A newline even exists after a lone string:

```
$ ./test.py <<< "AAAA"
repr: 'AAAA\n'
 hex: 414141410a
```

You can create files in a bash script with:

```
$ cat > b.txt <<MY_END
> one
> two
> three
> MY_END
$ cat b.txt
one
two
three
```

You can create binaries too, since base64 ignores the newlines introduced in the "here document":

```
$ python -c 'import sys; sys.stdout.buffer.write(b"".join([x.to_bytes(1,"big") for x in range(256)]))' > test.bin
$ xxd -g 1 ./test.bin
00000000: 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f  ................
00000010: 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f  ................
00000020: 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f   !"#$%&'()*+,-./
00000030: 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f  0123456789:;<=>?
00000040: 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f  @ABCDEFGHIJKLMNO
00000050: 50 51 52 53 54 55 56 57 58 59 5a 5b 5c 5d 5e 5f  PQRSTUVWXYZ[\]^_
00000060: 60 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f  `abcdefghijklmno
00000070: 70 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f  pqrstuvwxyz{|}~.
00000080: 80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f  ................
00000090: 90 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f  ................
000000a0: a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af  ................
000000b0: b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 ba bb bc bd be bf  ................
000000c0: c0 c1 c2 c3 c4 c5 c6 c7 c8 c9 ca cb cc cd ce cf  ................
000000d0: d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 da db dc dd de df  ................
000000e0: e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 ea eb ec ed ee ef  ................
000000f0: f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 fa fb fc fd fe ff  ................

$ base64 ./test.bin
AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4
OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3Bx
cnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmq
q6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj
5OXm5+jp6uvs7e7v8PHy8/T19vf4+fr7/P3+/w==

$ base64 -d <<MY_END > test2.bin
> AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4
OTo7PD0+P0BBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWltcXV5fYGFiY2RlZmdoaWprbG1ub3Bx
cnN0dXZ3eHl6e3x9fn+AgYKDhIWGh4iJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChoqOkpaanqKmq
q6ytrq+wsbKztLW2t7i5uru8vb6/wMHCw8TFxsfIycrLzM3Oz9DR0tPU1dbX2Nna29zd3t/g4eLj
5OXm5+jp6uvs7e7v8PHy8/T19vf4+fr7/P3+/w==
> MY_END

$ diff test.bin test2.bin
$
```

This can be extended to multiple files in a single blob, by encoding the output
of tar, and piping it to base64 and `tar -x` at runtime.
