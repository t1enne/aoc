let day = "1";
for (let i = 0; i < Deno.args.length; i++) {
  const arg = Deno.args[i];
  if (arg == "-d") {
    day = Deno.args[i + 1];
    break;
  }
}

if (!day) {
  console.log("YOu need to add a day as a flag; [-d 1]");
  Deno.exit(0);
}

const result = await (await import(`./day${day}.ts`)).solve();
console.log({ result });
