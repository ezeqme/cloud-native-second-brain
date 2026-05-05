---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Business Value"
themes: ["Business Value"]
speakers: ["Pavel Nikolov", "Section"]
sched_url: https://kccnceu2022.sched.com/event/yttC/building-for-the-inevitable-next-cloud-outage-pavel-nikolov-section
youtube_search_url: https://www.youtube.com/results?search_query=Building+for+the+%28Inevitable%29+Next+Cloud+Outage+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Building for the (Inevitable) Next Cloud Outage - Pavel Nikolov, Section

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Business Value]]
- Temas: [[Business Value]]
- País/cidade: Spain / Valencia
- Speakers: Pavel Nikolov, Section
- Schedule: https://kccnceu2022.sched.com/event/yttC/building-for-the-inevitable-next-cloud-outage-pavel-nikolov-section
- Busca YouTube: https://www.youtube.com/results?search_query=Building+for+the+%28Inevitable%29+Next+Cloud+Outage+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Building for the (Inevitable) Next Cloud Outage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttC/building-for-the-inevitable-next-cloud-outage-pavel-nikolov-section
- YouTube search: https://www.youtube.com/results?search_query=Building+for+the+%28Inevitable%29+Next+Cloud+Outage+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=02a8VB__UQ4
- YouTube title: Building for the (Inevitable) Next Cloud Outage - Pavel Nikolov, Section
- Match score: 0.884
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/building-for-the-inevitable-next-cloud-outage/02a8VB__UQ4.txt
- Transcript chars: 31495
- Keywords: events, disaster, recovery, cluster, server, address, clusters, happen, always, consistency, servers, requests, database, another, internet, question, request, response

### Resumo baseado na transcript

i guess we are ready to start hola bueno almondo hello everyone my name is pavel and um i'm here to talk to you about high availability and high reliability in a distributed cloud native infrastructure and i believe that everybody in this room at one point or another has had problems with cloud outages these things happen they're inevitable it is really difficult to avoid them and no cloud provider can guarantee 100 uptime just because there are so many things that even the best teams can't avoid because

### Excerpt da transcript

i guess we are ready to start hola bueno almondo hello everyone my name is pavel and um i'm here to talk to you about high availability and high reliability in a distributed cloud native infrastructure and i believe that everybody in this room at one point or another has had problems with cloud outages these things happen they're inevitable it is really difficult to avoid them and no cloud provider can guarantee 100 uptime just because there are so many things that even the best teams can't avoid because they don't depend on themselves there are external factors like upstream provider internet connection issues there is the human factor and sometimes we can make mistakes in our deployments or code that we deploy there are natural disasters that can take regions down or cause major trouble for all kinds of services around the globe and it is prohibitively expensive no matter what type of business you are to deploy your applications everywhere around the world at the same time so it is not a question of if your servers will go down or services it is a question of when and usually these things happen when you least expect it or you're not prepared for them and somebody gets paged in your company and they have to figure out in probably in the middle of the night if they're lucky during business hours how to solve a problem um and even major things like your dns can go down and your team can make you know a mistake that is difficult to roll back so many of us usually deal with these things with disaster recovery and the vast majority of people fall in one of these four categories when it comes to disaster recovery you either have some form of active active um deployment which means you know if your primary server goes down you flip the switch in your dns and your request go to the second one the which is active if you're in this category probably or one of the lucky guys the other one is active passive it is similar to the previous one but it's cheaper because you don't pay for the hosting for the passive instance or cluster or whatever it might be and you have to spin up the passive instance then you flip the switch in your dns and now you have happy users no more complaints in you know social media that your services are down or maybe your customers aren't happy another option is again to have a periodic backups of your databases and then when things go down you spin up your code somewhere you restore the backups and then you continue serving as normal and th
