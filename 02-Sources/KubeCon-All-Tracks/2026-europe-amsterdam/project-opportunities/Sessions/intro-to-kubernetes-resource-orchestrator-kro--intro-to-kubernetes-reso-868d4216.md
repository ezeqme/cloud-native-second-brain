---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: ["Abdel Sghiouar"]
sched_url: https://kccnceu2026.sched.com/event/2Jo8K/intro-to-kubernetes-resource-orchestrator-kro-abdel-sghiouar
youtube_search_url: https://www.youtube.com/results?search_query=Intro+to+Kubernetes+Resource+Orchestrator+%28KRO%29+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Intro to Kubernetes Resource Orchestrator (KRO) - Abdel Sghiouar

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Abdel Sghiouar
- Schedule: https://kccnceu2026.sched.com/event/2Jo8K/intro-to-kubernetes-resource-orchestrator-kro-abdel-sghiouar
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+to+Kubernetes+Resource+Orchestrator+%28KRO%29+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Intro to Kubernetes Resource Orchestrator (KRO).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2Jo8K/intro-to-kubernetes-resource-orchestrator-kro-abdel-sghiouar
- YouTube search: https://www.youtube.com/results?search_query=Intro+to+Kubernetes+Resource+Orchestrator+%28KRO%29+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=A0qZDj-90G4
- YouTube title: Introducing Kubernetes Resource Orchestrator (KRO) - Abdel Sghiouar
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/intro-to-kubernetes-resource-orchestrator-kro/A0qZDj-90G4.txt
- Transcript chars: 32940
- Keywords: resource, create, resources, created, definition, object, called, controllers, define, ingress, particular, controller, application, inside, actually, basically, essentially, objects

### Resumo baseado na transcript

Each time I go to a conference and I I am about to do a talk about Crow, I never really understand why there is so much interest in this project because objectively Crow is a very very tiny part of Kubernetes as a project. But last time I did this talk was early this month in uh in India, CubeCon India and I had a room of 500 people. The pod runs on a node but you don't really tell Kubernetes what to do or how to do what it does. You express your intent in the form of YAML and then Kubernetes make that intent happen. One of the best ways that have been uh described to me in the podcast to think about Kubernetes is that Kubernetes is a promise machine. A different way to think about it is that Kubernetes is an eventually consistent system.

### Excerpt da transcript

[Music] from Container Days Hamburg. This video is proudly presented by DAX IT. Each time I go to a conference and I I am about to do a talk about Crow, I never really understand why there is so much interest in this project because objectively Crow is a very very tiny part of Kubernetes as a project. But last time I did this talk was early this month in uh in India, CubeCon India and I had a room of 500 people. There was 750 people in the room and there was people sitting right in front of me and I was like why are you all care about it's not even production ready and people care about it but anyway we're here so let's talk about this what is crow hi everyone my name is Abdell I'm a developer advocate at Google I'm based in Sweden Stockholm originally from Morocco if you care about knowing why my name is Abdell and uh I do this thing called the Kubernetes podcast by Google I don't know if there are any listeners oh a few of you okay I will give the rest of you five minutes for sup come. Um um so I I work on Kubernetes mostly on containers and my background is in infrastructure.

I came from data center world. I worked in data centers for a very long time. So I do fundamentally understand what Kubernetes is and and and what problems it solve. And I am going to preface my session by saying that sorry for everyone in the room who is a big fan. I am not a fan of Terraform and I am not a fan of Palumi. I do not like infrastructure as code at all and I am a huge fan of YAML. I know that there's a lot of debates about this. I know that a lot of people hate YAML. I don't. So for me, Crow represents the solution to the Terraform problem. So I'm going to walk all of us through some fundamentals so we can get to understand what Crow is and what it does. Starting with the fundamental of how Kubernetes work. I think this is should not be new to most of you. If this is the first time you see a diagram like this, you are in the wrong conference. Um, so Kubernetes is what? It's basically a system composed of two components. A control plane and a worker plane. The control plane is the brain of the system.

That's where you tell Kubernetes what to do. The data plane is where things happen. You as a developer, user, platform engineer, DevOps engineer, whatever you want to call yourself. You're running containers. Containers runs inside a thing called a pod. The pod runs on a node but you don't really tell Kubernetes what to do or how to do what it does. You tell Kubernetes
