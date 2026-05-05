---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Diana Patton", "Gunna Marripudi", "NetApp", "Scott Surovich", "HSBC Bank", "USA", "Scott Miller", "DreamWorks Animation", "Lisa-Marie Namphy", "Cockroach Labs"]
sched_url: https://kccncna2022.sched.com/event/182EX/stateful-apps-on-kubernetes-bring-them-on-diana-patton-gunna-marripudi-netapp-scott-surovich-hsbc-bank-usa-scott-miller-dreamworks-animation-lisa-marie-namphy-cockroach-labs
youtube_search_url: https://www.youtube.com/results?search_query=Stateful+Apps+On+Kubernetes+-+Bring+Them+On%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Stateful Apps On Kubernetes - Bring Them On! - Diana Patton & Gunna Marripudi, NetApp; Scott Surovich, HSBC Bank, USA; Scott Miller, DreamWorks Animation; Lisa-Marie Namphy, Cockroach Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Diana Patton, Gunna Marripudi, NetApp, Scott Surovich, HSBC Bank, USA, Scott Miller, DreamWorks Animation, Lisa-Marie Namphy, Cockroach Labs
- Schedule: https://kccncna2022.sched.com/event/182EX/stateful-apps-on-kubernetes-bring-them-on-diana-patton-gunna-marripudi-netapp-scott-surovich-hsbc-bank-usa-scott-miller-dreamworks-animation-lisa-marie-namphy-cockroach-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Stateful+Apps+On+Kubernetes+-+Bring+Them+On%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Stateful Apps On Kubernetes - Bring Them On!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182EX/stateful-apps-on-kubernetes-bring-them-on-diana-patton-gunna-marripudi-netapp-scott-surovich-hsbc-bank-usa-scott-miller-dreamworks-animation-lisa-marie-namphy-cockroach-labs
- YouTube search: https://www.youtube.com/results?search_query=Stateful+Apps+On+Kubernetes+-+Bring+Them+On%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x8MJlUNhsO0
- YouTube title: Stateful Apps On Kubernetes - Bring Them On!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/stateful-apps-on-kubernetes-bring-them-on/x8MJlUNhsO0.txt
- Transcript chars: 35725
- Keywords: actually, storage, database, application, databases, running, applications, stateful, talking, containers, understand, heritage, journey, deploy, little, clusters, interesting, environment

### Resumo baseado na transcript

I'm Lisa as was mentioned I'm also a cncf Ambassador which is why I'm wearing this scarf and also shout out to our brother Eeyore um and so happy to be here moderating this amazing session with some of my favorite people talking about one of my favorite topics um so you've all heard the joke I'm sure by now I've said it almost every time I've done this talk that um there really isn't any such thing as a stateless application like maybe the only stateless application that exists if you're running kubernetes in production more hands went up than were before that was interesting okay keep them up if you're running State full applications on kubernetes and production okay okay all right well that's actually more than I would have thought um we

### Excerpt da transcript

I'm Lisa as was mentioned I'm also a cncf Ambassador which is why I'm wearing this scarf and also shout out to our brother Eeyore um and so happy to be here moderating this amazing session with some of my favorite people talking about one of my favorite topics um so you've all heard the joke I'm sure by now I've said it almost every time I've done this talk that um there really isn't any such thing as a stateless application like maybe the only stateless application that exists is Hello World possibly um so everything has some form of state and um so we're going to kind of dive into that a little bit deeper um so if you're wondering why you're here wondering if you can run stateful applications in kubernetes I know you all know you can but we have some experts up here who have taken it to another level so why don't we have everybody introduce themselves starting with gonna thanks for joining I'm uh Guna maripuri senior director of product management for NetApp I actually work with a lot of customers including Scotty and Scott so thanks for I hope to have a good panel hi I'm Scott sorovich I work for HSBC Bank and I'm the global container engineering lead and I also own kubernetes globally for on-prem and hybrid Solutions my name is Scotty Miller I'm a technology fellow at Dreamworks Animation and I oversee strategy and architecture for infrastructure including kubernetes virtualization and Legacy so not legacy Heritage the new term is Heritage on kubernetes Solutions I love it you haven't stopped saying Heritage for weeks I just learned it today everything old is old and classy again very funny okay I also just have to um do one more thing to embarrass I love to embarrass the panelists um but in case you haven't downloaded this bought this or read this Scott has written a book you can't see what I'm showing them you might be able to if you can see my screen yeah I had to um get this book it's available on Amazon and um he's an expert we had to validate we have at least one expert on the panel I'm sorry they're all experts okay but back to us um so we're going to talk about the different phases of the cloud Journey uh a little bit and um the journey to containerization so um Scotty why don't we start with you uh sure so our container Journey started in about 2015 we had a relatively unique opportunity to re-implement the production pipeline for feature film so a pipeline's a collection of digital content creation applications data sets workflows how you han
