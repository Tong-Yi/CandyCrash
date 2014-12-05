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

   int n = atoi(getenv("CONTENT_LENGTH"));
   int firstWord = 0;

   FILE* membersData = fopen("./members.csv", "r");
   FILE* loggedIn = fopen("./loggedin.csv", "w");
   char tempLine[1024];
   int successLogin = 1;
   char* tempName;
   char* tempUsername;
   char* tempPass;
   char* tempTags;
   char* inputUsername;
   char* inputPassword;
   
   char* inputString = getenv("QUERY_STRING");
   temptags = strtok(inputString, "=");
   inputUsername = strtok(NULL, "&");
   tempTags = strtok(NULL, "=");

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


