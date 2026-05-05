---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Keynote Sessions"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Ricardo Rocha", "Lead Platforms Infrastructure", "CERN", "Marcin Wielgus", "Staff Software Engineer", "Google"]
sched_url: https://kccncna2024.sched.com/event/1iCOV/keynote-multicluster-batch-jobs-dispatching-with-kueue-at-cern-ricardo-rocha-lead-platforms-infrastructure-cern-marcin-wielgus-staff-software-engineer-google
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Multicluster+Batch+Jobs+Dispatching+with+Kueue+at+CERN+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keynote: Multicluster Batch Jobs Dispatching with Kueue at CERN - Ricardo Rocha, Lead Platforms Infrastructure, CERN & Marcin Wielgus, Staff Software Engineer, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Ricardo Rocha, Lead Platforms Infrastructure, CERN, Marcin Wielgus, Staff Software Engineer, Google
- Schedule: https://kccncna2024.sched.com/event/1iCOV/keynote-multicluster-batch-jobs-dispatching-with-kueue-at-cern-ricardo-rocha-lead-platforms-infrastructure-cern-marcin-wielgus-staff-software-engineer-google
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Multicluster+Batch+Jobs+Dispatching+with+Kueue+at+CERN+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keynote: Multicluster Batch Jobs Dispatching with Kueue at CERN.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iCOV/keynote-multicluster-batch-jobs-dispatching-with-kueue-at-cern-ricardo-rocha-lead-platforms-infrastructure-cern-marcin-wielgus-staff-software-engineer-google
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Multicluster+Batch+Jobs+Dispatching+with+Kueue+at+CERN+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xMmskWIlktA
- YouTube title: Keynote: Multicluster Batch Jobs Dispatching with Kueue at CERN - Ricardo Rocha & Marcin Wielgus
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keynote-multicluster-batch-jobs-dispatching-with-kueue-at-cern/xMmskWIlktA.txt
- Transcript chars: 14863
- Keywords: cluster, running, clusters, workload, resources, premises, brenda, basically, workloads, obviously, capacity, actually, submit, available, completed, around, already, multiple

### Resumo baseado na transcript

hello everyone my name is Marin I'm Tech lead of a team that develops Q at Google hello I'm Ricardo I'm a competing engineer at CERN I'm extremely excited to be here again and see you all uh let me start with a brief introduction on what Q is all about imagine that we have a scientific institutions and there are three researchers Adam Brenda and Chen and they love containers and so obviously they love kubernetes they want to analyze huge amount of data coming out from particle accelerators

### Excerpt da transcript

hello everyone my name is Marin I'm Tech lead of a team that develops Q at Google hello I'm Ricardo I'm a competing engineer at CERN I'm extremely excited to be here again and see you all uh let me start with a brief introduction on what Q is all about imagine that we have a scientific institutions and there are three researchers Adam Brenda and Chen and they love containers and so obviously they love kubernetes they want to analyze huge amount of data coming out from particle accelerators to create support or reject theories about the structure of the matter and the universe or to make things a little bit more realistic in the light of the recent Nobel prizes to train some new Lama model that will create and prove these theories for them okay so Adam Brenda and Chen have their ml training jobs and they want to run them on a vanilla kubernetes class both Adam's and Brand's jobs have 10 pots each CH jobs is a little bit smaller just two pots each of the PO requires a whole note from the cluster on the right if they submit the job at roughly the same time bad things can happen kubernetes schedular looks at the poorts in isolation and May schedule them in a random order like this one here effectively neither anam's nor branda's job May schedule completely as many M War clots require all pods to be up and running to start any real computations the presented situation is problematic and in fact it's a deadlock the cluster in theory is well utilized but in practice it is doing nothing the situation will not improve without manual intervention obviously it is B for Adam brand and Chen and they need to prevent it this problem from reoccurring in the future what they basically need is a component that will either admit and schedule their workloads in full or keep them on hold until the sufficient amount of resources is available in the cluster there are a number of tools that can do this there is for example unicorn there is volcano and there's a co- scheduling plugin and there is a project called Q developed by kubernetes working group batch in collaboration with scheduling autoscaling and apps what with Q Adams Brandel and CH workloads are as the name suggest CED if there are enough resources available the workloads from the queue can be admitted and get scheduled on the notes like the yellow one from Adam as there is not enough resources for the Violet one Brenda has to wait there is however enough capacity for 10 his workload gets admitted eventually Adam workl
