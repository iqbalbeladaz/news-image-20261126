// news-image-20261125 entry point.
//
// The picture is drawn ahead of time by generate.py and stored in this
// repository as entry.png. The judging harness runs this file on Node 22
// with no network access, so its whole job is to place that picture
// where the harness looks for it: $MAKEFUN_OUTPUT_DIR/entry.png
// (falling back to /output).
//
// Try it locally:
//   MAKEFUN_OUTPUT_DIR=/tmp/out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(targetDir, { recursive: true });
writeFileSync(join(targetDir, "entry.png"), readFileSync(join(here, "entry.png")));
