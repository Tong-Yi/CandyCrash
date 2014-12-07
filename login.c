#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printCatalogue(char* username)
{
   FILE* catalogue = fopen("./catalogue.html", "r");
   char check[50] = "<input type=\"hidden\" name=\"hiddenUser\" value=\"\">\n";
   char* newLine = malloc(strlen(check)+strlen(username)+1);
   strcat(newLine, "<input type=\"hidden\" name=\"hiddenUser\" value=\"");
   strcat(newLine, username);
   strcat(newLine, "\">\n");
   if (catalogue != NULL )
   {
      char line[128];
      while (fgets (line, sizeof line, catalogue ) != NULL )
      {
         if(strcmp(check, line)==0)
         {
            fputs (newLine, stdout);
         }
         else fputs (line, stdout);
      }
      fclose ( catalogue );
   }
   else
   {
      printf("<head><title>ERROR: 404</title></head>");
      printf("<body><p>Error 404: Catalogue not found!</p><body>");
   }
}
int main()
{	

   printf("Content-Type:text/html\n\n");

   char inputString[200];
   char c;
   int counter = 0;
   int firstWord = 0;
   int length = atoi((getenv("CONTENT_LENGTH")));

   FILE* membersData = fopen("../csv/members.csv", "r");
   FILE* loggedIn = fopen("../csv/loggedin.csv", "a");
   char tempLine[1024];
   int successLogin = 1;
   char* tempTags;
   char* tempName;
   char* tempUsername;
   char* tempPass;
   char* inputUsername;
   char* inputPassword;
   while ((c = getchar()) != EOF && counter<length)
   {
      if (counter < 200)
      {
         if (c!='+') inputString[counter]=c;
         else inputString[counter]=' ';
         counter++;
      }
   }
   inputString[counter] = '\0';
   tempTags = strtok(inputString, "=");
   inputUsername = strtok(NULL, "&");
   tempTags = strtok(NULL, "=");
   inputPassword = strtok(NULL, "\0");
   if(tempTags == NULL)
   {
      printf("<html>");
      printf("<head><title>ERROR</title></head>");
      printf("<body><p>Error: Missing Username and/or Password!</p><body>");
   }
   else
   {
      printf("<html>");
      printf("<head><title>%s</title></head>",tempTags);
      printf("<body><p>Error: Missing Username and/or Password!</p><body>");
      while (fgets(tempLine, 1024, membersData))
      {
         tempName = strtok(tempLine, ",");
         tempUsername = strtok(NULL, ",");
         tempPass = strtok(NULL,"\n");
         if((strcmp(inputUsername,tempUsername)==0)&&(strcmp(inputPassword,tempPass)==0))
         {
            fprintf(loggedIn, "%s\n", inputUsername);
            successLogin = 0;
            printCatalogue(inputUsername);
            break;
         }
         memset(tempLine,0,sizeof(tempLine));
      }
      if(successLogin != 0)
      {
         printf("<html>");
         printf("<head><title>ERROR</title></head>");
         printf("<body><p>Error: Wrong Username and/or Password!</p><body>");
      }
   }
   printf("</html>");
   return 0;
}


