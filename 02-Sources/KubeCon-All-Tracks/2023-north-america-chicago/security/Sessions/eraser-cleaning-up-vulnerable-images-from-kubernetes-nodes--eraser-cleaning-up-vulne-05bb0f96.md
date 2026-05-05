---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Peter Engelbert", "Ashna Mehrotra", "Microsoft"]
sched_url: https://kccncna2023.sched.com/event/1R2q9/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-peter-engelbert-ashna-mehrotra-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Eraser%3A+Cleaning+up+Vulnerable+Images+from+Kubernetes+Nodes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Eraser: Cleaning up Vulnerable Images from Kubernetes Nodes - Peter Engelbert & Ashna Mehrotra, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Peter Engelbert, Ashna Mehrotra, Microsoft
- Schedule: https://kccncna2023.sched.com/event/1R2q9/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-peter-engelbert-ashna-mehrotra-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Eraser%3A+Cleaning+up+Vulnerable+Images+from+Kubernetes+Nodes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Eraser: Cleaning up Vulnerable Images from Kubernetes Nodes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2q9/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes-peter-engelbert-ashna-mehrotra-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Eraser%3A+Cleaning+up+Vulnerable+Images+from+Kubernetes+Nodes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LjDzn7qI5SE
- YouTube title: Eraser: Cleaning up Vulnerable Images from Kubernetes Nodes - Peter Engelbert & Ashna Mehrotra
- Match score: 0.869
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/eraser-cleaning-up-vulnerable-images-from-kubernetes-nodes/LjDzn7qI5SE.txt
- Transcript chars: 16215
- Keywords: images, eraser, cluster, container, scanner, remove, vulnerable, running, collector, little, provide, containers, questions, controller, default, runtime, reason, schedule

### Resumo baseado na transcript

okay hi everyone thank you for coming my name is Ashna and I'm a software engineer at Microsoft uh hi I'm Peter I'm also a software engineer at Microsoft um thank you all for coming today uh we're really excited to talk about eraser Asha and I and whole heap of others have been working on it for some time now and we're excited to share it with you yeah so eraser briefly is a tool to clean up vulnerable images from kubernetes notes and before we get get into

### Excerpt da transcript

okay hi everyone thank you for coming my name is Ashna and I'm a software engineer at Microsoft uh hi I'm Peter I'm also a software engineer at Microsoft um thank you all for coming today uh we're really excited to talk about eraser Asha and I and whole heap of others have been working on it for some time now and we're excited to share it with you yeah so eraser briefly is a tool to clean up vulnerable images from kubernetes notes and before we get get into the technical details of eraser we want to give a little background on why we created it so the first reason is to eliminate the risk of spinning up vulnerable images so as you can see software supplychain attacks jumped over 300% in 2021 and by leaving lingering images on nodes we're giving attackers the opportunity to spin up vulnerable containers the second reason is to eliminate alerts for non-compliant images a lot of teams and organizations are overwhelmed with the amount of alerts they receive and there's no easy and effortless solution to this problem so a common approach developers will take that is they'll create a crown drob and they'll use container D to Target the non-running images in the cluster but this is a manual approach so it takes up a lot of time and it can be more error prone and a common followup is usually what about the current kubernetes garbage collection unfortunately it isn't as efficient since it deletes by a percentage of load so once the dis usage reaches 85% it'll start the cleanup of the unused images until it reaches 80% and while you can customize this value you don't have any control over when it happens or what images it's targeting and finally these Solutions don't have any customization features so as you can see eraser uses a config map and you can plug in different components like the scanner or the repeat period um you can also have control over the cleanup and more so as a solution we created eraser eraser is a cncf Sandbox project and what distinguishes eraser is the control it provides the developer so you decide what gets removed and when now I'll pass it on to Peter to go over the architecture yeah thanks asna um as the slide says this is architecture um and we have this architecture diagram it's a little bit dense um with a lot of arrows and words um so we are going to break it down a little bit and talk about it piece by piece um before I get uh into the questions that erase our answers and the actions that it takes um just kind of wanted to talk a litt
