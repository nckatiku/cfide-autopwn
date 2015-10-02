This program checks for the well known CFIDE directory traversal vulnerability in ColdFusion. It attempts to retrieve the password.properties located on the web server of which it is attempting to pentest.

The directory traversal vulnerability affects ColdFusionMX, ColdFusionMX7 and ColdFusion8.

This script attempts to check for the vulnerability, and then saves the hashes found into a text file.

Currently, it only supports ColdFusionMX7 and ColdFusion8.

The CVE for this vulnerability is: CVE-2010-2861

In later stages, I will be adding support for multi-threading, list input and shell spawning.

<a href='javascript://aaaa.com'>aaa</a>