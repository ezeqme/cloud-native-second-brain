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
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Cassie Coyle", "Artur Souza", "Diagrid"]
sched_url: https://kccncna2024.sched.com/event/1i7lq/scale-job-triggering-with-a-distributed-scheduler-cassie-coyle-artur-souza-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Scale+Job+Triggering+with+a+Distributed+Scheduler+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scale Job Triggering with a Distributed Scheduler - Cassie Coyle & Artur Souza, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[SDLC]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Cassie Coyle, Artur Souza, Diagrid
- Schedule: https://kccncna2024.sched.com/event/1i7lq/scale-job-triggering-with-a-distributed-scheduler-cassie-coyle-artur-souza-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Scale+Job+Triggering+with+a+Distributed+Scheduler+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scale Job Triggering with a Distributed Scheduler.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lq/scale-job-triggering-with-a-distributed-scheduler-cassie-coyle-artur-souza-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Scale+Job+Triggering+with+a+Distributed+Scheduler+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rMv4wbHhnxc
- YouTube title: Scale Job Triggering with a Distributed Scheduler - Cassie Coyle & Artur Souza, Diagrid
- Match score: 0.828
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scale-job-triggering-with-a-distributed-scheduler/rMv4wbHhnxc.txt
- Transcript chars: 27779
- Keywords: scheduler, reminders, dapper, actors, workflow, trigger, schedulers, course, schedule, reminder, application, single, library, running, placement, partition, actually, triggering

### Resumo baseado na transcript

so welcome to our presentation on how to scale job triggering with a distributed schuer and we're going to present it in the context of the daer project and how that help us solve some scaling problems that we had in the project uh my name is Arthur Susan and I'm Cassie Coyle a software engineer at diagrid where I am an approver for the Dappa runtime project along with the Java yeah and uh hi of a diagrid and maintainer of dapper for The Last 5 Years um and

### Excerpt da transcript

so welcome to our presentation on how to scale job triggering with a distributed schuer and we're going to present it in the context of the daer project and how that help us solve some scaling problems that we had in the project uh my name is Arthur Susan and I'm Cassie Coyle a software engineer at diagrid where I am an approver for the Dappa runtime project along with the Java yeah and uh hi of a diagrid and maintainer of dapper for The Last 5 Years um and so going to reach out to us here's our contact information so here's some agenda of what we're going to be talking about today um I'm going to start by in showing a talk AIT Baer the architecture that we have go deeper into actors actor reminders and daer workflow and that will be a s way for you to understand why we had this needed AER project um and it might also be helpful for the project you have if you're having similar problems okay so Inu to Dapper um is anyone here familiar with the Dapper project okay quite a few is anyone running Dapper in production a few some of half production what is what is half production products not ready yet okay so in development okay I get that so it's St by Booth if you want to talk about that too okay uh so for those who don't know I'm going to give a quick overview so imagine that you have an application with M micro services and you want to do service inv location uh you usually have to configure your application to know the endpoint of each service um or us a service MH in case it's Dapper you make a API call to the Dapper API say calls call service b or call service C or a and Dapper will handle the invocation for you we do mtls we also do retries all that configurable including tracing as well and metrics the same thing happens for Pub sub when you do a publisher message you can publish to Kafka or publish to a service bus um or publish to sqs all that distracted from the application because daa offers the API for you um on top of those Primitives we also offer for actors with virtual actors and also workflow which was built on top of um actors uh so this like a high level overview of what daer can do for you and then you can check our website for more information here's some some of the apis we have jobs zi we're going to talk about today workflow disb law configuration Secrets observability actors uh what is that uh binding Pub sub State Management and service invocation and all that runs on kubernetes so daer runs as a separate process as a side car um you
