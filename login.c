#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{	
   FILE* membersData = fopen("./Members.csv", "r");
   FILE* loggedIn = fopen("./LoggedIn.csv", "w");
   char tempLine[1024];
   if(argc==3)
   {
      int successLogin = 1;
      char* tempName;
      char* tempUsername;
      char* tempPass;
      while (fgets(tempLine, 1024, membersData))
      {
	 tempName = strtok(tempLine, ",");
         tempUsername = strtok(NULL, ",");
         tempPass = strtok(NULL,"\n");
         if((strcmp(argv[1],tempUsername)==0)&&(strcmp(argv[2],tempPass)==0))
         {
            fprintf(loggedIn, "%s\n", argv[1]);
            successLogin = 0;
            //go to catalouge
         }
         memset(tempLine,0,sizeof(tempLine));
      }
      if(successLogin != 0)
      {
         //go to error page
         printf("Wrong username and/or password\n");
      }
      
   }
   else
   {
      printf("Missing Input\n");
   }
}
