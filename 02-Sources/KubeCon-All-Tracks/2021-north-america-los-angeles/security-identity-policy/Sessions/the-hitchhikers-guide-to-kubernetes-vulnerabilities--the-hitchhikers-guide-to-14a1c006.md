---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Robert Clark", "Micah Hausler", "Amazon"]
sched_url: https://kccncna2021.sched.com/event/lV5g/the-hitchhikers-guide-to-kubernetes-vulnerabilities-robert-clark-micah-hausler-amazon
youtube_search_url: https://www.youtube.com/results?search_query=The+Hitchhiker%27s+Guide+to+Kubernetes+Vulnerabilities+CNCF+KubeCon+2021
slides: []
status: parsed
---

# The Hitchhiker's Guide to Kubernetes Vulnerabilities - Robert Clark & Micah Hausler, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Robert Clark, Micah Hausler, Amazon
- Schedule: https://kccncna2021.sched.com/event/lV5g/the-hitchhikers-guide-to-kubernetes-vulnerabilities-robert-clark-micah-hausler-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hitchhiker%27s+Guide+to+Kubernetes+Vulnerabilities+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre The Hitchhiker's Guide to Kubernetes Vulnerabilities.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5g/the-hitchhikers-guide-to-kubernetes-vulnerabilities-robert-clark-micah-hausler-amazon
- YouTube search: https://www.youtube.com/results?search_query=The+Hitchhiker%27s+Guide+to+Kubernetes+Vulnerabilities+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RKm5QA3pdaQ
- YouTube title: The Hitchhiker's Guide to Kubernetes Vulnerabilities - Robert Clark & Micah Hausler, Amazon
- Match score: 0.83
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/the-hitchhikers-guide-to-kubernetes-vulnerabilities/RKm5QA3pdaQ.txt
- Transcript chars: 25056
- Keywords: vulnerabilities, vulnerability, security, actually, little, interesting, important, number, understand, around, information, looking, version, recently, presentation, trying, better, committee

### Resumo baseado na transcript

hello my name's robert clark and i'm here today to talk to you about the hitchhiker's guide to kubernetes vulnerabilities i recently joined the amazon elastic kubernetes service eks where i lead security i co-wrote this presentation with michael hauser who's been working on eks and contributing to the kubernetes security community for several years this presentation is really an exploration of what kubernetes vulnerabilities are how they are handled by the community and the things that the kubernetes operators users should take into consideration when deciding what to do early days of kubernetes uh maybe it actually stayed pretty great all the way up to the end of december 2018 you know modulo a small hiccup around the 1.9 release apparently things took a turn around version 1.14 if we just base only on when fixes are released 2019 through 2020 were really bad years for kubernetes and it and definitely uh busy years for the security response committee but at least things seem to have gotten better recently with only one issue fixed in the last couple of

### Excerpt da transcript

hello my name's robert clark and i'm here today to talk to you about the hitchhiker's guide to kubernetes vulnerabilities i recently joined the amazon elastic kubernetes service eks where i lead security i co-wrote this presentation with michael hauser who's been working on eks and contributing to the kubernetes security community for several years this presentation is really an exploration of what kubernetes vulnerabilities are how they are handled by the community and the things that the kubernetes operators users should take into consideration when deciding what to do about any given vulnerability in some ways this presentation is about how not to look at vulnerability data and a warning of the dangers of taking the data and data sources at face value neither myself or micah are data scientists most security architects engineers people who are going to be looking at vulnerability data and trying to use it to help make more informed choices aren't going to be a data scientist either so we've taken that approach we've pulled the data together uh we've tried to present it in a couple of different ways to help us understand whether kubernetes is doing better or worse with regards to software vulnerabilities and understand what we expect the trends to be in the future in the spring of 2021 red hat produced a kubernetes security report it was a short useful survey of industry but it showed that vulnerabilities were only the second most concerning issue raised among the more than 500 devops engineering and security professionals that participated in the survey there were some interesting call-outs in the survey 94 of respondents experienced at least one security incident in their kubernetes environments in just the last 12 months that is a terrifying statistic and 55 percent of respondents actually had to delay or slow down application deployments into production due to container or kubernetes security concerns so wall vulnerabilities might not be top of mind for survey respondents i believe that market pressures over the next 12 years may change the results of a similar survey and what do i mean by that well there's lots of attention being paid to improving the secure defaults in kubernetes right this is where everything the far far left of this graph today is all about misconfigurations there's an entire ecosystem of tools and support aimed at improving the full life cycle of kubernetes deployments by contrast not much has changed in the vulnerability manage
