#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char* getfield(char* line, int num)
{
	const char* tok;
	for (tok = strtok(line, ",");
		tok && *tok;
		tok = strtok(NULL, ",\n"))
	{
		if (!--num)
			return tok;
	}
	return NULL;
}

int main(int argc, char *argv[])
{
	FILE* stream = fopen("./Members.csv", "r");
	if(argc>1)
	{
		char line[1024];
		while (fgets(line, 1024, stream))
		{
			char* tmp = strdup(line);
			//printf("Field 3 would be %s\n", getfield(tmp, 3));
			// NOTE strtok clobbers tmp
			if(strcmp(argv[1], getfield(tmp,3))==0)
				printf("hi");
			free(tmp);
		}
	}
}


