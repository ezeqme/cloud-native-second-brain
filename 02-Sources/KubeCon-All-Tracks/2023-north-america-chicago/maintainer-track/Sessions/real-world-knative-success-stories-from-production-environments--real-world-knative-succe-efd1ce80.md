---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Naina Singh", "Red Hat", "Norris Sam Osarenkhoe", "SVA", "Andrew Senetar", "CoreWeave", "Adolfo García Veytia", "Chainguard", "Ricardo Rocha", "CERN"]
sched_url: https://kccncna2023.sched.com/event/1R2vT/real-world-knative-success-stories-from-production-environments-naina-singh-red-hat-norris-sam-osarenkhoe-sva-andrew-senetar-coreweave-adolfo-garcia-veytia-chainguard-ricardo-rocha-cern
youtube_search_url: https://www.youtube.com/results?search_query=Real-World+Knative%3A+Success+Stories+from+Production+Environments+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Real-World Knative: Success Stories from Production Environments - Naina Singh, Red Hat; Norris Sam Osarenkhoe, SVA; Andrew Senetar, CoreWeave; Adolfo García Veytia, Chainguard; Ricardo Rocha, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Naina Singh, Red Hat, Norris Sam Osarenkhoe, SVA, Andrew Senetar, CoreWeave, Adolfo García Veytia, Chainguard, Ricardo Rocha, CERN
- Schedule: https://kccncna2023.sched.com/event/1R2vT/real-world-knative-success-stories-from-production-environments-naina-singh-red-hat-norris-sam-osarenkhoe-sva-andrew-senetar-coreweave-adolfo-garcia-veytia-chainguard-ricardo-rocha-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Real-World+Knative%3A+Success+Stories+from+Production+Environments+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Real-World Knative: Success Stories from Production Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vT/real-world-knative-success-stories-from-production-environments-naina-singh-red-hat-norris-sam-osarenkhoe-sva-andrew-senetar-coreweave-adolfo-garcia-veytia-chainguard-ricardo-rocha-cern
- YouTube search: https://www.youtube.com/results?search_query=Real-World+Knative%3A+Success+Stories+from+Production+Environments+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-DN7LQCn7aU
- YouTube title: Real-World Knative: Success Stories from Production Environments...
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/real-world-knative-success-stories-from-production-environments/-DN7LQCn7aU.txt
- Transcript chars: 33559
- Keywords: native, actually, customers, models, serving, conative, eventing, deploy, container, issues, workflows, production, challenges, software, experience, running, gpu, manage

### Resumo baseado na transcript

greetings everyone welcome to the project K native maintainers session where you are not going to hear from maintainers this time around how great K native is but hear about the stories how K native fars in the real world I am NAA Singh I am K native steering committee member and today I have with me four guest speakers who are going to talk about what how they are using K native in the world so if you attended one of my previous sessions you will think that I'm

### Excerpt da transcript

greetings everyone welcome to the project K native maintainers session where you are not going to hear from maintainers this time around how great K native is but hear about the stories how K native fars in the real world I am NAA Singh I am K native steering committee member and today I have with me four guest speakers who are going to talk about what how they are using K native in the world so if you attended one of my previous sessions you will think that I'm repeating myself but I think it is worth repeating that K native is more than sever less now what do I mean by that uh in kubernetes to create and deploy a service you have a lot of constructs that you need to keep take care of to create to configure to deploy what K native does it takes away the cognitive toil that you need to have because you run a command on a container it gives you a ready to use URL with autot TLS and also provide you Auto scaling Based On Demand with Infamous scale back to zero and that makes it a serverless platform for kubernetes as well as a simplified kubernetes for application developers but that's not all it is also event driven platform for kubernetes because it provides you the Eventing infrastructure for your all your event driven needs and with one more what I want to say is if I can reduce it to tagline it is K native by default and kubernetes when you must so today we will learn from our guest speakers their use cases what scenarios they are using K native for and why K native and with that I am going to give it to my first guest speaker to kick it off so I'm Andrew senar and um I work for cor weave who's a GPU Focus cloud provider so HPC rendering sort of things like that and we use K native for a managed service that allows our customers to run serverless style workloads most of our customers are using K native to serve large language models and like image generation and one of the reasons they like to use these is because of the ability to scale up and down scale to zero these are very big features that they want some of them deploy a lot of fine tunes that don't get a lot of usage so scale Zer is pretty important so con of serving provides a very simplified deployment for them and it handles the scaling the Ingress everything all inone you can set this up and we have seen some customers do this manually with like kada autoscaler and whatnot but this is so much easier for them to manage and use you get the one crd so that's the really big driver for uh the K of
