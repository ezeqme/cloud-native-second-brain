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
speakers: ["Jason Dellaluce", "Leonardo Grasso", "Luca Guerra", "Sysdig", "Melissa Kilby", "Apple", "Carlos Tadeu Panato Junior", "Chainguard"]
sched_url: https://kccncna2023.sched.com/event/1R2oH/avoid-an-ill-wind-and-catch-the-jet-stream-using-falco-to-detect-attackers-compliance-violations-jason-dellaluce-leonardo-grasso-luca-guerra-sysdig-melissa-kilby-apple-carlos-tadeu-panato-junior-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Avoid+an+Ill+Wind+and+Catch+the+Jet+Stream+%E2%80%93+Using+Falco+to+Detect+Attackers+%26+Compliance+Violations+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Avoid an Ill Wind and Catch the Jet Stream – Using Falco to Detect Attackers & Compliance Violations - Jason Dellaluce, Leonardo Grasso & Luca Guerra, Sysdig; Melissa Kilby, Apple; Carlos Tadeu Panato Junior, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Jason Dellaluce, Leonardo Grasso, Luca Guerra, Sysdig, Melissa Kilby, Apple, Carlos Tadeu Panato Junior, Chainguard
- Schedule: https://kccncna2023.sched.com/event/1R2oH/avoid-an-ill-wind-and-catch-the-jet-stream-using-falco-to-detect-attackers-compliance-violations-jason-dellaluce-leonardo-grasso-luca-guerra-sysdig-melissa-kilby-apple-carlos-tadeu-panato-junior-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Avoid+an+Ill+Wind+and+Catch+the+Jet+Stream+%E2%80%93+Using+Falco+to+Detect+Attackers+%26+Compliance+Violations+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Avoid an Ill Wind and Catch the Jet Stream – Using Falco to Detect Attackers & Compliance Violations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2oH/avoid-an-ill-wind-and-catch-the-jet-stream-using-falco-to-detect-attackers-compliance-violations-jason-dellaluce-leonardo-grasso-luca-guerra-sysdig-melissa-kilby-apple-carlos-tadeu-panato-junior-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Avoid+an+Ill+Wind+and+Catch+the+Jet+Stream+%E2%80%93+Using+Falco+to+Detect+Attackers+%26+Compliance+Violations+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ck-E2NzLhDY
- YouTube title: Avoid an Ill Wind and Catch the Jet Stream – Using Falco to Detect Attackers & Compliance Violations
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/avoid-an-ill-wind-and-catch-the-jet-stream-using-falco-to-detect-attac/Ck-E2NzLhDY.txt
- Transcript chars: 27431
- Keywords: kernel, actually, process, security, container, detection, version, another, everything, plugins, maintainer, probably, talking, pretty, better, framework, performance, basically

### Resumo baseado na transcript

hello everyone and welcome to the maintainer track for Falco avoid a little wind and catch the jet stream using Falco to detect attackers and compliance violation I am Luca and I work as a software engineer at ssig and I'm joined here and I'm also Falcon maintainer and I'm joined here with other awesome Falcon maintainers uh we have Carlos who is a software engineer and very expert coffee maker at chuard and also I'm joined by Jason also a software engineer at ssig and a security engineer at

### Excerpt da transcript

hello everyone and welcome to the maintainer track for Falco avoid a little wind and catch the jet stream using Falco to detect attackers and compliance violation I am Luca and I work as a software engineer at ssig and I'm joined here and I'm also Falcon maintainer and I'm joined here with other awesome Falcon maintainers uh we have Carlos who is a software engineer and very expert coffee maker at chuard and also I'm joined by Jason also a software engineer at ssig and a security engineer at Apple so uh today we'll be talking about Falco and I guess that if you're in the maintainer track for Falco you know uh what what we're talking about but anyways as a refresher Falco is an open source security project for threat detection across kubernetes containers hosts and the cloud it started as a project to detect any suspicious events via rules in system C by Roots using system calls in your hosts and your containerized environment and then gain the ability to inspect kubernetes as well and then now with its powerful plug-in system is extended to the cloud and pretty much every sort of event that you can think about it uh Falco is currently a currently a cncf incubation level project but I have some uh exciting news to share that the Falon maintainer and contributor community have have worked uh very hard to get the Falco project closer to graduation and indeed we we made a lot of progress and I am very happy to say that we have passed I think what is the most important part of the graduation Pro process which is uh knowing that the cncf technical oversight committee uh has decided that uh FAL is mature enough to really proceed to graduation of course we are still working a lot with the community to get it to complete graduation but really uh we just wanted to take this time to say thank you to uh actually you the the not just the code contributors but the people that use FCO the adopters and everyone that made it actually successful and not just a a simple open source project that someone at a company started one day so so just stay tuned for a graduated version uh well for graduated in the cncf Falon uh but anyways Falco is not just uh talking about graduation Falco uh the Falco project has been working a lot to uh be easier to use for everyone to have better detection capability and to have better security and and all these things and uh I would like to um to ask uh meliss and to give the word to Melissa who has worked a lot to about something that has been a
