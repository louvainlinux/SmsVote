-- to change the view it's 'alter view as'

use gammu;

create view velo as 
select ID, ReceivingDateTime, SenderNumber, TextDecoded from gammu.inbox where ID in (
	select max(ID) from gammu.inbox 
    where ID in
		(
			select ID from gammu.inbox where lower(TextDecoded) REGEXP  '^(\ *?24h\ )'
		)
	group by SenderNumber
);
