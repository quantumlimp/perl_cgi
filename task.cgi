#!/usr/bin/perl  
use strict;  
use warnings;  
use CGI;  
use DBI;
use Cpanel::JSON::XS qw(encode_json decode_json);

my $query = CGI->new();  
print $query->header(); 
my $jquery = "//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.
+js";
print "<script src='$jquery'  type='text/javascript'></script>\n";
    print "<script src=print $query->defaults(`SEARCH')'domManager.js'    type='text/javascript'></script>\n";
if (!$query->param) {
	server_side_ajax($query);
	};
 
print <<"HTMLcode"; 
	<html> 
	<head> 
	</head> 
	<body> 
	<div id="error" name="error"> 
	</div>
	<div> 
		<input type="Button" id="new" value="New" align="left" onclick="showForm_onclick()" /> 
		<input type="Button" id="cancel" value="Cancel" align="right" style="display:none;" onclick="hideForm_onclick()"/> 
	</div>
	<div> 
		<input type="text" id="text_field"/> 
		<input type="Button" id="SEARCH" value="Search" onclick="getAppointments()"/> 
	</div>
	
	<form id="form1" name="form1" style="display:none;"> 
		<table> 
			<tr> 
				<td>Date</td> 
				<td>
					<input type="text" name="Date" value="Date"/> 
				</td> 
			</tr> 
			<tr> 		
				<td> Time</td> 
				<td>
					<input type="text" name="time" value="Time"/> 
				</td> 
			</tr> 
			<tr> 	
				<td> Time</td> 
				<td>
					<input type="text" name="description" value="Description"/> 
				</td>				
			</tr> 
		</table> 
	</form> 
	</body> 
	</html> 
HTMLcode  
1;

## Subroutines ##

sub server_side_ajax {
my ($query) = @_;
my $user_input = $query->param;
if ($query->param('text_field')){
my $appointments = decode_json retrieve_appointments($user_input);
return $appointments;
}
elsif ($query->param('ADD')){
 if (!validate_input($user_input))
 {
 my $response = {message => "Invalid input"};
 my $response_json = encode_json $response;
 return $response_json;
 }
 add_appointment($user_input);
}

}

sub validate_input {
use POSIX qw(strftime);

my $input = @_;
my $date = $input[0];
my $time = $input[1];
my $desription = $input[2];
my $today = strftime "%Y-%m-%d_%H-%M-%S", localtime;
my $input_date = strftime "%Y-%m-%d_%H-%M-%S", $date;

if ($today ge $date || !($date) || !($time) || !($description)){
return undef;
}

}
sub retrieve_appointments {
my $dbfile = "appointments.db";
 
my $dsn = "dbi:MySQL:dbname=$dbfile";
my $user = "";
my $password = "";
my $dbh = DBI->connect($dsn, $user, $password);
my $user_input = @_;
my $sql = 'SELECT date, time, description FROM appointments';
my $sth = $dbh->prepare($sql);
$sth->execute;

while (my @row = $sth->fetchrow_array) {
   # return only rows that match user input
   if (index($row[2],$user_input) != -1){
   my $response = {date => $row[0], time => $row[1],description => $row[2]};
   }
}
my $response_json = encode_json $response;
$dbh->disconnect;

return $response_json;
}

sub add_appointment {
my $dbfile = "appointments.db";
 
my $dsn = "dbi:MySQL:dbname=$dbfile";
my $user = "";
my $password = "";
my $dbh = DBI->connect($dsn, $user, $password);
my $user_input = @_;
my $date = $user_input[0];
my $time = $user_input[1];
my $description = $user_input[2];

my $sql = 'INSERT into appointments ($date, $time, $description) VALUES (?,?,?)';
my $sth = $dbh->prepare($sql);
$sth->execute;


$dbh->disconnect;

}

