# Postmortem Report

## Issue Summary
- **Duration:** June 15, 2024, 14:00 UTC to June 15, 2024, 16:30 UTC
- **Impact:** The main web application was down. Users were unable to log in or access any services. Approximately 80% of users were affected.
- **Root Cause:** Database connection pool exhaustion.

## Timeline
- **14:00 UTC:** Issue detected by monitoring alert indicating high response times and failed login attempts.
- **14:05 UTC:** Engineers began investigating the web application servers.
- **14:15 UTC:** Initial assumption was a high traffic spike causing server overload.
- **14:30 UTC:** Investigation showed normal traffic levels; focus shifted to database servers.
- **14:45 UTC:** Database team joined the investigation.
- **15:00 UTC:** Misleading path - suspected a network issue between the application and database servers.
- **15:30 UTC:** Realized database connection pool was exhausted, preventing new connections.
- **15:45 UTC:** Database connection pool size increased, and idle connections were cleared.
- **16:00 UTC:** Services began to recover.
- **16:30 UTC:** Full functionality restored.

## Root Cause and Resolution
- **Root Cause:** The database connection pool was configured with a maximum of 100 connections. A recent code deployment introduced a bug causing connections to not be released properly, leading to exhaustion of the connection pool.
- **Resolution:** The connection pool size was increased to 200 as a temporary measure. The code was rolled back to the previous stable version, and the bug causing connection leaks was identified and fixed.

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
