---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Adnan Hodzic", "ING"]
sched_url: https://kccnceu2023.sched.com/event/1HyVH/kubernetes-resistance-is-futile-adnan-hodzic-ing
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes%2C+Resistance+Is+Futile+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes, Resistance Is Futile - Adnan Hodzic, ING

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Adnan Hodzic, ING
- Schedule: https://kccnceu2023.sched.com/event/1HyVH/kubernetes-resistance-is-futile-adnan-hodzic-ing
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes%2C+Resistance+Is+Futile+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes, Resistance Is Futile.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVH/kubernetes-resistance-is-futile-adnan-hodzic-ing
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes%2C+Resistance+Is+Futile+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=issubK49f6E
- YouTube title: Kubernetes, Resistance Is Futile - Adnan Hodzic, ING
- Match score: 0.865
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-resistance-is-futile/issubK49f6E.txt
- Transcript chars: 24797
- Keywords: cluster, platform, thought, everything, public, migration, around, working, running, changes, private, workloads, option, giving, saying, biggest, environment, existing

### Resumo baseado na transcript

so uh hi everyone my name is Adnan hodzik or hodrich for all the Balkan people here I've been with ing for more than four years where I work as a lead side of a liability engineer as part of a public Cloud team at uh data at a data analytics platform as part of Amsterdam this talk covers ing machine learning platform uh migration Journey or a battle to kubernetes which took over two years and what uh initially started off with a lot of resistance that lasted throughout

### Excerpt da transcript

so uh hi everyone my name is Adnan hodzik or hodrich for all the Balkan people here I've been with ing for more than four years where I work as a lead side of a liability engineer as part of a public Cloud team at uh data at a data analytics platform as part of Amsterdam this talk covers ing machine learning platform uh migration Journey or a battle to kubernetes which took over two years and what uh initially started off with a lot of resistance that lasted throughout the process ultimately resulted to be the only right choice for us in the end just uh to set up your expectations uh one Focus too much on technical implementation details but we'll instead focus on giving a high level overview to answer some of the questions I had I was looking for in kubecons and to provide some guidance if you're in the same situation in your company and just so there's no confusion while I'm part of the public Cloud team now this talk revolves around my time in the same role at MLP team and since I'll be saying MLP a lot MLP is an uh NLP as an acronym the clicker uh MLP is an acronym stands for machine learning platform uh so please keep this in mind because I'll say it a lot of times so our uh our premise takes place at ing ing is one of the world's biggest banks definitely the biggest banks in Netherlands it has around 60 000 employees 18 000 of them work in uh in Tech uh offices in around 40 countries and uh serving around 38 million customers now this is a case in many environments but especially Banks since we work in a highly regulated environment and are subject to rigorous policies in terms of risk security change management controls it's not as easy to deploy our workloads to production uh what's even more complicated if you're a data scientist who would like to do the same without any underlying SRE or deployment or infrastructure knowledge and that's where MLP steps in as it will allow data Sciences to seamlessly deploy their machine learning model to production while abstracting all of this underlying complexity from them and it will uh in the end it will serve as a as a model hosting platform setup consisted of python ml models being wrapped into python containers which then along with other services are part of the docker compose files and then these Docker compose files are deployed to various and numerous VMS using ansible you could say that things work great but I thought the missing link in and this whole picture was that it was not running on kubernete
