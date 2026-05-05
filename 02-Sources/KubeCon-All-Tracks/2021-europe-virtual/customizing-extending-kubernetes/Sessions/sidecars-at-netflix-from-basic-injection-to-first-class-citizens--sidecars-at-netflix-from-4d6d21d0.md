---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Rodrigo Campos Catelin", "Kinvolk", "Manas Alekar", "Netflix"]
sched_url: https://kccnceu2021.sched.com/event/iE2f/sidecars-at-netflix-from-basic-injection-to-first-class-citizens-rodrigo-campos-catelin-kinvolk-manas-alekar-netflix
youtube_search_url: https://www.youtube.com/results?search_query=Sidecars+at+Netflix%3A+From+Basic+Injection+to+First+Class+Citizens+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sidecars at Netflix: From Basic Injection to First Class Citizens - Rodrigo Campos Catelin, Kinvolk & Manas Alekar, Netflix

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Rodrigo Campos Catelin, Kinvolk, Manas Alekar, Netflix
- Schedule: https://kccnceu2021.sched.com/event/iE2f/sidecars-at-netflix-from-basic-injection-to-first-class-citizens-rodrigo-campos-catelin-kinvolk-manas-alekar-netflix
- Busca YouTube: https://www.youtube.com/results?search_query=Sidecars+at+Netflix%3A+From+Basic+Injection+to+First+Class+Citizens+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sidecars at Netflix: From Basic Injection to First Class Citizens.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2f/sidecars-at-netflix-from-basic-injection-to-first-class-citizens-rodrigo-campos-catelin-kinvolk-manas-alekar-netflix
- YouTube search: https://www.youtube.com/results?search_query=Sidecars+at+Netflix%3A+From+Basic+Injection+to+First+Class+Citizens+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YB5rlo2cq9s
- YouTube title: Sidecars at Netflix: From Basic Injection to First Class Ci... Rodrigo Campos Catelin & Manas Alekar
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sidecars-at-netflix-from-basic-injection-to-first-class-citizens/YB5rlo2cq9s.txt
- Transcript chars: 21981
- Keywords: container, containers, sidecar, running, mesh, problems, application, ordering, netflix, developers, expect, starts, instance, metadata, sidecars, software, executor, change

### Resumo baseado na transcript

hi welcome to the sidecars and netflix presentation uh i'm rodrigo i'm a software engineer at kinfold uh a little bit about me i studied computer science in argentina and i'm a maintainer of middleweight and core coordinates reviewer and as i said i work at kinfolk we are focused on developing open source software you may know some of our projects like flat car container linux there is a container optimized rs or headlamp or coordinated work ui or locomotive a fully self-hosted coordinated distribution today i'll be presenting

### Excerpt da transcript

hi welcome to the sidecars and netflix presentation uh i'm rodrigo i'm a software engineer at kinfold uh a little bit about me i studied computer science in argentina and i'm a maintainer of middleweight and core coordinates reviewer and as i said i work at kinfolk we are focused on developing open source software you may know some of our projects like flat car container linux there is a container optimized rs or headlamp or coordinated work ui or locomotive a fully self-hosted coordinated distribution today i'll be presenting with manus a software engineer at netflix he works on the compute infrastructure team on container execution and we work together on the cycle ordering on the cubit the top is divided in two parts first manus will share how netflix is using size car containers and in the second part i'll talk about the problems we face today with sidecars and the efforts we didn't improve this situation in ground at the saturn hi i'm manus and before we dive into side cars here is some background at netflix our fleet is composed of more vms and titus our container platform is gaining organic adoption we are now working to make titus the primary deployment target to give developers one well supported infrastructure that allows them to iterate fast and is also more scalable and more efficient at the same time the goal is to do this migration fast and automate as much as we can so hundreds of platform engineers are not supporting two deployment targets for a very long time to get a sense of what we are migrating here is what a typical vm runs at netflix we have the application typically running in the jvm and a series of daemons providing service discovery security and observability to name a few things application developers expect these demons to just work and so we run them in an operationally sensitive fashion by which i mean we start and shut them down in a specific order restart them when they fail and they are generally available to the application as an example the metrics forwarder starts up before the agent which boots traps certificates this is important because consider what happens when that agent starts failing in our case it can publish a metric to report these failures and we can use our monitoring and alerting systems to track and remediate these in the same way the service mesh expects tls certificates and the open policy agent to be available before it starts up otherwise every application has to decide if the mesh needs to fail open
