const getGameId = (line: string) => +line.slice(4, line.indexOf(":"));
const regex = /(\d+)\s(red|green|blue)/g;
const ceils = {
  red: 12,
  green: 13,
  blue: 14,
};
export async function solve() {
  const textFile = await Deno.readTextFile("../inputs/02-01.txt");
  const lines = textFile.trim().split("\n");
  console.log("Day 2");
  return { 1: solvePart1(lines), 2: solvePart2(lines) };
}

const solvePart1 = (lines: string[]) => {
  let total = 0;

  const validateSet = (set: string) => {
    const localCount: Record<string, number> = structuredClone(ceils);
    return Array.from(set.matchAll(regex), (m) => [m[1], m[2]])
      .every(([count, color]) => {
        localCount[color] -= +count;
        return localCount[color] >= 0;
      });
  };

  lines.forEach((line) => {
    const sets = line.slice(line.indexOf(":")).split(";");
    const isValid = sets.every(validateSet);
    if (isValid) total += getGameId(line);
  });
  return total;
};

const solvePart2 = (lines: string[]) => {
  const results = lines.map((line) => {
    const localState: Record<string, number> = {};
    const sets = line.slice(line.indexOf(":") + 1).split(";");
    for (let i = 0; i < sets.length; i++) {
      const set = sets[i];
      const r = Array.from(set.matchAll(regex), (m: string[]) => [m[1], m[2]]);
      for (const [count, color] of r) {
        if (!localState[color] || localState[color] < +count) {
          localState[color] = +count;
        }
      }
    }
    return Object.values(localState).reduce((a = 1, v) => v * a);
  });
  return results.reduce((acc = 0, val: number) => acc + val);
};
