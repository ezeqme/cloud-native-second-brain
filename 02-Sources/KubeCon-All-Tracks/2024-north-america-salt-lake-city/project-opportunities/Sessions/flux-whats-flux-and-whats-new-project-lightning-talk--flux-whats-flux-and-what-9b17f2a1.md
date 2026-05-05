---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["GitOps Delivery"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8J/flux-whats-flux-and-whats-new-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Flux%3A+What%27s+Flux+and+What%27s+New%3F+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Flux: What's Flux and What's New? | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8J/flux-whats-flux-and-whats-new-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Flux%3A+What%27s+Flux+and+What%27s+New%3F+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Flux: What's Flux and What's New? | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8J/flux-whats-flux-and-whats-new-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Flux%3A+What%27s+Flux+and+What%27s+New%3F+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4le3ekQCsJA
- YouTube title: Flux: What's Flux and What's New? | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/flux-whats-flux-and-whats-new-project-lightning-talk/4le3ekQCsJA.txt
- Transcript chars: 5673
- Keywords: flux, gitops, multiple, source, controllers, flagger, single, companies, thanks, hopefully, cluster, manage, controller, operator, automation, threshold, progressive, delivery

### Resumo baseado na transcript

hey it's Lee and tommo from the flux project so yeah all right let's do this um great so we are representing the flux project and its sub project Flagger so thanks for listening um this will show gitops and Progressive delivery at scale so what is flux we are okay it's good so hopefully you know that uh flux is what triggered the term gitops which hopefully most of you know by now um but just some Basics gitops is operations by poll request in which you have a

### Excerpt da transcript

hey it's Lee and tommo from the flux project so yeah all right let's do this um great so we are representing the flux project and its sub project Flagger so thanks for listening um this will show gitops and Progressive delivery at scale so what is flux we are okay it's good so hopefully you know that uh flux is what triggered the term gitops which hopefully most of you know by now um but just some Basics gitops is operations by poll request in which you have a repo with a yaml file that acts as a single source of Truth flux listens to that repo and if there's a change to the yaml file it will alert kubernetes please make sure that the cluster is uh as is represented by the yaml file um as we'll talk later uh giops has evolved so much that now you don't even need git but that was the beginning of flux and giops and flux is incredibly powerful so we've been doing this for several years now which is why you can see that enterprises Banks Telos Microsoft Amazon gitlab and many many companies not only use flux but they trust flux to provide gitops to their end users and so these are just some of the logos and it's just so many different types of verticals and industries represented as companies that need and um use flux regularly and so it is so mature and secure um it has been a graduated project in the cncf for several years now it is General availability and security scale and reliability are core to its design which is why it is trusted by these companies So speaking of the design thanks T yeah flux is a set of controllers that is managing multiple different kinds of resource types we built flux to be installed even multiple times to a single cluster a single installation of flux can manage multiple clusters and you can safely do multi-tenancy with the flux apis because of how they're factored you'll see in the diagram that there are a couple controllers interacting with each other to make sure that desired state from git from S3 from the tags inside of your oci repos uh they get then reconciled by Helm controller and customized controller or you can even use raw manifests uh to then talk to the kubernetes API now flux is very easy to manage we knew that with this kind of complexity people were going to have a hard time getting started which is why we wrote the flux bootstrap command the code for flux bootstrap eventually made its way into a terraform and open toe proof providers many SAS control planes such as the ones offered by Azure and gitlab allow you
