---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Eduardo Silva", "Calyptia"]
sched_url: https://kccncna2023.sched.com/event/1R2pQ/fluent-bit-telemetry-agent-eduardo-silva-calyptia
youtube_search_url: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Telemetry+Agent+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Fluent Bit: Telemetry Agent - Eduardo Silva, Calyptia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Eduardo Silva, Calyptia
- Schedule: https://kccncna2023.sched.com/event/1R2pQ/fluent-bit-telemetry-agent-eduardo-silva-calyptia
- Busca YouTube: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Telemetry+Agent+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Fluent Bit: Telemetry Agent.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2pQ/fluent-bit-telemetry-agent-eduardo-silva-calyptia
- YouTube search: https://www.youtube.com/results?search_query=Fluent+Bit%3A+Telemetry+Agent+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TYUrYMZ1tvg
- YouTube title: Fluent Bit: Telemetry Agent - Eduardo Silva, Calyptia
- Match score: 0.773
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/fluent-bit-telemetry-agent/TYUrYMZ1tvg.txt
- Transcript chars: 35490
- Keywords: fluent, information, collect, events, around, memory, metrics, everything, processing, question, logs, process, running, windows, output, plugin, chunks, called

### Resumo baseado na transcript

hello welcome to I think the last session of the day the first day at cucon so my name is Ardo Silva and maybe I would like to know who's your first time here at cucon today first timers oh that's great cool and do we have any new fluent bit users who's not using the technology already or are old users somehow happy or not your users okay questions questions okay no no left for one answer right for the other both that works awesome so to get it

### Excerpt da transcript

hello welcome to I think the last session of the day the first day at cucon so my name is Ardo Silva and maybe I would like to know who's your first time here at cucon today first timers oh that's great cool and do we have any new fluent bit users who's not using the technology already or are old users somehow happy or not your users okay questions questions okay no no left for one answer right for the other both that works awesome so to get it started today we're going to introduce the technology we're going to talk about and the stand of the project where we going and how do we fit in all this huge ecosystem that for new starters is got sometimes a bit complex right you don't know where to start now we have I don't know how many projects we have in the cncf but when we join we were six projects and now I I lost the count but today we're going to focus on flu and B what is called the Telemetry agent my name is Ardo Silva and the creator of flu and bed a cncf maintainer I has been with the cncf for a long time and a Founder also this company called calpia and actual CEO and let's talk about the problems that we solved in the ecosystem and I think that's the most important thing when you start doing the in this journey for example most of you might start with loging one of the challenges that we had is like you don't want to wake up one morning and say I want to do login and feel really happy about it actually you want to solve another problem which is about data analysis that ended up that you want to solve loging right so if we Look Backwards our goal is to get insights and to get insights you need to collect information from applications from the running systems and when you got an issue or you talk to an Ops person or if you an UPS person the first question is hey do we have the ls or give me more LS right but you might understand that in today's world getting more LS or more data doesn't means more value doesn't mean more more answers right and we need different approaches to deal with the scalability of data that we have in our systems if you think about applications all of them store the data in different places usually in the file system right with a different file for example genx creates an access log for HTTP requests an error error log CIS loog has its own endpoint but if you go to for example a Windows system you will find that hey there's an API a way to extract logs from that a not common operating system and when you go want to go deeper and
