# HoneyPots

**Date**: 2023-07-27

Today I learned that Honeypots are similar to regular computer systems but are aimed to attract cybercriminals into thinking that they are real target.
Once the hackers are in, they can be tracked and their behaviour is later analysed to idenfity how to make systems more secure.
They normally allow attackers in the system by leaving some deliberate security vulnerabilities. Some examples of this are vulnerable ports left open, or weak passwords.

There are different types of honeypots

- Email traps: place fake email address in a hiden location where only an automated address harvester will be able to find it.
- Decoy database: set up to monitor software vulnerabilities and spot attacks exploiting insecure system architecture or using SQL injection, SQL services exploitation or privilege abuse.
- Malware honeypot: mimics software apps and APIs to invite malware attacks. The attacks are later analysed to develop anti-malware software or fix vulnerabilities in the API.
- Spider honeypot: intended to trap webcrawlers by creating web pages and links only accessible to crawlers. Crawler detection are studied to learn how to block bots as well as ad-networks crawlers.

By monitoring traffic coming into the honeypot system, you can assess:

- where the cybercriminals are coming from
- the level of threat
- what modus operandi they are using
- what data or applications they are interested in
- how well your security measures are working to stop cyberattacks

### Benefits of using honeypots
- Expose vulnerabilities in major systems.
- Honeypot shouldn't get any legitimate traffic, so any activity logged is likely to be a probe or intrusion attempt.
- They are also resource light, since they handle limited traffic.
- They have a low false positive rate

### Disadvantage of using honeypots
- Honeypots won't see everything that is going on, only activity that's directed at the honeypot. You can't assume you don't have vulnerabilities just because you did not detected it.
- If an attacker manages to identify your honeypot, they can proceed to attack your other systems while leaving the honeypot untouched.
- Once a honeypot has been 'fingerprinted', an attacker can create spoofed attacks to distract attention from a real exploit being targeted against your production systems. They can also feed bad information to the honeypot.
<!-- Write more about what you learned -->

## References

- [Kaspersky](https://usa.kaspersky.com/resource-center/threats/what-is-a-honeypot)
