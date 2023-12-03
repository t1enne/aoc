export async function solve() {
  const textFile = await Deno.readTextFile("../inputs/01-01.txt");
  const lines = textFile.trim().split("\n");
  console.log("Day 1");
  return { 1: solvePart1(lines), 2: solvePart2(lines) };
}

/**
 * Part 1
 * get first and last digit from line
 */
function solvePart1(lines: string[]) {
  let acc = 0;
  for (const line of lines) {
    const matches = line.match(/\d/g)!;
    acc += Number(matches.at(0)! + matches.at(-1));
  }
  return acc;
}

/**
 * Part 2
 * Had a hard time finding a way to solve this with regexes.
 * Using a (lookbehind)[https://mtsknn.fi/blog/how-to-do-overlapping-matches-with-regular-expressions/] was the (?=) solution
 */
function solvePart2(lines: string[]) {
  let acc = 0;
  const cases: Record<string, string> = {
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
  };

  const keys = Object.keys(cases);
  const endRe = new RegExp(`(?<=(${keys.join("|")}))`, "g");

  for (const line of lines) {
    const matches = Array.from(line.matchAll(endRe), (m) => m.at(1));
    const first = matches[0]!;
    const last = matches.at(-1)!;
    const lineTotal = cases[first] + cases[last];
    acc += +lineTotal;
  }
  return acc;
}
