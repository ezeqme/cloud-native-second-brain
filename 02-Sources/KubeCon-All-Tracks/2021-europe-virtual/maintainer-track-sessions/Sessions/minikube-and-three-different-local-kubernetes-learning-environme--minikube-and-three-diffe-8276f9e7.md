---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Anders Björklund", "Predrag Rogic"]
sched_url: https://kccnceu2021.sched.com/event/iE7w/minikube-and-three-different-local-kubernetes-learning-environments-anders-bjorklund-predrag-rogic
youtube_search_url: https://www.youtube.com/results?search_query=Minikube+and+Three+Different+Local+Kubernetes+Learning+Environments+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Minikube and Three Different Local Kubernetes Learning Environments - Anders Björklund & Predrag Rogic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Anders Björklund, Predrag Rogic
- Schedule: https://kccnceu2021.sched.com/event/iE7w/minikube-and-three-different-local-kubernetes-learning-environments-anders-bjorklund-predrag-rogic
- Busca YouTube: https://www.youtube.com/results?search_query=Minikube+and+Three+Different+Local+Kubernetes+Learning+Environments+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Minikube and Three Different Local Kubernetes Learning Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7w/minikube-and-three-different-local-kubernetes-learning-environments-anders-bjorklund-predrag-rogic
- YouTube search: https://www.youtube.com/results?search_query=Minikube+and+Three+Different+Local+Kubernetes+Learning+Environments+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nqKYgeUtk8s
- YouTube title: Minikube & Three Different Local Kubernetes Learning Environments - Anders Björklund & Predrag Rogic
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/minikube-and-three-different-local-kubernetes-learning-environments/nqKYgeUtk8s.txt
- Transcript chars: 24261
- Keywords: container, machine, running, docker, virtual, driver, install, support, environment, minicube, runtime, cluster, operating, kernel, virtualization, control, native, command

### Resumo baseado na transcript

hello everyone and thank you for taking part in this mini cube session my name is fredrik rogic and i am one of the contributors to the mini cube project this session has two parts first part is an introduction to the mini-q project where we will cover why was mini-q project created what it is and what it's not where we are now and what are the plans for the future also we'll talk about how you can join the community and start contributing to the project the second

### Excerpt da transcript

hello everyone and thank you for taking part in this mini cube session my name is fredrik rogic and i am one of the contributors to the mini cube project this session has two parts first part is an introduction to the mini-q project where we will cover why was mini-q project created what it is and what it's not where we are now and what are the plans for the future also we'll talk about how you can join the community and start contributing to the project the second part will be deep dive to local kubernetes learning environments and here others will introduce the three different environments that mini cube supports hypervisor container and bare metal there will be details about each pros sequence and some suggestions where would you want to choose one over the other and since this is a recorded session we'll leave some time for answering your questions at the end the session time is limited to about 30 minutes so let's jump straight on and talk a little bit about the background and explain which problems were meant to be solved but by this project so this year is a special anniversary for mini cube that started five years ago offering a solution that would improve the existing single node local cluster experience in kubernetes as you can see here the original proposal was not to deal with multi-node clusters nor to be used for production workloads and as we will see later on this original vision changed a little bit but for the better the primary goal of mini cube is to make it simple and easy for people to run kubernetes locally for learning and day-to-day development including testing and debugging and the main guiding principles are to be inclusive and community driven user friendly to support all kubernetes features to be cross-platform reliable high-performance and developer focused here are some specific design goals derived from those principles simple ux that allows setup and teardown of the cluster with the single command as easy as minicube start and minicube delete unified ux cross operating systems support for local storage networking auto scaling dns load balancing and so on minimal dependencies on third-party software as much as possible and minimal resource overhead and we'll touch on this one in more details here you can also visit the link to original design proposal document if you're interested to learn more we're now going to see how minicube development is reflecting specifically these principles and goals this is an example output of
