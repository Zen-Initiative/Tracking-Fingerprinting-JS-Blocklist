# 🛡️ Tracking (Fingerprinting) JS Blocklist 

---

- **Test only, use at your own risk :)**  
- Blocks common tracking JS that may use multiple browser APIs to fingerprint users.  
- Data source: [DuckDuckGo Tracker Radar](https://github.com/duckduckgo/tracker-radar) (see their [blog post](https://spreadprivacy.com/duckduckgo-tracker-radar/) and [docs](https://github.com/duckduckgo/tracker-radar/tree/main/docs) for detail) 

---  
  
#### 🔒 Tracking (Fingerprinting) JS Blocklist - High Certainty
- **URL blocklist**:  
[https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/URL-blocklists/tracking-js-high-URLs.txt](https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/URL-blocklists/tracking-js-high-URLs.txt)  
- **uBO blocklist**:  
[https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-high-uBO.txt](https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-high-uBO.txt)  
- **uBO blocklist - strict**:  
[https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-high-uBO-strict.txt](https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-high-uBO-strict.txt)
  
---
  
#### 🔏 Tracking (Fingerprinting) JS Blocklist - Possible tracking URLs
- **URL blocklist**:  
[https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/URL-blocklists/tracking-js-possible-URLs.txt](https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/URL-blocklists/tracking-js-possible-URLs.txt)  
- **uBO blocklist**:  
[https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-possible-uBO.txt](https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-possible-uBO.txt)  
- **uBO blocklist - strict**:  
[https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-possible-uBO-strict.txt
](https://raw.githubusercontent.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/main/uBO-blocklists/tracking-js-possible-uBO-strict.txt)
  
---
  
#### 🎯Source & Parameters 
Source:  
- DuckDuckGo Tracker Radar: [https://github.com/duckduckgo/tracker-radar](https://github.com/duckduckgo/tracker-radar)  
  
Parameters: 
- High Certainty blocklist: Fingerprinting = 3 ("almost certainly for tracking purposes")
- Possible tracking URLs blocklist: Fingerprinting = 2 ("possibly for tracking purposes")  
  
What does this mean?
- See [DDG Tracker Radar Data Model](https://github.com/duckduckgo/tracker-radar/blob/main/docs/DATA_MODEL.md#fingerprinting-0-3)  

---

#### 🔒🔒 uBO strict blocklists 🔏🔏

The strict version of the uBO blocklists makes use of the `$all` option in [uBO's extended syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax#all), mainly for additional protection concerning `inline script tags` and `inline font tags` (which can be used to fingerprint users) when another filter list contains an exception to unblock the URL.  

See a real-life example with more detail in our Wiki: [Notes on uBO strict blocklists](https://github.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/wiki/Notes-on-uBO-strict-blocklists)  
  
---
  
#### 🔓 Whitelisting & potential false positives
- Currently no whitelist is applied when generating the blocklists.
- You can create local exceptions (in uBO ect) to handle any false positives.
  
---
  
#### ⚙️ Generate blocklists
- The script used to generate these blocklists was adapted from [malware-filter/tracking-filter](https://gitlab.com/malware-filter/tracking-filter), converted to python with changes and tweaks.
  
---
  
## License
- This project: [Creative Commons Zero v1.0 Universal](https://github.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/blob/main/LICENSE)  
- DuckDuckGo Tracker Radar data: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This repository is not endorsed by DuckDuckGo.
- [Original scripts](https://gitlab.com/malware-filter/tracking-filter/-/tree/main/src) for URL extraction and blocklist generation: [Creative Commons Zero v1.0 Universal](https://gitlab.com/malware-filter/tracking-filter/-/blob/main/LICENSE-CC0.md) and [MIT License](https://gitlab.com/malware-filter/tracking-filter/-/blob/main/LICENSE).

---
