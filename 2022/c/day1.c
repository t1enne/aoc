#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int part_one(char *lines) {
  int current_elf_cals = 0;
  int max = 0;
  for (int i = 0; i < 100; i++) {
    if (lines[i] == NULL) {
      if (current_elf_cals > max) {
        max = current_elf_cals;
      }
      current_elf_cals = 0;
    } else {
      current_elf_cals += atoi(lines[i]);
    }
  }
  return max;
}

int main() {
  FILE *file = fopen("../inputs/input1.sample.txt", "r");
  if (file == NULL) {
    printf("Failed to open the file.");
    return 1;
  }

  int max;
  int current_elf_cals = 0;
  int total_lines = 0;
  char ch;
  while ((ch = fgetc(file)) != EOF) {
    if (ch == '\n') {
      total_lines++;
    }
  }

  fseek(file, 0, SEEK_SET);
  char **lines = (char **)malloc(total_lines * sizeof(char *));
  part_one(&lines);

  for (int i = 0; i < total_lines; i++) {
    lines[i] = (char *)malloc(100 * sizeof(char));
    fgets(lines[i], 100, file);
  }
  fclose(file);

  for (int i = 0; i < total_lines; i++) {
    char *line = lines[i];
    if (line[0] == '\n') {
      if (current_elf_cals > max) {
        max = current_elf_cals;
      }
      current_elf_cals = 0;
      continue;
    }
    current_elf_cals += atoi(strtok(line, "\n"));
    printf("Current elf cals is: %d. Sum is: %d\n", current_elf_cals, max);
  }

  for (int i = 0; i < total_lines; i++) {
    free(lines[i]);
  }

  free(lines);
  return 0;
}
