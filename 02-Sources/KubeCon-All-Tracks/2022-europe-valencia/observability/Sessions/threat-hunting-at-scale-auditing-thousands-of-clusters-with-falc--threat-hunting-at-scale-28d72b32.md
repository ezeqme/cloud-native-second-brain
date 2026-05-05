---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Observability"
themes: ["Observability", "Kubernetes Core", "SRE Reliability"]
speakers: ["Furkan Türkal", "Emin Aktaş", "Trendyol"]
sched_url: https://kccnceu2022.sched.com/event/ytrP/threat-hunting-at-scale-auditing-thousands-of-clusters-with-falco-+-fluent-furkan-turkal-emin-aktas-trendyol
youtube_search_url: https://www.youtube.com/results?search_query=Threat+Hunting+at+Scale%3A+Auditing+Thousands+of+Clusters+With+Falco+%2B+Fluent+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Threat Hunting at Scale: Auditing Thousands of Clusters With Falco + Fluent - Furkan Türkal & Emin Aktaş, Trendyol

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Furkan Türkal, Emin Aktaş, Trendyol
- Schedule: https://kccnceu2022.sched.com/event/ytrP/threat-hunting-at-scale-auditing-thousands-of-clusters-with-falco-+-fluent-furkan-turkal-emin-aktas-trendyol
- Busca YouTube: https://www.youtube.com/results?search_query=Threat+Hunting+at+Scale%3A+Auditing+Thousands+of+Clusters+With+Falco+%2B+Fluent+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Threat Hunting at Scale: Auditing Thousands of Clusters With Falco + Fluent.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytrP/threat-hunting-at-scale-auditing-thousands-of-clusters-with-falco-+-fluent-furkan-turkal-emin-aktas-trendyol
- YouTube search: https://www.youtube.com/results?search_query=Threat+Hunting+at+Scale%3A+Auditing+Thousands+of+Clusters+With+Falco+%2B+Fluent+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OyB0TWVjZvY
- YouTube title: Threat Hunting at Scale: Auditing Thousands of Clusters With Falco + F... Furkan Türkal & Emin Aktaş
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/threat-hunting-at-scale-auditing-thousands-of-clusters-with-falco-flue/OyB0TWVjZvY.txt
- Transcript chars: 22960
- Keywords: logs, cluster, events, second, clusters, kernel, containers, pipeline, security, monitoring, already, collect, labels, session, production, source, simply, basically

### Resumo baseado na transcript

hi welcome to keep calm and sincere this session is pre-recorded and we are speaking to you from the past our present stars will be watching the chat and please feel free to ask any questions we will talk about threat of hunting and scale by using kubernetes audit logs and current kernel events and in this journey we are not going to dip that into each technology that we utilize for our purpose but it's more than that we want to tell our user story to show the way your trust boundaries here our transponder is basically our clusters nodes and of course containers the main key point here is to create a focused defense area that we should create fine-tuned rules and alert mechanisms especially if you work on a high scale you need to label your logs to mark where the data is sourced if we are able to find repeatable patterns to detect threats by person looks we can easily optimize our hunting here our security pipeline and we call it our second path security pipeline

### Excerpt da transcript

hi welcome to keep calm and sincere this session is pre-recorded and we are speaking to you from the past our present stars will be watching the chat and please feel free to ask any questions we will talk about threat of hunting and scale by using kubernetes audit logs and current kernel events and in this journey we are not going to dip that into each technology that we utilize for our purpose but it's more than that we want to tell our user story to show the way how we did it and demonstrate how everything works in harmony and our production let's get started i am for country cal and international i am maintaining production level clusters as a platform engineer also i am contributing to various cnc projects and open source projects hello my name is imin i have been working on containers and the technologies around containers for the last two years i love working on open source projects and i love watching uh car videos okay before we get into it uh we want to introduce ourselves uh tranquil is a tech company that they focus on e-commerce in turkey and creates a positive impact on our country and the ecosystem at 10 years we are running thousands of kubernetes elasticsearch nosql databases and much more we are highly motivated to include open source project into our systems and be part of open source project community and projects we are mostly managing our infrastructure on prem that is distributed across seven different data centers running h8 kubernetes clusters this is going to be our very first cncf presentation as a trend yo so as you see here this is our infrastructure matrix you can monitor our metrics at real time by just entering informatics infometrix.chandual.com and before we get into the presentation we want to thank our platform team for their great work and send special greetings to our squad for the awesome teamwork okay who is this station for if you are curious about runtime security and trade hunting at production and want to know how you can monitor entire system this session is definitely for you you will learn how we detect rates automate the process of collecting and analyzing outlooks to monitor of potential security threats then to edge these threats with appropriate actions moreover this session is investigating this suspicious of this in your infrastructure and create a baseline for monitoring and alerting best of all we it's all done with open source projects okay in today in this session uh we'll talk about the threats and o
