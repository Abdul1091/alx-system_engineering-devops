# Postmortem: WordPress 500 Internal Server Error

## Issue Summary

- **Duration:** The outage lasted from 14:00 UTC to 16:00 UTC.
- **Impact:** The WordPress site was down, affecting 100% of users who tried to access the site during this time.
- **Root Cause:** A typo in the `wp-settings.php` file where `.phpp` was used instead of `.php`.

## Timeline

- **14:00 UTC:** Issue detected. The website was down, returning a 500 Internal Server Error.
- **14:15 UTC:** The issue was detected by a monitoring alert.
- **14:30 UTC:** Investigation began, focusing on Apache logs and file configurations.
- **15:00 UTC:** Misleading investigation paths included checking server configurations and plugin issues.
- **15:30 UTC:** Issue escalated to the web development team.
- **16:00 UTC:** The typo in `wp-settings.php` was identified and corrected.

## Root Cause and Resolution

- **Root Cause:** The error was caused by a typo in the `wp-settings.php` file where `.phpp` was mistakenly used instead of `.php`.
- **Resolution:** Corrected the typo in the `wp-settings.php` file and restarted the Apache server.

## Corrective and Preventative Measures

- **Improvements:** Implement stricter code reviews and testing procedures to catch similar issues.
- **Tasks to Address the Issue:**
  1. Patch the typo in `wp-settings.php`.
  2. Add automated tests to catch such errors in the future.
  3. Enhance monitoring to detect similar issues more quickly.

![Strace is your friend]()
