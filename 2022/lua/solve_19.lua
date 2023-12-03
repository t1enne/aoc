Rules = {}

local create_matcher_func = function(rule)
  for fst, _ in string.gmatch(rule, "(%d)") do
    print(fst)
  end
end

for line in io.lines("../inputs/input19.sample") do
  if #line == 0 then
    break
  end

  if line == "" then
    break
  end

  for idx, def in string.gmatch(line, "(.*): (.*)") do
    local pipe = string.match(def, "|")
    if pipe then
    else
      Rules[idx] = create_matcher_func(def)
    end
  end
end
