---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Karen Jex", "Crunchy Data"]
sched_url: https://kccnceu2023.sched.com/event/1HyYB/mission-critical-postgresql-databases-on-kubernetes-karen-jex-crunchy-data
youtube_search_url: https://www.youtube.com/results?search_query=Mission-Critical+PostgreSQL+Databases+on+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Mission-Critical PostgreSQL Databases on Kubernetes - Karen Jex, Crunchy Data

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Karen Jex, Crunchy Data
- Schedule: https://kccnceu2023.sched.com/event/1HyYB/mission-critical-postgresql-databases-on-kubernetes-karen-jex-crunchy-data
- Busca YouTube: https://www.youtube.com/results?search_query=Mission-Critical+PostgreSQL+Databases+on+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Mission-Critical PostgreSQL Databases on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYB/mission-critical-postgresql-databases-on-kubernetes-karen-jex-crunchy-data
- YouTube search: https://www.youtube.com/results?search_query=Mission-Critical+PostgreSQL+Databases+on+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_NBQ9JmOMko
- YouTube title: Mission-Critical PostgreSQL Databases on Kubernetes - Karen Jex, Crunchy Data
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/mission-critical-postgresql-databases-on-kubernetes/_NBQ9JmOMko.txt
- Transcript chars: 21093
- Keywords: database, postgres, databases, containers, cluster, deploy, container, running, obviously, replica, operator, backup, deploying, primary, knowledge, already, monitoring, architecture

### Resumo baseado na transcript

so I'm Karen Jacks I'm a Senior Solutions architect at crunchy data and I'm here to talk to you about running Mission critical postgres databases on kubernetes it is such an honor to be here to talk to you I'm really amazed that there's such a a crowd interested in database on kubernetes you know just a few years ago that would have been unheard of so it's fantastic so I've described this talk as suitable for get for beginners so I will go over some basic concepts but um

### Excerpt da transcript

so I'm Karen Jacks I'm a Senior Solutions architect at crunchy data and I'm here to talk to you about running Mission critical postgres databases on kubernetes it is such an honor to be here to talk to you I'm really amazed that there's such a a crowd interested in database on kubernetes you know just a few years ago that would have been unheard of so it's fantastic so I've described this talk as suitable for get for beginners so I will go over some basic concepts but um I'm assuming that most people in this room actually know more about kubernetes than I do so I'm not going to try and teach you kubernetes I'm just going to go quickly over and recap some of the basic concepts as they're relevant to the topic at hand we're good no it doesn't want to work hard over the old-fashioned I did start my time I think it doesn't want to do that come on you can do it right we'll try again so um this is the shape of my career so far very database shaped so that's why I'm saying that you probably know a lot more about kubernetes than I do I'm talking about the one subject that I know about and that's databases I don't really like my current title Solutions architect because I don't think it really says much I quite liked the fact that I was a DBA I knew where I was I knew knew where I stood um so that's uh that's me just to kind of give a bit of background so as a Solutions architect I have kind of come a little bit out of my database bubble and I've come to recognize that there is an ecosystem that goes around the database but I'm still I I help my customers to implement database Solutions I'm still very much focused on the database at the heart of the system and if anyone ever wants to talk to me about it I'm also doing a part-time PhD in computer science I give up on that so we'll briefly look at the evolution of database architecture how things were deployed how databases are currently deployed how things are changing how things might change remind ourselves what containers are why they might be useful where container orchestration comes in just so that we can then understand why where and how we might want to deploy databases in general and postgres in particular on kubernetes and then finally the best way to explain these things is via edema so I'm not going to go back too far in the history of databases just about 25 years to the start of my career as a DBA so I think that qualifies me as a vintage DBA now so that time most databases were deployed on bare metal
