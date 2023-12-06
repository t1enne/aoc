export async function solve() {
  console.log("Day 3");
  const textFile = await Deno.readTextFile("../inputs/03-01.txt");
  const lines = textFile.trim().split(/\n/);
  return { 1: solvePart1(lines), 2: solvePart2(lines) };
}

const isSymbol = (char: string) => !/[\d\.\s]/.test(char);

const addIfValid = (
  partMatch: [string, number],
  ysi: number,
  lines: string[],
) => {
  const [partNum, xsi] = partMatch;
  const xei = xsi + partNum.length;

  // look at chars from xsi-1 to xei and ysi-1 to ysi+1
  for (let yIdx = ysi - 1; yIdx <= ysi + 1; yIdx++) {
    for (let xIdx = xsi - 1; xIdx <= xei; xIdx++) {
      const cell = lines[yIdx]?.[xIdx];
      if (cell && isSymbol(cell)) return +partNum;
    }
  }
  return 0;
};

function solvePart1(lines: string[]) {
  const digits = /\d+/g;
  const partNums = lines.reduce((acc, line, li) => {
    const matches = Array.from(line.matchAll(digits), (m) => [m[0], m.index])
      .filter(Boolean) as unknown as [string, number][];
    const lineAdder = (acc: number, val: [string, number]) =>
      acc + addIfValid(val, li, lines);
    return acc + matches.reduce(lineAdder, 0);
  }, 0);
  return partNums;
}

function solvePart2(lines: string[]) {
}
