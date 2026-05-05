---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Unclassified"
themes: ["Storage Data", "GitOps Delivery"]
speakers: ["Rick Spencer", "Wojciech Kocjan", "InfluxData"]
sched_url: https://kccnceu2022.sched.com/event/ytlM/effective-disaster-recovery-the-day-we-deleted-production-rick-spencer-wojciech-kocjan-influxdata
youtube_search_url: https://www.youtube.com/results?search_query=Effective+Disaster+Recovery%3A+The+Day+We+Deleted+Production+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Effective Disaster Recovery: The Day We Deleted Production - Rick Spencer & Wojciech Kocjan, InfluxData

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[GitOps Delivery]]
- País/cidade: Spain / Valencia
- Speakers: Rick Spencer, Wojciech Kocjan, InfluxData
- Schedule: https://kccnceu2022.sched.com/event/ytlM/effective-disaster-recovery-the-day-we-deleted-production-rick-spencer-wojciech-kocjan-influxdata
- Busca YouTube: https://www.youtube.com/results?search_query=Effective+Disaster+Recovery%3A+The+Day+We+Deleted+Production+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Effective Disaster Recovery: The Day We Deleted Production.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlM/effective-disaster-recovery-the-day-we-deleted-production-rick-spencer-wojciech-kocjan-influxdata
- YouTube search: https://www.youtube.com/results?search_query=Effective+Disaster+Recovery%3A+The+Day+We+Deleted+Production+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xDGjmav8UBg
- YouTube title: Effective Disaster Recovery: The Day We Deleted Production - Rick Spencer & Wojciech Kocjan
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/effective-disaster-recovery-the-day-we-deleted-production/xDGjmav8UBg.txt
- Transcript chars: 34121
- Keywords: argo, stateful, started, application, storage, objects, production, actually, volumes, incident, valero, customers, wanted, object, basically, questions, influx, single

### Resumo baseado na transcript

okay hi everyone i hope you can hear me all the way in the back so my name is henrik i'm the moderator for these sessions we'll get started here in just a second just want to remind you uh once the session concludes we'll have a microphone here in the middle for questions so please line up and ask any questions you might have i'll try and get a couple of questions from the the virtual meeting room as well make sure those guys are included and after the

### Excerpt da transcript

okay hi everyone i hope you can hear me all the way in the back so my name is henrik i'm the moderator for these sessions we'll get started here in just a second just want to remind you uh once the session concludes we'll have a microphone here in the middle for questions so please line up and ask any questions you might have i'll try and get a couple of questions from the the virtual meeting room as well make sure those guys are included and after the session please don't forget to to rate the session and if you have additional questions after the session concludes and we're out of time please continue those discussions out in the hall so we can clear the room and prepare for the next session and with that i'm going to leave it over to you thanks good morning everybody can you give me a thumbs up if i'm perfectly audible great okay so this is the title of our talk it was originally the subtitle was the title of our talk but our pr person about had an aneurysm when they saw that i was submitting that talk but i explained to her first of all everybody at least all of our customers know we had an outage and second of all everybody has outages it's not news when a sas provider has an outage so we wanted to come here and share our experience with the community to maybe help you avoid an outage or deal with it when it comes up so my name is rick i'm currently the vp of product at influx data at the time of this incident i was the vp of engineering for the platform team so i was there during the the day that we deleted and restored one of our production environments and hi my name is wojciech i'm a platform engineer at the deployments team at influx data and i've been involved in many parts of the incidents and follow-ups including post-mortem and fixes around what broke and how we make sure that it doesn't happen again okay so who are we why are we using kubernetes why might our experience be relevant so at influx data we view ourselves as a development platform for writing time series applications we don't really view ourselves as a kubernetes tools vendor that said a lot of our customers use us to monitor their kubernetes clusters and then we have different companies that have actually built sas solutions for monitoring kubernetes on top of us so while we are an application development platform for time series at the heart is a database called influx db it's an open source database that's purpose built for time series but currently our flagship product is cal
