# Flask Website Outage Postmortem

## Incident Summary:

### Duration of Outage:
- **Start Time:** March 10, 2022, 15:30 WAT (West Africa Time)
- **End Time:** March 10, 2022, 17:45 WAT

### Impact:
The Flask website experienced an outage due to a security flaw, resulting in downtime for users. Users were unable to access the website during the outage, causing a 100% user impact. The root cause was identified as a security vulnerability in the Flask application.

## Timeline:

### Detection:
- **Detected:** March 10, 2022, 15:30 WAT
- **How Detected:** A user detected the issue and alerted the team.

### Actions Taken:
1. Investigated the issue through cPanel, revealing a security flaw.
2. Discovered deleted course code files, leading to a quick decision to restore from a GitHub backup.
3. Commenced immediate efforts to secure the Flask application.
4. Initially assumed the issue might be related to server misconfigurations or deployment problems.

### Escalation:
- Incident escalated to the development team for code restoration and security enhancement.

### Resolution:
1. Restored the Flask application using a backup from GitHub.
2. Transitioned the project to Django for enhanced security features.
3. Implemented security measures provided by the Django framework.
4. Verified the application was operational and secure post-migration.

## Root Cause:

The security flaw in the Flask web application allowed a malicious attacker to exploit the system, resulting in the outage. Lack of sufficient technical knowledge in securing Flask applications contributed to the vulnerability.

### Resolution:
- Migrated the Flask application to Django for improved security.
- Implemented Django's robust security features, addressing the identified vulnerability.
- Enhanced monitoring and auditing processes to identify and respond promptly to security threats.

## Corrective and Preventative Measures:

### Improvements/Fixes:
1. Strengthening security knowledge and practices for Flask applications.
2. Regularly updating and patching software to address known vulnerabilities.
3. Implementing a more robust and proactive monitoring system for early issue detection.

### Tasks:
1. Conduct security training for the development team to enhance Flask application security.
2. Regularly update and patch software components.
3. Implement continuous monitoring for abnormal behavior and security threats.
4. Conduct periodic security audits to identify and address potential vulnerabilities.

This incident served as a learning experience, emphasizing the importance of prioritizing security in web development. The migration to Django not only resolved the immediate issue but also provided a more secure platform for the application.
