---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Service Mesh"
themes: ["Security", "Networking"]
speakers: ["Catherine Paganini", "Buoyant", "Kasper Nissen", "Lunar", "Fredrik Klingenberg", "Aurum AS", "Eli Goldberg", "Salt Security", "Christian Hüning", "Finleap Connect"]
sched_url: https://kccnceu2022.sched.com/event/ytsZ/linkerd-end-user-panel-case-studies-from-production-catherine-paganini-buoyant-kasper-nissen-lunar-fredrik-klingenberg-aurum-as-eli-goldberg-salt-security-christian-huning-finleap-connect
youtube_search_url: https://www.youtube.com/results?search_query=Linkerd+End+User+Panel%3A+Case+Studies+from+Production+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Linkerd End User Panel: Case Studies from Production - Catherine Paganini, Buoyant; Kasper Nissen, Lunar; Fredrik Klingenberg, Aurum AS; Eli Goldberg, Salt Security; Christian Hüning, Finleap Connect

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Service Mesh]]
- Temas: [[Security]], [[Networking]]
- País/cidade: Spain / Valencia
- Speakers: Catherine Paganini, Buoyant, Kasper Nissen, Lunar, Fredrik Klingenberg, Aurum AS, Eli Goldberg, Salt Security, Christian Hüning, Finleap Connect
- Schedule: https://kccnceu2022.sched.com/event/ytsZ/linkerd-end-user-panel-case-studies-from-production-catherine-paganini-buoyant-kasper-nissen-lunar-fredrik-klingenberg-aurum-as-eli-goldberg-salt-security-christian-huning-finleap-connect
- Busca YouTube: https://www.youtube.com/results?search_query=Linkerd+End+User+Panel%3A+Case+Studies+from+Production+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Linkerd End User Panel: Case Studies from Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytsZ/linkerd-end-user-panel-case-studies-from-production-catherine-paganini-buoyant-kasper-nissen-lunar-fredrik-klingenberg-aurum-as-eli-goldberg-salt-security-christian-huning-finleap-connect
- YouTube search: https://www.youtube.com/results?search_query=Linkerd+End+User+Panel%3A+Case+Studies+from+Production+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_DbZ6SFdY1g
- YouTube title: Linkerd End User Panel: Case Studies from Production
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/linkerd-end-user-panel-case-studies-from-production/_DbZ6SFdY1g.txt
- Transcript chars: 35408
- Keywords: actually, mesh, cluster, looking, little, everything, linkedin, another, clusters, around, features, started, running, solution, multi-cluster, having, production, platform

### Resumo baseado na transcript

okay i think we're live um well welcome everyone to today's linker the end user panels on case studies on production uh and i'm catherine paganini with buoyant the creator of linkerd where i work very closely with our end user community including our panelists today we'll hear from four panelists today from a variety of industries uh all of them have lots of linker d production experience and so yeah why don't we go through the line and why don't you introduce yourself and tell us a little bit once we had linkedin we only noticed that this is a problem once we ran this like in dev uh without link id occasionally so yeah you got it for free you get it for free yeah okay and um you did write a cncf blog post and then there you wrote that once you meshed your your services you a new whole world of reliability visibility and security opened up can you tell us about that right yeah so i mean at first we didn't really know what a

### Excerpt da transcript

okay i think we're live um well welcome everyone to today's linker the end user panels on case studies on production uh and i'm catherine paganini with buoyant the creator of linkerd where i work very closely with our end user community including our panelists today we'll hear from four panelists today from a variety of industries uh all of them have lots of linker d production experience and so yeah why don't we go through the line and why don't you introduce yourself and tell us a little bit about who you are uh your implementation and what were you trying to achieve eileen yeah so uh my name is ellie goldberg uh i'm with the platform team and solid security sold as a as an api security company so we protect apis for our customers um we're running link rd on multiple production clusters and we came to found link rd because we were actually looking for a grpc load balancing solution and that was a perfect fit for us so happy to be here cool my name is casper i work at a company called lunar i'm the lead platform architect i'm also a cncf ambassador and yeah we use lingadine in production across multiple clouds so we primarily use the multi-cluster feature and we are sort of slowly adopting cherished machine in general yeah my name is christian hooning i'm the tech lead or the the cloud lead for at findlay connect we are using linkedin since um 2019 in production so we were quite early adopters and finite connect is a financial services provider from germany that's uh why we care deeply about the mutual tls features and these kind of things yeah my name is federer cleanbach i work for a small consulting company in norway oslo i've been helping various companies over to the cloud the more kubernetes landscapes and using linkedin on a couple of projects awesome yeah and definitely different reason uh different reasons for you to link rd right and so let's talk about grpc load balancing real quick um so you did implement jpc at sold security and can you tell us a little bit about that and how you realized that you needed a service mesh sure so um sorry yeah um so install security we're running with about 40 micro services on kubernetes and we introduced grpc in the past couple years because well we we're growing rapidly and we we've seen a lot of friction between teams and deployments of microservices so apis would break and we're looking for kind of a way to prevent prevent that from happening before we reach production so grpc was kind of the perfect soluti
