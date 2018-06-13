# Emotet_Downloader_V2
Basically this program will extract the final payload from this Emotet Downloader: 53ea2608f0e34e3e746801977b778305
The payload is contained in macros, which when they are deobfuscated, forms a Base64 encoded string, which when decoded,
contains what looks like shellcode (but isn't). When you deobfuscate the not-shellcode, you get a powershell command that
decodes a base64 encoded string, and then decompresses it. This results in the final downloader script.
