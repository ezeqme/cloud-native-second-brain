---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["John Belamaric", "Google", "Davanum Srinivas", "AWS"]
sched_url: https://kccnceu2024.sched.com/event/1Yhht/kubernetes-sig-architecture-intro-and-updates-john-belamaric-google-davanum-srinivas-aws
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+SIG+Architecture+Intro+and+Updates+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kubernetes SIG Architecture Intro and Updates - John Belamaric, Google & Davanum Srinivas, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: John Belamaric, Google, Davanum Srinivas, AWS
- Schedule: https://kccnceu2024.sched.com/event/1Yhht/kubernetes-sig-architecture-intro-and-updates-john-belamaric-google-davanum-srinivas-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+SIG+Architecture+Intro+and+Updates+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kubernetes SIG Architecture Intro and Updates.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhht/kubernetes-sig-architecture-intro-and-updates-john-belamaric-google-davanum-srinivas-aws
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+SIG+Architecture+Intro+and+Updates+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8YaKHvoVZy4
- YouTube title: Kubernetes SIG Architecture Intro and Updates - John Belamaric & Davanum Srinivas
- Match score: 0.818
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubernetes-sig-architecture-intro-and-updates/8YaKHvoVZy4.txt
- Transcript chars: 26928
- Keywords: architecture, process, security, conformance, kubernets, working, review, feature, around, write, production, exactly, figure, clusters, another, design, policy, within

### Resumo baseado na transcript

uh thanks for coming to this talk this afternoon um I would like to introduce the ourselves this is the Sig architecture kubernetes intro and update talk um to like I did want to ask you all like what do you think this stock is about uh anyone have an idea what this talk is about good not in the traditional sense as such uh we are not going to talk about deep into the internals of kubernetes but we'll talk about like how we take architectural decisions how the

### Excerpt da transcript

uh thanks for coming to this talk this afternoon um I would like to introduce the ourselves this is the Sig architecture kubernetes intro and update talk um to like I did want to ask you all like what do you think this stock is about uh anyone have an idea what this talk is about good not in the traditional sense as such uh we are not going to talk about deep into the internals of kubernetes but we'll talk about like how we take architectural decisions how the company uh Community operates um how we go about uh doing the different things uh you know which might not be very specific to one area uh or one um special interest group in the community and things like that um you know this is an intro and an update so we do uh this kind of talk to Welcome All of You Into the community to take part in the processes that we have uh and help uh you know make kubernetes better for everyone going forward so we'll talk about like what how how do you make enhancements in the community how do you add new features how do you make sure that the old features you know like just installing kuber net is not the end of the story right like you have to have a you know upgrade maintenance everything comes into the picture and then it becomes really hard like just like any other software that that we have so Sig architecture is a place where we talk about these things and uh work on practical uh Solutions uh around how to make sure that uh we don't break people uh and how to make sure that uh people are getting the things that they need from kubernetes uh hope that helps um just warning you ahead of time so uh my nickname is dims uh you can call me dims I'm on GitHub Twitter it's uh same dims everywhere um John I'm I'm John uh and uh dims and I are two-thirds of the uh the Sig architecture uh co-chairs yeah um John is from Google I work for AWS currently um so let's take a quick look at the goals of the cubus project itself right like you've seen this before you've seen how kubernetes is being used by everybody everywhere uh people have called it you know the uh I think Priyanka called it as a Linux moment of kubernetes in one of our Keynotes U we try to be very flexible extensible automated able um we have some new ideas around like um you know how exactly people need to uh do their apis and how uh you know declarative patterns and things like that are new how to use aaml for all the things uh so you've seen all those things and that's why you are here in this conference um and y
