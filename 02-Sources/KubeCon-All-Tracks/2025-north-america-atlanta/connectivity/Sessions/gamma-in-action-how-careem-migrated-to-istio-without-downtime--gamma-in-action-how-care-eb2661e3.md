---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Suren Raju", "Careem", "Sergey Marunich", "Tetrate"]
sched_url: https://kccncna2025.sched.com/event/27FX9/gamma-in-action-how-careem-migrated-to-istio-without-downtime-suren-raju-careem-sergey-marunich-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=GAMMA+in+Action%3A+How+Careem+Migrated+To+Istio+Without+Downtime+CNCF+KubeCon+2025
slides: []
status: parsed
---

# GAMMA in Action: How Careem Migrated To Istio Without Downtime - Suren Raju, Careem & Sergey Marunich, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Suren Raju, Careem, Sergey Marunich, Tetrate
- Schedule: https://kccncna2025.sched.com/event/27FX9/gamma-in-action-how-careem-migrated-to-istio-without-downtime-suren-raju-careem-sergey-marunich-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=GAMMA+in+Action%3A+How+Careem+Migrated+To+Istio+Without+Downtime+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre GAMMA in Action: How Careem Migrated To Istio Without Downtime.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FX9/gamma-in-action-how-careem-migrated-to-istio-without-downtime-suren-raju-careem-sergey-marunich-tetrate
- YouTube search: https://www.youtube.com/results?search_query=GAMMA+in+Action%3A+How+Careem+Migrated+To+Istio+Without+Downtime+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=igJXmbwMYAc
- YouTube title: GAMMA in Action: How Careem Migrated To Istio Without Downtime - Suren Raju & Sergey Marunich
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/gamma-in-action-how-careem-migrated-to-istio-without-downtime/igJXmbwMYAc.txt
- Transcript chars: 25763
- Keywords: migration, traffic, gateway, canary, flagger, process, deployment, cluster, basically, across, needed, without, platform, ingress, mesh, journey, object, migrated

### Resumo baseado na transcript

There is a story in front of us which is migration story or maturity story uh to be presented. So it will be technical story but again not to bore you prepare your questions and once again it's a half an hour a journey of people that run people mash you know irony here we'll talk about mash but technically this gentleman named Suren I'm a staff site reliability engineer part of traffic engineering team at Kharim. But our current traffic platform was uh limiting us to deliver them and our team had to learn and maintain these different stacks. So we had to redesign our traffic platform and what we needed came down to four key things. First we needed a single cohesive architecture something that could hand that could handle ingress egress and service to service traffic seamlessly.

### Excerpt da transcript

Folks, let's get started. Uh, I appreciate you coming. It's 4 p.m. I know it's been long day, a first day, right? So, uh, we'll try not to bore you, but that'll excite you. There is a story in front of us which is migration story or maturity story uh to be presented. So it will be technical story but again not to bore you prepare your questions and once again it's a half an hour a journey of people that run people mash you know irony here we'll talk about mash but technically this gentleman named Suren he's part of the company that actually runs people mash and uh it's not that loud sort of a thing but I'll let you start and talk about us through the journey and then prep your questions and we're here to today until you stay to answer your questions. All right, so Surren over to you. >> All right, let's get started. Let's forget the tech for a moment and think about people. Um, it's a Thursday evening, 6:00 p.m. Busy time across Middle East. In Riyad, a mother opens an app. She is trying to get a ride to get her child to hospital.

It's an emergency. In Aman, a restaurant owner opens an app. She got caught, all the ingredients stacked, stops ready. She's counting on those evening delivery orders to make her week. In Dubai, a driver starts his shift. He opens the same app and waiting for his first booking. He's working away from home trying to earn enough to support his family. All of this moments, all of this human moments depends on a single digital platform. For most of the apps, if they go down for 10 minutes, sure maybe it's bit annoying. But if this one goes down, it affects someone's ability to earn for the day or it could delay someone getting to hospital on time or it could mean something real. We are talking about Karim the region's everything app and we are here to talk about how Karim migrated to without downtime using gamma as a foundation and my name is Surin Raju. I'm a staff site reliability engineer part of traffic engineering team at Kharim. >> Sergey is here from that trade doing some from day to day. [snorts] >> Let me tell you a bit more about Kharim and what drives um everything we everything we do.

Have you ever been to Dubai? Anyone? Okay. If you have been to Dubai before, I'm pretty sure you have used Kareem app or at least seen Kareem fleets around. for everybody else. Karim is everything app from the Middle East, helping millions of people get around, order food, groceries, manage payments, uh, and and all in one one app. Karim's
