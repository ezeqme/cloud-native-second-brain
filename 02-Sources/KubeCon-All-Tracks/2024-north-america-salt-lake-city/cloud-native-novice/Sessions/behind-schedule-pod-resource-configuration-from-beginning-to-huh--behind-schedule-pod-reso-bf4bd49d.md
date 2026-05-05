---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Novice"
themes: ["Cloud Native Novice"]
speakers: ["Joe Thompson", "Clarity Business Solutions"]
sched_url: https://kccncna2024.sched.com/event/1i7kb/behind-schedule-pod-resource-configuration-from-beginning-to-huh-joe-thompson-clarity-business-solutions
youtube_search_url: https://www.youtube.com/results?search_query=Behind+Schedule%3A+Pod+Resource+Configuration+from+Beginning+to...+Huh%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Behind Schedule: Pod Resource Configuration from Beginning to... Huh? - Joe Thompson, Clarity Business Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Cloud Native Novice]]
- País/cidade: United States / Salt Lake City
- Speakers: Joe Thompson, Clarity Business Solutions
- Schedule: https://kccncna2024.sched.com/event/1i7kb/behind-schedule-pod-resource-configuration-from-beginning-to-huh-joe-thompson-clarity-business-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=Behind+Schedule%3A+Pod+Resource+Configuration+from+Beginning+to...+Huh%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Behind Schedule: Pod Resource Configuration from Beginning to... Huh?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kb/behind-schedule-pod-resource-configuration-from-beginning-to-huh-joe-thompson-clarity-business-solutions
- YouTube search: https://www.youtube.com/results?search_query=Behind+Schedule%3A+Pod+Resource+Configuration+from+Beginning+to...+Huh%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2OkpYGtFd1Y
- YouTube title: Behind Schedule: Pod Resource Configuration from Beginning to... Huh? - Joe Thompson
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/behind-schedule-pod-resource-configuration-from-beginning-to-huh/2OkpYGtFd1Y.txt
- Transcript chars: 31117
- Keywords: priority, cluster, actually, running, resources, resource, eviction, schedule, requests, guaranteed, memory, preemption, critical, disruption, limits, little, quality, request

### Resumo baseado na transcript

let's jump into it uh welcome to my session behind schedule pod resource configuration from beginning to I'm sure we've all had that moment where we we thought that something was going to start running and it did not and it didn't seem like it did so for a reason that made any sense at all yes so let's do a little bit of introduction I'll tell you a little bit about myself although not too much so we don't take up too much time I like to take the

### Excerpt da transcript

let's jump into it uh welcome to my session behind schedule pod resource configuration from beginning to I'm sure we've all had that moment where we we thought that something was going to start running and it did not and it didn't seem like it did so for a reason that made any sense at all yes so let's do a little bit of introduction I'll tell you a little bit about myself although not too much so we don't take up too much time I like to take the temp tempure the room a little bit as I get started too and then kind of what are we here for today so before we get started and for real it's really dry out there if you just flew in last night and you woke up this morning and your throat felt like the desert outside Salt Lake City and Utah are the one of the driest areas in the US please for your own health and safety drink water constantly the whole time you're here there's water bottle swag at Plenty Of Enders I'm sure go buy one from the cncf store if you have need one uh definitely it is worth your time it's worth your time and attention to make sure that you're getting enough water here so who am I uh my name is Joe Thompson uh I've been working in it overall for almost 30 years depending on how you count uh I usually count from December of 1995 that was my first full-time paying it job along the way to get to today I've worked for Red Hat cor mesosphere hashy forp some of the names people in the room might know uh currently I a Consulting engineer for a company called Clarity Business Solutions they're based uh fairly near DC and the part of the company that I work in is their mongod DB partnership uh we provide escalation support for mongod DB customers among other things my basic pronouns right there uh the pop culture reference center of gravity is fairly important if you're talking to me you will eventually get a movie reference to like a John Hughes movie or office space or something like that and there's some contact info there now as far as people in the room I see we still have some people coming in but it looks like we're pretty full up now uh who here this is your first cubec con okay yeah usually a lot of hands go up for that um who here has been working with kubernetes for less than a year okay keep your hands up uh put your hands down if you've been working more than 6 months who hear still is okay so we have a few that are really really new to this so great because this is very much a Basics talk but it does get into kind of like ezure learni
