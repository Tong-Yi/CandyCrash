#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void errorMessage()
{
   printf("%s%c%c\n","Content-Type:text/html",13,10);
   printf("%s\n\n","Content-Type:text/html");
   printf("Content-Type:text/html\n\n");
   printf("<html>");
   printf("<head><title>ERROR</title></head>");
   printf("<body><p>Wrong username and/or password!</p><body>");
   printf("</html>");
}
int main()
{	
   char inputedUsername[200];
   char inputedPassword[200];
   char c;
   int a = 0;
   int b = 0;
   int lengthCounter = 0;
   
   int n = atoi(getenv("CONTENT_LENGTH"));
   int firstWord = 0;

   FILE* membersData = fopen("./members.csv", "r");
   FILE* loggedIn = fopen("./loggedin.csv", "w");
   char tempLine[1024];
   int successLogin = 1;
   char* tempName;
   char* tempUsername;
   char* tempPass;
   
   while((c = getchar()) != EOF && lengthCounter<n && a<200 && b<200)
   {
      if(firstWord = 0)
      {
         if(c!='+')
         {
            inputedUsername[a] = c;
            a++;
         }
         else firstWord = 1;
      }
      else
      {
         inputedPassword[b] = c;
         b++;
      }
      lengthCounter++;
   }


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
      errorMessage();
   }

}


