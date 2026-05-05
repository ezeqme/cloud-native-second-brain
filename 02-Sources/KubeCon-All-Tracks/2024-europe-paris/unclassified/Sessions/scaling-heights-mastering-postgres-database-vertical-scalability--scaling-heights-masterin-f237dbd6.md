---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Gabriele Bartolini", "EDB", "Gari Singh", "Google"]
sched_url: https://kccnceu2024.sched.com/event/1YeM4/scaling-heights-mastering-postgres-database-vertical-scalability-with-kubernetes-storage-magic-gabriele-bartolini-edb-gari-singh-google
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Heights%3A+Mastering+Postgres+Database+Vertical+Scalability+with+Kubernetes+Storage+Magic+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scaling Heights: Mastering Postgres Database Vertical Scalability with Kubernetes Storage Magic - Gabriele Bartolini, EDB & Gari Singh, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Gabriele Bartolini, EDB, Gari Singh, Google
- Schedule: https://kccnceu2024.sched.com/event/1YeM4/scaling-heights-mastering-postgres-database-vertical-scalability-with-kubernetes-storage-magic-gabriele-bartolini-edb-gari-singh-google
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Heights%3A+Mastering+Postgres+Database+Vertical+Scalability+with+Kubernetes+Storage+Magic+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scaling Heights: Mastering Postgres Database Vertical Scalability with Kubernetes Storage Magic.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeM4/scaling-heights-mastering-postgres-database-vertical-scalability-with-kubernetes-storage-magic-gabriele-bartolini-edb-gari-singh-google
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Heights%3A+Mastering+Postgres+Database+Vertical+Scalability+with+Kubernetes+Storage+Magic+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LArl0VWxr3Y
- YouTube title: Scaling Heights: Mastering Postgres Database Vertical Scalability... Gabriele Bartolini & Gari Singh
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scaling-heights-mastering-postgres-database-vertical-scalability-with/LArl0VWxr3Y.txt
- Transcript chars: 30347
- Keywords: storage, database, actually, basically, volume, volumes, pretty, performance, spaces, obviously, simple, create, operator, native, scalability, running, results, cluster

### Resumo baseado na transcript

hey thanks everybody for uh joining us at uh 5:25 on uh on uh Thursday I guess it's good to see you're still awake um we've got a pretty exciting session for you today you can read the title here um we'll introduce ourselves in a second but we just wanted to start out with a few questions hopefully we can click it to it that way maybe we have there I have a I have my new manual clicker um how many people here hopefully you're here for this

### Excerpt da transcript

hey thanks everybody for uh joining us at uh 5:25 on uh on uh Thursday I guess it's good to see you're still awake um we've got a pretty exciting session for you today you can read the title here um we'll introduce ourselves in a second but we just wanted to start out with a few questions hopefully we can click it to it that way maybe we have there I have a I have my new manual clicker um how many people here hopefully you're here for this are running databases on kubernetes today awesome and then on the next one of course if you'll be interested how many of you are actually running postgress on kubernetes today I guess that's why you're here because that's what this talk is about um all right so what are we going to sort of cover today uh there's a couple of interesting ways of deploying postgress um so we're want to talk about how do we actually scale postgress and some of the cool things we do kubernetes so how can I deal with like a single primary deployment how do I scale that right many people may think just add more replicas um so that's going to be the key thing and then the second part we're going to talk about is just in general how do we scale these sort of databases now who are we uh my name's uh Gary Singh I uh I don't describe myself very much because I'm very secretive so I'm just a product manager at Google and I'm going to pass it over to Gabriella who is much cooler than me thank you Gary let's see if this works I don't see yeah it doesn't work so need to stay here yeah it's okay I'll stay here that's okay so I'm Gabriel bini I'm vice president of cloud and kubernetes ATB and uh I I don't know I mean this is kind of a dream for me you know I've been using pgus for many many years uh since uh early 2000 I'm a pus contributor I'm also data on kubernetes Ambassador and devops is actually what led me to kubernetes and my first Cube con was in 2019 and I was with Marco was here with me one of the maintainers and we started to think about these operator for Posas using local storage you know like we had it been done for many years outside kubernetes and people thought we were crazy so I'm really happy to be here today you know after this journey that's when Cloud native PG basically was born there was August 20 2019 so and I'm a proud co-founder and maintainer of cloud npg and previously I don't know if you're familiar with uh pogus how many of you need know Barman okay I'm the one that came with the came up with the name and you know and uh ag
