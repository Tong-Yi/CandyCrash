#!/usr/bin/perl
use strict;
use CGI ':standard';

my $realName = 'Tong Yi';#param('realName');
my $userName = 'yi';#param('userid');
my $password = 'abc123'; #param('password');
my $confirmPassword = 'abc123'; #param('Cpassword');
$! = 'Error file not found!';
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
      if($userName eq $tempUsername){
         print "username already fucking taken!\n";
      }
      else
      {
         open(MYFILE, '>>members.csv') or die $!;
         print MYFILE $tempRealName;
         print MYFILE ",";
         print MYFILE $tempUsername;
         print MYFILE ",";
         print MYFILE $tempPassword;
         close (MYFILE);
         open(MYFILE, '>>loggedin.csv') or die $1;
         print MYFILE $tempUsername;
         close (MYFILE);
         #go to catalouge
      }
   }
}
else
{
   print "passwords do not match!\n";
}
