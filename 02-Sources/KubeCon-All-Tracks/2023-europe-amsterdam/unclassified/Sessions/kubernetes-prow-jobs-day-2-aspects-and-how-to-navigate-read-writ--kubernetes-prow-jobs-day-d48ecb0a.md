---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["Kubernetes Core"]
speakers: ["Priyanka Saggu", "SUSE", "Mario Jason Braganza", "Independent"]
sched_url: https://kccnceu2023.sched.com/event/1HyYE/kubernetes-prow-jobs-day-2-aspects-and-how-to-navigate-read-write-them-priyanka-saggu-suse-mario-jason-braganza-independent
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+Prow+Jobs+-+Day+2+Aspects+and+How+to+Navigate%2C+Read+%26+Write+Them+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes Prow Jobs - Day 2 Aspects and How to Navigate, Read & Write Them - Priyanka Saggu, SUSE & Mario Jason Braganza, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Priyanka Saggu, SUSE, Mario Jason Braganza, Independent
- Schedule: https://kccnceu2023.sched.com/event/1HyYE/kubernetes-prow-jobs-day-2-aspects-and-how-to-navigate-read-write-them-priyanka-saggu-suse-mario-jason-braganza-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+Prow+Jobs+-+Day+2+Aspects+and+How+to+Navigate%2C+Read+%26+Write+Them+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes Prow Jobs - Day 2 Aspects and How to Navigate, Read & Write Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyYE/kubernetes-prow-jobs-day-2-aspects-and-how-to-navigate-read-write-them-priyanka-saggu-suse-mario-jason-braganza-independent
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+Prow+Jobs+-+Day+2+Aspects+and+How+to+Navigate%2C+Read+%26+Write+Them+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gKKfXTZd7VU
- YouTube title: Kubernetes Prow Jobs - Day 2 Aspects and How to Navigate, Read &...- Priyanka Saggu & Mario Braganza
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-prow-jobs-day-2-aspects-and-how-to-navigate-read-write-them/gKKfXTZd7VU.txt
- Transcript chars: 40346
- Keywords: cluster, release, called, container, running, version, folder, inside, create, changes, available, itself, looking, script, github, giving, whatever, logs

### Resumo baseado na transcript

specifically about the day two aspect aspects and how to navigate read and write them and before we do that a quick introduction about us um my name is Priyanka sagu I work at Souza's kubernetes integration engineer and I've been part of the kubernetes project for a while in Sig release and Sig contracts hello I'm Jason I'm a next Consulting ID manager trying to Pivot into the world of devops I worked on the kubernetes once I assisted with the kubernetes 1.25 release part of signalese and I'm Pro uh okay whenever you are creating a fork for this job every release we have multiple releases that we are maintaining um in kubernetes projects so create a fork every release and keep replacing those values those flag values every time and those flag

### Excerpt da transcript

specifically about the day two aspect aspects and how to navigate read and write them and before we do that a quick introduction about us um my name is Priyanka sagu I work at Souza's kubernetes integration engineer and I've been part of the kubernetes project for a while in Sig release and Sig contracts hello I'm Jason I'm a next Consulting ID manager trying to Pivot into the world of devops I worked on the kubernetes once I assisted with the kubernetes 1.25 release part of signalese and I'm excited to be here so with that aside um just want to give a quick intro on what this talk is about we have about agenda for today um so we have divided our talk into three parts we'll be discussing uh what brow jobs are what are the different types and we'll be going into our anatomy of brow jobs we'll also be looking at how what are the various user interfaces we have to read and go through brow jobs and where the config actually sits and will end with looking at few examples of actually running kubernetes brow jobs a few examples from there and also we'll see how to replicate them locally um yeah with that let's get started so what is brow um prao is a kubernetes CI CD system built by the communities project itself and built for the kubernetes project so most of the Automation and Grant work that kubernetes project does that's done through pra and for the sake of this talk we won't be going into more more in the side of brow itself how to deploy proud that's not the um intention of this talk it's more day two we assume prow is already working there and how to consume what's already working there um and but there are already a lot of great talks out there from the community on itself so we although we'll be looking at a bit of workflow how brow comes in the picture for kubernetes um contributors for people like us who interact with the kubernetes project from GitHub so on the left side we have GitHub in terms of PR or any interface that we see are repos and on the right hand side we have the brow infrastructure now how to understand prior infrastructure we can read it as traditional kubernetes architecture we have masternodes and we have worker nodes similarly in prow we have something called service cluster which is the control plane of brow itself and all the workload that needs to be scheduled or where are actual brow job runs all that happens on that side in the build clusters so what happens is we start from GitHub anybody for example creates a PR or they comme
