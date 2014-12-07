#!/usr/bin/perl
use strict;
use CGI ':standard';

$! = 'Error file not found!';
my $registered = 1;

my @membersInfo;
my $tempRealName;
my $tempUsername;
my $tempPassword;

my $realName = param('realName');
my $userName = param('userid');
my $password = param('password');
my $confirmPassword = param('Cpassword');

print "Content-Type:text/html\n\n";
print "<html>";

if(length($realName) != 0 && length($userName) != 0 && length($password) != 0 && length($confirmPassword) != 0)
{
	

	if($password eq $confirmPassword)
	{
		open FILE, '<./csv/members.csv' or die $!;
		while (my $membersLine = <FILE>)
		{
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
		print "<head><title>ERROR</title></head>";
		print "<body><p>Error: Passwords do not match!</p><body>";
		print "</html>";
		exit;
	}
	if($registered == 0)
	{
		open FILE, '>>./csv/members.csv' or die $!;
		print FILE $realName;
		print FILE ",";
		print FILE $userName;
		print FILE ",";
		print FILE $password;
		print FILE "\n";
		close (FILE);
		open FILE, '<./catalogue.html' or die $!;
		while(my $catalogueLine = <FILE>)
		{
			print $catalogueLine;

		}
		close(FILE);
	}
	else
	{
		print "<head><title>ERROR</title></head>";
		print "<body><p>Error: Username already taken!</p><body>";
		print '<a href="http://cgi.cs.mcgill.ca/~tyi/index.html">Home </a>';
		print '<a href="http://cgi.cs.mcgill.ca/~tyi/registration.html">Registration</a>';
		print "</html>";
	}
}
else
{
	print "<head><title>ERROR</title></head>";
	print "<body><p>Error: Missing Parameters!</p><body>";
	print "</html>";
}

