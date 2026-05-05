---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Tutorials"
themes: ["Storage Data"]
speakers: ["Le Tran", "Michael Cade", "Kasten by Veeam"]
sched_url: https://kccnceu2023.sched.com/event/1Hyah/tutorial-what-went-wrong-with-my-persistent-data-le-tran-michael-cade-kasten-by-veeam
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+What+Went+Wrong+with+My+Persistent+Data%3F+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Tutorial: What Went Wrong with My Persistent Data? - Le Tran & Michael Cade, Kasten by Veeam

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Tutorials]]
- Temas: [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Le Tran, Michael Cade, Kasten by Veeam
- Schedule: https://kccnceu2023.sched.com/event/1Hyah/tutorial-what-went-wrong-with-my-persistent-data-le-tran-michael-cade-kasten-by-veeam
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+What+Went+Wrong+with+My+Persistent+Data%3F+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Tutorial: What Went Wrong with My Persistent Data?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyah/tutorial-what-went-wrong-with-my-persistent-data-le-tran-michael-cade-kasten-by-veeam
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+What+Went+Wrong+with+My+Persistent+Data%3F+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nV8s7FN3s0o
- YouTube title: Tutorial: What Went Wrong with My Persistent Data? - Le Tran & Michael Cade, Kasten by Veeam
- Match score: 0.802
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/tutorial-what-went-wrong-with-my-persistent-data/nV8s7FN3s0o.txt
- Transcript chars: 51233
- Keywords: storage, volume, persistent, within, database, create, around, cluster, running, access, volumes, application, created, obviously, everyone, actually, available, delete

### Resumo baseado na transcript

honestly thank you for for joining us so the whole premise of this session is going to be a workshop it's going to be Hands-On we've got some Labs out there in the cloud that will give us the ability to walk through some of the storage fundamentals and then some storage troubleshooting obviously the name of the the session is what went wrong with my persistent data so first of all introductions are Michael Cade I'm a technologist at veeam software or more focused on the cloud native world

### Excerpt da transcript

honestly thank you for for joining us so the whole premise of this session is going to be a workshop it's going to be Hands-On we've got some Labs out there in the cloud that will give us the ability to walk through some of the storage fundamentals and then some storage troubleshooting obviously the name of the the session is what went wrong with my persistent data so first of all introductions are Michael Cade I'm a technologist at veeam software or more focused on the cloud native world um been at veeam looking after data protection storage for the last eight years and before that I was an infrastructure admin focusing on things like NetApp storage virtualization so I'm hoping I can bring some of that storage operations into into the session and I'm joined with Lee my name is Lee I'm part of the engineering unready and cognitive in general I worked with Bosch before in the automotive sector and I have just joined Captain one and a half years ago so on the same same beginner in a boat with a lot of folks here I think and I think that that's a trend between everyone that we're speaking to over this week is we have some we have some developers we have some devops focused engineers and we have some operations here whereas obviously going back kubernetes or cubecon on cloud nativecon it was probably more focused around developers to begin with and now we're seeing that trend of people having to look after storage provision storage so that's why we wanted to to start that um bring that Workshop to everyone and get get people Hands-On and start looking it from a 101 perspective so I mean if you're if you're a storage admin in a kubernetes world and you're running in production um it's probably going to be stuff that you already know but we want to get people Hands-On and understanding what volumes are and everything around the the kubernetes storage space the other call out that I want to make is uh Matt beta he's the labs that we've got Bill he's he's uh worked tirelessly on on creating those so he's a huge huge asset to what we're delivering today as well okay so I put this tweet out a couple of a couple of weeks ago kubernetes storage is easy right how many people think kubernetes storage is easy cool there's probably more sessions that you need to be in but I think when it comes to kubernetes storage you can see just surrounding this like the word cloud there's lots of different factors and the storage that maybe started with kubernetes and that Evolution t
