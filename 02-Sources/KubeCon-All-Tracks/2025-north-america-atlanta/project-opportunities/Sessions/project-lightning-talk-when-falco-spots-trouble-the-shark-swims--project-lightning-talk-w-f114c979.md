---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Gerald Combs", "Falco Core Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d4o/project-lightning-talk-when-falco-spots-trouble-the-shark-swims-in-gerald-combs-falco-core-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+When+Falco+Spots+Trouble%2C+The+Shark+Swims+In+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: When Falco Spots Trouble, The Shark Swims In - Gerald Combs, Falco Core Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Gerald Combs, Falco Core Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d4o/project-lightning-talk-when-falco-spots-trouble-the-shark-swims-in-gerald-combs-falco-core-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+When+Falco+Spots+Trouble%2C+The+Shark+Swims+In+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: When Falco Spots Trouble, The Shark Swims In.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4o/project-lightning-talk-when-falco-spots-trouble-the-shark-swims-in-gerald-combs-falco-core-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+When+Falco+Spots+Trouble%2C+The+Shark+Swims+In+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=phndUkSlIvs
- YouTube title: Project Lightning Talk: When Falco Spots Trouble, The Shark Swims In - Gerald Combs
- Match score: 0.99
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-when-falco-spots-trouble-the-shark-swims-in/phndUkSlIvs.txt
- Transcript chars: 4407
- Keywords: process, wireshark, capture, happened, investigate, stratark, familiar, looking, filter, stream, environment, feature, messages, couple, libraries, libcap, sounds, scroll

### Resumo baseado na transcript

I am the creator and lead developer of Wireshark and I'm also a Falco maintainer. And today I'm going to talk about how those tools can work together to help you detect and investigate threats in your environment. Um as a bit of a demo suppose you have Falco deployed in your environment and it sends you an alert. Uh if you want to learn more about Falco and Stratark, they both have their respective websites, falco.org and stratshock.org.

### Excerpt da transcript

All right, good morning everyone. I am Gerald Combmes. I am the creator and lead developer of Wireshark and I'm also a Falco maintainer. And today I'm going to talk about how those tools can work together to help you detect and investigate threats in your environment. First of all, Falco is a cloudnative real-time threat detection engine. It runs on your systems and monitors the system calls that are, you know, happening on that system and if it detects anything sketchy, it will send you an alert. Uh the latest release of Falco also has this really cool feature that will optionally save those system calls out to a capture file. This lets you then pivot over to a tool like Stratoshark. Stratark is based on Wireshark if you're familiar with that. It uh focuses on letting you investigate system calls and log messages on locally on your desktop. And I'll show that off here in a second. Um but both of these tools are based around a couple of libraries. Uh libcap and libs. LibCap will capture system calls and through a plug-in interface also capture log messages.

Libsense will then pull those up and enrich them and add uh you know contextual data and then the applications that use those libraries can then you know display useful information and make you know use of that otherwise. Um as a bit of a demo suppose you have Falco deployed in your environment and it sends you an alert. Um somebody popped a shell in a container. Uh that sounds bad. So Falco has graciously given us a process ID to work with and a process name. So let's kind of take a look at what happened. I'm going to switch over to Stratark here and load up the capture file that FCO provided me. Um if you're familiar with Wireshark, this should look kind of or if you if you've used Wireshark, this should look familiar. But instead of looking at packets here, we're looking at system calls. you can see you know the system call name and the process name, process ID and so on up top and the event list and down below you can see details about the event that you have selected. Um I can see that the very first event is bash starting up uh with the executive e system call and the correct process ID.

So I'm going to take that process ID field and drag it up to the filter bar here and apply this as a filter. And this shows me only the system calls that have to do with this bash process. If I scroll down, you know, I kind of want to see what the user typed in this bash process. So, I see a bunch of reads here.
