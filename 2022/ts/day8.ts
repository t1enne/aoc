#!/usr/bin/env -S deno run --allow-read

const input = await Deno.readTextFile("../inputs/input8.prod");
const visible: boolean[][] = [];
const lines = input
  .trim()
  .split("\n")
  .map((line) => line.split("").map((c) => parseInt(c)));

for (let y = 0; y < lines.length; y++) {
  const line = lines[y];
  visible[y] = [];

  for (let x = 0; x < line.length; x++) {
    // const tree = parseInt(line[y][x])
    if (y == 0 || x == 0 || y == lines.length - 1 || x == line.length - 1) {
      visible[y][x] = true;
    } else {
      const res = look(y, x);
      visible[y][x] = res;
    }
  }
}

const partOne = visible.flat().reduce((total, tree) => {
  if (tree == true) {
    return total + 1;
  }
  return total;
}, 0);

console.log(partOne);

function look(y: number, x: number) {
  const DIRS: {
    [dir: string]: (y: number, x: number) => boolean;
  } = {
    up: (y: number, x: number) => {
      const tree = lines[y][x];
      for (let i = y - 1; i >= 0; i--) {
        const nextUp = lines[i][x];
        if (nextUp >= tree) {
          return false;
        }
      }
      return true;
    },
    right: (y: number, x: number) => {
      const tree = lines[y][x];
      for (let i = x + 1; i <= lines[y].length; i++) {
        const nextR = lines[y][i];
        if (nextR >= tree) {
          return false;
        }
      }
      return true;
    },
    down: (y: number, x: number) => {
      const tree = lines[y][x];
      for (let i = y + 1; i < lines[y].length; i++) {
        const nextD = lines[i][x];
        if (nextD >= tree) {
          return false;
        }
      }
      return true;
    },
    left: (y: number, x: number) => {
      const tree = lines[y][x];
      for (let i = x - 1; i >= 0; i--) {
        const nextL = lines[y][i];
        if (nextL >= tree) {
          return false;
        }
      }
      return true;
    },
  };

  for (const key in DIRS) {
    const method = DIRS[key];
    const visible = method(y, x);
    if (visible) return true;
  }
  return false;
}
