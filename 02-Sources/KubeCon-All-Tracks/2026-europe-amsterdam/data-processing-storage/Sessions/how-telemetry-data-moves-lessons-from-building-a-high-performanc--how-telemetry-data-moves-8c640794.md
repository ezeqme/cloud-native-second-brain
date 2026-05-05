---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["AI ML", "Networking", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Eduardo Silva", "Chronosphere | A Palo Alto Networks Company"]
sched_url: https://kccnceu2026.sched.com/event/2CW7N/how-telemetry-data-moves-lessons-from-building-a-high-performance-open-source-agent-eduardo-silva-chronosphere-a-palo-alto-networks-company
youtube_search_url: https://www.youtube.com/results?search_query=How+Telemetry+Data+Moves%3A+Lessons+From+Building+a+High-Performance+Open+Source+Agent+CNCF+KubeCon+2026
slides: []
status: parsed
---

# How Telemetry Data Moves: Lessons From Building a High-Performance Open Source Agent - Eduardo Silva, Chronosphere | A Palo Alto Networks Company

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[AI ML]], [[Networking]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Eduardo Silva, Chronosphere | A Palo Alto Networks Company
- Schedule: https://kccnceu2026.sched.com/event/2CW7N/how-telemetry-data-moves-lessons-from-building-a-high-performance-open-source-agent-eduardo-silva-chronosphere-a-palo-alto-networks-company
- Busca YouTube: https://www.youtube.com/results?search_query=How+Telemetry+Data+Moves%3A+Lessons+From+Building+a+High-Performance+Open+Source+Agent+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre How Telemetry Data Moves: Lessons From Building a High-Performance Open Source Agent.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7N/how-telemetry-data-moves-lessons-from-building-a-high-performance-open-source-agent-eduardo-silva-chronosphere-a-palo-alto-networks-company
- YouTube search: https://www.youtube.com/results?search_query=How+Telemetry+Data+Moves%3A+Lessons+From+Building+a+High-Performance+Open+Source+Agent+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SdovZWMJsgs
- YouTube title: How Telemetry Data Moves: Lessons From Building a High-Performance Open Source Agent - Eduardo Silva
- Match score: 1.002
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/how-telemetry-data-moves-lessons-from-building-a-high-performance-open/SdovZWMJsgs.txt
- Transcript chars: 22779
- Keywords: kernel, message, thread, always, concept, hardware, apache, application, course, format, memory, moving, connection, actually, behind, single, process, familiar

### Resumo baseado na transcript

Well, this is almost one of well almost one of the last session of today on the this cube con. So I appreciate you being here and actually it's always a bless that when you get this time is you know that people is around and you have less sessions so you will get more folks and but it's not about me it's about you and I appreciate the time to try to to learn about how data moves in a in a real system. Basically this is how two applications can connect right you might create a TCP connection on one client one server but behind the scenes all this data flow is happening and when we talk about hardware very realistically we talk about CPU cores memory disk that we use for storage. Of course today if you are generating a web app it won't be a problem because most of these things are abstracted but when it's about to moving data like um like a system level application it's not something that most of the time will However with experience you learn that you have to prepare for something for the worst case scenario. That's like a simple structure on how do we structure the logs internally in a chunk right and that chunk can rely in memory or in the file system.

### Excerpt da transcript

Thanks for coming. It's full. I appreciate the time. Who's leaving today? Almost everybody traveling back. Okay. I promise you won't be late to your flight. Okay. Would you mind if I take a photo of you guys? This fullback. Just raise your hands like There you go. One, two, three. Awesome. Well, this is almost one of well almost one of the last session of today on the this cube con. So I appreciate you being here and actually it's always a bless that when you get this time is you know that people is around and you have less sessions so you will get more folks and but it's not about me it's about you and I appreciate the time to try to to learn about how data moves in a in a real system. We have been doing this for a while and we always pitch our own projects, our own stuff. But behind every single project, there is a lot of engineering hours, lot of failures, lot of success and it's always good to share um how do we accomplish things, right? So that's why we're here. H for those who don't know me, my name is Eduardo.

Then you got my email. I have been around the Fluent DFL influent ecosystem for almost 10 years, a bit more. and let's get started. So this is not a product talk. I'm not going to pitch you a solution or something like that. But this is about how data moves, how data is buffer and go how it gets processed. Right? I know that you might have a lot of questions and the end of the session. If so, please you will have the microphone or we can talk after the session in case we don't have that much time. Okay. So the core path there's something that is called the kernel the operating system some something that we call the agent or the user space application and there's a concept of buffers where we accumulate data and outputs and all telemetry data all telemetry pipelines follow the same pattern. We get a mix of operating system, user space, application. We get the data from some place which we process and deliver to an special point. And if you look at any type of product, any open source project is the same.

We have what we call inputs or sources in a way. How do we retrieve or collect data? Then we got the concept of processors that we take this data. So we do some processing of it and then we ship this information out. Okay, nothing is h too different from that. Okay, we're going to get back now for a second to operating systems one. Okay, don't be scared. This is very high level and nobody want to get too much in detail. Who's familiar with ke
