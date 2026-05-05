---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "SRE Reliability"]
speakers: ["Cat Morris", "Syntasso", "Stéphane Di Cesare", "DKB", "Anna Kozachenko", "Amadeus", "Gayathri Thiyagarajan", "AWS"]
sched_url: https://kccnceu2026.sched.com/event/2CW59/scaling-platform-engineering-lessons-from-europes-largest-enterprises-cat-morris-syntasso-stephane-di-cesare-dkb-anna-kozachenko-amadeus-gayathri-thiyagarajan-aws
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Platform+Engineering%3A+Lessons+From+Europe%E2%80%99s+Largest+Enterprises+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Scaling Platform Engineering: Lessons From Europe’s Largest Enterprises - Cat Morris, Syntasso; Stéphane Di Cesare, DKB; Anna Kozachenko, Amadeus; Gayathri Thiyagarajan, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Cat Morris, Syntasso, Stéphane Di Cesare, DKB, Anna Kozachenko, Amadeus, Gayathri Thiyagarajan, AWS
- Schedule: https://kccnceu2026.sched.com/event/2CW59/scaling-platform-engineering-lessons-from-europes-largest-enterprises-cat-morris-syntasso-stephane-di-cesare-dkb-anna-kozachenko-amadeus-gayathri-thiyagarajan-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Platform+Engineering%3A+Lessons+From+Europe%E2%80%99s+Largest+Enterprises+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Scaling Platform Engineering: Lessons From Europe’s Largest Enterprises.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW59/scaling-platform-engineering-lessons-from-europes-largest-enterprises-cat-morris-syntasso-stephane-di-cesare-dkb-anna-kozachenko-amadeus-gayathri-thiyagarajan-aws
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Platform+Engineering%3A+Lessons+From+Europe%E2%80%99s+Largest+Enterprises+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8JyvkE-8__8
- YouTube title: Scaling Platform Engineering: Lessons From Europe’s Larges... Cat M, Stéphane C, Anna K & Gayathri T
- Match score: 0.867
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/scaling-platform-engineering-lessons-from-europes-largest-enterprises/8JyvkE-8__8.txt
- Transcript chars: 26192
- Keywords: platform, actually, scaling, important, engineering, platforms, interesting, challenges, started, amados, technical, always, operations, having, panelists, devops, strong, automation

### Resumo baseado na transcript

Um so first thank you for all joining us because we were a little bit worried half five on day two everyone was going to be too tired. But uh it's lovely to see you all here joining us to talk about scaling platform engineering. So um scaling existing platform capabilities which is mainly around provisioning Kafka and then moving on to actually building 0ero to one uh data quality platform from scratch but for a very large scale operations um and then moved on to AWS uh again very similar domain um and this time managing the Kafka service for AWS which is msk um but to compare the scale where before in Xeda it was managing uh a platform of about 10 clusters suddenly this is about 50,000 clusters and 150,000 brokers so you can imagine there are some very interesting problems that manifest at such scale makes up for very good war stories um and then uh currently I'm working for a different service team and that is AWS resource explorer again this is uh a service >> Yeah, I think that's a very interesting question because I don't think anybody starts out thinking I'm going to be building for 10x scale in the future, right?

### Excerpt da transcript

Hello everyone. How are you all doing? Awesome. >> Thank you. Yes. Um so first thank you for all joining us because we were a little bit worried half five on day two everyone was going to be too tired. But uh it's lovely to see you all here joining us to talk about scaling platform engineering. So this is a topic that's a little bit near and dear to my heart because I read the original Gartner report when it said that 80% of organizations were going to have a platform engineering team by 2026 I think it was which is super exciting but also that means a lot of organizations now have platforms that they need to scale to prove their success. So platform engineering is not new anymore. These big big organizations particularly across Europe, it's very relevant for this conference today have lots of challenges. So I've gathered three excellent people who have worked in some very large organizations and have dealt with platform engineering for a while to hopefully share some insight as to how you scale effectively.

So to begin, let's start with a couple of introductions. Uh so I'm Cat. I'm product manager at Centaso and I'm the least interesting person here today. Uh so I'm going to let the panelists tell you a little bit about themselves, how they get started in engine platform engineering and maybe a little bit about the teams they work with today. So Stefan to my left. >> Hello, my name is Stefan Dare. Um I'm a platform engineer uh specializing on user experience on developer experience at DKB. So DKB is um online bank in Germany. So we have about 5,000 employees. Um and I have a more of an operations background. So I started uh getting very interested in DevOps because I'm more interested in what is the use of operations not only what the technology behind it. Um and in the past uh I worked as um professional services engineer for VMware. So helping companies uh automating their um virtualization infrastructure and I also worked as a consultant at um at Accenture. So helping company uh setting up DevOps technically but also organizationally.

So I've been also in contact with different kinds of platforms in different stages. >> Thank you. Anna, how did you get started? >> Hello. Uh I'm Anna and I'm platform architect at Amados. For those who doesn't know about Amados, Amados is an IT company in a travel industry. So if you have planned this trip for CubeCon, you probably booked an airplane ticket, you have your reservation at the hotel, you checked in your l
