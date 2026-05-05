---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Runtime Containers", "Community Governance"]
speakers: ["Jason Dellaluce", "Leonardo Grasso", "Luca Guerra", "Sysdig", "Carlos Tadeu Panato Junior", "Chainguard", "Melissa Kilby", "Apple"]
sched_url: https://kccncna2024.sched.com/event/1howz/peak-innovation-and-cloud-tweaks-falcos-ongoing-runtime-security-development-jason-dellaluce-leonardo-grasso-luca-guerra-sysdig-carlos-tadeu-panato-junior-chainguard-melissa-kilby-apple
youtube_search_url: https://www.youtube.com/results?search_query=Peak+Innovation+and+Cloud+Tweaks%3A+Falco%E2%80%99s+Ongoing+Runtime+Security+Development+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Peak Innovation and Cloud Tweaks: Falco’s Ongoing Runtime Security Development - Jason Dellaluce, Leonardo Grasso & Luca Guerra, Sysdig; Carlos Tadeu Panato Junior, Chainguard; Melissa Kilby, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Jason Dellaluce, Leonardo Grasso, Luca Guerra, Sysdig, Carlos Tadeu Panato Junior, Chainguard, Melissa Kilby, Apple
- Schedule: https://kccncna2024.sched.com/event/1howz/peak-innovation-and-cloud-tweaks-falcos-ongoing-runtime-security-development-jason-dellaluce-leonardo-grasso-luca-guerra-sysdig-carlos-tadeu-panato-junior-chainguard-melissa-kilby-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Peak+Innovation+and+Cloud+Tweaks%3A+Falco%E2%80%99s+Ongoing+Runtime+Security+Development+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Peak Innovation and Cloud Tweaks: Falco’s Ongoing Runtime Security Development.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howz/peak-innovation-and-cloud-tweaks-falcos-ongoing-runtime-security-development-jason-dellaluce-leonardo-grasso-luca-guerra-sysdig-carlos-tadeu-panato-junior-chainguard-melissa-kilby-apple
- YouTube search: https://www.youtube.com/results?search_query=Peak+Innovation+and+Cloud+Tweaks%3A+Falco%E2%80%99s+Ongoing+Runtime+Security+Development+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bpl9nuSIHuU
- YouTube title: Peak Innovation and Cloud Tweaks: Falco’s Ongoing Runtime Security Development - Panel
- Match score: 1.042
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/peak-innovation-and-cloud-tweaks-falcos-ongoing-runtime-security-devel/bpl9nuSIHuU.txt
- Transcript chars: 25118
- Keywords: security, plugins, itself, actually, introduced, plug-in, provide, course, support, plugin, language, latest, specific, output, alerts, always, kernel, environment

### Resumo baseado na transcript

hello everyone and welcome to the Falcon M Tru in in Salt Lake City oh sorry okay I'm Leonardo one of the Falco core maintainer joining me today are my fellow maintainers Carlos Jason and Luca Melissa should have also been here but unfortunately she couldn't join us today so we are sending her a big H today we are we will talk about Falcon going development in the cloud net security so thank you for being here and let's dive in to begin let's answer the question what Falco

### Excerpt da transcript

hello everyone and welcome to the Falcon M Tru in in Salt Lake City oh sorry okay I'm Leonardo one of the Falco core maintainer joining me today are my fellow maintainers Carlos Jason and Luca Melissa should have also been here but unfortunately she couldn't join us today so we are sending her a big H today we are we will talk about Falcon going development in the cloud net security so thank you for being here and let's dive in to begin let's answer the question what Falco is Falco is a cloud native tool for and time security across host containers kubernets and the cloud it offers realtime threat detection by monitor Canal activity and other data source then delivering alerts when unexpected Beav detected it's extensible flexible Falco support plugins and custom room tool that allow you to tailor it for your security needs think of FAL as a security camera for your cloud and infrastructure offering real-time visibility and automatic DET detection of security Poli violations as a cncf graduated project Falco is trusted and widely adopted and an incredible Community take care of its development we are always proud to remark that Falco is not just about technology but is also about people to honor these we always remember the principle that have shaped the Falco project and that are also formalized into our governance our commitment to those values has always been the project powers and a call to everyone to join our journey now let's look at how Falco Works Falco monitors kernel or Cloud events through plug-in capturing the activity in your environment then reaches this events with contextual metadata like container formation or kubernetes metadata then it evaluates them against defined security rules to detect anomalies if suspicious activity is detected Falco generates realtime alerts notifying you immediately Falco can also forward alerts to any service or we will see later can even react automatically this continuous process provide you deeper visibility and contributes to the security of your Cloud application I want to complete this overview by letting you explore the fal Journey from from its Inception everything started in 2016 when CDI created Falco to address the need of for time Security in Cloud native environment in 2018 FAL became the first ever runtime security project accepted by the cncf and due to strong adoption and contribution it Advanced to the incubation level two years later finally uh by February 2024 Falco graduated from the cncf s
