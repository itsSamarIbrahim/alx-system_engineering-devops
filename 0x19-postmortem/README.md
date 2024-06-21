# Postmortem Report

## Issue Summary
- **Duration:** June 15, 2024, 14:00 UTC to June 15, 2024, 16:30 UTC
- **Impact:** The main web application was down. Users were unable to log in or access any services. Approximately 80% of users were affected.
- **Root Cause:** Database connection pool exhaustion. 

**Translation:** Our database got as crowded as a beach on a sunny day!

## Timeline
- **14:00 UTC:** Issue detected by monitoring alert indicating high response times and failed login attempts. (Our servers were having a "why aren't you working?" moment)
- **14:05 UTC:** Engineers began investigating the web application servers. (It's always the servers, isn't it?)
- **14:15 UTC:** Initial assumption was a high traffic spike causing server overload. (The classic "blame the users" tactic)
- **14:30 UTC:** Investigation showed normal traffic levels; focus shifted to database servers. (Turns out, it wasn't you, it was us)
- **14:45 UTC:** Database team joined the investigation. (Enter the database gurus)
- **15:00 UTC:** Misleading path - suspected a network issue between the application and database servers. (Network team, you get a break this time)
- **15:30 UTC:** Realized database connection pool was exhausted, preventing new connections. (Aha! The plot thickens)
- **15:45 UTC:** Database connection pool size increased, and idle connections were cleared. (Making room for everyone to fit in)
- **16:00 UTC:** Services began to recover. (It's alive!)
- **16:30 UTC:** Full functionality restored. (Mission accomplished)

## Root Cause and Resolution
- **Root Cause:** The database connection pool was configured with a maximum of 100 connections. A recent code deployment introduced a bug causing connections to not be released properly, leading to exhaustion of the connection pool.

**In plain terms:** We let in too many guests to our database party and forgot to ask some to leave, causing a bit of a crowd.

- **Resolution:** The connection pool size was increased to 200 as a temporary measure. The code was rolled back to the previous stable version, and the bug causing connection leaks was identified and fixed.

**Translation:** We threw out the rowdy guests, made the party area bigger, and fixed the door policy to ensure it doesn't happen again.

## Corrective and Preventative Measures
- **Improvements:**
  - Increase the database connection pool size.
  - Add monitoring for connection pool usage.
  - Conduct a thorough code review process before deployment.
- **Tasks:**
  - [ ] Patch the bug in the recent code deployment.
  - [ ] Increase the database connection pool size to 200 permanently.
  - [ ] Implement monitoring alerts for connection pool usage.
  - [ ] Conduct training for developers on resource management.
  - [ ] Schedule regular audits of database configurations.

## Diagram

Here's a fun diagram to illustrate what happened:

![Database Connection Pool Exhaustion]([path/to/your/saved/diagram.png](https://github.com/itsSamarIbrahim/alx-system_engineering-devops/blob/master/0x19-postmortem/database_connection_pool_exhaustion.png))

_Above: Our database trying to handle too many connections._
