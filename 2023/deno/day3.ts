export async function solve() {
  console.log("Day 3");
  const textFile = await Deno.readTextFile("../inputs/03-01.txt");
  const lines = textFile.trim().split(/\n/);
  return { 1: solvePart1(lines), 2: solvePart2(lines) };
}

function solvePart1(lines: string[]) {
  const digits = /\d+/g;
  const partNums = lines.reduce((acc, line, li) => {
    const lineAdder = (acc: number, val: [string, number]) =>
      acc + addIfValid(val, li, lines);

    const matches = Array.from(line.matchAll(digits), (m) => [m[0], m.index])
      .filter(Boolean) as unknown as [string, number][];
    return acc + matches.reduce(lineAdder, 0);
  }, 0);
  return partNums;
}

function solvePart2(lines: string[]) {
  const digits = /\d+/g;
  const map = {} as Record<string, number[]>;
  return lines.reduce((_acc, line, li) => {
    const matches = Array.from(line.matchAll(digits), (m) => [m[0], m.index])
      .filter(Boolean) as unknown as [string, number][];
    return Object.values(matches
      .reduce((m, val) => {
        const res = getPartNum(val, li, lines);
        if (!res) return m;
        const [value, id] = res;
        m[id] ??= [];
        m[id].push(value);
        return m;
      }, map))
      .reduce(
        (retVal, val) => val.length == 2 ? retVal + val[0] * val[1] : retVal,
        0,
      );
  }, 0);
}
const isSymbol = (char: string) => !/[\d\.\s]/.test(char);
const addIfValid = (
  val: [string, number],
  li: number,
  lines: string[],
) => {
  const [partNum, xsi] = val;
  const xei = xsi + partNum.length;

  // look at chars from xsi-1 to xei and ysi-1 to ysi+1
  for (let yIdx = li - 1; yIdx <= li + 1; yIdx++) {
    for (let xIdx = xsi - 1; xIdx <= xei; xIdx++) {
      const cell = lines[yIdx]?.[xIdx];
      if (cell && isSymbol(cell)) return +partNum;
    }
  }
  return 0;
};

const getPartNum = (
  partMatch: [string, number],
  ysi: number,
  lines: string[],
): [number, string] | undefined => {
  const [partNum, xsi] = partMatch;
  const xei = xsi + partNum.length;

  // look at chars from xsi-1 to xei and ysi-1 to ysi+1
  for (let yIdx = ysi - 1; yIdx <= ysi + 1; yIdx++) {
    for (let xIdx = xsi - 1; xIdx <= xei; xIdx++) {
      const cell = lines[yIdx]?.[xIdx];
      if (cell && /\*/.test(cell)) return [+partNum, `${yIdx},${xIdx}`];
    }
  }
};
