#!/usr/bin/perl
use strict;
use CGI ':standard';

my $realName = 'Tong Yi';#param('realName');
my $userName = 'ti';#param('userid');
my $password = 'abc123'; #param('password');
my $confirmPassword = 'abc123'; #param('Cpassword');
$! = 'Error file not found!';
my $registered = 1;
#my $members = 'members.csv';
#my $loggedIn = 'loggedin.csv';

#my @membersLine = <./members.csv>;

#open FILE, "<members.csv" or die $!;
my @membersInfo;
my $tempRealName;
my $tempUsername;
my $tempPassword;
open FILE, '<members.csv' or die $!;
if($password eq $confirmPassword)
{
   while (my $membersLine = <FILE>){
      @membersInfo=split/,/,$membersLine;
      $tempRealName=shift(@membersInfo);
      $tempUsername=shift(@membersInfo);
      $tempPassword=shift(@membersInfo);
      if($userName eq $tempUsername)
      {
         $registered = 1;
         last;
      }
      else
      {
         $registered = 0;
      }
   }
}
else
{
   print "passwords do not match!\n";
}
if($registered == 0)
{
   open(MYFILE, '>>members.csv') or die $!;
   print MYFILE $realName;
   print MYFILE ",";
   print MYFILE $userName;
   print MYFILE ",";
   print MYFILE $password;
   print MYFILE "\n";
   close (MYFILE);
   open(MYFILE, '>>loggedin.csv') or die $1;
   print MYFILE $userName;
   print MYFILE "\n";
   close (MYFILE);
   #go to catalouge
}
else
{
   #load error
}
