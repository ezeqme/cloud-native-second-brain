---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Bridget Kromhout", "Microsoft", "Michael McCune", "Joel Speed", "Red Hat", "Walter Fender", "Google", "Jesse Butler", "AWS"]
sched_url: https://kccncna2025.sched.com/event/27NoX/sig-cloud-provider-deep-dive-expanding-our-mission-bridget-kromhout-microsoft-michael-mccune-joel-speed-red-hat-walter-fender-google-jesse-butler-aws
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Deep+Dive%3A+Expanding+Our+Mission+CNCF+KubeCon+2025
slides: []
status: parsed
---

# SIG Cloud Provider Deep Dive: Expanding Our Mission - Bridget Kromhout, Microsoft; Michael McCune & Joel Speed, Red Hat; Walter Fender, Google; Jesse Butler, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Bridget Kromhout, Microsoft, Michael McCune, Joel Speed, Red Hat, Walter Fender, Google, Jesse Butler, AWS
- Schedule: https://kccncna2025.sched.com/event/27NoX/sig-cloud-provider-deep-dive-expanding-our-mission-bridget-kromhout-microsoft-michael-mccune-joel-speed-red-hat-walter-fender-google-jesse-butler-aws
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Deep+Dive%3A+Expanding+Our+Mission+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre SIG Cloud Provider Deep Dive: Expanding Our Mission.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NoX/sig-cloud-provider-deep-dive-expanding-our-mission-bridget-kromhout-microsoft-michael-mccune-joel-speed-red-hat-walter-fender-google-jesse-butler-aws
- YouTube search: https://www.youtube.com/results?search_query=SIG+Cloud+Provider+Deep+Dive%3A+Expanding+Our+Mission+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BcUWVmluRdw
- YouTube title: SIG Cloud Provider Deep Dive: Expanding Our Miss... Bridget K, Michael M, Joel S, Walter F & Jesse B
- Match score: 0.775
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/sig-cloud-provider-deep-dive-expanding-our-mission/BcUWVmluRdw.txt
- Transcript chars: 30538
- Keywords: provider, talking, excited, testing, together, started, cluster, simple, little, blocks, working, actually, thinking, walter, google, future, providers, wanted

### Resumo baseado na transcript

We are the last time slot at CubeCon North America 2025, which is a real year that definitely exists. Um, we we are super excited to hear your thoughts and to give you some insights into what we're thinking, where we're going, and uh I think we'll just kick it off with introducing our panelists and jumping right in. I have also been active in, you know, cluster API and other, uh, you know, areas in the Kubernetes ecosystem. So, you know, we've been doing a lot of work uh over the years to remove cloud provider specific code from the core of Kubernetes, right? And I think that part of that movement pushes us in a direction where now we have to look at Kubernetes from a more agnostic position in terms of the cloud provider that it runs on. And so, you know, one of the things that I'm really excited about is the possibility that we could we could create building blocks that will give cloud providers more tools for interfacing with Kubernetes and and interfacing with Kubernetes in a way where they

### Excerpt da transcript

All right, welcome to the SIG cloud provider deep dive. We are the last time slot at CubeCon North America 2025, which is a real year that definitely exists. Um, we we are super excited to hear your thoughts and to give you some insights into what we're thinking, where we're going, and uh I think we'll just kick it off with introducing our panelists and jumping right in. Let's start with you, Walter. >> Hi. So, I'm Walter Fender. I also go by Chef Taco on GitHub. I work for Google and I do a variety of things, but Sigcloud provider is definitely one of the larger ones, including maintaining things like the API server network proxy. Uh, occasionally helping out on Crow and, uh, doing things in the cloud controller manager and very occasionally in cloud provider GCP. Uh, I'm Michael McCuin, uh, known in GitHub as Zel Mo or Elmo, depending on how you choose to pronounce it. Uh, I do some cloud provider maintenance at Red Hat. Uh, I also do a lot of cluster autoscaler maintenance and carpenter maintenance, especially related to the cluster API project.

Um, and I'm hoping to do more cloud provider in the future, but splitting your time is sometimes difficult. >> Hi, I'm Joel Speed. Uh I also work at Red Hat on Open Shift. Uh I'm a sick cloud tech lead. I spent the last 5 years finding gnarly issues in the different cloud providers and raising bugs against them all. Uh if I'm not doing cloud stuff, then I'm doing Cappy or having very strong opinions about APIs. >> And I'm Jesse Butler. I'm a principal PM in Amazon EKS. I work at AWS. I was uh in various other open- source uh uh products and uh and projects along last 15 years or so. Uh most recently in Crow uh with uh some of these fine folks here and uh also um really excited about what we're doing in SIG cloud provider with it. So I'm really excited to talk about it. Thanks everybody for sticking around to the last slot of the conference. >> Wonderful. All right. Thank you. So, um, like I said, >> wait, wait, wait. Aren't you gonna introduce yourself? >> Oh, no. I'm gonna introduce myself. It's fine. >> Okay, >> it's all good.

Like I said, uh, I'm Bridget Cromhout and I work at Microsoft Azure, uh, in upstream open source. I am also a SIG cloud provider co-chair. I have also been active in, you know, cluster API and other, uh, you know, areas in the Kubernetes ecosystem. I'm I think I'm really excited about Crow and about um our other endeavors to improve our testing etc. Because do you ever feel like you co
