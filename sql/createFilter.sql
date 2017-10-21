create view gammu.filter as 
select ID, lower(REGEXP_REPLACE(TextDecoded,'[^a-zA-Z0-9\ ]', '\ ')) as TextDecoded, SenderNumber, ReceivingDateTime from gammu.inbox;
