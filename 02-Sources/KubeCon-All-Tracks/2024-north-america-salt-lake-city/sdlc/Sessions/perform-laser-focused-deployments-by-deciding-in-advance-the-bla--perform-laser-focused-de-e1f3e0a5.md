---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "SDLC"
themes: ["GitOps Delivery"]
speakers: ["Kostis Kapelonis", "Octopus deploy"]
sched_url: https://kccncna2024.sched.com/event/1i7mH/perform-laser-focused-deployments-by-deciding-in-advance-the-blast-radius-kostis-kapelonis-octopus-deploy
youtube_search_url: https://www.youtube.com/results?search_query=Perform+Laser+Focused+Deployments+by+Deciding+in+Advance+the+Blast+Radius+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Perform Laser Focused Deployments by Deciding in Advance the Blast Radius - Kostis Kapelonis, Octopus deploy

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Salt Lake City
- Speakers: Kostis Kapelonis, Octopus deploy
- Schedule: https://kccncna2024.sched.com/event/1i7mH/perform-laser-focused-deployments-by-deciding-in-advance-the-blast-radius-kostis-kapelonis-octopus-deploy
- Busca YouTube: https://www.youtube.com/results?search_query=Perform+Laser+Focused+Deployments+by+Deciding+in+Advance+the+Blast+Radius+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Perform Laser Focused Deployments by Deciding in Advance the Blast Radius.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7mH/perform-laser-focused-deployments-by-deciding-in-advance-the-blast-radius-kostis-kapelonis-octopus-deploy
- YouTube search: https://www.youtube.com/results?search_query=Perform+Laser+Focused+Deployments+by+Deciding+in+Advance+the+Blast+Radius+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=95OFqU4UjiE
- YouTube title: Perform Laser Focused Deployments by Deciding in Advance the Blast Radius - Kostis Kapelonis
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/perform-laser-focused-deployments-by-deciding-in-advance-the-blast-rad/95OFqU4UjiE.txt
- Transcript chars: 33126
- Keywords: version, canary, traffic, header, request, feature, gateway, application, argo, everybody, change, provider, headers, canaris, support, affected, decide, running

### Resumo baseado na transcript

welcome to another cubon presentation this time about my favorite project aror outs and how you do laser focus deployments so my name is ctis I'm working as a developer Advocate at uh codr now octopus deploy I'm also part of the Argo team focusing mainly on Argo CD and Argo alls uh Cod is an Enterprise Solution on top of all the four Argo projects um we also offer a hard and sec distribution of Argo CD and we are the creators of the first ever gups certification this

### Excerpt da transcript

welcome to another cubon presentation this time about my favorite project aror outs and how you do laser focus deployments so my name is ctis I'm working as a developer Advocate at uh codr now octopus deploy I'm also part of the Argo team focusing mainly on Argo CD and Argo alls uh Cod is an Enterprise Solution on top of all the four Argo projects um we also offer a hard and sec distribution of Argo CD and we are the creators of the first ever gups certification this presentation is not about cpress but if this is interesting to you we have a booth uh outside and you can come and talk to us so today we are going to talk about Argo outs we are going to see how you can do laser focused uh deployments I'm actually going to show you two methods the easy but not very flexible and the hard but flexible as it usually goes and then the CCF sent an email to all um speakers and said if you have a demo do a recording because the Wi-Fi sucks so I followed their advice and we have not just one but two live demos without any recording so hopefully this will work so just to start with the basics we are going to talk about Progressive delivery and Progressive delivery in the context of Argo roll out means blue green and Canary deployments so for blue green you have your version running it's live users are looking looking at it then you start a new instance of the application the next version it doesn't get any traffic so this is your chance to do some unit test some integration test some smoke tests then you're confident and you say okay this looks correct and you switch the traffic and after a while you completely discard the old version so this is blue green and for canaris it's the same thing but instead of having a single point of time where you do the traffic switch you gradually send more traffic to the new version so you start with 10% then 20% 30% and so on if and if something goes wrong at any point you can roll back so why do we need this because if you are familiar with how kubernetes works out of the box kubernetes only offers um rolling deployments where you lose one pod and you gain another pod from the new version and this is not something you have direct control on you cannot you know stop the process and do something else and there is also the recreate strategy which I'm not going to talk about it because it has downtime and we don't want downtime at all so how do we do canaris we use Argo roll outs which is one of the four Argo projects one important thi
