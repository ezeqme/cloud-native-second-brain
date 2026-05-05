---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Simon Emms", "Christian Weichel", "Gitpod"]
sched_url: https://kccncna2022.sched.com/event/182DK/kubernet-bees-how-bees-solve-problems-of-distributed-systems-simon-emms-christian-weichel-gitpod
youtube_search_url: https://www.youtube.com/results?search_query=Kubernet-Bees%3A+How+Bees+Solve+Problems+Of+Distributed+Systems+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernet-Bees: How Bees Solve Problems Of Distributed Systems - Simon Emms & Christian Weichel, Gitpod

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: United States / Detroit
- Speakers: Simon Emms, Christian Weichel, Gitpod
- Schedule: https://kccncna2022.sched.com/event/182DK/kubernet-bees-how-bees-solve-problems-of-distributed-systems-simon-emms-christian-weichel-gitpod
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernet-Bees%3A+How+Bees+Solve+Problems+Of+Distributed+Systems+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernet-Bees: How Bees Solve Problems Of Distributed Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182DK/kubernet-bees-how-bees-solve-problems-of-distributed-systems-simon-emms-christian-weichel-gitpod
- YouTube search: https://www.youtube.com/results?search_query=Kubernet-Bees%3A+How+Bees+Solve+Problems+Of+Distributed+Systems+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JymVi3aJp1c
- YouTube title: Kubernet-Bees: How Bees Solve Problems Of Distributed Systems - Simon Emms & Christian Weichel
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernet-bees-how-bees-solve-problems-of-distributed-systems/JymVi3aJp1c.txt
- Transcript chars: 27860
- Keywords: drones, honeycomb, literally, worker, within, control, specifically, workloads, mechanism, temperature, distributed, analogy, produce, thousand, happens, signal, basically, outside

### Resumo baseado na transcript

thank you all for making it to this to this talk so this talk is kubernetes what bees and kubernetes have in common and how bees have solved many other problems that kubernetes solves and that we have in distributed systems except 100 million years ago so this talk is was supposed to be together with Simon EMS a uh calling a friend of mine who unfortunately was not able to uh to make it so you'll have to make do with me my name is Chris um working at

### Excerpt da transcript

thank you all for making it to this to this talk so this talk is kubernetes what bees and kubernetes have in common and how bees have solved many other problems that kubernetes solves and that we have in distributed systems except 100 million years ago so this talk is was supposed to be together with Simon EMS a uh calling a friend of mine who unfortunately was not able to uh to make it so you'll have to make do with me my name is Chris um working at Gip pod um so a few disclaimers to begin with first much like there's more than one way to build a distributed system and much like there is more than one way to run kubernetes there is more than one way to do beekeeping and the views presented in here are a very eurocentric view of this practice there is a strong cultural element to beekeeping and we do not represent the entirety of all practices that exist we'll also very specifically talk about the kind of bees that we'll find in these areas so specifically the north of Germany and the middle of the UK the purpose of this talk is to leave you with an increased appreciation for bees their complexity and the analogy of problems that they face and that we face and with that let's get right into it the things that we're going to talk about is predominantly bees specifically which is a type of Honey Bee a cultivated type of Honey Bee so we're not talking about bumblebees or anything of that sort peace in our analogy here are the workloads it is the workloads and the people who work with things so there are three main types of bees one is the worker B and we're going to talk about that first then there are drones and there's what's known as the queen the Drone the work could be uh a strange combination of what in kubernetes you would consider a pod and people who operate those pods and they go through a series of steps along their career so they start out as an intern and they get to clean up the things that others didn't want to clean up that's the first three days in the life of a bee then they move on into a sort of devops and delivery role where they help bring new bees I.E workloads into life so they're literally nannies that feed other bees and help them get out of get out of their comb then they become Builders which in our world would be the equivalent of an SRE they quite literally built honeycomb they quite literally produce wax and they stand the infrastructure that the rest of the hive runs on after that they move to The Blue Team where they prevent B
