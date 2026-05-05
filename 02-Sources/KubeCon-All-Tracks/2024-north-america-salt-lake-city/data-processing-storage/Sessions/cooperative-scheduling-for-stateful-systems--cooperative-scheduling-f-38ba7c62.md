---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Michael Youssef", "Zhantong Shang", "LinkedIn"]
sched_url: https://kccncna2024.sched.com/event/1i7n9/cooperative-scheduling-for-stateful-systems-michael-youssef-zhantong-shang-linkedin
youtube_search_url: https://www.youtube.com/results?search_query=Cooperative+Scheduling+for+Stateful+Systems+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cooperative Scheduling for Stateful Systems - Michael Youssef & Zhantong Shang, LinkedIn

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: United States / Salt Lake City
- Speakers: Michael Youssef, Zhantong Shang, LinkedIn
- Schedule: https://kccncna2024.sched.com/event/1i7n9/cooperative-scheduling-for-stateful-systems-michael-youssef-zhantong-shang-linkedin
- Busca YouTube: https://www.youtube.com/results?search_query=Cooperative+Scheduling+for+Stateful+Systems+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cooperative Scheduling for Stateful Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7n9/cooperative-scheduling-for-stateful-systems-michael-youssef-zhantong-shang-linkedin
- YouTube search: https://www.youtube.com/results?search_query=Cooperative+Scheduling+for+Stateful+Systems+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jB2MI7ZKw40
- YouTube title: Cooperative Scheduling for Stateful Systems - Michael Youssef & Zhantong Shang, LinkedIn
- Match score: 0.763
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cooperative-scheduling-for-stateful-systems/jB2MI7ZKw40.txt
- Transcript chars: 29449
- Keywords: operator, stateful, linkedin, actually, operation, maintenance, application, cluster, essentially, infrastructure, operations, basically, disruption, running, safety, applications, everyone, temporary

### Resumo baseado na transcript

all right hello everyone thanks for coming to listen to our lovely talk on how we're doing stateful uh LinkedIn on kubernetes so before we get started a little bit about us I'm a Staff engineer at LinkedIn I've been at LinkedIn for about five years now for the first three and a half years I worked on all things Commerce at LinkedIn so if you ever bought something on LinkedIn premium uh I touched that and then for the next for the last one and a half years I've

### Excerpt da transcript

all right hello everyone thanks for coming to listen to our lovely talk on how we're doing stateful uh LinkedIn on kubernetes so before we get started a little bit about us I'm a Staff engineer at LinkedIn I've been at LinkedIn for about five years now for the first three and a half years I worked on all things Commerce at LinkedIn so if you ever bought something on LinkedIn premium uh I touched that and then for the next for the last one and a half years I've been working on all the goodies that you're going to see in this talk um hi everyone uh my name is dantong I am a software engineer from one of uh linkedin's data infrastructure teams uh the team manages linkedin's um document store and we are the pilot application the Pilot State for application on kubernetes at LinkedIn um I'm really excited to be here to share our experience about running State applications on top of kubernetes yeah wrong way so uh what are we going to talk about today just a small overview of sort of of where we started and how we arrived to the solution that we're going to present today uh we're going to talk a bit about cooperation with the application cluster managers uh we'll talk a bit about what our operator actually looks like what it does uh we'll talk about host life cycle maintenance some of the lessons learned acknowledgements and some Q&A at the end oh um all right uh let's start with uh the problem we are trying to solve so uh at LinkedIn we run quite a few staple applications for example we have CFA for stream processing we have our graph database and of course we have the document store which is one of the state applications at LinkedIn so um on the Lexi computer infrastructure uh each of these St applications operates in their own private pool of notes the applications run on Bal machines uh each team have developed like numerous um automations and toolings to manage their workloads uh to handle things like scaling maintenance and so on so uh if you compare the automation tooling developed by each team it's easy to see that uh they have great similarities for example they um use the same set of APs from the computer infrastructure they perform similar tasks so basically like every team is Reinventing uh re inventing will um on the other hand uh despite all the automation tooling developed by by teams we still hit limits uh especially with big operations like Tech refresh this kind of operations uh usually requires collaboration between the hardware team and the ap
